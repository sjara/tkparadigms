# === Amplitude Modulation (freely moving) ===
amDiscrimStage0 = {'experimenter':'gabriel', 'outcomeMode':'sides_direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20',}
amDiscrimStage1 = {'experimenter':'gabriel', 'outcomeMode':'direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20',}
amDiscrimStage2 = {'experimenter':'gabriel', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'automationMode':'increase_delay', 
                     'targetMaxIntensity':70,'targetIntensityMode':'randMinus20',}
amDiscrimStage3 = {'experimenter':'gabriel', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20',}
amDiscrimBiasCorr = {'experimenter':'gabriel', 'outcomeMode':'only_if_correct','antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20',}

sole010 = {'subject':'sole010', **amDiscrimStage1}
sole011 = {'subject':'sole011', **amDiscrimStage3}
sole012 = {'subject':'sole012', **amDiscrimStage3}
sole013 = {'subject':'sole013', **amDiscrimStage3}
sole014 = {'subject':'sole014', **amDiscrimStage3}
sole015 = {'subject':'sole015', **amDiscrimBiasCorr}
sole016 = {'subject':'sole016', **amDiscrimStage3}
sole017 = {'subject':'sole017', **amDiscrimStage2}
sole018 = {'subject':'sole018', **amDiscrimStage0}

sole001 = {'subject':'sole001', **amDiscrimStage3}
sole002 = {'subject':'sole002', **amDiscrimStage3}
sole003 = {'subject':'sole003', **amDiscrimStage3}
sole004 = {'subject':'sole004', **amDiscrimStage3}
sole005 = {'subject':'sole005', **amDiscrimBiasCorr}
sole006 = {'subject':'sole006', **amDiscrimStage3}
sole007 = {'subject':'sole007', **amDiscrimStage3}
sole008 = {'subject':'sole008', **amDiscrimBiasCorr}
sole009 = {'subject':'sole009', **amDiscrimStage3}


# === Frequency discrimination (freely moving) ===
freqDiscrimStage0 = {'experimenter':'gabriel', 'outcomeMode':'sides_direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20', 'currentBlock':'mid_boundary', 
                     'highFreq':16200, 'midFreq':9000, 'lowFreq':5000}
freqDiscrimStage1 = {'experimenter':'gabriel', 'outcomeMode':'direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20', 'currentBlock':'mid_boundary', 
                     'highFreq':16200, 'midFreq':9000, 'lowFreq':5000}
freqDiscrimStage2 = {'experimenter':'gabriel', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'automationMode':'increase_delay', 
                     'targetMaxIntensity':70,'targetIntensityMode':'randMinus20', 'currentBlock':'mid_boundary', 
                     'highFreq':16200, 'midFreq':9000, 'lowFreq':5000}
freqDiscrimStage3 = {'experimenter':'gabriel', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20', 'currentBlock':'mid_boundary', 
                     'highFreq':16200, 'midFreq':9000, 'lowFreq':5000}
freqDiscrimBiasCorr = {'experimenter':'gabriel', 'outcomeMode':'only_if_correct','antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':70,
                     'targetIntensityMode':'randMinus20', 'currentBlock':'mid_boundary', 
                     'highFreq':16200, 'midFreq':9000, 'lowFreq':5000}

test000 = {'subject':'test000', **freqDiscrimStage0}
#sole001 = {'subject':'sole001', **freqDiscrimStage3}
#sole002 = {'subject':'sole002', **freqDiscrimStage3}
#sole003 = {'subject':'sole003', **freqDiscrimStage3}
#sole004 = {'subject':'sole004', **freqDiscrimStage3}
#sole005 = {'subject':'sole005', **freqDiscrimStage3}
#sole006 = {'subject':'sole006', **freqDiscrimStage3}
#sole007 = {'subject':'sole007', **freqDiscrimStage3}
#sole008 = {'subject':'sole008', **freqDiscrimStage3}
#sole009 = {'subject':'sole009', **freqDiscrimStage3}


# === Speech categorization (freely moving) ===
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

# bili animals
bili052 = {'subject':'bili052', **FTstage4}
bili053 = {'subject':'bili053', **FTstage3}
bili054 = {'subject':'bili054', **FTstage3}
bili055 = {'subject':'bili055', **FTstage4}
bili056 = {'subject':'bili056', **FTstage4}
bili057 = {'subject':'bili057', **FTstage4}
bili058 = {'subject':'bili058', **FTBiasCorr}
bili059 = {'subject':'bili059', **FTstage3}
bili060 = {'subject':'bili060', **FTstage3}


## Headfixed
headfix_habituation = {'rewardSideMode':'toggle'}

febeSpectralStage1 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'water_after_sound', 'rewardSideMode':'random', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage2 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'lick_on_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStageBiasCorrect = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage3 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage4 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage5 = {'experimenter':'gabriel', 'relevantFeature':'spectral',  'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeSpectralStage6 = {'experimenter':'gabriel', 'relevantFeature':'spectral', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}


febe013 = {'subject':'febe013', **febeSpectralStage3}
febe019 = {'subject':'febe019', **febeSpectralStage4}
febe020 = {'subject':'febe020', **febeSpectralStage5}
febe007 = {'subject':'febe007', **febeSpectralStage4}
febe012 = {'subject':'febe012', **febeSpectralStageBiasCorrect}
