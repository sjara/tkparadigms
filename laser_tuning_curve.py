'''
Tuning curve presentation paradigm: allows presentation of tones at different
magnitudes, and will send triggers to electrophysiology recording software. 


Nick Ponvert and Santiago Jaramillo

'''

from PySide import QtGui
from taskontrol.core import dispatcher
from taskontrol.core import paramgui
from taskontrol.core import savedata
from taskontrol.settings import rigsettings
from taskontrol.core import statematrix
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import manualcontrol
from numpy import log
import numpy as np
import itertools
import random
from taskontrol.plugins import soundclient
import time

#class clearButton(QtGui.QPushButton):
#    def __init__(self, parent=None):
#        super(OutputButton, self).__init__('Clear Tone List')
#        self.clicked.connect(self.clear_tone_list)

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

        self.name = 'tuning_curve'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION)

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
                                                            group='Parameters')
        self.params['subject'] = paramgui.StringParam('Subject',value='test030',
                                                       group='Parameters')
        self.params['minFreq'] = paramgui.NumericParam('Min Frequency (Hz)',
                                                        value=2000,
                                                        group='Parameters')
        self.params['maxFreq'] = paramgui.NumericParam('Max Frequency (Hz)',
                                                        value=40000,
                                                        group='Parameters')
        self.params['numTones'] = paramgui.NumericParam('Number of Frequencies',
                                                         value=16,
                                                         group='Parameters')
        self.params['minInt'] = paramgui.NumericParam('Min Intensity (dB SPL)',
                                                       value=60,
                                                       group='Parameters')
        self.params['maxInt'] = paramgui.NumericParam('Max Intensity (dB SPL)',
                                                       value=60,
                                                       group='Parameters')
        self.params['numInt'] = paramgui.NumericParam('Number of Intensities',
                                                       value=1,
                                                       group='Parameters')
        self.params['stimDur'] = paramgui.NumericParam('Tone Duration (s)',
                                                        value=0.01,
                                                        group='Parameters')
        '''
        self.params['isiMin'] = paramgui.NumericParam('Minimum Interstimulus Interval (s)',
                                                       value=1,
                                                       group='Parameters')
        self.params['isiMax'] = paramgui.NumericParam('Maximum Interstimulus Interval',
                                                      value=3,
                                                      group='Parameters')
        '''
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus interval mean (s)',
                                                       value=2,
                                                       group='Parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=1,
                                                      group='Parameters')
        self.params['noiseAmp'] = paramgui.NumericParam('Amplitude in Noise-Mode',
                                                       value=0.3,
                                                       group='Parameters')
        self.params['randomMode'] = paramgui.MenuParam('Presentation Mode',
                                                         ['Ordered','Random'],
                                                         value=1,group='Parameters')
        self.params['stimType'] = paramgui.MenuParam('Sound Type',
                                                         ['Sine','Chord', 'Noise','Laser'],
                                                         value=2,group='Parameters')
        self.params['currentFreq'] = paramgui.NumericParam('Current Frequency (Hz)',
                                                            value=0, units='Hz',
                                                            enabled=False,
                                                            group='Parameters')

        self.params['currentIntensity'] = paramgui.NumericParam('Target Intensity',
                                                                 value=0,
                                                                 enabled=False,
                                                                 group='Parameters')
        self.params['currentAmp'] = paramgui.NumericParam('Current Amplitude',value=0,
                                                           enabled=False,
                                                           group='Parameters',
                                                           decimals=4)
        '''
        self.params['laserDuration'] = paramgui.NumericParam('Laser duration',value=0.01,
                                                             group='Parameters',
                                                             decimals=4)
        '''
        timingParams = self.params.layout_group('Parameters')
        
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
        layoutCol2.addWidget(timingParams)  #Add the parameter GUI to column 2

        self.centralWidget.setLayout(layoutMain) #Assign the layouts to the main window
        self.setCentralWidget(self.centralWidget)

        # -- Connect signals from dispatcher --
        
        #prepare_next_trial is sent whenever the dispatcher reaches the end of 
        #the current trial. 
        self.dispatcherModel.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        print "Connecting to sound server"
        print '***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****'        
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()
        #soundFreq = self.params['soundFreq'].get_value()

        # -- Initialize the list of trial parameters --
        self.trialParams = []
        self.soundParamList = []

    def populate_sound_params(self):

        '''This function reads the GUI inputs and populates a list of three-item tuples
        containing the frequency, and amplitude for each trial. This function is
        called by prepare_next_trial at the beginning of the experiment and whenever 
        we run out of combinations of sounds to present'''

        ## -- Get the parameters --

        maxFreq = self.params['maxFreq'].get_value()
        minFreq = self.params['minFreq'].get_value()
        numFreqs = self.params['numTones'].get_value()
        
        # -- Create a list of frequencies --
        toneList = self.logscale(minFreq, maxFreq, numFreqs) 


        minInt = self.params['minInt'].get_value()
        maxInt = self.params['maxInt'].get_value()
        numInt = self.params['numInt'].get_value()
        
        ampList = np.linspace(minInt, maxInt, num=numInt)

        # -- Make a tuple list of all of the products of the three parameter lists
        productList = list(itertools.product(toneList, ampList))

        # -- If in random presentation mode, shuffle the list of products
        randomMode = self.params['randomMode'].get_string()
        if randomMode == 'Random':
            random.shuffle(productList)
        else:
            pass

        # -- Set the sound parameter list to the product list

        self.soundParamList = productList




    def logscale(self, minFreq, maxFreq, numFreqs):
        '''This function returns a specified number of frequencies 
        scaled logarithmically between a minimum and maximum val'''

        slope=(log(maxFreq)-log(minFreq))/(numFreqs-1)
        xVals=range(numFreqs)
        logs=[slope * x + log(minFreq) for x in xVals]
        logs=np.array(logs)
        vals=np.exp(logs)
        return vals

    def prepare_next_trial(self, nextTrial):

        '''
        Prepare the target sound, send state matrix to the statemachine, and 
        update the list of GUI parameters so that we can save the history of the
        frequency, intensity, and amplitude parameters for each trial. 
        '''

        if nextTrial > 0:  ## Do not update the history before the first trial
            self.params.update_history()

        self.sm.reset_transitions()

        ## -- Choose an ISI randomly
        '''
        minIsi = self.params['isiMin'].get_value()
        maxIsi = self.params['isiMax'].get_value()
        isi=np.random.random() * (maxIsi - minIsi) + minIsi
        '''
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['isiMean'].get_value() + \
              self.params['isiHalfRange'].get_value()*randNum


        # -- Get the sound parameters from the parameter list --
        # -- If the parameter list is empty, populate it  --
        # -- returns a tuple with (frequency, intensity)
        try:
            self.trialParams = self.soundParamList.pop(0) #pop(0) pops from the left
        except IndexError:
            self.populate_sound_params()
            self.trialParams = self.soundParamList.pop(0)



        # -- Prepare the sound using randomly chosen parameters from parameter lists --

        stimDur = self.params['stimDur'].get_value()
        targetAmp = self.spkCal.find_amplitude(self.trialParams[0],
                                               self.trialParams[1])[1]  
                                               #Only calibrated right speaker

        # -- Determine the sound presentation mode and prepare the appropriate sound
        stimType = self.params['stimType'].get_string()
        
        if stimType == 'Sine':
            sound = {'type':'tone', 'duration':stimDur, 
                     'amplitude':targetAmp, 'frequency':self.trialParams[0]}
        elif stimType == 'Chord':
            sound = {'type':'chord', 'frequency':self.trialParams[0], 'duration':stimDur,
                  'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        elif stimType == 'Noise':
            noiseAmp=self.params['noiseAmp'].get_value()
            sound = {'type':'noise', 'duration':stimDur,
                     'amplitude':noiseAmp}

        if stimType == 'Laser':
            stimOutput = stimSync+laserSync
            serialOutput = 0
        else:
            stimOutput = stimSync
            serialOutput = 1
            self.soundClient.set_sound(1,sound)

        self.params['currentFreq'].set_value(self.trialParams[0])
        self.params['currentIntensity'].set_value(self.trialParams[1])
        self.params['currentAmp'].set_value(targetAmp)

        # -- Prepare the state transition matrix --
        self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,  
                          transitions={'Tup':'output1On'})
        self.sm.add_state(name='output1On', statetimer=stimDur, 
                          transitions={'Tup':'output1Off'},
                          outputsOn=stimOutput, 
                          serialOut=serialOutput)
        self.sm.add_state(name='output1Off', statetimer = 0.5 * isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=stimOutput) 

        
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()

    #def _timer_tic(self, etime, lastEvents):
    #    #timer_tic is sent whenever the dispatcher gets information from the Arduino
    #    pass 
    
    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcherModel,
                               self.sm],
                              self.dispatcherModel.currentTrial,
                              experimenter=self.params['experimenter'].get_value(),
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
        self.dispatcherModel.die()
        event.accept()

if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(Paradigm)

