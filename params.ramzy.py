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
                  'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
                  'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                  'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                  'laserTrialsFraction':0.25}

optoTuningAM = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
                'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
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

poniDisplayTuning = {'subject':'poni000','experimenter':'ramzy', 'interTrialInterval': 1.0, 'soundFrequency':1000,
                     'soundDuration':0.1, 'stimType':'Sine','soundIntensity':60, 'soundAmplitude':0.0, 
                     'lightIntensity':100, 'xOuterSize':4, 'yOuterSize':4, 'xInnerSize':3, 'yInnerSize':1, 
                     'xInnerInd':1, 'yInnerInd':2, 'randomMode':'Random', 'imageTrialsFraction':1.0, }
