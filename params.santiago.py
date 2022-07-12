
auto000 = {'subject':'auto000','experimenter':'santiago', 
           'delayToTargetMean':0, 'delayToTargetHalfRange':0,
           'lowFreq':1000,'midFreq':5000,'highFreq':10000,
           'outcomeMode':'simulated', 'targetDuration':0.2, 'intensityMode':'fixed'}

tuningFreq = {'subject':'test000', 'experimenter':'santiago', 
              'minFreq':2000, 'maxFreq':40000, 'numTones':16, 
              'stimType':'Sine', 'stimDur':0.1,
              'isiMean':1, 'isiHalfRange':0,
              'minInt':60, 'maxInt':60}

tuningAM = {'subject':'test000', 'experimenter':'santiago', 
            'minFreq':4, 'maxFreq':128, 'numTones':11, 
            'stimType':'AM', 'stimDur':0.5,
            'isiMean':1, 'isiHalfRange':0,
            'minInt':60, 'maxInt':60}

laser000 = {'subject':'test000',
           'delayToTargetHalfRange':0,
           'lowFreq':1000, 'highFreq':2000, 'targetIntensityMode':'fixed',
           'delayToTargetMean':0.2,
           'laserOnsetFromSoundOnset1':1.5,
           'laserDuration':0.5,
           'targetDuration':0.5}

test000 = {'subject':'test000',
           'lowFreq':1000, 'midFreq':1400, 'highFreq':2000, 'targetIntensityMode':'fixed',
           'currentBlock':'mid_boundary',
           'delayToTargetMean':0.2, 'delayToTargetHalfRange':0,
           'targetDuration':0.5,
           'outcomeMode':'on_next_correct',
           'allowEarlyWithdrawal':'on'}

bili000 = {'subject':'bili000',
           'laserMode':'bilateral','fractionLaserTrials':0.99, 'relevantFeature':'temporal'}

pred000 = {'subject':'pred000', 'oddballFreq':400, 'standardFreq':500, 'nFreq':9, 'stimDur':0.1,
           'isiMean':0.2, 'isiHalfRange':0, 'stimType':'Sine', 'sequenceMode':'Descending'}

hfix000 = {'subject':'test000', 'taskMode':'water_on_sound', 'interTrialIntervalMean':1,
           'interTrialIntervalHalfRange':0, 'targetIntensity':50, 'soundType':'chords',
           'highFreq':1200, 'lowFreq':500, 'psycurveMode':'off', 'rewardSideMode':'toggle'}

hfix001 = {'subject':'test000', 'taskMode':'lick_on_stim', 'interTrialIntervalMean':1,
           'interTrialIntervalHalfRange':0, 'targetIntensity':50, 'soundType':'chords',
           'highFreq':1200, 'lowFreq':500, 'psycurveMode':'off', 'rewardSideMode':'toggle',
           'targetDuration': 2, 'lickBeforeStimOffset':'abort'}

hfix002 = {'subject':'test000', 'taskMode':'discriminate_stim', 'interTrialIntervalMean':1,
           'lickingPeriod':0, 'psycurveMode':'mid_and_extreme', 'psycurveNsteps':8,
           'interTrialIntervalHalfRange':0, 'targetIntensity':50, 'soundType':'chords',
           'highFreq':1300, 'lowFreq':600, 'rewardSideMode':'random'}

hfix003b = {'subject':'test000', 'taskMode':'discriminate_stim', 'interTrialIntervalMean':1,
           'lickingPeriod':0.5, 'interTrialIntervalHalfRange':0,
           'targetIntensity':50, 'targetDuration': 0.5,
           'soundType':'chords', 'highFreq':2260, 'lowFreq':566, 'rewardSideMode':'toggle'}

hfix003 = {'subject':'test000', 'taskMode':'discriminate_stim', 'interTrialIntervalMean':1,
           'lickingPeriod':0.5, 'interTrialIntervalHalfRange':0,
           'targetIntensity':55, 'targetDuration': 0.5,
           'soundType':'tone_cloud', 'highFreq':3200, 'lowFreq':400, 'rewardSideMode':'toggle'}

#chad000 = {'subject':'test000', 'taskMode':'discriminate_change',
#           'interTrialIntervalMean':2, 'maxFreq':600, 'minFreq':500}
chad00x = {'subject':'test000', 'taskMode':'lick_after_change',
           'rewardSideMode':'toggle',
           'interTrialIntervalMean':2, 'maxFreq':600, 'minFreq':500,
           'postDuration':0.5,
           'nFreqs':3, 'minFreqRatio':1.01 }

chad000 = {'subject':'test000', 'taskMode':'water_on_lick',
           'interTrialIntervalMean':2, 'minFreq':500, 'maxFreq':600,
           'postDuration':0.5, 'taskMode':'lick_after_change',
           'nFreqs':3, 'minFreqRatio':1.01 }

fm000 = {'subject':'test000', 'taskMode':'discriminate_stim', 'interTrialIntervalMean':1,
         'lickingPeriod':0.2, 'interTrialIntervalHalfRange':0,
         'targetDuration': 0.5,
         'soundType':'FM_direction', 'highFreq':1300, 'lowFreq':600, 'rewardSideMode':'toggle'}

speech000 = {'subject':'test000', 'outcomeMode':'passive_exposure'}


quicktrials = {'interTrialIntervalMean':2, 'interTrialIntervalHalfRange':0}

detect_sound_stage1 = {'experimenter':'santiago', 'taskMode':'water_after_sound'}
detect_sound_stage2 = {'experimenter':'santiago', 'taskMode':'detect_single_sound'}

pure000 = {'subject': 'pure000', **detect_sound_stage2, **quicktrials}
pure014 = {'subject': 'pure014', **detect_sound_stage2}
pure015 = {'subject': 'pure015', **detect_sound_stage2}
