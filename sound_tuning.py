"""
Present AM noise (at different AM rates) and fading noise (fade in or fade out
between a lowest and highest intensity) at calibrated intensities.
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
        self.name = 'sound_tuning'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object --
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

        self.params['includeAM'] = paramgui.MenuParam('Include AM noise',
                                                      ['No','Yes'],
                                                      value=1, group='AM noise')
        self.params['amRateLow'] = paramgui.NumericParam('Rate Low (Hz)',
                                                         value=4, group='AM noise')
        self.params['amRateHigh'] = paramgui.NumericParam('Rate High (Hz)',
                                                          value=16, group='AM noise')
        self.params['amNRates'] = paramgui.NumericParam('N Rates', value=3, group='AM noise')
        self.params['amIntensity'] = paramgui.NumericParam('Intensity (dB SPL)',
                                                           value=60, group='AM noise')
        self.params['currentAMRate'] = paramgui.NumericParam('Current AM Rate (Hz)',
                                                             value=0, enabled=False,
                                                             decimals=3,
                                                             group='AM noise')
        amParams = self.params.layout_group('AM noise')

        self.params['includeFading'] = paramgui.MenuParam('Include fading noise',
                                                            ['No','Yes'],
                                                            value=1, group='Fading noise')
        self.params['fadeIntensityLow'] = paramgui.NumericParam('Lowest Intensity (dB SPL)',
                                                                 value=45, group='Fading noise')
        self.params['fadeIntensityHigh'] = paramgui.NumericParam('Highest Intensity (dB SPL)',
                                                                  value=75, group='Fading noise')
        self.params['fadeDirection'] = paramgui.MenuParam('Fade Direction',
                                                          ['fade_in','fade_out'],
                                                          value=0, enabled=False,
                                                          group='Fading noise')
        fadeParams = self.params.layout_group('Fading noise')

        self.params['stimDuration'] = paramgui.NumericParam('Stim Duration (s)',
                                                        value=1.0,
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
        self.params['soundLocation'] = paramgui.MenuParam('Sound Location',
                                                          ['binaural', 'left', 'right'],
                                                          value=0, group='Stim parameters')
        stimParams = self.params.layout_group('Stim parameters')

        self.params['currentStimType'] = paramgui.MenuParam('Current Stim Type',
                                                            ['AM','FadingNoise'],
                                                            value=0, enabled=False,
                                                            group='Current values')
        self.params['currentIntensity'] = paramgui.NumericParam('Current Intensity',
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

        # -- Module for saving the data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR)

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
        layoutCol2.addWidget(currentValues)

        layoutCol3.addWidget(amParams)
        layoutCol3.addWidget(fadeParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(self.saveData)

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
        '''This function reads the GUI inputs and populates a list of dicts, one
        per stimulus condition, containing the type and the type-specific
        parameters needed to build each sound. This function is called by
        prepare_next_trial at the beginning of the experiment and whenever we
        run out of conditions to present.'''

        stimConditions = []

        if self.params['includeAM'].get_string() == 'Yes':
            rateLow = self.params['amRateLow'].get_value()
            rateHigh = self.params['amRateHigh'].get_value()
            nRates = int(self.params['amNRates'].get_value())
            rates = np.logspace(np.log10(rateLow), np.log10(rateHigh), nRates) if nRates>1 else [rateLow]
            amIntensity = self.params['amIntensity'].get_value()
            for rate in rates:
                stimConditions.append({'stimType':'AM', 'modRate':rate,
                                       'intensity':amIntensity})

        if self.params['includeFading'].get_string() == 'Yes':
            intensityLow = self.params['fadeIntensityLow'].get_value()
            intensityHigh = self.params['fadeIntensityHigh'].get_value()
            for fadeDirection in ['fade_in','fade_out']:
                stimConditions.append({
                    'stimType': 'FadingNoise',
                    'intensityLow': intensityLow,
                    'intensityHigh': intensityHigh,
                    'fadeDirection': fadeDirection,
                })

        if not stimConditions:
            raise ValueError('At least one of AM noise or fading noise must be included.')

        stimOrder = self.params['stimOrder'].get_string()
        if stimOrder == 'Random':
            random.shuffle(stimConditions)

        self.soundParamList = stimConditions

    def prepare_next_trial(self, nextTrial):
        '''
        Prepare the target sound, send state matrix to the statemachine, and
        update the list of GUI parameters so that we can save the history of the
        type, intensity, and amplitude parameters for each trial.
        '''

        if nextTrial > self.params['nMaxTrials'].get_value():
            self.dispatcher.widget.stop()
            if self.saveOnStop.isChecked():
                self.save_to_file()
            return

        if nextTrial > 0:  # Do not update the history before the first trial
            self.params.update_history(nextTrial-1)

        self.sm.reset_transitions()

        # -- Choose an ISI randomly --
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['isiMean'].get_value() + \
              self.params['isiHalfRange'].get_value()*randNum
        self.params['isi'].set_value(isi)

        # -- Get the sound condition from the parameter list --
        # If the parameter list is empty, populate it --
        try:
            self.trialParams = self.soundParamList.pop(0) #pop(0) pops from the left
        except IndexError:
            self.populate_sound_params()
            self.trialParams = self.soundParamList.pop(0)

        stimType = self.trialParams['stimType']
        stimDuration = self.params['stimDuration'].get_value()

        soundLocation = self.params['soundLocation'].get_string()

        # -- Determine the sound presentation mode and prepare the appropriate sound --
        if stimType == 'AM':
            targetAmp = self.noiseCal.find_amplitude(self.trialParams['intensity'])
            if soundLocation == 'left':
                targetAmp = np.array([targetAmp[0], 0])
            elif soundLocation == 'right':
                targetAmp = np.array([0, targetAmp[1]])
            sound = {'type':'AM', 'duration':stimDuration,
                     'amplitude':targetAmp, 'modFrequency':self.trialParams['modRate']}
            currentIntensity = self.trialParams['intensity']
            self.params['currentAMRate'].set_value(self.trialParams['modRate'])
        elif stimType == 'FadingNoise':
            intensityLow = self.trialParams['intensityLow']
            intensityHigh = self.trialParams['intensityHigh']
            fadeDirection = self.trialParams['fadeDirection']
            self.params['fadeDirection'].set_string(fadeDirection)
            if fadeDirection == 'fade_in':
                intensityStart, intensityEnd = intensityLow, intensityHigh
            else:
                intensityStart, intensityEnd = intensityHigh, intensityLow
            targetAmp = self.noiseCal.find_amplitude(intensityEnd)
            if soundLocation == 'left':
                targetAmp = np.array([targetAmp[0], 0])
            elif soundLocation == 'right':
                targetAmp = np.array([0, targetAmp[1]])
            ampRatio = 10**((intensityStart-intensityEnd)/20.0)
            sound = {'type':'loomingNoise', 'duration':stimDuration,
                     'amplitude':targetAmp, 'amplitudeStart':ampRatio, 'amplitudeEnd':1.0}
            currentIntensity = intensityEnd

        stimOutput = stimSync
        serialOutput = 1
        self.soundClient.set_sound(1,sound)

        self.params['currentStimType'].set_string(stimType)
        self.params['currentIntensity'].set_value(currentIntensity)
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
