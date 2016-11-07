laserSounds = {'subject':'adap011',
               'experimenter' : 'lan',
               'noiseAmp':0.1,
               'laserFrontOverhang':0.01,
               'laserBackOverhang':0.01}


lasertrain = {'stimDur':0.01,
               'isiMean':1,
               'isiHalfRange': 0,
               'noiseAmp':0.05,
               'stimType' : 'LaserTrain',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'adap011',
               'experimenter' : 'lan'}

noisebursts = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'noiseAmp':0.1,
               'stimType' : 'Noise',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'adap011',
               'experimenter' : 'lan'}

laserpulse = {'stimDur':0.05,
               'isiMean':0.95,
               'isiHalfRange': 0,
               'noiseAmp':0.05,
               'stimType' : 'Laser',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'adap011',
               'experimenter' : 'lan'}


tuningCurve = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Chord',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':50,
               'numInt':2,
               'numTones':12,
               'subject':'d1pi014',
               'experimenter' : 'lan'}

tuningCurveLite = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Chord',
               'minFreq':7000,
               'maxFreq':22000,
               'minInt':50,
               'maxInt':50,
               'numInt':1,
               'numTones':6,
               'subject':'d1pi014',
               'experimenter' : 'lan'}

tuningAM = {'subject':'adap011', 'experimenter':'lan', 
            'minFreq':4, 'maxFreq':128, 'numTones':11, 
            'stimType':'AM', 'stimDur':0.5,
            'isiMin':1, 'isiMax':2}


psyCurveChangeReward = {'punishTimeError':4,
                     'delayToTargetMean':0.1,
                     'currentBlock':'same_reward',
                     'psycurveMode':'uniform',
                     'automationMode':'same_left_right',
                     'punishTimeEarly':0.5,
                     'punishTimeError':2,
                     'punishSoundAmplitude':0.05}


basicDiscriminationMode = {'delayToTargetMean':0.2,'currentBlock':'mid_boundary',
                           'punishTimeEarly':0.5,'punishSoundAmplitude':0.05}
frequencySet5to24 = {'lowFreq':5000,'midFreq':11000,'highFreq':24000}
frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}
frequencySet3to16 = {'lowFreq':3000,'midFreq':7000,'highFreq':16000}
frequencySet4to13 = {'lowFreq':3800,'midFreq':7000,'highFreq':12600}




pardict = {'subject':'d1pi011','experimenter':'lan'}
pardict.update({'lowFreq':5400,'highFreq':12600,'psycurveMode':'uniform','psycurveNfreq':6})
pardict.update({'percentLaserTrialLeft':0.2,'percentLaserTrialRight':0.2, 'stimFreq':'continuous'})
pardict.update({'punishSoundAmplitude':0.015})
pardict.update({'targetMaxIntensity':53,'targetIntensityMode':'fixed'})
pardict.update({'delayToTargetMean':0.1, 'delayToTargetHalfRange':0.02})
d1pi011 = pardict.copy()



pardict = {'subject':'d1pi008','experimenter':'lan'}
pardict.update({'lowFreq':7300,'highFreq':16300,'psycurveMode':'uniform','psycurveNfreq':6})
pardict.update({'percentLaserTrialLeft':0.2,'percentLaserTrialRight':0.2, 'stimFreq':'continuous'})
pardict.update({'punishSoundAmplitude':0.015})
pardict.update({'targetMaxIntensity':50,'targetIntensityMode':'fixed'})
pardict.update({'delayToTargetMean':0.11, 'delayToTargetHalfRange':0.02})
d1pi008 = pardict.copy()


pardict = {'subject':'d1pi016','experimenter':'lan'}
pardict.update({'lowFreq':7000,'highFreq':22000,'psycurveMode':'uniform','psycurveNfreq':6})
pardict.update({'percentLaserTrialLeft':0,'percentLaserTrialRight':0, 'stimFreq':'continuous'})
pardict.update({'punishSoundAmplitude':0.015,'punishTimeError':2})
pardict.update({'targetMaxIntensity':50,'targetIntensityMode':'fixed'})
pardict.update({'delayToTargetMean':0.10, 'delayToTargetHalfRange':0.02})
d1pi016 = pardict.copy()

pardict = {'subject':'d1pi014','experimenter':'lan'}
pardict.update({'lowFreq':7300,'highFreq':16300,'psycurveMode':'uniform','psycurveNfreq':6})
pardict.update({'percentLaserTrialLeft':0,'percentLaserTrialRight':0, 'stimFreq':'continuous'})
pardict.update({'punishSoundAmplitude':0.015,'punishTimeError':2})
pardict.update({'targetMaxIntensity':50,'targetIntensityMode':'fixed'})
pardict.update({'delayToTargetMean':0.15, 'delayToTargetHalfRange':0.05})
d1pi014 = pardict.copy()
