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
febe019 = {'subject':'febe019', **febeSpectralStageBiasCorrect}
febe020 = {'subject':'febe020', **febeSpectralStage3}
febe021 = {'subject':'febe021', **febeSpectralStage3}
