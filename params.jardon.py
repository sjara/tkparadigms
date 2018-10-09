
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
               'subject':'adap071',
               'experimenter' : 'jardon'}

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
               'subject':'adap071',
               'experimenter' : 'jardon'}

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
               'subject':'adap067',
               'experimenter' : 'jardon'}


frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}
psyCurveMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                'punishTimeEarly':0.5, 'punishSoundAmplitude':50, 'psycurveMode':'uniform'}

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

#This should be run with 'reward_change_freq_discrim.py'
pardict = {'subject':'adap071','experimenter':'jardon'}
pardict.update({'lowFreq':6200,'highFreq':19200,'targetIntensityMode':'fixed'})
pardict.update(psyCurveChangeReward)
#pardict.update(frequencySet6to19)
#pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
#This will use 3 frequencies in psycurve
pardict.update({'psycurveMode':'uniform','psycurveNfreq':8}) 
adap071 = pardict.copy()

#This should be run with 'reward_change_freq_discrim.py'
pardict = {'subject':'adap067','experimenter':'jardon'}
pardict.update({'lowFreq':6200,'highFreq':19200,'targetIntensityMode':'fixed'})
pardict.update(psyCurveChangeReward)
#pardict.update(frequencySet6to19)
#pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'delayToTargetMean':0.15})
pardict.update({'psycurveMode':'uniform','psycurveNfreq':8}) 
adap067 = pardict.copy()



