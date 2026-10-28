"""
Check whether the sounds presented by sound_tuning.py would saturate on this rig.

For each stimulus condition, this script finds the amplitude from the rig's speaker
calibration (as the paradigm does), creates the waveform with taskontrol's
soundclient.create_soundwave(), and reports the peak absolute value of each channel.
Waveforms must stay within [-1, 1]: the jack server clips values outside this range,
and the pygame server converts to int16 and wraps around, which is worse.

Only pure tones are evaluated for now.

Usage (the same parameter arguments as the paradigm):
    python check_sound_saturation.py                          # sound_tuning GUI defaults
    python check_sound_saturation.py pure_tones               # dict from rigsettings.DEFAULT_PARAMSFILE
    python check_sound_saturation.py params.evan.py pure_tones
Options:
    --intensity DB       override the intensity (dB SPL) from the parameters
    --calibration FILE   sine calibration file (default: rigsettings.SPEAKER_CALIBRATION_SINE)
    --sampling-rate HZ   sampling rate of the sound server (default: 44100, as with pygame)

The exit status is 1 if any waveform saturates, and 0 otherwise.
"""

import sys
import argparse
import importlib.util
import numpy as np
from taskontrol import rigsettings
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import soundclient

FULL_SCALE = 1.0  # Largest absolute value a waveform can have without saturating

# -- Default values of the sound_tuning.py parameters used here (keep in sync with the paradigm) --
DEFAULT_PARAMS = {
    'tone_freq_low': 2000,
    'tone_freq_high': 40000,
    'tone_n_freq': 16,
    'tone_intensity': 60,
    'stim_duration': 0.5,
    'sound_location': 'Binaural',
}


def load_params(paramfile=None, paramdictname=None):
    """
    Return the paradigm defaults updated with the values of a dictionary in a params file.
    Only keys in DEFAULT_PARAMS are used; any other key in the dictionary is ignored.
    """
    params = dict(DEFAULT_PARAMS)
    if paramfile is not None:
        spec = importlib.util.spec_from_file_location('params_module', paramfile)
        params_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(params_module)
        try:
            param_dict = getattr(params_module, paramdictname)
        except AttributeError:
            sys.exit("There is no '{0}' in {1}".format(paramdictname, paramfile))
        params.update({key: value for key, value in param_dict.items() if key in params})
    return params


def apply_sound_location(target_amp, sound_location):
    """Silence one channel as sound_tuning.py does for 'Left' or 'Right'."""
    if sound_location == 'Left':
        target_amp = np.array([target_amp[0], 0])
    elif sound_location == 'Right':
        target_amp = np.array([0, target_amp[1]])
    return target_amp


def pure_tone_sounds(params, sine_cal):
    """
    Return a list of (description, intensity, sound_dict) for each pure-tone condition,
    built in the same way as in sound_tuning.py.
    """
    freq_low = params['tone_freq_low']
    freq_high = params['tone_freq_high']
    n_freq = int(params['tone_n_freq'])
    freqs = np.logspace(np.log10(freq_low), np.log10(freq_high), n_freq) if n_freq>1 else [freq_low]
    tone_intensity = params['tone_intensity']
    sounds = []
    for freq in freqs:
        target_amp = sine_cal.find_amplitude(freq, tone_intensity)
        target_amp = apply_sound_location(target_amp, params['sound_location'])
        sound = {'type':'tone', 'duration':params['stim_duration'],
                 'amplitude':target_amp, 'frequency':freq}
        sounds.append(('{:8.0f} Hz'.format(freq), tone_intensity, sound))
    return sounds


def evaluate_sounds(sounds, sampling_rate):
    """
    Create each waveform, print its peak value per channel, and return the number
    of waveforms that saturate.
    """
    header = '{:>11}  {:>9}  {:>8}  {:>8}  {:>8}  {:>8}  {:>12}  {}'.format(
        'Condition', 'Int (dB)', 'Amp L', 'Amp R', 'Peak L', 'Peak R', 'Max int (dB)', 'Status')
    print(header)
    print('-'*len(header))
    n_saturated = 0
    for description, intensity, sound in sounds:
        time_vec, sound_wave = soundclient.create_soundwave(dict(sound), sampling_rate)
        peak_each_channel = np.max(np.abs(sound_wave), axis=1)
        peak = peak_each_channel.max()
        # -- Highest intensity that this condition could have without saturating --
        max_intensity = intensity + 20*np.log10(FULL_SCALE/peak) if peak > 0 else np.inf
        saturated = peak > FULL_SCALE
        n_saturated += saturated
        print('{:>11}  {:9.1f}  {:8.4f}  {:8.4f}  {:8.4f}  {:8.4f}  {:12.1f}  {}'.format(
            description, intensity, sound['amplitude'][0], sound['amplitude'][1],
            peak_each_channel[0], peak_each_channel[1], max_intensity,
            'SATURATED' if saturated else 'OK'))
    return n_saturated


def main():
    parser = argparse.ArgumentParser(description='Check whether sound_tuning.py sounds saturate.')
    parser.add_argument('paramargs', nargs='*', metavar='[paramfile] paramdictname',
                        help='params file (default: rigsettings.DEFAULT_PARAMSFILE) and dict name')
    parser.add_argument('--intensity', type=float, default=None,
                        help='override the intensity (dB SPL) from the parameters')
    parser.add_argument('--calibration', default=rigsettings.SPEAKER_CALIBRATION_SINE,
                        help='sine calibration file (default: rigsettings.SPEAKER_CALIBRATION_SINE)')
    parser.add_argument('--sampling-rate', type=float, default=44100,
                        help='sampling rate of the sound server in Hz (default: 44100)')
    args = parser.parse_args()

    if len(args.paramargs) == 0:
        paramfile, paramdictname = None, None
    elif len(args.paramargs) == 1:
        paramfile, paramdictname = rigsettings.DEFAULT_PARAMSFILE, args.paramargs[0]
    elif len(args.paramargs) == 2:
        paramfile, paramdictname = args.paramargs
    else:
        parser.error('give at most two arguments: [paramfile] paramdictname')

    params = load_params(paramfile, paramdictname)
    if args.intensity is not None:
        params['tone_intensity'] = args.intensity

    if args.calibration is None:
        print('WARNING: no sine calibration file given. Using the default amplitudes '
              'from speakercalibration.Calibration, which do not reflect any rig.')
    sine_cal = speakercalibration.Calibration(args.calibration)

    print('Calibration file: {}'.format(args.calibration))
    if paramfile is not None:
        print('Parameters: {} from {}'.format(paramdictname, paramfile))
    print('Sound location: {}    Sampling rate: {:g} Hz    Full scale: +/-{:g}\n'.format(
        params['sound_location'], args.sampling_rate, FULL_SCALE))

    print('== Pure tones ==')
    n_saturated = evaluate_sounds(pure_tone_sounds(params, sine_cal), args.sampling_rate)

    print('\n{} waveform(s) saturated.'.format(n_saturated))
    return 1 if n_saturated else 0


if __name__ == "__main__":
    sys.exit(main())
