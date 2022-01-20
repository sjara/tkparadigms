tuningFRA = {'subject':'pals027','experimenter':'jenny', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1, 'isiHalfRange':0,
              'minInt':10, 'maxInt':60, 'numInt':6 }

tuningFreq = {'subject':'feat004','experimenter':'jenny', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':60, 'maxInt':70, 'numInt':2, 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }


tuningAM = {'subject':'feat004','experimenter':'jenny', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':60,
            'maxInt':60, 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

speechPilot = {'subject':'feat004', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':3.0,'delayToTargetHalfRange':1,'psycurveMode':'uniform', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

speechFT = {'subject':'feat004', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':3.0,'delayToTargetHalfRange':1,'psycurveMode':'uniform', 'relevantFeature':'spectral', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

speechVOT = {'subject':'feat004', 'experimenter':'jenny', 'outcomeMode':'passive_exposure', 'delayToTargetMean':3.0, 'delayToTargetHalfRange':1, 'psycurveMode':'uniform', 'relevantFeature':'temporal', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

speechTest = {'subject':'feat003', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':1.0,'delayToTargetHalfRange':0,'psycurveMode':'uniform', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

### Behavior ###
## VOT ##
VOTstage0 = {'experimenter':'jenny', 'outcomeMode':'sides_direct', 'relevantFeature':'temporal', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

VOTstage1 = {'experimenter':'jenny', 'outcomeMode':'direct', 'relevantFeature':'temporal', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

VOTstage2 = {'experimenter':'jenny', 'outcomeMode':'on_next_correct', 'relevantFeature':'temporal', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0.0,'automationMode':'increase_delay', 'targetMaxIntensity':60}

VOTstage3 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':60}

VOTstage4 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'psycurveMode':'uniform', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':60}

VOTBiasCorr = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'antibiasMode':'repeat_mistake', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':60}


bili034 = {'subject':'bili034', 'soundActionMode':'low_left', **VOTBiasCorr}

bili035 = {'subject':'bili035', 'soundActionMode':'low_left', **VOTBiasCorr}

bili036 = {'subject':'bili036', 'soundActionMode':'low_left', **VOTstage2}

bili037 = {'subject':'bili037', 'soundActionMode':'low_left', **VOTBiasCorr}

bili038 = {'subject':'bili038', 'soundActionMode':'low_left', **VOTstage2}

bili039 = {'subject':'bili039', 'soundActionMode':'high_left', **VOTstage2}

bili040 = {'subject':'bili040', 'soundActionMode':'high_left', **VOTstage2}

bili041 = {'subject':'bili041', 'soundActionMode':'high_left', **VOTstage2}

bili042 = {'subject':'bili042', 'soundActionMode':'high_left', **VOTBiasCorr}


## FT ##
FTstage0 = {'experimenter':'jenny', 'outcomeMode':'sides_direct', 'relevantFeature':'spectral', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

FTstage1 = {'experimenter':'jenny', 'outcomeMode':'direct', 'relevantFeature':'spectral', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

FTstage2 = {'experimenter':'jenny', 'outcomeMode':'on_next_correct', 'relevantFeature':'spectral', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0.0,'automationMode':'increase_delay', 'targetMaxIntensity':60}

FTstage3 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':60}

FTstage4 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'psycurveMode':'uniform', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':60}

FTBiasCorr = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'antibiasMode':'repeat_mistake', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':60}


bili043 = {'subject':'bili043', 'soundActionMode':'low_left', **FTstage3}

bili044 = {'subject':'bili044', 'soundActionMode':'low_left', **FTBiasCorr}

bili045 = {'subject':'bili045', 'soundActionMode':'low_left', **FTstage3}

bili046 = {'subject':'bili046', 'soundActionMode':'low_left', **FTstage3}

bili047 = {'subject':'bili047', 'soundActionMode':'low_left', **FTBiasCorr}

bili048 = {'subject':'bili048', 'soundActionMode':'high_left', **FTstage2}

bili049 = {'subject':'bili049', 'soundActionMode':'high_left', **FTstage3}

bili050 = {'subject':'bili050', 'soundActionMode':'high_left', **FTstage3}

bili051 = {'subject':'bili051', 'soundActionMode':'high_left', **FTstage3}
