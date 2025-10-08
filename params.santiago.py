
wifi000 = {'subject':'test000', 'experimenter':'santiago', 
           'minFreq':2000, 'maxFreq':3000, 'numTones':2, 
           'stimType':'ToneTrain', 'stimDur':0.1,
           'isiMean':2, 'isiHalfRange':0,
           'minInt':70, 'maxInt':70}

depth000 = {'soundType':'AM_depth', 'interTrialIntervalMean':1, 'interTrialIntervalHalfRange':0, 'rewardSideMode':'toggle'}

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
           'targetIntensity':55, 'targetDuration': 1, 'lickBeforeStimOffset':'punish',
           'punishmentSound':'white_noise', 'punishmentIntensity': 40,
           'soundType':'tone_cloud', 'highFreq':3200, 'lowFreq':400, 'rewardSideMode':'onlyL'}

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


quicktrials = {'interTrialIntervalMean':1, 'interTrialIntervalHalfRange':0}

detect_sound_stage1 = {'experimenter':'santiago', 'taskMode':'water_after_sound'}
detect_sound_stage2 = {'experimenter':'santiago', 'taskMode':'detect_single_sound'}
detect_sound_stage3 = {'experimenter':'santiago', 'taskMode':'detect_with_distractors',
                       'distractorType':'lower', 'punishmentType':'noise', 'punishmentIntensity':50,
                       'interTrialIntervalMean':2, 'interTrialIntervalHalfRange':0.5}
detect_sound_stage4 = {'experimenter':'santiago', 'taskMode':'detect_with_distractors',
                       'distractorType':'lower_and_higher', 'punishmentType':'noise',
                       'punishmentIntensity':50,
                       'interTrialIntervalMean':2, 'interTrialIntervalHalfRange':0.5}
detect_tones = {'soundType':'tone', 'stimIntensity':60}
target_7k = {'targetFrequency':7000, 'distractorFreqDelta':0.8}
target_12k = {'targetFrequency':12188, 'distractorFreqDelta':0.8}

pure000 = {'subject': 'pure000', **detect_sound_stage4, **quicktrials, **detect_tones, **target_12k}
pure014 = {'subject': 'pure014', **detect_sound_stage4, **detect_tones, **target_12k}
pure015 = {'subject': 'pure015', **detect_sound_stage4, **detect_tones, **target_12k}

pupilAM = {'minFreq':4, 'maxFreq':12, 'soundType':'AM_rate', 'preDurationMean':3, 'totalStimDuration':5}

oddball = {'stimType':'FM', 'oddballStim':'FM_down', 'stimDuration':0.2,
           'oddballPeriod':3}

amdisc = {'allowEarlyWithdrawal':'off', 'punishTimeEarly':0.5,
          'targetIntensity':70, 'highSoundFreq':1600, 'lowSoundFreq':500,
          'automationMode':'increase_duration'}

amlaser = {'allowEarlyWithdrawal':'off', 'punishTimeEarly':0.2, 'laserMode':'random',
           'laserProbability':0.5,
           'targetIntensity':50, 'visibleLightMode':'center', 'punishIntensity':50}
