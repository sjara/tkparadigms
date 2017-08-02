
auto000 = {'subject':'auto000','experimenter':'santiago', 
           'delayToTargetMean':0, 'delayToTargetHalfRange':0,
           'lowFreq':1000,'midFreq':5000,'highFreq':10000,
           'outcomeMode':'simulated', 'targetDuration':0.2, 'intensityMode':'fixed'}

tuningAM = {'subject':'test000', 'experimenter':'santiago', 
            'minFreq':4, 'maxFreq':128, 'numTones':11, 
            'stimType':'AM', 'stimDur':0.5,
            'isiMin':1, 'isiMax':2}

tuningAM2 = {'subject':'test089', 'experimenter':'billy', 
            'minFreq':4, 'maxFreq':128, 'numTones':11, 
            'stimType':'AM', 'stimDur':0.5,
            'isiMin':0.5, 'isiMax':2, 'noiseAmp':0.1}

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
