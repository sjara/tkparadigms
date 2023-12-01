"""
This file defines the paradigm parameters for each subject.
"""
tuningFRA = {'subject':'pals027','experimenter':'jackie', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1, 'isiHalfRange':0,
              'minInt':10, 'maxInt':60, 'numInt':6 }

tuningFreq = {'subject':'feat004','experimenter':'jackie', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.1, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':60, 'maxInt':70, 'numInt':2, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1 }


tuningAM = {'subject':'feat004','experimenter':'jackie', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':60,
            'maxInt':60, 'syncLightMode':'from_stim_offset', 'syncLight':'centerLED', 'delayToSyncLight': 0.2, 'syncLightDuration':0.1}


### Behavior ###
## AM Depth
AMstage1_onlyL = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'water_after_sound', 'psycurveMode':'off', 'rewardSideMode':'onlyL', 'lickingPeriod':1.5, 'rewardAvailability':1,'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'} 

AMstage1b_punish_onlyL = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'onlyL', 'lickBeforeStimOffset':'punish', 'punishmentSound':'chord', 'punishmentDuration':.1, 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'} #only added punish here

AMstage1b_onlyL = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'onlyL', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstage1bfull_onlyL = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'onlyL', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstage1_onlyR = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'water_after_sound', 'psycurveMode':'off', 'rewardSideMode':'onlyR', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'} #May need to add 'automationMode':'increase_delay'

AMstage1b_punish_onlyR = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'onlyR', 'lickBeforeStimOffset':'punish', 'punishmentSound':'chord', 'punishmentDuration':.1, 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstage1bfull_onlyR = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'onlyR', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstage1b_onlyR = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'onlyR', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstage2 = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'water_after_sound', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':1,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'} #might want to skip
#prob skip AMstage2 for now
AMstage2b = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'automationMode':'increase_delay', 'interTrialIntervalMean':1,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'} #this has the 'automationMode':'increase_delay'

AMstage2b_punish = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'punish','punishmentSound':'chord', 'punishmentDuration':.1, 'lickingPeriod':1.5, 'rewardAvailability':1, 'automationMode':'increase_delay', 'interTrialIntervalMean':1,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'} 

#AMstage2 = {'experimenter':'jackie', 'soundType':'AM_depth', 'taskMode':'lick_on_stim', 'psycurveMode':'off', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'ignore', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3}
#AMstage2b = {'experimenter':'jackie', 'soundType':'AM_depth', 'taskMode':'lick_on_stim', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'automationMode':'increase_delay', 'interTrialIntervalMean':1,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3}
#AMstage3 = {'experimenter':'jackie', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

AMstageBiasCorrect = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'off', 'rewardSideMode':'repeat_mistake', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

#AMstage4 = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'extreme80pc', 'psycurveNsteps':'6', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}
#AMstage5 = {'experimenter':'wendy', 'soundType':'AM_depth', 'taskMode':'discriminate_stim', 'psycurveMode':'uniform', 'psycurveNsteps':'6', 'rewardSideMode':'random', 'lickBeforeStimOffset':'abort', 'lickingPeriod':1.5, 'rewardAvailability':1, 'interTrialIntervalMean':2.5,'interTrialIntervalHalfRange':1,'targetIntensity':65, 'timeWaterValve':0.03, 'stimType':'sound_only', 'highAMrate':8, 'lowAMrate':8, 'highAMdepth':100, 'lowAMdepth':0, 'targetDuration':0.3, 'syncLight':'centerLED'}

## TEST AM DEPTH ANIMALS ##
#test133 = {'subject':'test133', **AMstage3}
sole020 = {'subject':'sole020', **AMstage1b_punish_onlyL}
test134 = {'subject':'test134', **AMstage1b_onlyR}
wifi001 = {'subject':'wifi001', **AMstage2b_punish}
#sole018 = {'subject':'sole018', **AMstage2b}
#sole019 = {'subject':'sole019', **AMstage2b}
