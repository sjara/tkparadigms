'''
Present a sequence of sounds where a standard is repeated often and an oddball appears rarely.

Sequence modes:
* Oddball:
  Present oddball with some probability, otherwise present standard.
* Random:
  Present sounds in random order, with freq from oddball/Factor to oddball*Factor.
* Ascending:
  Present sound in ascending order, with freq from oddball/Factor to oddball*Factor.
* Descending:
  Present sound in descending order, with freq from oddball/Factor to oddball*Factor.

--Santiago Jaramillo
'''

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

        self.name = 'oddball_sequence'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        # -- Create dispatcher --
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,
                                                     interval=0.1)

        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcherModel.statemachine)

        # -- Add parameters --
        self.params = paramgui.Container()
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='santiago',
                                                            group='Session info')
        self.params['subject'] = paramgui.StringParam('Subject',value='test030',
                                                       group='Session info')
        sessionInfo = self.params.layout_group('Session info')

        
        self.params['standardFreq'] = paramgui.NumericParam('Standard freq (Hz)',
                                                        value=2000,
                                                        group='Stimulus parameters')
        self.params['oddballFreq'] = paramgui.NumericParam('Oddball freq (Hz)',
                                                        value=2100,
                                                        group='Stimulus parameters')
        self.params['oddballProb'] = paramgui.NumericParam('Oddball probability',
                                                        value=0.2,
                                                        group='Stimulus parameters')
        self.params['freqFactorFromOddball'] = paramgui.NumericParam('Freq factor from odd',
                                                        value=2,
                                                        group='Stimulus parameters')
        self.params['nFreq'] = paramgui.NumericParam('Number of frequencies',
                                                         value=9,
                                                         group='Stimulus parameters')
        '''
        self.params['minFreq'] = paramgui.NumericParam('Min Frequency (Hz)',
                                                        value=2000,
                                                        group='Stimulus parameters')
        self.params['maxFreq'] = paramgui.NumericParam('Max Frequency (Hz)',
                                                        value=40000,
                                                        group='Stimulus parameters')
        '''
        '''
        self.params['minIntensity'] = paramgui.NumericParam('Min intensity (dB SPL)',
                                                       value=60,
                                                       group='Stimulus parameters')
        self.params['maxIntensity'] = paramgui.NumericParam('Max intensity (dB SPL)',
                                                       value=60,
                                                       group='Stimulus parameters')
        self.params['numInt'] = paramgui.NumericParam('Number of Intensities',
                                                       value=1,
                                                       group='Stimulus parameters')
        '''
        self.params['soundIntensity'] = paramgui.NumericParam('Sound intensity (dB SPL)',
                                                       value=60,
                                                       group='Stimulus parameters')
        self.params['stimDur'] = paramgui.NumericParam('Sound duration (s)',
                                                        value=0.01,
                                                        group='Stimulus parameters')
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus mean (s)',
                                                       value=2,
                                                       group='Stimulus parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=1,
                                                      group='Stimulus parameters')
        self.params['sequenceMode'] = paramgui.MenuParam('Sequence mode',
                                                         ['Oddball','Random','Ascending','Descending'],
                                                         value=0,group='Stimulus parameters')
        self.params['stimType'] = paramgui.MenuParam('Stim type',
                                                         ['Sine','Chord'],
                                                         value=2,group='Stimulus parameters')
        self.params['currentFreq'] = paramgui.NumericParam('Current Frequency (Hz)',
                                                            value=0, units='Hz', decimals=0,
                                                            enabled=False,
                                                            group='Stimulus parameters')
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

        # -- Initialize the list of trial parameters --
        self.sequence = []

    '''   
    def set_sequence(self, nFreq, seqMode):
        if seqMode=='Random':
            self.sequence = p.random.permutation(10)
    '''
    
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
        standardFreq = self.params['standardFreq'].get_value()
        oddballFreq = self.params['oddballFreq'].get_value()
        oddballProb = self.params['oddballProb'].get_value()
        freqFactorFromOddball = self.params['freqFactorFromOddball'].get_value()
        nFreq = self.params['nFreq'].get_value()
        sequenceMode = self.params['sequenceMode'].get_string()
        minFreq = oddballFreq/freqFactorFromOddball
        maxFreq = oddballFreq*freqFactorFromOddball
        possibleFreqs = np.logspace(np.log10(minFreq), np.log10(maxFreq), nFreq)

        # -- Set the order of sounds for next batch of trials --
        stepInSequence = nextTrial%nFreq
        if stepInSequence==0 or not len(self.sequence):
            if sequenceMode=='Random':
                self.sequence = np.random.permutation(nFreq)
            elif sequenceMode=='Ascending':
                self.sequence = np.arange(nFreq)
            elif sequenceMode=='Descending':
                self.sequence = np.arange(nFreq)[::-1]

        if sequenceMode=='Oddball':
            if np.random.random(1)[0] < oddballProb:
                currentFreq = oddballFreq
            else:
                currentFreq = standardFreq
        else:
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
        if stimType == 'Sine':
            sound = {'type':'tone', 'duration':stimDur, 
                     'amplitude':soundAmp, 'frequency':currentFreq}
        elif stimType == 'Chord':
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

