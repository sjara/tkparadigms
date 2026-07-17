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

widefieldMapping = {'subject':'imag03X', 'experimenter':'Evan', 
              'sessionID':'12121212', 'nMaxTrials':285, 
              'freq1':3000,'intensity1':75, 'freq2':15500,
              'intensity2':70, 'freq3':28000,'intensity3':80,
              'stimDuration':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 
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
            'include_AM':'Yes', 'AM_rate_low':4, 'AM_rate_high':32, 'AM_n_rates':4, 'AM_intensity':70,
            'include_fading':'Yes', 'fade_intensity_low':45, 'fade_intensity_high':80, 'stim_duration':0.4}

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

