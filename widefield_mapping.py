"""
Present a set of stimuli at different intensities.
"""

import numpy as np
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


class Paradigm(QtWidgets.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):
        """
        Set up the taskontrol core modules, add parameters to the GUI, and
        initialize the sound server.
        """
        super(Paradigm, self).__init__(parent)
        self.name = 'widefield_mapping'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_SINE)
        self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)

        # -- Create dispatcher --
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType, interval=0.1)

        # -- Add parameters --
        self.params = paramgui.Container()

        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='experimenter',
                                                            group='Session parameters')
        self.params['subject'] = paramgui.StringParam('Subject',value='test000',
                                                       group='Session parameters')
        self.params['sessionID'] = paramgui.StringParam('Session ID',value='',
                                                       group='Session parameters')
        self.params['nMaxTrials'] = paramgui.NumericParam('N trials (max)',value=99999,
                                                       group='Session parameters')
        sessionParams = self.params.layout_group('Session parameters')

        self.params['freqHigh'] = paramgui.NumericParam('High Frequency (Hz)',
                                                        value=32000,
                                                        group='Frequency and intensity')
        self.params['intensityHigh'] = paramgui.NumericParam('High Intensity (dB SPL)',
                                                       value=75,
                                                       group='Frequency and intensity')
        self.params['freqMid'] = paramgui.NumericParam('Mid Frequency (Hz)',
                                                        value=10000,
                                                        group='Frequency and intensity')
        self.params['intensityMid'] = paramgui.NumericParam('Mid Intensity (dB SPL)',
                                                       value=65,
                                                       group='Frequency and intensity')
        self.params['freqLow'] = paramgui.NumericParam('Low Frequency (Hz)',
                                                        value=3000,
                                                        group='Frequency and intensity')
        self.params['intensityLow'] = paramgui.NumericParam('Low Intensity (dB SPL)',
                                                       value=70,
                                                       group='Frequency and intensity')
        freqIntParams = self.params.layout_group('Frequency and intensity')

        self.params['stimDuration'] = paramgui.NumericParam('Stim Duration (s)',
                                                        value=0.5,
                                                        group='Stim parameters')
        self.params['isiMean'] = paramgui.NumericParam('ISI Mean (s)',
                                                       value=1.2,
                                                       group='Stim parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('ISI +/-',
                                                      value=0.2,
                                                      group='Stim parameters')
        self.params['isi'] = paramgui.NumericParam('ISI (s)',
                                                   value=2, enabled=False, decimals=3,
                                                   group='Stim parameters')
        self.params['stimOrder'] = paramgui.MenuParam('Order',
                                                         ['Ordered','Random'],
                                                         value=1,group='Stim parameters')
        self.params['stimType'] = paramgui.MenuParam('Stim Type',
                                                     ['ToneTrain', 'Sine', 'Chord','Noise', 'AM'],
                                                     value=0, group='Stim parameters')
        self.params['soundLocation'] = paramgui.MenuParam('Sound Location',
                                                          ['binaural', 'left', 'right'],
                                                          value=0, group='Stim parameters')
        stimParams = self.params.layout_group('Stim parameters')

        self.params['currentFreq'] = paramgui.NumericParam('Current Frequency (Hz)',
                                                            value=0, units='Hz',
                                                            enabled=False, decimals=3,
                                                            group='Current values')
        self.params['currentIntensity'] = paramgui.NumericParam('Target Intensity',
                                                                 value=0,
                                                                 enabled=False,
                                                                 group='Current values')
        self.params['currentAmpL'] = paramgui.NumericParam('Current Amplitude - L',value=0,
                                                           enabled=False,
                                                           group='Current values',
                                                           decimals=4)
        self.params['currentAmpR'] = paramgui.NumericParam('Current Amplitude - R',value=0,
                                                           enabled=False,
                                                           group='Current values',
                                                           decimals=4)
        currentValues = self.params.layout_group('Current values')

        # -- Load parameters from a file --
        self.params.from_file(paramfile, paramdictname)

        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Module for savng the data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR)
        # self.saveData.checkInteractive.setChecked(True)

        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()
        layoutCol3 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)

        self.saveOnStop = QtWidgets.QCheckBox('Save data on auto-stop')
        self.saveOnStop.setChecked(True)

        layoutCol1.addWidget(sessionParams)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)
        layoutCol1.addWidget(self.saveOnStop)

        layoutCol2.addWidget(stimParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(self.saveData)
        #layoutCol2.addWidget(self.saveOnStop)

        layoutCol3.addWidget(freqIntParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(currentValues)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Connect signals from dispatcher --
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        # -- Connect messenger --
        self.messagebar = paramgui.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect('Created window')

        # -- Connect signals to messenger
        self.saveData.logMessage.connect(self.messagebar.collect)
        self.dispatcher.logMessage.connect(self.messagebar.collect)

        print("Connecting to sound server")
        print('***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****')
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()

        # -- Initialize the list of trial parameters --
        self.trialParams = []
        self.soundParamList = []

    def populate_sound_params(self):

        '''This function reads the GUI inputs and populates a list of two-item tuples
        containing the frequency and intensity for each trial. This function is
        called by prepare_next_trial at the beginning of the experiment and whenever
        we run out of combinations of sounds to present'''

        # -- Get the parameters --
        freqIntPairs = [(self.params['freqLow'].get_value(), self.params['intensityLow'].get_value()),
                         (self.params['freqMid'].get_value(), self.params['intensityMid'].get_value()),
                         (self.params['freqHigh'].get_value(), self.params['intensityHigh'].get_value())]

        # -- If in random presentation mode, shuffle the list of pairs
        stimOrder = self.params['stimOrder'].get_string()
        if stimOrder == 'Random':
            random.shuffle(freqIntPairs)
        else:
            pass

        # -- Set the sound parameter list to the list of pairs

        self.soundParamList = freqIntPairs


    def prepare_next_trial(self, nextTrial):

        '''
        Prepare the target sound, send state matrix to the statemachine, and
        update the list of GUI parameters so that we can save the history of the
        frequency, intensity, and amplitude parameters for each trial.
        '''

        if nextTrial > self.params['nMaxTrials'].get_value():
            self.dispatcher.widget.stop()
            if self.saveOnStop.isChecked():
                self.save_to_file()
            return

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
        stimDuration = self.params['stimDuration'].get_value()

        if stimType in ['Noise', 'AM']:
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
        if stimType == 'ToneTrain':
            sound = {'type':'toneTrain', 'duration':stimDuration,
                     'amplitude':targetAmp, 'frequency':self.trialParams[0],
                     'toneDuration':0.025, 'rate':20}
        elif stimType == 'Sine':
            sound = {'type':'tone', 'duration':stimDuration,
                     'amplitude':targetAmp, 'frequency':self.trialParams[0]}
        elif stimType == 'Chord':
            sound = {'type':'chord', 'frequency':self.trialParams[0], 'duration':stimDuration,
                  'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        elif stimType == 'Noise':
            sound = {'type':'noise', 'duration':stimDuration,
                     'amplitude':targetAmp}
        elif stimType == 'AM':
            sound = {'type':'AM', 'duration':stimDuration,
                     'amplitude':targetAmp,'modFrequency':self.trialParams[0]}

        stimOutput = stimSync
        serialOutput = 1
        self.soundClient.set_sound(1,sound)

        self.params['currentFreq'].set_value(self.trialParams[0])
        self.params['currentIntensity'].set_value(self.trialParams[1])
        self.params['currentAmpL'].set_value(targetAmp[0])
        self.params['currentAmpR'].set_value(targetAmp[1])

        # -- Prepare the state transition matrix --
        self.sm.add_state(name='startTrial', statetimer = 0,
                          transitions={'Tup':'outputOn'})
        self.sm.add_state(name='outputOn', statetimer=stimDuration,
                          transitions={'Tup':'outputOff'},
                          outputsOn=stimOutput,
                          serialOut=serialOutput)
        self.sm.add_state(name='outputOff', statetimer=isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=stimOutput)

        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        sessionID = self.params['sessionID'].get_value()
        suffix = '' if sessionID == '' else '_' + sessionID
        self.saveData.to_file([self.params, self.dispatcher,
                               self.sm],
                              self.dispatcher.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name,
                              suffix=suffix)
        
    def _show_message(self, msg):
        self.statusBar().showMessage(str(msg))
        print(msg)

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
