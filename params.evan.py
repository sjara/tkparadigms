"""
Parameters for taskontrol paradigms.
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

# WARNING! playing natural sounds so that the nominal SPL is actually accomplished depends on the existence of a chord calibration
# file, and that the settings file has the correct line commented so that this file is actually used
# in the case that the settings file indicates "none", it is still possible to run by setting the SPL here - the actual loudness then
# will be the value here minus 60 dB adjusted on a default voltage of 0.01 V.
natSounds = {'subject':'imag022','experimenter':'evan', 'targetMaxIntensity':70} 


# -- For video sync light --
#, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }
