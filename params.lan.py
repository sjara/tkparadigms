


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
               'subject':'d1pi002',
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
               'subject':'d1pi002',
               'experimenter' : 'lan'}

laserpulse = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0,
               'noiseAmp':0.05,
               'stimType' : 'Laser',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'d1pi002',
               'experimenter' : 'lan'}


tuningCurve = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Sine',
               'minFreq':2000,
               'maxFreq':40000,
               'minInt':20,
               'maxInt':70,
               'numInt':6,
               'subject':'d1pi002',
               'experimenter' : 'lan'}

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
