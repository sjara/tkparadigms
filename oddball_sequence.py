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

import time
import numpy as np
from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import utils
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import soundclient


if 'outBit1' in rigsettings.OUTPUTS:
    trialStartSync = ['outBit1'] # Sync signal for trial-start.
else:
    trialStartSync = []
if 'outBit0' in rigsettings.OUTPUTS:
    stimSync = ['outBit0'] # Sync signal for sound stimulus
else:
    stimSync = []


class Paradigm(QtWidgets.QMainWindow):
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
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,
                                                     interval=0.1)

        ###self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)

        # -- Add parameters --
        self.params = paramgui.Container()
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='',
                                                            group='Session info')
        self.params['subject'] = paramgui.StringParam('Subject',value='test000',
                                                       group='Session info')
        sessionInfo = self.params.layout_group('Session info')

        
        self.params['stimType'] = paramgui.MenuParam('Stim type',
                                                         ['Sine','Chord','FM'],
                                                         value=0,group='Stimulus parameters')
        self.params['highFreq'] = paramgui.NumericParam('High frequency', value=3500, units='Hz',
                                                        group='Stimulus parameters')
        self.params['lowFreq'] = paramgui.NumericParam('Low frequency', value=2000, units='Hz',
                                                        group='Stimulus parameters')
        self.params['oddballStim'] = paramgui.MenuParam('Oddball stim',
                                                         ['high_freq','low_freq','FM_down','FM_up'],
                                                         value=0,group='Stimulus parameters')
        '''
        self.params['standardFreq'] = paramgui.NumericParam('Standard freq (Hz)',
                                                        value=2000,
                                                        group='Stimulus parameters')
        self.params['oddballFreq'] = paramgui.NumericParam('Oddball freq (Hz)',
                                                        value=2100,
                                                        group='Stimulus parameters')
        self.params['oddballProb'] = paramgui.NumericParam('Oddball probability',
                                                        value=0.1,
                                                        group='Stimulus parameters')
        '''
        self.params['oddballPeriod'] = paramgui.NumericParam('Oddball period',
                                                        value=10,
                                                        group='Stimulus parameters')
        self.params['oddballPeriodHalfRange'] = paramgui.NumericParam('+/-',
                                                        value=1,
                                                        group='Stimulus parameters')        
        self.params['freqFactorFromOddball'] = paramgui.NumericParam('Freq factor from odd',
                                                        value=2,
                                                        group='Stimulus parameters', enabled=False)
        self.params['nFreq'] = paramgui.NumericParam('Number of frequencies',
                                                         value=9,
                                                         group='Stimulus parameters', enabled=False)
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
        self.params['stimDuration'] = paramgui.NumericParam('Sound duration (s)',
                                                        value=0.05,
                                                        group='Stimulus parameters')
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus mean (s)',
                                                       value=0.5,
                                                       group='Stimulus parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=0,
                                                      group='Stimulus parameters')
        self.params['sequenceMode'] = paramgui.MenuParam('Sequence mode',
                                                         ['Oddball','Random','Ascending','Descending'],
                                                         value=0, group='Stimulus parameters',
                                                         enabled=False)
        self.params['currentStartFreq'] = paramgui.NumericParam('Current start freq (Hz)',
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
        self.params['soundLocation'] = paramgui.MenuParam('Sound location',
                                                          ['binaural', 'left', 'right'],
                                                          value=0, group='Stimulus parameters')
        stimParams = self.params.layout_group('Stimulus parameters')

        self.params['syncLight'] = paramgui.MenuParam('Sync light',
                                                       ['off', 'leftLED', 'centerLED', 'rightLED'],
                                                       value=0, group='Sync parameters')
        self.params['syncLightMode'] = paramgui.MenuParam('Sync light mode',
                                                          ['from_stim_offset', 'overlap_with_stim'],
                                                          value=1, group='Sync parameters',
                                                          enabled=False)
        #self.params['delayToSyncLight'] = paramgui.NumericParam('Delay to sync light',value=0,
        #                                                units='s',group='Sync parameters')
        #self.params['syncLightDuration'] = paramgui.NumericParam('Sync light duration',value=0.1,
        #                                                units='s',group='Sync parameters')
        syncParams = self.params.layout_group('Sync parameters')
        
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
        layoutMain = QtWidgets.QHBoxLayout() #Create a main layout and two columns
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1) #Add the columns to the main layout
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(sessionInfo)
        layoutCol1.addWidget(self.dispatcher.widget)
        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.manualControl)
        layoutCol2.addWidget(stimParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(syncParams)

        self.centralWidget.setLayout(layoutMain) #Assign the layouts to the main window
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = 8000 # Preallocating space for each vector makes things easier
        self.results = utils.EnumContainer()
        self.results['timeTrialStart'] = np.empty(maxNtrials,dtype=float)

        # -- Connect signals from dispatcher --
        # --- Sent when dispatcher reaches the end of the current trial ---
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        # -- Connect to sound server and define sounds --
        print('Conecting to soundserver (waiting for 200ms) ...')
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()

        # -- General variables --
        self.nextOddballPeriod = self.params['oddballPeriod'].get_value()
        self.nPatternsAfterOddball = 0
        self.stepInSequence = 0
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
            self.params.update_history(nextTrial-1)
            self.calculate_results(nextTrial-1)

        # -- Choose an ISI randomly --
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['isiMean'].get_value() + \
              self.params['isiHalfRange'].get_value()*randNum

        # -- Determine freq of next sound --
        #standardFreq = self.params['standardFreq'].get_value()
        #oddballFreq = self.params['oddballFreq'].get_value()
        #oddballProb = self.params['oddballProb'].get_value()
        highFreq = self.params['highFreq'].get_value()
        lowFreq = self.params['lowFreq'].get_value()
        oddballStim =  self.params['oddballStim'].get_string()
        sequenceMode = self.params['sequenceMode'].get_string()
        '''
        freqFactorFromOddball = self.params['freqFactorFromOddball'].get_value()
        nFreq = self.params['nFreq'].get_value()
        minFreq = oddballFreq/freqFactorFromOddball
        maxFreq = oddballFreq*freqFactorFromOddball
        possibleFreqs = np.logspace(np.log10(minFreq), np.log10(maxFreq), nFreq)
        '''

        '''
        # -- Set the order of sounds for next batch of trials --
        stepInSequence = nextTrial%nFreq
        if stepInSequence==0 or not len(self.sequence):
            if sequenceMode=='Random':
                self.sequence = np.random.permutation(nFreq)
            elif sequenceMode=='Ascending':
                self.sequence = np.arange(nFreq)
            elif sequenceMode=='Descending':
                self.sequence = np.arange(nFreq)[::-1]
        '''
        '''
        if sequenceMode=='Oddball':
            if np.random.random(1)[0] < oddballProb:
                currentStartFreq = oddballFreq
            else:
                currentStartFreq = standardFreq
        else:
            currentStartFreq = possibleFreqs[self.sequence[stepInSequence]]
        '''
        if (oddballStim == 'high_freq') or (oddballStim == 'FM_down'):
            oddballFreq = highFreq
            standardFreq = lowFreq
        elif (oddballStim == 'low_freq') or (oddballStim == 'FM_up'):
            oddballFreq = lowFreq
            standardFreq = highFreq
        else:
            raise ValueError()

        '''
        syncLightMode = self.params['syncLightMode'].get_string()
        delayToSyncLight = self.params['delayToSyncLight'].get_value()
        syncLightDuration = self.params['syncLightDuration'].get_value()
        if isi-delayToSyncLight-syncLightDuration < 0:
            raise ValueError('ISI needs to be longer to have time for the sync light.')
        '''
        syncLightPortStr = self.params['syncLight'].get_string()
        if syncLightPortStr=='off':
            syncLightPort = []
        else:
            syncLightPort = [syncLightPortStr]
        
        if sequenceMode=='Oddball':
            if self.nPatternsAfterOddball >= (self.nextOddballPeriod-1):
                currentStartFreq = oddballFreq
                endFreq = standardFreq  # To be used if FM sounds
                self.nPatternsAfterOddball = 0
                oddballPeriod = self.params['oddballPeriod'].get_value()
                oddballPeriodHalfRange = self.params['oddballPeriodHalfRange'].get_value()
                jitter = np.random.randint(2*oddballPeriodHalfRange+1)-oddballPeriodHalfRange
                self.nextOddballPeriod = oddballPeriod + jitter
                print(f'----------- self.nextOddballPeriod: {self.nextOddballPeriod} -------------')
            else:
                currentStartFreq = standardFreq
                endFreq = oddballFreq  # To be used if FM sounds
                self.nPatternsAfterOddball += 1
        self.params['currentStartFreq'].set_value(currentStartFreq)

        # -- Prepare the sound  --
        stimDuration = self.params['stimDuration'].get_value()
        soundIntensity = self.params['soundIntensity'].get_value()
        soundAmp = self.spkCal.find_amplitude(currentStartFreq, soundIntensity)
        self.params['currentAmpL'].set_value(soundAmp[0])
        self.params['currentAmpR'].set_value(soundAmp[1])

        soundLocation = self.params['soundLocation'].get_string()
        if soundLocation == 'left':
            soundAmp = [soundAmp[0], 0]
        elif soundLocation == 'right':
            soundAmp = [0, soundAmp[1]]

        # -- Determine the sound type --
        stimType = self.params['stimType'].get_string()
        if stimType == 'Sine':
            sound = {'type':'tone', 'duration':stimDuration, 
                     'amplitude':soundAmp, 'frequency':currentStartFreq}
        elif stimType == 'Chord':
            sound = {'type':'chord', 'frequency':currentStartFreq, 'duration':stimDuration,
                  'amplitude':soundAmp, 'ntones':12, 'factor':1.2}
        elif stimType == 'FM':
            sound = {'type':'FM', 'frequencyStart':currentStartFreq, 'frequencyEnd':endFreq,
                     'duration':stimDuration, 'amplitude':soundAmp}
            
        soundID = 1
        self.soundClient.set_sound(soundID,sound)

        # -- Prepare the state transition matrix --
        self.sm.reset_transitions()
        self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,  
                          transitions={'Tup':'output1On'})
        self.sm.add_state(name='output1On', statetimer=stimDuration, 
                          transitions={'Tup':'output1Off'},
                          outputsOn=stimSync+syncLightPort, 
                          serialOut=soundID)
        self.sm.add_state(name='output1Off', statetimer = 0.5 * isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=stimSync+syncLightPort) 
        
        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()


    def calculate_results(self,trialIndex):
        # -- Find beginning of trial --
        eventsThisTrial = self.dispatcher.events_one_trial(trialIndex)
        statesThisTrial = eventsThisTrial[:,2]
        startTrialStateID = self.sm.statesNameToIndex['startTrial']
        startTrialInd = np.flatnonzero(statesThisTrial==startTrialStateID)[0]
        self.results['timeTrialStart'][trialIndex] = eventsThisTrial[startTrialInd,0]

        
    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcher,
                               self.sm, self.results],
                              self.dispatcher.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def clear_tone_list(self):
        '''Allow the user to clear the list of tones and assign new tones from the GUI'''

        self.soundParamList = []

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

