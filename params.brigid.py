## Headfixed

headfix_habituation = {'rewardSideMode':'toggle'}

febeStage1 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'water_after_sound', 'rewardSideMode':'random', 'lickingPeriod':1.5, 'rewardAvailability':1, 'delayToTargetMean':2.5,'delayToTargetHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage2 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'lick_on_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'delayToTargetMean':2.5,'delayToTargetHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage3 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'delayToTargetMean':2.5,'delayToTargetHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage4 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'delayToTargetMean':2.5,'delayToTargetHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage5 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'extreme80pc', 'psycurveNsteps':6, 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'delayToTargetMean':2.5,'delayToTargetHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage6 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'uniform', 'psycurveNsteps':6, 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'delayToTargetMean':2.5,'delayToTargetHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}


febe001 = {'subject':'febe001', **febeStage1}
febe007 = {'subject':'febe007', **febeStage2}
febe008 = {'subject':'febe008', **febeStage4}
febe009 = {'subject':'febe009', **febeStage4}
febe012 = {'subject':'febe012', **febeStage2}
