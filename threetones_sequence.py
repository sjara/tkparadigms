"""
Present a sequence of three tones that repeats. This sequence is violated every now and then.


--Santiago Jaramillo
"""

import numpy as np
import itertools
import random
import time
from PySide import QtGui
from taskontrol.core import dispatcher
from taskontrol.core import paramgui
from taskontrol.core import savedata
from taskontrol.settings import rigsettings
from taskontrol.core import statematrix
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import soundclient


if rigsettings.OUTPUTS.has_key('outBit1'):
    trialStartSync = ['outBit1'] # Sync signal for trial-start.
else:
    trialStartSync = []
if rigsettings.OUTPUTS.has_key('outBit0'):
    stimSync = ['outBit0'] # Sync signal for sound stimulus
else:
    stimSync = []
if rigsettings.OUTPUTS.has_key('outBit2'):
    laserSync = ['outBit2','stim1'] # Sync signal for laser
else:
    laserSync = ['centerLED'] # Use center LED during emulation


class Paradigm(QtGui.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):
        '''
        Set up the taskontrol core modules, add parameters to the GUI, and 
        initialize the sound server.
        '''
        super(Paradigm, self).__init__(parent)

        self.name = 'threetones_sequence'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        # -- Create dispatcher --
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,
                                                     interval=0.05)

        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcherModel.statemachine)

        # -- Add parameters --
        self.params = paramgui.Container()
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='santiago',
                                                            group='Session info')
        self.params['subject'] = paramgui.StringParam('Subject',value='test000',
                                                       group='Session info')
        sessionInfo = self.params.layout_group('Session info')

        
        self.params['lowFreq'] = paramgui.NumericParam('Low freq (Hz)',
                                                        value=2100,
                                                        group='Stimulus parameters')
        self.params['midFreq'] = paramgui.NumericParam('Mid freq (Hz)',
                                                        value=3100,
                                                        group='Stimulus parameters')
        self.params['highFreq'] = paramgui.NumericParam('High freq (Hz)',
                                                        value=4200,
                                                        group='Stimulus parameters')
        self.params['oddballPeriod'] = paramgui.NumericParam('Oddball period',
                                                        value=10,
                                                        group='Stimulus parameters')
        self.params['oddballPeriodHalfRange'] = paramgui.NumericParam('+/-',
                                                        value=2,
                                                        group='Stimulus parameters')
        self.params['soundIntensity'] = paramgui.NumericParam('Sound intensity (dB SPL)',
                                                       value=60,
                                                       group='Stimulus parameters')
        self.params['stimDur'] = paramgui.NumericParam('Sound duration (s)',
                                                        value=0.1,
                                                        group='Stimulus parameters')
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus mean (s)',
                                                       value=0.1,
                                                       group='Stimulus parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=0,
                                                      group='Stimulus parameters')
        self.params['sequenceMode'] = paramgui.MenuParam('Sequence mode',
                                                         ['ascending','descending'],
                                                         value=0,group='Stimulus parameters')
        self.params['stimType'] = paramgui.MenuParam('Stim type',
                                                         ['sine','chord'],
                                                         value=0,group='Stimulus parameters')
        self.params['currentFreq'] = paramgui.NumericParam('Current Frequency (Hz)',
                                                            value=0, units='Hz', decimals=0,
                                                            enabled=False,
                                                            group='Stimulus parameters')
        self.params['stimCondition'] = paramgui.MenuParam('Stimulus condition',
                                                          ['standard','oddball'],
                                                          enabled=False,
                                                          value=0,group='Stimulus parameters')
        '''
        self.params['currentIntensity'] = paramgui.NumericParam('Current Intensity',
                                                                 value=0,
                                                                 enabled=False,
                                                                 group='Stimulus parameters')
        '''
        self.params['currentAmpL'] = paramgui.NumericParam('Current Amplitude - L',value=0,
                                                           enabled=False,
                                                           group='Stimulus parameters',
                                                           decimals=4)
        self.params['currentAmpR'] = paramgui.NumericParam('Current Amplitude - R',value=0,
                                                           enabled=False,
                                                           group='Stimulus parameters',
                                                           decimals=4)
        stimParams = self.params.layout_group('Stimulus parameters')

        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)


        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Module for savng the data -- 
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR,
                                          remotedir=rigsettings.REMOTE_DIR)
        self.saveData.checkInteractive.setChecked(True)

        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout() #Create a main layout and two columns
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()

        layoutMain.addLayout(layoutCol1) #Add the columns to the main layout
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.dispatcherView) #Add the dispatcher to col1
        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.manualControl)
        layoutCol2.addWidget(sessionInfo)  #Add the parameter GUI to column 2
        layoutCol2.addWidget(stimParams)  #Add the parameter GUI to column 2

        self.centralWidget.setLayout(layoutMain) #Assign the layouts to the main window
        self.setCentralWidget(self.centralWidget)

        # -- Connect signals from dispatcher --
        # --- Sent when dispatcher reaches the end of the current trial ---
        self.dispatcherModel.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        print "Connecting to sound server"
        print '***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****'        
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()

        # -- General variables --
        self.nextOddballPeriod = self.params['oddballPeriod'].get_value()
        self.nPatternsAfterOddball = 0
        self.stepInSequence = 0
        self.sequence = []

    
    def prepare_next_trial(self, nextTrial):
        '''
        Prepare the target sound, send state matrix to the statemachine, and 
        update the list of GUI parameters so that we can save the history of the
        frequency, intensity, and amplitude parameters for each trial. 
        '''

        if nextTrial > 0:  # Do not update the history before the first trial
            self.params.update_history()

        # -- Choose an ISI randomly --
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['isiMean'].get_value() + \
              self.params['isiHalfRange'].get_value()*randNum

        # -- Determine freq of next sound --
        lowFreq = self.params['lowFreq'].get_value()
        midFreq = self.params['midFreq'].get_value()
        highFreq = self.params['highFreq'].get_value()
        sequenceMode = self.params['sequenceMode'].get_string()
        possibleFreqs = [lowFreq, midFreq, highFreq]
        nFreq = len(possibleFreqs)

        
        stepInSequence = nextTrial%nFreq
        # -- Define next sequence --
        if self.nPatternsAfterOddball >= self.nextOddballPeriod:
            self.params['stimCondition'].set_string('oddball')
            self.nPatternsAfterOddball = 0
            oddballPeriod = self.params['oddballPeriod'].get_value()
            oddballPeriodHalfRange = self.params['oddballPeriodHalfRange'].get_value()
            jitter = np.random.randint(2*oddballPeriodHalfRange+1)-oddballPeriodHalfRange
            self.nextOddballPeriod = oddballPeriod + jitter
            if sequenceMode=='ascending':
                self.sequence = [0,2,1]
            elif sequenceMode=='descending':
                self.sequence = [2,0,1]
            else:
                raise ValueError('Sequence not defined')
                # FIXME: first item is ignored because of the way nPatternsAfterOddball is updated
        else:
            if stepInSequence==0 or not len(self.sequence):
                self.params['stimCondition'].set_string('standard')
                self.nPatternsAfterOddball += 1
                if sequenceMode=='ascending':
                    self.sequence = np.arange(nFreq)
                elif sequenceMode=='descending':
                    self.sequence = np.arange(nFreq)[::-1]
                else:
                    raise ValueError('Sequence not defined')
        '''
        # -- DEBUG --
        print('=========================================================')
        print('next:{}  nAfter:{}'.format(self.nextOddballPeriod,self.nPatternsAfterOddball))
        print('=========================================================')
        '''
            
        currentFreq = possibleFreqs[self.sequence[stepInSequence]]
        self.params['currentFreq'].set_value(currentFreq)

        
        # -- Prepare the sound  --
        stimDur = self.params['stimDur'].get_value()
        soundIntensity = self.params['soundIntensity'].get_value()
        soundAmp = self.spkCal.find_amplitude(currentFreq,soundIntensity)
        self.params['currentAmpL'].set_value(soundAmp[0])
        self.params['currentAmpR'].set_value(soundAmp[1])

        # -- Determine the sound type --
        stimType = self.params['stimType'].get_string()
        if stimType == 'sine':
            sound = {'type':'tone', 'duration':stimDur, 
                     'amplitude':soundAmp, 'frequency':currentFreq}
        elif stimType == 'chord':
            sound = {'type':'chord', 'frequency':currentFreq, 'duration':stimDur,
                  'amplitude':soundAmp, 'ntones':12, 'factor':1.2}
            
        soundID = 1
        self.soundClient.set_sound(soundID,sound)

        # -- Prepare the state transition matrix --
        self.sm.reset_transitions()
        self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,  
                          transitions={'Tup':'output1On'})
        self.sm.add_state(name='output1On', statetimer=stimDur, 
                          transitions={'Tup':'output1Off'},
                          outputsOn=stimSync, 
                          serialOut=soundID)
        self.sm.add_state(name='output1Off', statetimer = 0.5 * isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=stimSync) 
        
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()

        
    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcherModel,
                               self.sm],
                              self.dispatcherModel.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def clear_tone_list(self):
        '''Allow the user to clear the list of tones and assign new tones from the GUI'''

        self.soundParamList = []

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcherModel.die()
        event.accept()

if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(Paradigm)

