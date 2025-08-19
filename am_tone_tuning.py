'''
Present a range of stimuli (either pure tones or AM noise) logarithmically space
and at different intensities.
'''

import numpy as np
import itertools
import random
import time
from qtpy import QtWidgets
from taskontrol import dispatcher
from taskontrol import paramgui
from taskontrol import savedata
from taskontrol import statematrix
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import soundclient
from taskontrol import rigsettings


if 'outBit1' in rigsettings.OUTPUTS:
    trialStartSync = ['outBit1'] # Sync signal for trial-start.
else:
    trialStartSync = []
if 'outBit0' in rigsettings.OUTPUTS:
    stimSync = ['outBit0'] # Sync signal for sound stimulus
else:
    stimSync = []
if 'outBit2' in rigsettings.OUTPUTS:
    laserSync = ['outBit2','stim2'] # Sync signal for laser
else:
    laserSync = ['centerLED'] # Use center LED during emulation


class Paradigm(QtWidgets.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):
        """
        Set up the taskontrol core modules, add parameters to the GUI, and
        initialize the sound server.
        """
        super(Paradigm, self).__init__(parent)
        self.name = 'am_tuning_curve'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_SINE)
        self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)

        # -- Create dispatcher --
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,
                                                     interval=0.1)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)

        # -- Add parameters --
        self.params = paramgui.Container()

        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='experimenter',
                                                            group='Session parameters')
        self.params['subject'] = paramgui.StringParam('Subject',value='test000',
                                                       group='Session parameters')
        sessionParams = self.params.layout_group('Session parameters')

        self.params['minFreq'] = paramgui.NumericParam('Min Tone Frequency (Hz)',
                                                        value=2000,
                                                        group='Stim parameters')
        self.params['maxFreq'] = paramgui.NumericParam('Max Tone Frequency (Hz)',
                                                        value=40000,
                                                        group='Stim parameters')
        self.params['numTones'] = paramgui.NumericParam('Number of Tone Frequencies',
                                                         value=16,
                                                         group='Stim parameters')
        
        self.params['minModRate'] = paramgui.NumericParam('Min AM Rate (Hz)',
                                                        value=4,
                                                        group='Stim parameters')
        self.params['maxModRate'] = paramgui.NumericParam('Max AM Rate (Hz)',
                                                        value=128,
                                                        group='Stim parameters')
        self.params['numModRates'] = paramgui.NumericParam('Number of AM rates',
                                                         value=4,
                                                         group='Stim parameters')
        
        self.params['minInt'] = paramgui.NumericParam('Min Intensity (dB SPL)',
                                                       value=70,
                                                       group='Stim parameters')
        self.params['maxInt'] = paramgui.NumericParam('Max Intensity (dB SPL)',
                                                       value=70,
                                                       group='Stim parameters')
        self.params['numInt'] = paramgui.NumericParam('Number of Intensities',
                                                       value=1,
                                                       group='Stim parameters')
        self.params['stimDur'] = paramgui.NumericParam('Stimulus Duration (s)',
                                                        value=0.1,
                                                        group='Stim parameters')
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus interval mean (s)',
                                                       value=2,
                                                       group='Stim parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=1,
                                                      group='Stim parameters')
        self.params['isi'] = paramgui.NumericParam('Interstimulus interval (s)',
                                                   value=2, enabled=False, decimals=3,
                                                   group='Stim parameters')
        self.params['randomMode'] = paramgui.MenuParam('Presentation Mode',
                                                         ['Ordered','Random'],
                                                         value=1,group='Stim parameters')
        self.params['stimType'] = paramgui.MenuParam('Stim Type',
                                                         ['Sine','Chord', 'Noise', 'AM',
                                                          'ToneTrain', 'AMtone',
                                                          'Laser', 'LaserTrain', 'Light'],
                                                         value=2,group='Stim parameters')
        
        self.params['currentFreq'] = paramgui.NumericParam('Current Tone Frequency (Hz)',
                                                            value=0, units='Hz',
                                                            enabled=False, decimals=3,
                                                            group='Stim parameters')
        self.params['currentMod'] = paramgui.NumericParam('Current Mod Rate (Hz)',
                                                            value=0, units='Hz',
                                                            enabled=False, decimals=3,
                                                            group='Stim parameters')
        self.params['currentIntensity'] = paramgui.NumericParam('Target Intensity',
                                                                 value=0,
                                                                 enabled=False,
                                                                 group='Stim parameters')
        self.params['currentAmpL'] = paramgui.NumericParam('Current Amplitude - L',value=0,
                                                           enabled=False,
                                                           group='Stim parameters',
                                                           decimals=4)
        self.params['currentAmpR'] = paramgui.NumericParam('Current Amplitude - R',value=0,
                                                           enabled=False,
                                                           group='Stim parameters',
                                                           decimals=4)
        self.params['soundLocation'] = paramgui.MenuParam('Sound location',
                                                          ['binaural', 'left', 'right'],
                                                          value=0, group='Stim parameters')


        stimParams = self.params.layout_group('Stim parameters')

        self.params['syncLight'] = paramgui.MenuParam('Sync light',
                                                       ['off', 'leftLED', 'centerLED', 'rightLED'],
                                                       value=0, group='Sync parameters')
        self.params['syncLightMode'] = paramgui.MenuParam('Sync light mode',
                                                          ['from_stim_offset', 'overlap_with_stim'],
                                                          value=0, group='Sync parameters')
        self.params['delayToSyncLight'] = paramgui.NumericParam('Delay to sync light',value=0,
                                                        units='s',group='Sync parameters')
        self.params['syncLightDuration'] = paramgui.NumericParam('Sync light duration',value=0,
                                                        units='s',group='Sync parameters')
        syncParams = self.params.layout_group('Sync parameters')

        self.params['laserTrialsFraction'] = paramgui.NumericParam('Fraction of trials with laser',
                                                                   value=0,
                                                                   group='Laser parameters')
        self.params['laserFrontOverhang'] = paramgui.NumericParam('Laser Front Overhang',value=0,
                                                                  group='Laser parameters', enabled=False,
                                                                  decimals=1)
        self.params['laserBackOverhang'] = paramgui.NumericParam('Laser Back Overhang',value=0,
                                                                 group='Laser parameters', enabled=False,
                                                                 decimals=1)
        self.params['laserTrial'] = paramgui.NumericParam('Laser Trial?',value=0,
                                                           enabled=False,
                                                           group='Laser parameters',
                                                           decimals=0)
        laserParams = self.params.layout_group('Laser parameters')

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
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(sessionParams)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)
        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.manualControl)

        self.clearButton = QtWidgets.QPushButton('Clear Stim List', self)
        self.clearButton.clicked.connect(self.clear_tone_list)
        layoutCol1.addWidget(self.clearButton)

        layoutCol2.addWidget(stimParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(syncParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(laserParams)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Connect signals from dispatcher --
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        print("Connecting to sound server")
        print('***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****')
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()

        # -- Initialize the list of trial parameters --
        self.trialParams = []
        self.soundParamList = []

    def populate_sound_params(self):

        '''This function reads the GUI inputs and populates a list of three-item tuples
        containing the frequency, and amplitude for each trial. This function is
        called by prepare_next_trial at the beginning of the experiment and whenever
        we run out of combinations of sounds to present'''

        # -- Get the parameters --
        maxFreq = self.params['maxFreq'].get_value()
        minFreq = self.params['minFreq'].get_value()
        numFreqs = self.params['numTones'].get_value()
        maxModRate = self.params['maxModRate'].get_value()
        minModRate = self.params['minModRate'].get_value()
        numModRates = self.params['numModRates'].get_value()

        # -- Create a list of frequencies --
        toneList = np.logspace(np.log10(minFreq), np.log10(maxFreq),num = numFreqs)
        modList = np.logspace(np.log10(minModRate), np.log10(maxModRate),num = numModRates)


        minInt = self.params['minInt'].get_value()
        maxInt = self.params['maxInt'].get_value()
        numInt = self.params['numInt'].get_value()

        ampList = np.linspace(minInt, maxInt, num=numInt)

        # -- Make a tuple list of all of the products of the three parameter lists
        productList = list(itertools.product(toneList, ampList, modList))

        # -- If in random presentation mode, shuffle the list of products
        randomMode = self.params['randomMode'].get_string()
        if randomMode == 'Random':
            random.shuffle(productList)
        else:
            pass

        # -- Set the sound parameter list to the product list

        self.soundParamList = productList


    def prepare_next_trial(self, nextTrial):

        '''
        Prepare the target sound, send state matrix to the statemachine, and
        update the list of GUI parameters so that we can save the history of the
        frequency, intensity, and amplitude parameters for each trial.
        '''

        if nextTrial > 0:  # Do not update the history before the first trial
            self.params.update_history(nextTrial-1)

        self.sm.reset_transitions()

        # -- Choose an ISI randomly
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['isiMean'].get_value() + \
              self.params['isiHalfRange'].get_value()*randNum
        self.params['isi'].set_value(isi)

        # Get the sound parameters (frequency, intensity) from the parameter list
        # If the parameter list is empty, populate it  --
        try:
            self.trialParams = self.soundParamList.pop(0) #pop(0) pops from the left
        except IndexError:
            self.populate_sound_params()
            self.trialParams = self.soundParamList.pop(0)

        # -- Prepare the sound using randomly chosen parameters from parameter lists --
        stimType = self.params['stimType'].get_string()
        stimDur = self.params['stimDur'].get_value()

        if stimType in ['Noise', 'AM','AMtone']:
            targetAmp = self.noiseCal.find_amplitude(self.trialParams[1])
        else:
            targetAmp = self.spkCal.find_amplitude(self.trialParams[0],
                                                   self.trialParams[1])
        soundLocation = self.params['soundLocation'].get_string()
        if soundLocation == 'left':
            targetAmp = [targetAmp[0], 0]
        elif soundLocation == 'right':
            targetAmp = [0, targetAmp[1]]

        # -- Determine the sound presentation mode and prepare the appropriate sound
        if stimType == 'Sine':
            sound = {'type':'tone', 'duration':stimDur,
                     'amplitude':targetAmp, 'frequency':self.trialParams[0]}
        elif stimType == 'Chord':
            sound = {'type':'chord', 'frequency':self.trialParams[0], 'duration':stimDur,
                  'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        elif stimType == 'Noise':
            sound = {'type':'noise', 'duration':stimDur,
                     'amplitude':targetAmp}
        elif stimType == 'AM':
            sound = {'type':'AM', 'duration':stimDur,
                     'amplitude':targetAmp,'modFrequency':self.trialParams[0]}
        elif stimType == 'ToneTrain':
            sound = {'type':'toneTrain', 'duration':stimDur,
                     'amplitude':targetAmp, 'frequency':self.trialParams[0],
                     'toneDuration':0.025, 'rate':20}
        elif stimType == 'AMtone':
            sound = {'type':'AMtone', 'duration':stimDur, 'toneFrequency':self.trialParams[0],
                     'amplitude':targetAmp,'modFrequency':self.trialParams[2]}

        fractionLaserTrials = self.params['laserTrialsFraction'].get_value()
        laserTrial = np.random.rand(1)[0]<fractionLaserTrials
        self.params['laserTrial'].set_value(int(laserTrial))

        if (stimType == 'Laser') or (stimType == 'LaserTrain'):
            stimOutput = stimSync+laserSync
            serialOutput = 0
        elif stimType=='Light':
            stimOutput = stimSync + ['leftLED', 'centerLED', 'rightLED']
            if laserTrial:
                stimOutput = stimOutput + laserSync
            serialOutput = 0
        else:
            stimOutput = stimSync
            if laserTrial:
                stimOutput = stimOutput + laserSync
            serialOutput = 1
            self.soundClient.set_sound(1,sound)

        syncLightMode = self.params['syncLightMode'].get_string()
        delayToSyncLight = self.params['delayToSyncLight'].get_value()
        syncLightDuration = self.params['syncLightDuration'].get_value()
        if isi-delayToSyncLight-syncLightDuration < 0:
            raise ValueError('ISI needs to be longer to have time for the sync light.')
        syncLightPortStr = self.params['syncLight'].get_string()
        if syncLightPortStr=='off':
            syncLightPort = []
        else:
            syncLightPort = [syncLightPortStr]

        self.params['currentFreq'].set_value(self.trialParams[0])
        self.params['currentMod'].set_value(self.trialParams[2])
        self.params['currentIntensity'].set_value(self.trialParams[1])
        self.params['currentAmpL'].set_value(targetAmp[0])
        self.params['currentAmpR'].set_value(targetAmp[1])

        # -- Prepare the state transition matrix --
        soa = 0.2
        if stimType == 'LaserTrain':
            self.sm.add_state(name='startTrial', statetimer = 0,
                              transitions={'Tup':'output1On'})
            self.sm.add_state(name='output1On', statetimer=stimDur,
                              transitions={'Tup':'output1Off'},
                              outputsOn=stimOutput,
                              serialOut=serialOutput)
            self.sm.add_state(name='output1Off', statetimer = soa-stimDur,
                              transitions={'Tup':'output2On'},
                              outputsOff=stimOutput)
            self.sm.add_state(name='output2On', statetimer=stimDur,
                              transitions={'Tup':'output2Off'},
                              outputsOn=stimOutput,
                              serialOut=serialOutput)
            self.sm.add_state(name='output2Off', statetimer = soa-stimDur,
                              transitions={'Tup':'output3On'},
                              outputsOff=stimOutput)
            self.sm.add_state(name='output3On', statetimer=stimDur,
                              transitions={'Tup':'output3Off'},
                              outputsOn=stimOutput,
                              serialOut=serialOutput)
            self.sm.add_state(name='output3Off', statetimer = soa-stimDur,
                              transitions={'Tup':'output4On'},
                              outputsOff=stimOutput)
            self.sm.add_state(name='output4On', statetimer=stimDur,
                              transitions={'Tup':'output4Off'},
                              outputsOn=stimOutput,
                              serialOut=serialOutput)
            self.sm.add_state(name='output4Off', statetimer = soa-stimDur,
                              transitions={'Tup':'output5On'},
                              outputsOff=stimOutput)
            self.sm.add_state(name='output5On', statetimer=stimDur,
                              transitions={'Tup':'output5Off'},
                              outputsOn=stimOutput,
                              serialOut=serialOutput)
            self.sm.add_state(name='output5Off', statetimer = isi,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=stimOutput)
        else:
            if syncLightMode=='from_stim_offset':
                self.sm.add_state(name='startTrial', statetimer = 0,
                                  transitions={'Tup':'outputOn'})
                self.sm.add_state(name='outputOn', statetimer=stimDur,
                                  transitions={'Tup':'outputOff'},
                                  outputsOn=stimOutput,
                                  serialOut=serialOutput)
                self.sm.add_state(name='outputOff', statetimer=delayToSyncLight,
                                  transitions={'Tup':'syncLightOn'},
                                  outputsOff=stimOutput)
                self.sm.add_state(name='syncLightOn', statetimer=syncLightDuration,
                                  transitions={'Tup':'syncLightOff'},
                                  outputsOn=syncLightPort)
                self.sm.add_state(name='syncLightOff', statetimer=isi-delayToSyncLight-syncLightDuration,
                                  transitions={'Tup':'readyForNextTrial'},
                                  outputsOff=syncLightPort)
            elif syncLightMode=='overlap_with_stim':
                self.sm.add_state(name='startTrial', statetimer = 0,
                                  transitions={'Tup':'outputOn'})
                self.sm.add_state(name='outputOn', statetimer=stimDur,
                                  transitions={'Tup':'outputOff'},
                                  outputsOn=stimOutput+syncLightPort,
                                  serialOut=serialOutput)
                self.sm.add_state(name='outputOff', statetimer=isi,
                                  transitions={'Tup':'readyForNextTrial'},
                                  outputsOff=stimOutput+syncLightPort)

        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    #def _timer_tic(self, etime, lastEvents):
    #    #timer_tic is sent whenever the dispatcher gets information from the Arduino
    #    pass

    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcher,
                               self.sm],
                              self.dispatcher.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def clear_tone_list(self):
        '''Allow the user to clear the list of tones and assign new tones from the GUI'''

        print(self.soundParamList)
        self.soundParamList = []
        print(self.soundParamList)

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtWidgets.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcher.die()
        event.accept()

if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(Paradigm)
