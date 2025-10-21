# Parameters for paradigms used by Ramzy

# === For Asym Study ===

stimInt = 40
tuningFreqL = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':stimInt, 'maxInt':stimInt, 'numInt':1, 'syncLightMode':'from_stim_offset',
              'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
              'soundLocation':'left'}
tuningFreqR = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':stimInt, 'maxInt':stimInt, 'numInt':1, 'syncLightMode':'from_stim_offset',
              'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
              'soundLocation':'right'}
              
tuningAML = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':stimInt,
            'maxInt':stimInt, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED',
            'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
            'soundLocation':'left'}
tuningAMR = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':stimInt,
            'maxInt':stimInt, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED',
            'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
            'soundLocation':'right'}

tuningAMtoneL = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
              'numModRates':5, 'minInt':stimInt, 'maxInt':stimInt, 'numInt':1, 'syncLightMode':'from_stim_offset',
              'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
              'soundLocation':'left','minModRate':4,'maxModRate':64,'numModRates':5}

tuningAMtoneR = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
              'numModRates':5, 'minInt':stimInt, 'maxInt':stimInt, 'numInt':1, 'syncLightMode':'from_stim_offset',
              'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
              'soundLocation':'right','minModRate':4,'maxModRate':64,'numModRates':5}

naturalSoundL = {'subject':'poni000','experimenter':'ramzy', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':3.5, 'delayToTargetHalfRange':0.5,
                         'targetMaxIntensity':stimInt,'soundLocation':'left'}

naturalSoundR = {'subject':'poni000','experimenter':'ramzy', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':3.5, 'delayToTargetHalfRange':0.5,
                         'targetMaxIntensity':stimInt,'soundLocation':'right'}


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

tuningAMtone = {'subject':'test000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
              'numModRates':5, 'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
              'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
              'soundLocation':'left','minModRate':4,'maxModRate':64,'numModRates':5}

#test000 = {'subject':'test000', **tuningFreq}
test000 = {'subject':'test000', **tuningAM}


"""
Parameters for paradigms during optogenetic activation of PV neurons in the auditory cortex (based on ehsan's params).
"""

optoTuningFreq = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                    'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':2.0, 'isiHalfRange':0.5,
                    'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'laserTrialsFraction':0.5}

optoTuningFreqEarbuds = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                    'numTones':16, 'stimType':'Sine', 'stimDur':0.25, 'isiMean':2.5, 'isiHalfRange':0.5,
                    'minInt':40, 'maxInt':40, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'soundLocation':'left',
                    'laserTrialsFraction':0.5,'laserFrontOverhang':0.25}

optoTuningAM = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
                    'stimType':'AM', 'stimDur':0.5, 'isiMean':2.0, 'isiHalfRange':0.5, 
                    'minInt':70,'maxInt':70, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'laserTrialsFraction':0.5}

optoValidation = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':2,
                    'stimType':'AM', 'stimDur':0.5, 'isiMean':2.5, 'isiHalfRange':0.5, 'soundTrialsFraction':0.6667,
                    'minInt':70,'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'off', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'laserTrialsFraction':0.25}

optoTuningAMtone = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                    'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':2.5, 'isiHalfRange':0.5,
                    'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'soundLocation':'binaural','minModRate':4,'maxModRate':64,'numModRates':2,
                    'laserTrialsFraction':0.5}

optoTuningAMtoneEarbuds = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                    'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':2.5, 'isiHalfRange':0.5,
                    'minInt':40, 'maxInt':40, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'soundLocation':'left','minModRate':4,'maxModRate':64,'numModRates':2,
                    'laserTrialsFraction':0.5}

optoNaturalCategories = {'subject':'poni000','experimenter':'ramzy', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                         'laserMode':'bilateral', 'laserDuration':4.2, 'fractionLaserTrials':0.25,
                         'targetMaxIntensity':70, 'soundsSubset':'onePerCateg'}

optoNaturalInstances = {'subject':'poni000','experimenter':'ramzy', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                         'laserMode':'bilateral', 'laserDuration':4.2, 'fractionLaserTrials':0.25,
                         'targetMaxIntensity':70, 'soundsSubset':'twoPerTwoCateg'}

poniTuningSpont = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128,
                         'stimType':'AM', 'stimDur':0.5, 'isiMean':2.5, 'isiHalfRange':0.5,
                         'minInt':-100, 'maxInt':-100, 'numInt':1, 'syncLightMode':'from_stim_offset','randomImageMode':'Random',
                         'screenBottomAxis':'Posterior','syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 
                         'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSubregion':0, 'nRowSubregion':0, 
                         'subregionPosX':0, 'subregionPosY':0, 'randomMode':'Random', 'imageTrialsFraction':1.0}

poniTuningFreq = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                         'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':2.0, 'isiHalfRange':0.5,
                         'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset','randomImageMode':'Random',
                         'screenBottomAxis':'Posterior','syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 
                         'lightIntensity':100, 'nColGrid':4, 'nRowGrid':1, 'nColSubregion':0, 'nRowSubregion':0, 
                         'subregionPosX':0, 'subregionPosY':0, 'randomMode':'Random', 'imageTrialsFraction':0.8}

poniTuningAM = {'subject':'poni000','experimenter':'ramzy', 'minFreq':4, 'maxFreq':128, 'numTones':11,
                    'stimType':'AM', 'stimDur':0.5, 'isiMean':2.0, 'isiHalfRange':0.5,
                    'minInt':70,'maxInt':70, 'syncLightMode':'from_stim_offset', 'randomImageMode':'Random',
                    'screenBottomAxis':'Posterior','syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 
                    'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSubregion':0, 'nRowSubregion':0, 
                    'subregionPosX':0, 'subregionPosY':0, 'randomMode':'Random', 'imageTrialsFraction':0.8}


poniTuningAMtone = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                    'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':2.5, 'isiHalfRange':0.5,
                    'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'soundLocation':'left','minModRate':4,'maxModRate':64,'numModRates':2, 
                    'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSubregion':0, 'nRowSubregion':0, 
                    'subregionPosX':0, 'subregionPosY':0, 'randomMode':'Random', 'imageTrialsFraction':0.8,
                    'imageFrontOverhang':0.25}

poniTuningAMtoneEarbuds = {'subject':'poni000','experimenter':'ramzy', 'minFreq':2000, 'maxFreq':40000,
                    'numTones':16, 'stimType':'AMtone', 'stimDur':0.5, 'isiMean':2.5, 'isiHalfRange':0.5,
                    'minInt':40, 'maxInt':40, 'numInt':1, 'syncLightMode':'from_stim_offset',
                    'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1,
                    'soundLocation':'left','minModRate':4,'maxModRate':64,'numModRates':2, 
                    'lightIntensity':100, 'nColGrid':4, 'nRowGrid':4, 'nColSubregion':0, 'nRowSubregion':0, 
                    'subregionPosX':0, 'subregionPosY':0, 'randomMode':'Random', 'imageTrialsFraction':0.8,
                    'imageFrontOverhang':0.25}