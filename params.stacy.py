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
               'subject':'gosi004',
               'experimenter' : 'stacy'}

tuningCurve1 = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Chord',
               'minFreq':2000,
               'maxFreq':40000,
               'minInt':50,
               'maxInt':50,
               'numInt':1,
               'numTones':16,
               'subject':'gosi004',
               'experimenter' : 'stacy'}

tuningCurve2 = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Chord',
               'minFreq':2000,
               'maxFreq':40000,
               'minInt':50,
               'maxInt':50,
               'numInt':1,
               'numTones':16,
               'subject':'gosi008',
               'experimenter' : 'stacy'}

tuningCurve3 = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Chord',
               'minFreq':2000,
               'maxFreq':40000,
               'minInt':50,
               'maxInt':50,
               'numInt':1,
               'numTones':16,
               'subject':'gosi001',
               'experimenter' : 'stacy'}

psyCurveChangeReward = {'punishTimeError':4,
                     'delayToTargetMean':0.2,
                     'currentBlock':'more_left',
                     'psycurveMode':'off',
                     'automationMode':'left_right_left',
                     'punishTimeEarly':0.5,
                     'punishTimeError':2,
                     'punishSoundAmplitude':0.0,
                     'trialsPerBlock':200,
                     'baseWaterValveL':0.015,
                     'baseWaterValveR':0.015,
                     'factorWaterValveL':4,
                     'factorWaterValveR':4}


pardict = {'subject':'gosi004','experimenter':'stacy'}
pardict.update({'lowFreq':8100,'highFreq':19200,'targetIntensityMode':'fixed'})
pardict.update(psyCurveChangeReward)
gosi004 = pardict.copy()

pardict = {'subject':'gosi008','experimenter':'stacy'}
pardict.update({'lowFreq':6200,'highFreq':19200,'targetIntensityMode':'fixed'})
pardict.update(psyCurveChangeReward)
gosi008 = pardict.copy()

pardict = {'subject':'gosi001','experimenter':'stacy'}
pardict.update({'lowFreq':6200,'highFreq':19200,'targetIntensityMode':'fixed'})
pardict.update(psyCurveChangeReward)
gosi001 = pardict.copy()

pardict = {'subject':'gosi010','experimenter':'stacy'}
pardict.update({'lowFreq':6200,'highFreq':19200,'targetIntensityMode':'fixed'})
pardict.update(psyCurveChangeReward)
gosi010 = pardict.copy()
