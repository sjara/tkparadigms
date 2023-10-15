tuningFRA = {'subject':'pals027','experimenter':'jenny', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1, 'isiHalfRange':0,
              'minInt':10, 'maxInt':60, 'numInt':6 }

tuningFreq = {'subject':'feat004','experimenter':'jenny', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':60, 'maxInt':70, 'numInt':2, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }


tuningAM = {'subject':'feat004','experimenter':'jenny', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':60,
            'maxInt':60, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

widefieldLOW = {'subject':'wifi000','experimenter':'jenny', 'minFreq':4000, 'maxFreq':4000,
              'numTones':1, 'stimType':'Sine', 'stimDur':0.2, 'isiMean':2.5, 'isiHalfRange':0.5,
              'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }

widefieldMID = {'subject':'wifi000','experimenter':'jenny', 'minFreq':16000, 'maxFreq':16000,
              'numTones':1, 'stimType':'Sine', 'stimDur':0.2, 'isiMean':2.5, 'isiHalfRange':0.5,
              'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }

widefieldHIGH = {'subject':'wifi000','experimenter':'jenny', 'minFreq':32000, 'maxFreq':32000,
              'numTones':1, 'stimType':'Sine', 'stimDur':0.2, 'isiMean':2.5, 'isiHalfRange':0.5,
              'minInt':70, 'maxInt':70, 'numInt':1, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }

speechPilot = {'subject':'feat004', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':3.0,'delayToTargetHalfRange':1,'psycurveMode':'uniform', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

FTVOTBorders = {'subject':'feat005', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':3.0,'delayToTargetHalfRange':1,'psycurveMode':'uniform', 'relevantFeature':'spectral', 'irrelevantFeatureMode':'matrix_border', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 'targetMaxIntensity':60}

speechFT = {'subject':'feat004', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':3.0,'delayToTargetHalfRange':1,'psycurveMode':'uniform', 'relevantFeature':'spectral', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 'targetMaxIntensity':60}

speechVOT = {'subject':'feat004', 'experimenter':'jenny', 'outcomeMode':'passive_exposure', 'delayToTargetMean':3.0, 'delayToTargetHalfRange':1, 'psycurveMode':'extreme80pc', 'relevantFeature':'temporal', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1, 'targetMaxIntensity':60}

speechTest = {'subject':'feat003', 'experimenter':'jenny','outcomeMode':'passive_exposure','delayToTargetMean':1.0,'delayToTargetHalfRange':0,'psycurveMode':'uniform', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}

### Behavior ###
## AM Depth
AMstage1 = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'water_after_sound', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3}

AMstage2 = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'lick_on_stim', 'psycurveMode':'off', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3}

AMstage2b = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'lick_on_stim', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':1,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3}

AMstage3 = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstageBiasCorrect = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

#AMstage4 = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}


AMstage5 = {'experimenter':'jenny', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

## TEST AM DEPTH ANIMALS ##
test133 = {'subject':'test133', **AMstage3}
test134 = {'subject':'test134', **AMstage3}
wifi001 = {'subject':'wifi001', **AMstage3}
sole018 = {'subject':'sole018', **AMstage2}
sole019 = {'subject':'sole019', **AMstage2}

## VOT ##
VOTstage0 = {'experimenter':'jenny', 'outcomeMode':'sides_direct', 'relevantFeature':'temporal', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

VOTstage1 = {'experimenter':'jenny', 'outcomeMode':'direct', 'relevantFeature':'temporal', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

VOTstage2 = {'experimenter':'jenny', 'outcomeMode':'on_next_correct', 'relevantFeature':'temporal', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0.0,'automationMode':'increase_delay', 'targetMaxIntensity':60}

VOTstage3 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

VOTstage4 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

VOTstage5 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

VOTstage6 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

VOTBiasCorr = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'temporal', 'antibiasMode':'repeat_mistake', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

## FT ##
FTstage0 = {'experimenter':'jenny', 'outcomeMode':'sides_direct', 'relevantFeature':'spectral', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

FTstage1 = {'experimenter':'jenny', 'outcomeMode':'direct', 'relevantFeature':'spectral', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 'targetMaxIntensity':60}

FTstage2 = {'experimenter':'jenny', 'outcomeMode':'on_next_correct', 'relevantFeature':'spectral', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0.0,'automationMode':'increase_delay', 'targetMaxIntensity':60}

FTstage3 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

FTstage4 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

FTstage5 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

FTstage6 = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}


FTBiasCorr = {'experimenter':'jenny', 'outcomeMode':'only_if_correct', 'relevantFeature':'spectral', 'antibiasMode':'repeat_mistake', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange':0.05, 'targetMaxIntensity':70}

leftBias = {'timeWaterValveL':0.025}

rightBias = {'timeWaterValveR':0.025}
#AM

bili034 = {'subject':'bili034', 'soundActionMode':'low_left', **VOTstage6}

bili035 = {'subject':'bili035', 'soundActionMode':'low_left', **VOTstage6}

bili036 = {'subject':'bili036', 'soundActionMode':'low_left', **VOTstage6}

bili037 = {'subject':'bili037', 'soundActionMode':'low_left', **VOTstage6}

bili038 = {'subject':'bili038', 'soundActionMode':'low_left', **VOTstage6}

bili048 = {'subject':'bili048', 'soundActionMode':'high_left', **FTstage3}

bili049 = {'subject':'bili049', 'soundActionMode':'high_left', **FTstage3}

bili050 = {'subject':'bili050', 'soundActionMode':'high_left', **FTstage3}

bili051 = {'subject':'bili051', 'soundActionMode':'high_left', **FTstage6}

#PM

bili039 = {'subject':'bili039', 'soundActionMode':'high_left', **VOTstage6}

bili040 = {'subject':'bili040', 'soundActionMode':'high_left', **VOTstage6}

bili041 = {'subject':'bili041', 'soundActionMode':'high_left', **VOTstage6}

bili042 = {'subject':'bili042', 'soundActionMode':'high_left', **VOTstage6}

bili043 = {'subject':'bili043', 'soundActionMode':'low_left', **FTstage3}

bili044 = {'subject':'bili044', 'soundActionMode':'low_left', **FTstage6}

bili045 = {'subject':'bili045', 'soundActionMode':'low_left', **FTstage3}

bili046 = {'subject':'bili046', 'soundActionMode':'low_left', **FTstage5}

bili047 = {'subject':'bili047', 'soundActionMode':'low_left', **FTstage6}

## Headfixed

headfix_habituation = {'rewardSideMode':'toggle'}

febeStage1 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'water_after_sound', 'rewardSideMode':'random', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':70, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage2 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'lick_on_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':70, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStageBiasCorrect = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':70, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage3 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':70, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage4 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage5 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only', 'syncLight':'centerLED', 'syncLightDuration':0.1}

febeStage6 = {'experimenter':'jenny', 'relevantFeature':'temporal', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only', 'syncLight':'centerLED', 'syncLightDuration':0.1}


febe008 = {'subject':'febe008', **febeStage6}
