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
               'maxFreq':40000,
               'minInt':60,
               'maxInt':60,
               'numInt':1,
               'subject':'adap011',
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
                     'punishSoundAmplitude':0.05}

pardict = {'subject':'adap005','experimenter':'santiago'}
pardict.update(psyCurveChangeReward)
pardict.update({'trialsPerBlock':150})
pardict.update({'lowFreq':6200,'highFreq':19200})
adap005 = pardict.copy()

pardict = {'subject':'adap008','experimenter':'santiago'}
pardict.update(psyCurveChangeReward)
pardict.update({'trialsPerBlock':100})
pardict.update({'lowFreq':5000,'highFreq':24000})
adap008 = pardict.copy()



basicDiscriminationMode = {'delayToTargetMean':0.2,'currentBlock':'mid_boundary',
                           'punishTimeEarly':0.5,'punishSoundAmplitude':0.05}
frequencySet5to24 = {'lowFreq':5000,'midFreq':11000,'highFreq':24000}
frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}
frequencySet3to16 = {'lowFreq':3000,'midFreq':7000,'highFreq':16000}
frequencySet4to13 = {'lowFreq':3800,'midFreq':7000,'highFreq':12600}


pardict = {'subject':'adap011','experimenter':'lan'}
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
pardict.update({'punishSoundAmplitude':0.02})
pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'targetMaxIntensity':70})
pardict.update({'delayToTargetMean':0.15})
adap011 = pardict.copy()
