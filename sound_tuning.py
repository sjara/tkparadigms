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
        self.params['session_ID'] = paramgui.StringParam('Session ID',value='',
                                                       group='Session parameters')
        self.params['n_max_trials'] = paramgui.NumericParam('N trials (max)',value=99999,
                                                       group='Session parameters')
        session_params = self.params.layout_group('Session parameters')

        self.params['include_AM'] = paramgui.MenuParam('Include AM noise',
                                                      ['No','Yes'],
                                                      value=1, group='AM noise')
        self.params['AM_rate_low'] = paramgui.NumericParam('Rate Low (Hz)',
                                                         value=4, group='AM noise')
        self.params['AM_rate_high'] = paramgui.NumericParam('Rate High (Hz)',
                                                          value=16, group='AM noise')
        self.params['AM_n_rates'] = paramgui.NumericParam('N Rates', value=3, group='AM noise')
        self.params['AM_intensity'] = paramgui.NumericParam('Intensity (dB SPL)',
                                                           value=60, group='AM noise')
        self.params['current_AM_rate'] = paramgui.NumericParam('Current AM Rate (Hz)',
                                                             value=0, enabled=False,
                                                             decimals=3,
                                                             group='AM noise')
        am_params = self.params.layout_group('AM noise')

        self.params['include_fading'] = paramgui.MenuParam('Include fading noise',
                                                            ['No','Yes'],
                                                            value=1, group='Fading noise')
        self.params['fade_intensity_low'] = paramgui.NumericParam('Lowest Intensity (dB SPL)',
                                                                 value=45, group='Fading noise')
        self.params['fade_intensity_high'] = paramgui.NumericParam('Highest Intensity (dB SPL)',
                                                                  value=75, group='Fading noise')
        self.params['fade_direction'] = paramgui.MenuParam('Fade Direction',
                                                          ['fade_in','fade_out'],
                                                          value=0, enabled=False,
                                                          group='Fading noise')
        fade_params = self.params.layout_group('Fading noise')

        self.params['stim_duration'] = paramgui.NumericParam('Stim Duration (s)',
                                                        value=1.0,
                                                        group='Stim parameters')
        self.params['ISI_mean'] = paramgui.NumericParam('ISI Mean (s)',
                                                       value=1.2,
                                                       group='Stim parameters')
        self.params['ISI_half_range'] = paramgui.NumericParam('ISI +/-',
                                                      value=0.2,
                                                      group='Stim parameters')
        self.params['ISI'] = paramgui.NumericParam('ISI (s)',
                                                   value=2, enabled=False, decimals=3,
                                                   group='Stim parameters')
        self.params['stim_order'] = paramgui.MenuParam('Order',
                                                         ['Ordered','Random'],
                                                         value=1,group='Stim parameters')
        self.params['sound_location'] = paramgui.MenuParam('Sound Location',
                                                          ['Binaural', 'Left', 'Right'],
                                                          value=0, group='Stim parameters')
        stim_params = self.params.layout_group('Stim parameters')

        self.params['current_stim_type'] = paramgui.MenuParam('Current Stim Type',
                                                            ['AM_noise','fading_noise'],
                                                            value=0, enabled=False,
                                                            group='Current values')
        self.params['current_intensity'] = paramgui.NumericParam('Current Intensity',
                                                                 value=0,
                                                                 enabled=False,
                                                                 group='Current values')
        self.params['current_amp_L'] = paramgui.NumericParam('Current Amplitude - L',value=0,
                                                           enabled=False,
                                                           group='Current values',
                                                           decimals=4)
        self.params['current_amp_R'] = paramgui.NumericParam('Current Amplitude - R',value=0,
                                                           enabled=False,
                                                           group='Current values',
                                                           decimals=4)
        current_values = self.params.layout_group('Current values')

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

        layoutCol1.addWidget(session_params)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)
        layoutCol1.addWidget(self.saveOnStop)

        layoutCol2.addWidget(stim_params)
        layoutCol2.addStretch()
        layoutCol2.addWidget(current_values)

        layoutCol3.addWidget(am_params)
        layoutCol3.addWidget(fade_params)
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
        self.trial_params = []
        self.sound_param_list = []

    def populate_sound_params(self):
        '''This function reads the GUI inputs and populates a list of dicts, one
        per stimulus condition, containing the type and the type-specific
        parameters needed to build each sound. This function is called by
        prepare_next_trial at the beginning of the experiment and whenever we
        run out of conditions to present.'''

        stim_conditions = []

        if self.params['include_AM'].get_string() == 'Yes':
            rate_low = self.params['AM_rate_low'].get_value()
            rate_high = self.params['AM_rate_high'].get_value()
            n_rates = int(self.params['AM_n_rates'].get_value())
            rates = np.logspace(np.log10(rate_low), np.log10(rate_high), n_rates) if n_rates>1 else [rate_low]
            am_intensity = self.params['AM_intensity'].get_value()
            for rate in rates:
                stim_conditions.append({'stim_type':'AM_noise', 'mod_rate':rate,
                                       'intensity':am_intensity})

        if self.params['include_fading'].get_string() == 'Yes':
            intensity_low = self.params['fade_intensity_low'].get_value()
            intensity_high = self.params['fade_intensity_high'].get_value()
            for fade_direction in ['fade_in','fade_out']:
                stim_conditions.append({
                    'stim_type': 'fading_noise',
                    'intensity_low': intensity_low,
                    'intensity_high': intensity_high,
                    'fade_direction': fade_direction,
                })

        if not stim_conditions:
            raise ValueError('At least one of AM noise or fading noise must be included.')

        stim_order = self.params['stim_order'].get_string()
        if stim_order == 'Random':
            random.shuffle(stim_conditions)

        self.sound_param_list = stim_conditions

    def prepare_next_trial(self, next_trial):
        '''
        Prepare the target sound, send state matrix to the statemachine, and
        update the list of GUI parameters so that we can save the history of the
        type, intensity, and amplitude parameters for each trial.
        '''

        if next_trial > self.params['n_max_trials'].get_value():
            self.dispatcher.widget.stop()
            if self.saveOnStop.isChecked():
                self.save_to_file()
            return

        if next_trial > 0:  # Do not update the history before the first trial
            self.params.update_history(next_trial-1)

        self.sm.reset_transitions()

        # -- Choose an ISI randomly --
        rand_num = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['ISI_mean'].get_value() + \
              self.params['ISI_half_range'].get_value()*rand_num
        self.params['ISI'].set_value(isi)

        # -- Get the sound condition from the parameter list --
        # If the parameter list is empty, populate it --
        try:
            self.trial_params = self.sound_param_list.pop(0) #pop(0) pops from the left
        except IndexError:
            self.populate_sound_params()
            self.trial_params = self.sound_param_list.pop(0)

        stim_type = self.trial_params['stim_type']
        stim_duration = self.params['stim_duration'].get_value()

        sound_location = self.params['sound_location'].get_string()

        # -- Determine the sound presentation mode and prepare the appropriate sound --
        if stim_type == 'AM_noise':
            target_amp = self.noiseCal.find_amplitude(self.trial_params['intensity'])
            if sound_location == 'Left':
                target_amp = np.array([target_amp[0], 0])
            elif sound_location == 'Right':
                target_amp = np.array([0, target_amp[1]])
            sound = {'type':'AM', 'duration':stim_duration,
                     'amplitude':target_amp, 'modFrequency':self.trial_params['mod_rate']}
            current_intensity = self.trial_params['intensity']
            self.params['current_AM_rate'].set_value(self.trial_params['mod_rate'])
        elif stim_type == 'fading_noise':
            intensity_low = self.trial_params['intensity_low']
            intensity_high = self.trial_params['intensity_high']
            fade_direction = self.trial_params['fade_direction']
            self.params['fade_direction'].set_string(fade_direction)
            if fade_direction == 'fade_in':
                intensity_start, intensity_end = intensity_low, intensity_high
            else:
                intensity_start, intensity_end = intensity_high, intensity_low
            target_amp = self.noiseCal.find_amplitude(intensity_end)
            if sound_location == 'Left':
                target_amp = np.array([target_amp[0], 0])
            elif sound_location == 'Right':
                target_amp = np.array([0, target_amp[1]])
            amp_ratio = 10**((intensity_start-intensity_end)/20.0)
            sound = {'type':'fadingNoise', 'duration':stim_duration,
                     'amplitude':target_amp, 'amplitudeStart':amp_ratio, 'amplitudeEnd':1.0}
            current_intensity = intensity_end

        stim_output = stimSync
        serial_output = 1
        self.soundClient.set_sound(1,sound)

        self.params['current_stim_type'].set_string(stim_type)
        self.params['current_intensity'].set_value(current_intensity)
        self.params['current_amp_L'].set_value(target_amp[0])
        self.params['current_amp_R'].set_value(target_amp[1])

        # -- Prepare the state transition matrix --
        self.sm.add_state(name='startTrial', statetimer = 0,
                          transitions={'Tup':'outputOn'})
        self.sm.add_state(name='outputOn', statetimer=stim_duration,
                          transitions={'Tup':'outputOff'},
                          outputsOn=stim_output,
                          serialOut=serial_output)
        self.sm.add_state(name='outputOff', statetimer=isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=stim_output)

        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        session_id = self.params['session_ID'].get_value()
        suffix = '' if session_id == '' else '_' + session_id
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
