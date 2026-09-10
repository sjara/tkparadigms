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
        self.sineCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_SINE)

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

        self.params['include_tone'] = paramgui.MenuParam('Include pure tones',
                                                      ['No','Yes'],
                                                      value=0, group='Pure tones')
        self.params['tone_freq_low'] = paramgui.NumericParam('Freq Low (Hz)',
                                                         value=2000, group='Pure tones')
        self.params['tone_freq_high'] = paramgui.NumericParam('Freq High (Hz)',
                                                          value=40000, group='Pure tones')
        self.params['tone_n_freq'] = paramgui.NumericParam('N Frequencies', value=16,
                                                              group='Pure tones')
        self.params['tone_intensity'] = paramgui.NumericParam('Intensity (dB SPL)',
                                                           value=60, group='Pure tones')
        self.params['current_tone_freq'] = paramgui.NumericParam('Current Frequency (Hz)',
                                                             value=0, enabled=False,
                                                             decimals=3,
                                                             group='Pure tones')
        tone_params = self.params.layout_group('Pure tones')

        self.params['include_AM'] = paramgui.MenuParam('Include AM noise',
                                                      ['No','Yes'],
                                                      value=0, group='AM noise')
        self.params['AM_rate_low'] = paramgui.NumericParam('Rate Low (Hz)',
                                                         value=4, group='AM noise')
        self.params['AM_rate_high'] = paramgui.NumericParam('Rate High (Hz)',
                                                          value=128, group='AM noise')
        self.params['AM_n_rates'] = paramgui.NumericParam('N Rates', value=11, group='AM noise')
        self.params['AM_intensity'] = paramgui.NumericParam('Intensity (dB SPL)',
                                                           value=60, group='AM noise')
        self.params['current_AM_rate'] = paramgui.NumericParam('Current AM Rate (Hz)',
                                                             value=0, enabled=False,
                                                             decimals=3,
                                                             group='AM noise')
        am_params = self.params.layout_group('AM noise')

        self.params['include_fading'] = paramgui.MenuParam('Include fading noise',
                                                            ['No','Yes'],
                                                            value=0, group='Fading noise')
        self.params['fade_intensity_low'] = paramgui.NumericParam('Lowest Intensity (dB SPL)',
                                                                 value=45, group='Fading noise')
        self.params['fade_intensity_high'] = paramgui.NumericParam('Highest Intensity (dB SPL)',
                                                                  value=75, group='Fading noise')
        self.params['fade_direction'] = paramgui.MenuParam('Fade Direction',
                                                          ['Fade_in','Fade_out'],
                                                          value=0, enabled=False,
                                                          group='Fading noise')
        fade_params = self.params.layout_group('Fading noise')

        self.params['include_chord3t'] = paramgui.MenuParam('Include chord',
                                                          ['No','Yes'],
                                                          value=0, group='Chord 3 tones')
        self.params['chord3t_F0'] = paramgui.NumericParam('F0 (Hz)',
                                                        value=4000, group='Chord 3 tones')
        self.params['chord3t_n_possible_middle'] = paramgui.MenuParam('N possible middle',
                                                          ['1','3','5','7'],
                                                          value=2, group='Chord 3 tones')
        self.params['chord3t_middle_scheme'] = paramgui.MenuParam('Middle tone scheme',
                                                          ['Irrational','Linear'],
                                                          value=0, group='Chord 3 tones')
        self.params['chord3t_intensity'] = paramgui.NumericParam('Intensity (dB SPL)',
                                                               value=60, group='Chord 3 tones')
        self.params['current_chord3t_middle_octave'] = paramgui.NumericParam(
            'Current Middle Octave', value=0, enabled=False, decimals=3,
            group='Chord 3 tones')
        chord_params = self.params.layout_group('Chord 3 tones')

        self.params['include_FM'] = paramgui.MenuParam('Include FM',
                                                      ['No','Yes'],
                                                      value=0, group='FM sounds')
        self.params['FM_center_freq'] = paramgui.NumericParam('Center Frequency (Hz)',
                                                             value=4000, group='FM sounds')
        self.params['FM_slope_min'] = paramgui.NumericParam('Min abs slope (oct/sec)',
                                                            value=5, group='FM sounds')
        self.params['FM_slope_max'] = paramgui.NumericParam('Max abs slope (oct/sec)',
                                                            value=40, group='FM sounds')
        self.params['FM_n_slopes'] = paramgui.NumericParam('N Slopes', value=8, group='FM sounds')
        self.params['FM_intensity'] = paramgui.NumericParam('Intensity (dB SPL)',
                                                           value=60, group='FM sounds')
        self.params['current_FM_slope'] = paramgui.NumericParam('Current Slope (oct/sec)',
                                                                value=0, enabled=False,
                                                                decimals=3,
                                                                group='FM sounds')
        fm_params = self.params.layout_group('FM sounds')

        self.params['stim_duration'] = paramgui.NumericParam('Stim Duration (s)',
                                                        value=0.5,
                                                        group='Stim parameters')
        self.params['ISI_mean'] = paramgui.NumericParam('ISI Mean (s)',
                                                       value=1.6,
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
                                                            ['Pure_tone','AM_noise','Fading_noise','Chord_3t','FM'],
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
        layoutCol4 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)
        layoutMain.addLayout(layoutCol4)

        self.saveOnStop = QtWidgets.QCheckBox('Save data on auto-stop')
        self.saveOnStop.setChecked(True)

        self.buttonResetStimSet = QtWidgets.QPushButton('Reset stimulus set')
        self.buttonResetStimSet.setFixedHeight(2*self.buttonResetStimSet.sizeHint().height())

        layoutCol1.addWidget(session_params)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.buttonResetStimSet)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)
        layoutCol1.addWidget(self.saveOnStop)

        layoutCol2.addWidget(stim_params)
        layoutCol2.addStretch()
        layoutCol2.addWidget(current_values)
        layoutCol2.addStretch()
        layoutCol2.addWidget(self.saveData)

        layoutCol3.addWidget(tone_params)
        layoutCol3.addWidget(am_params)
        layoutCol3.addWidget(fade_params)
        layoutCol3.addStretch()

        layoutCol4.addWidget(chord_params)
        layoutCol4.addWidget(fm_params)
        layoutCol4.addStretch()

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Connect signals from dispatcher --
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        # -- Connect the reset stimulus set button --
        self.buttonResetStimSet.clicked.connect(self.reset_stim_set)

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

    def chord_middle_octaves_linear(self, n_middle_tones):
        '''Return the candidate octave offsets (relative to F0) for the middle
        tone of the chord, symmetric around 1 octave (i.e. 2*F0).
        n_middle_tones=1 -> [1]
        n_middle_tones=3 -> [0.5, 1, 1.5]
        n_middle_tones=5 -> [1/3, 2/3, 1, 4/3, 5/3]
        n_middle_tones=7 -> [1/4, 1/2, 3/4, 1, 5/4, 3/2, 7/4]
        These are all simple rational fractions of an octave, so most of them
        land close to other harmonic ratios (e.g. 1/2 octave = a just fifth).
        '''
        step = 2.0/(n_middle_tones+1)
        return 1 + step*(np.arange(n_middle_tones) - (n_middle_tones-1)/2.0)

    def chord_middle_octaves_irrational(self, n_middle_tones, irrational_step=(np.sqrt(5)-1)/2):
        '''Return candidate octave offsets (relative to F0) for the middle tone
        of the chord, symmetric around 1 octave (i.e. 2*F0). The offsets from
        the center are generated from integer multiples of an irrational
        number (a Weyl/golden-ratio equidistribution sequence), so (unlike
        simple rational fractions of an octave, e.g. 1/2, 1/3, 2/3, which land
        close to other harmonic ratios) they spread out over the octave
        without clustering near any simple ratio, and never repeat or
        coincide with each other.

        n_middle_tones=1 -> [1]
        n_middle_tones=3 -> [1-d1, 1, 1+d1]
        n_middle_tones=5 -> [1-d1, 1-d2, 1, 1+d2, 1+d1]
        (unsorted order shown; sorted by the caller)

        The default irrational_step is the golden ratio conjugate
        (sqrt(5)-1)/2 ~ 0.618, which is the "most irrational" number (worst
        rational approximation), making it the standard choice for generating
        maximally non-resonant / maximally dissonant sampling points. When
        n_middle_tones is odd, the harmonic octave (1, i.e. 2*F0) is included
        as the (symmetric) center/reference condition.
        '''
        n_pairs = n_middle_tones//2
        octaves = [1.0] if n_middle_tones%2 else []
        for pair_index in range(1, n_pairs+1):
            offset = (pair_index*irrational_step) % 1.0
            octaves.extend([1.0-offset, 1.0+offset])
        return np.array(octaves)

    def populate_sound_params(self):
        '''This function reads the GUI inputs and populates a list of dicts, one
        per stimulus condition, containing the type and the type-specific
        parameters needed to build each sound. This function is called by
        prepare_next_trial at the beginning of the experiment and whenever we
        run out of conditions to present.'''

        stim_conditions = []

        if self.params['include_tone'].get_string() == 'Yes':
            freq_low = self.params['tone_freq_low'].get_value()
            freq_high = self.params['tone_freq_high'].get_value()
            n_freq = int(self.params['tone_n_freq'].get_value())
            freqs = np.logspace(np.log10(freq_low), np.log10(freq_high), n_freq) if n_freq>1 else [freq_low]
            tone_intensity = self.params['tone_intensity'].get_value()
            for freq in freqs:
                stim_conditions.append({'stim_type':'Pure_tone', 'frequency':freq,
                                       'intensity':tone_intensity})

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
            for fade_direction in ['Fade_in','Fade_out']:
                stim_conditions.append({
                    'stim_type': 'Fading_noise',
                    'intensity_low': intensity_low,
                    'intensity_high': intensity_high,
                    'fade_direction': fade_direction,
                })

        if self.params['include_chord3t'].get_string() == 'Yes':
            chord_F0 = self.params['chord3t_F0'].get_value()
            n_middle_tones = int(self.params['chord3t_n_possible_middle'].get_string())
            middle_scheme = self.params['chord3t_middle_scheme'].get_string()
            if middle_scheme == 'Linear':
                middle_octaves = np.sort(self.chord_middle_octaves_linear(n_middle_tones))
            else:
                middle_octaves = np.sort(self.chord_middle_octaves_irrational(n_middle_tones))
            chord_intensity = self.params['chord3t_intensity'].get_value()
            for middle_octave in middle_octaves:
                stim_conditions.append({
                    'stim_type': 'Chord_3t',
                    'F0': chord_F0,
                    'middle_octave': middle_octave,
                    'intensity': chord_intensity,
                })

        if self.params['include_FM'].get_string() == 'Yes':
            fm_center_freq = self.params['FM_center_freq'].get_value()
            slope_min = self.params['FM_slope_min'].get_value()
            slope_max = self.params['FM_slope_max'].get_value()
            n_slopes = int(self.params['FM_n_slopes'].get_value())
            if n_slopes<=1:
                slopes = [slope_max]
            else:
                n_pairs = n_slopes//2
                slope_magnitudes = np.logspace(np.log10(slope_min), np.log10(slope_max), n_pairs) \
                    if n_pairs>1 else [slope_max]
                slopes = np.concatenate([-np.array(slope_magnitudes)[::-1], slope_magnitudes])
                if n_slopes%2:
                    slopes = np.concatenate([slopes[:n_pairs], [0], slopes[n_pairs:]])
            fm_intensity = self.params['FM_intensity'].get_value()
            for slope in slopes:
                stim_conditions.append({
                    'stim_type': 'FM',
                    'center_freq': fm_center_freq,
                    'slope': slope,
                    'intensity': fm_intensity,
                })

        stim_order = self.params['stim_order'].get_string()
        if stim_order == 'Random':
            random.shuffle(stim_conditions)

        self.sound_param_list = stim_conditions

    def reset_stim_set(self):
        '''Discard any remaining conditions from the current set, so that the
        next trial regenerates the list of conditions from the current GUI
        parameter values. Triggered by button-clicked signal.'''
        self.sound_param_list = []

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
            if not self.sound_param_list:
                print('No sound type is included. Enable at least one "Include ..." '
                      'parameter (Pure tones, AM noise, Fading noise, Chord, or FM).')
                self.dispatcher.widget.stop()
                return
            self.trial_params = self.sound_param_list.pop(0)

        stim_type = self.trial_params['stim_type']
        stim_duration = self.params['stim_duration'].get_value()

        sound_location = self.params['sound_location'].get_string()

        # -- Determine the sound presentation mode and prepare the appropriate sound --
        if stim_type == 'Pure_tone':
            tone_freq = self.trial_params['frequency']
            tone_intensity = self.trial_params['intensity']
            target_amp = self.sineCal.find_amplitude(tone_freq, tone_intensity)
            if sound_location == 'Left':
                target_amp = np.array([target_amp[0], 0])
            elif sound_location == 'Right':
                target_amp = np.array([0, target_amp[1]])
            sound = {'type':'tone', 'duration':stim_duration,
                     'amplitude':target_amp, 'frequency':tone_freq}
            current_intensity = tone_intensity
            self.params['current_tone_freq'].set_value(tone_freq)
        elif stim_type == 'AM_noise':
            target_amp = self.noiseCal.find_amplitude(self.trial_params['intensity'])
            if sound_location == 'Left':
                target_amp = np.array([target_amp[0], 0])
            elif sound_location == 'Right':
                target_amp = np.array([0, target_amp[1]])
            sound = {'type':'AM', 'duration':stim_duration,
                     'amplitude':target_amp, 'modFrequency':self.trial_params['mod_rate']}
            current_intensity = self.trial_params['intensity']
            self.params['current_AM_rate'].set_value(self.trial_params['mod_rate'])
        elif stim_type == 'Fading_noise':
            intensity_low = self.trial_params['intensity_low']
            intensity_high = self.trial_params['intensity_high']
            fade_direction = self.trial_params['fade_direction']
            self.params['fade_direction'].set_string(fade_direction)
            if fade_direction == 'Fade_in':
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
        elif stim_type == 'Chord_3t':
            chord_F0 = self.trial_params['F0']
            middle_octave = self.trial_params['middle_octave']
            chord_intensity = self.trial_params['intensity']
            octaves = [0, middle_octave, 2]
            freq_each_comp = chord_F0 * (2.0**np.array(octaves))
            # -- amp_each_comp has shape (nTones, nChannels) --
            amp_each_comp = self.sineCal.find_amplitudes(freq_each_comp, chord_intensity)
            amp_F0 = amp_each_comp[0]
            # -- Per-tone correction factor relative to F0, averaged across channels --
            calibration = amp_each_comp.mean(axis=1)/amp_F0.mean()
            target_amp = amp_F0
            if sound_location == 'Left':
                target_amp = np.array([target_amp[0], 0])
            elif sound_location == 'Right':
                target_amp = np.array([0, target_amp[1]])
            sound = {'type':'chordFromOctaves', 'duration':stim_duration,
                     'amplitude':target_amp, 'frequency':chord_F0,
                     'octaves':octaves, 'calibration':calibration}
            current_intensity = chord_intensity
            self.params['current_chord3t_middle_octave'].set_value(middle_octave)
        elif stim_type == 'FM':
            fm_center_freq = self.trial_params['center_freq']
            fm_slope = self.trial_params['slope']
            fm_intensity = self.trial_params['intensity']
            target_amp = self.sineCal.find_amplitude(fm_center_freq, fm_intensity)
            if sound_location == 'Left':
                target_amp = np.array([target_amp[0], 0])
            elif sound_location == 'Right':
                target_amp = np.array([0, target_amp[1]])
            sound = {'type':'FMtrain', 'duration':stim_duration,
                     'amplitude':target_amp, 'centerFrequency':fm_center_freq,
                     'slope':fm_slope, 'sweepDuration':0.1, 'silenceDuration':0.1}
            current_intensity = fm_intensity
            self.params['current_FM_slope'].set_value(fm_slope)

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
