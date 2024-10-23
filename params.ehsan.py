"""
Parameters for paradigms during optogenetic inactivation of AC-pStr axons.
"""

optoTuningFreq = {'subject':'arch000','experimenter':'ehsan', 'minFreq':2000, 'maxFreq':40000,
                  'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
                  'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                  'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                  'laserTrialsFraction':0.25}

optoTuningAM = {'subject':'arch000','experimenter':'ehsan', 'minFreq':4, 'maxFreq':128, 'numTones':11,
                'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
                'minInt':60,'maxInt':60, 'syncLightMode':'from_stim_offset',
                'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                'laserTrialsFraction':0.25}

optoNaturalCategories = {'subject':'arch000','experimenter':'ehsan', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                         'laserMode':'bilateral', 'laserDuration':4.2, 'fractionLaserTrials':0.25,
                         'targetMaxIntensity':70, 'soundsSubset':'onePerCateg'}

optoNaturalInstances = {'subject':'arch000','experimenter':'ehsan', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                         'laserMode':'bilateral', 'laserDuration':4.2, 'fractionLaserTrials':0.25,
                         'targetMaxIntensity':70, 'soundsSubset':'twoPerTwoCateg'}

#                         'delayToTargetMean':3.5, 'delayToTargetHalfRange':0.5,




