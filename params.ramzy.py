# Parameters for paradigms used by Ramzy

# === AM tuning (test) ===
tuningFreq = {'subject':'test000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
              'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
              'soundLocation':'left'}
              
tuningAM = {'subject':'test000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':60,
            'maxInt':60, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED',
            'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
            'soundLocation':'left'}

#test000 = {'subject':'test000', **tuningFreq}
test000 = {'subject':'test000', **tuningAM}


"""
Parameters for paradigms during optogenetic activation of PV neurons in the auditory cortex (based on ehsan's params).
"""

optoTuningFreq = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                  'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':2.0, 'isiHalfRange':0.5,
                  'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                  'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                  'laserTrialsFraction':0.25}

optoTuningAM = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
                'stimType':'AM', 'stimDur':0.5, 'isiMean':2.0, 'isiHalfRange':0.5,
                'minInt':60,'maxInt':60, 'syncLightMode':'from_stim_offset',
                'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                'laserTrialsFraction':0.25}

optoNaturalCategories = {'subject':'poni000','experimenter':'ramzy', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                         'laserMode':'bilateral', 'laserDuration':4.2, 'fractionLaserTrials':0.25,
                         'targetMaxIntensity':70, 'soundsSubset':'onePerCateg'}

optoNaturalInstances = {'subject':'poni000','experimenter':'ramzy', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                         'laserMode':'bilateral', 'laserDuration':4.2, 'fractionLaserTrials':0.25,
                         'targetMaxIntensity':70, 'soundsSubset':'twoPerTwoCateg'}

poniTuningSpont = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'stimType':'Noise', 
                   'stimDur':0.1, 'isiMean':2.0, 'isiHalfRange':0.5,
                        'minInt':0, 'maxInt':0, 'numInt':1, 'syncLightMode':'from_stim_offset','randomImageMode':'Random',
                        'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 
                        'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSub':0, 'nRowSub':0, 
                        'subGridPosH':0, 'subGridPosV':0, 'randomMode':'Random', 'imageTrialsFraction':1.0}

poniTuningFreq = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                        'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':2.0, 'isiHalfRange':0.5,
                        'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset','randomImageMode':'Random',
                        'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 
                        'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSub':0, 'nRowSub':0, 
                        'subGridPosH':0, 'subGridPosV':0, 'randomMode':'Random', 'imageTrialsFraction':1.0}

poniTuningAM = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
                    'stimType':'AM', 'stimDur':0.5, 'isiMean':2.0, 'isiHalfRange':0.5,
                    'minInt':60,'maxInt':60, 'syncLightMode':'from_stim_offset', 'randomImageMode':'Random',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 
                    'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSub':3, 'nRowSub':1, 
                    'subGridPosH':1, 'subGridPosV':2, 'randomMode':'Random', 'imageTrialsFraction':1.0}