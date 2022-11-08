"""
This file defines the parameters to use for each subject.
"""

# --- Cooperation task ---

coopStage1 = {'taskMode':'auto_lights', 'waitTime':3}
coopStage2 = {'taskMode':'reward_on_first_poke', 'waitTime':3}
coopStage3 = {'taskMode':'reward_on_last_poke', 'waitTime':3}
coopStage4 = {'taskMode':'cooperate', 'waitTime':3}
coopStage5 = {'taskMode':'cooperate', 'waitTime':1}

coop006x007 = {'subject':'coop006x007', 'experimenter':'brigid', **coopStage4}
coop008x009 = {'subject':'coop008x009', 'experimenter':'brigid', **coopStage4}


# --- Headfixed ---

headfix_habituation = {'rewardSideMode':'toggle'}

febeStage1 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'water_after_sound', 'rewardSideMode':'random', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage2 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'lick_on_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStageBiasCorrect = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage3 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'off', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage4 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage5 = {'experimenter':'jenny', 'relevantFeature':'temporal',  'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}

febeStage6 = {'experimenter':'jenny', 'relevantFeature':'temporal', 'irrelevantFeatureMode':'random', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'taskMode':'discriminate_stim', 'rewardSideMode':'random', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetMaxIntensity':60, 'timeWaterValve':0.03, 'stimType':'sound_only'}


febe001 = {'subject':'febe001', **febeStage1}
#febe007 = {'subject':'febe007', **febeStage5}
febe008 = {'subject':'febe008', **febeStage6}
febe009 = {'subject':'febe009', **febeStage2}
#febe012 = {'subject':'febe012', **febeStage6}
