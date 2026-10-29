"""
This file defines the parameters for taskontrol paradigms WF (top block) and 2p (bottom block)
"""

#WF

lowtoneTrains70 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':3000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}
              
lowtoneTrains80 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':3000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':80, 'maxInt':80}

midtoneTrains70 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':15500, 'maxFreq':15500, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}

midtoneTrains80 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':15500, 'maxFreq':15500, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':80, 'maxInt':80}

hightoneTrains70 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':28000, 'maxFreq':28000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}
              
hightoneTrains80 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':28000, 'maxFreq':28000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':80, 'maxInt':80}
              
intensitytoneTrains = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':28000, 'numTones':3, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':80, 'numInt':2}
              
toneTrains = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':32000, 'numTones':3, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}

widefieldMapping_old = {'subject':'imag03X', 'experimenter':'Evan', 
              'sessionID':'12121212', 'nMaxTrials':285, 
              'freq1':3000,'intensity1':75, 'freq2':15500,
              'intensity2':70, 'freq3':28000,'intensity3':80,
              'stimDuration':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 
              'stimType':'ToneTrain'}
              

widefieldMapping = {'subject':'imag03X', 'experimenter':'Evan', 
              'sessionID':'12121212', 'nMaxTrials':285, 
              'N_FREQ_MAX':9, 'nFreq':9, 'stimDuration':0.5, 
              'isiMean':1.2, 'isiHalfRange':0.2, 
              'stimType':'ToneTrain'}

"""
Parameters for taskontrol paradigms. (2p)
"""

tuningFreqTrain = {'subject':'imag022','experimenter':'evan', 'minFreq':2000, 'maxFreq':40000,
                   'numTones':16, 'stimType':'ToneTrain', 'stimDur':0.5, 'isiMean':1.2,
                   'isiHalfRange':0.2, 'minInt':60, 'maxInt':60, 'numInt':1}

tuningAM = {'subject':'imag022','experimenter':'evan', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':60,
            'maxInt':60}

repeatAM = {'subject':'imag022','experimenter':'evan', 'minFreq':8, 'maxFreq':8, 'numTones':1,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':2.0, 'isiHalfRange':0.0, 'minInt':60,
            'maxInt':60}

tuningFreq = {'subject':'imag022','experimenter':'evan', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':60, 'maxInt':60, 'numInt':1}

AMfading = {'subject': 'imag03X', 'experimenter': 'evan', 'session_ID':'000', 'n_max_trials':320,
            'include_AM':'Yes', 'AM_rate_low':4, 'AM_rate_high':32, 'AM_n_rates':4, 'AM_intensity':65,
            'include_fading':'Yes', 'fade_intensity_low':45, 'fade_intensity_high':68, 'stim_duration':0.4}

# block_1: redo band noise, noise pair, and chords at second BF if 2 modes. use mode instead of median if 1 mode.
pure_tones = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':320,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_tone':'Yes', 'tone_freq_low':2000, 'tone_freq_high':40000,'tone_n_freq':16,
              'tone_intensity':73}

band_noise = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':300,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_bandnoise':'Yes', 'bandnoise_center_freq':8000, 'bandnoise_bandwidth_min':0.25, 'bandnoise_bandwidth_max':4,'bandnoise_n_bandwidths':5,
              'bandnoise_mod_rate':8,'bandnoise_intensity':65}

noise_pair = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':320,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left',
              'include_noisepair':'Yes', 'noisepair_center_freq':8000, 'noisepair_bandwidth':0.25, 'noisepair_sound_duration':0.1,
              'noisepair_gap_min':0.1, 'noisepair_gap_max':0.8, 'noisepair_n_gaps':4,'noisepair_intensity':60}

# do not run chords with an F0 above 10 kHz
chord_tones = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':250,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_chord3t':'Yes', 'chord3t_F0':4000, 'chord3t_n_possible_middle':'5',
              'chord3t_middle_scheme':'Irrational','chord3t_intensity':68}

# block_2: redo pure tones if run separately from block_1
fm_sounds_frange = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':300,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_FMfixedrange':'Yes', 'FMfixedrange_center_freq':8000, 'FMfixedrange_octave_range':6, 'FMfixedrange_slope_min':5,'FMfixedrange_slope_max':80,
              'FMfixedrange_n_slopes_per_direction':5,'FMfixedrange_intensity':70}

am_noise= {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':220,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_AM':'Yes', 'AM_rate_low':4, 'AM_rate_high':32,'AM_n_rates':4,
              'AM_intensity':65}

fading_noise = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':320,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_fading':'Yes', 'fade_intensity_low':45, 'fade_intensity_high':68}

#not currently used, but could be used in the future if we want to test FM sweeps with fixed duration instead of fixed frequency range
fm_sounds_fdur = {'experimenter':'evan','subject':'imag03X', 'session_ID':'000', 'n_max_trials':300,
              'stim_duration':0.5, 'ISI_mean':1.6, 'ISI_half_range':0.2, 'stim_order':'Random',
              'sound_location':'Left', 
              'include_FMfixeddur':'Yes', 'FMfixeddur_center_freq':4000, 'FMfixeddur_slope_min':5,'FMfixeddur_slope_max':80,
              'FMfixeddur_n_slopes_per_direction':5,'FMfixeddur_intensity':60}

# WARNING! playing natural sounds so that the nominal SPL is actually accomplished depends on the existence of a chord calibration
# file, and that the settings file has the correct line commented so that this file is actually used
# in the case that the settings file indicates "none", it is still possible to run by setting the SPL here - the actual loudness then
# will be the value here minus 60 dB adjusted on a default voltage of 0.01 V.
natSounds = {'subject':'imag03X','experimenter':'evan', 'targetMaxIntensity':70} 


# -- For video sync light --
#, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }
 
#toneTrains80LHH = {'subject':'imag02X', 'experimenter':'Willgaston', 
#              'minFreq':3000, 'maxFreq':32000, 'numTones':3, 
#              'stimType':'ToneTrain', 'stimDur':0.5,
#              'isiMean':1.2, 'isiHalfRange':0.2,
#              'minInt':80, 'maxInt':80}

#AMsounds = {'subject':'test000', 'experimenter':'Lizeth', 
#              'minFreq':8, 'maxFreq':16, 'numTones':2, 
#              'stimType':'AM', 'stimDur':1,
#              'isiMean':1.5, 'isiHalfRange':0.2,
#              'minInt':65, 'maxInt':65}

