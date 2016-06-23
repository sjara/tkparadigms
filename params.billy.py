'''
Define parameters for different subjects
'''
### globals()[pardict['subject']] = pardict.copy()


test000 = {'targetDuration':0.2, 'targetIntensityMode':'fixed',
           'targetMaxIntensity':80,
           'highFreq':2100, 'midFreq':1400,'lowFreq':1000, 'trialsPerBlock':3,
           'punishSoundAmplitude':0.1} #, 'outcomeMode':'simulated'

frequencySet5to24 = {'lowFreq':5000,'midFreq':11000,'highFreq':24000}
frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}
frequencySet3to16 = {'lowFreq':3000,'midFreq':7000,'highFreq':16000}
frequencySet4to13 = {'lowFreq':3800,'midFreq':7000,'highFreq':12600}

# ======== Adaptive categorization task ========
sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                     'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.05,
                     'antibiasMode':'repeat_mistake'}

basicDiscriminationMode = {'delayToTargetMean':0.2,'currentBlock':'mid_boundary'}

#onNextCorrectMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
#                   'currentBlock':'mid_boundary', 'targetDuration':0.1,'targetMaxIntensity':80,'lowFreq':4000,'highFreq':13000}

psyCurveMidBound = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                    'currentBlock':'mid_boundary','psycurveMode':'uniform','psycurveNfreq':6}

switchDailyMode = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2}

switchBlocksMode = {'punishTimeError':4, 'delayToTargetMean':0.2,'trialsPerBlock':200,}

stayBlockMode = {'punishTimeError':4, 'delayToTargetMean':0.2,'trialsPerBlock':2000,}

#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(basicDiscriminationMode)



##############################################################################################################

test086frequency = {'lowFreq':7200,'midFreq':11000,'highFreq':15000}
test053frequency = {'lowFreq':6000,'midFreq':14000,'highFreq':19200}
fixIntensity = {'targetIntensityMode':'fixed','targetMaxIntensity':50}

pardict = {'subject':'test086','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(test086frequency)
pardict.update(fixIntensity)
pardict.update({'punishTimeEarly':0,'punishSoundAmplitude':0.01})
test086 = pardict.copy()

pardict = {'subject':'test053','experimenter':'santiago'}
pardict.update(stayBlockMode)
pardict.update({'currentBlock':'low_boundary'})
pardict.update(test053frequency)
pardict.update(fixIntensity)
pardict.update({'punishTimeEarly':0,'punishSoundAmplitude':0.01})
test053 = pardict.copy()

pardict = {'subject':'test059','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0,'punishSoundAmplitude':0.01})
pardict.update(fixIntensity)
test059 = pardict.copy()
'''
#started on psycurve 2015-11-28
test087frequency = {'lowFreq':6200,'midFreq':10000,'highFreq':18000}
pardict = {'subject':'test087','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(test087frequency)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
pardict.update(fixIntensity)
test087 = pardict.copy()
'''
#test087frequency = {'lowFreq':8900,'midFreq':9100,'highFreq':9900}
test087frequency = {'lowFreq':9000,'midFreq':9200,'highFreq':9700}
pardict = {'subject':'test087','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(test087frequency)
pardict.update(fixIntensity)
pardict.update({'punishTimeEarly':0,'punishSoundAmplitude':0.01})
test087 = pardict.copy()

test089frequency = {'lowFreq':6200,'midFreq':9000,'highFreq':17000}
pardict = {'subject':'test089','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'low_boundary'})
pardict.update(test089frequency)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
pardict.update({'delayToTargetMean':0.13, 'delayToTargetHalfRange':0.02})
pardict.update(fixIntensity)
test089 = pardict.copy()


firstAdapMice = {'delayToTargetMean':0.2,'trialsPerBlock':300}
'''
pardict = {'subject':'adap002','experimenter':'santiago'}
pardict.update(firstAdapMice)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.2,'punishSoundAmplitude':0.03})
pardict.update({'punishTimeError':4})
adap002 = pardict.copy()
'''
#adap004frequency = {'lowFreq':6200,'midFreq':10000,'highFreq':19200}
adap004frequency = {'lowFreq':7200,'midFreq':10000,'highFreq':13600}#updated 2015-12-19
pardict = {'subject':'adap004','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(adap004frequency)
pardict.update(fixIntensity)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
pardict.update({'punishTimeError':4})
adap004 = pardict.copy()
'''
#Switch to psychometric curve as of 2015-12-02
pardict = {'subject':'adap004','experimenter':'santiago'}
pardict.update(firstAdapMice)
pardict.update(adap004frequency)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
pardict.update({'punishTimeError':4})
pardict.update(fixIntensity)
adap004 = pardict.copy()
'''

adap002frequency = {'lowFreq':6800,'midFreq':11000,'highFreq':16000}

pardict = {'subject':'adap002','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(adap002frequency)
pardict.update(fixIntensity)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
pardict.update({'punishTimeError':4})
adap002 = pardict.copy()


pardict = {'subject':'adap010','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet5to24)
pardict.update(fixIntensity)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.01})
pardict.update({'punishTimeError':4})
adap010 = pardict.copy()

adap3 = psyCurveMidBound
adap3.update({'delayToTargetMean':0.2})

pardict = {'subject':'adap015','experimenter':'santiago'}
pardict.update(adap3)
pardict.update({'lowFreq':6200,'highFreq':17000})
pardict.update(fixIntensity)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.01})
adap015 = pardict.copy()

pardict = {'subject':'adap013','experimenter':'santiago'}
pardict.update(adap3)
pardict.update({'lowFreq':9000,'highFreq':12000})
pardict.update(fixIntensity)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.01})
adap013 = pardict.copy()

pardict = {'subject':'adap017','experimenter':'santiago'}
pardict.update(adap3)
pardict.update({'lowFreq':7000,'highFreq':17000})
pardict.update(fixIntensity)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.01})
adap017 = pardict.copy()

#######################################################################################################
#######################################################################################################
#FOR REWARD CHANGE MICE
#######################################################################################################
#######################################################################################################

#'currentBlock':'more_right',
psyCurveChangeReward = {'punishTimeError':4,
                     'delayToTargetMean':0.2,
                     'psycurveMode':'off',
                     'automationMode':'left_right_left',
                     'punishTimeEarly':0.5,
                     'punishSoundAmplitude':0.01,
                     'targetIntensityMode':'fixed',
                     'baseWaterValveL':0.015,
                     'baseWaterValveR':0.015,
                     'factorWaterValveL':4,
                     'factorWaterValveR':4,
                     'currentBlock':'more_left'}


pardict = {'subject':'adap015','experimenter':'billy'}
pardict.update(psyCurveChangeReward)
pardict.update({'trialsPerBlock':150})
pardict.update({'lowFreq':6200,'highFreq':17000})
adap015reward = pardict.copy()

pardict = {'subject':'adap013','experimenter':'billy'}
pardict.update(psyCurveChangeReward)
pardict.update({'trialsPerBlock':150})
pardict.update({'lowFreq':8000,'highFreq':14000})
adap013reward = pardict.copy()

pardict = {'subject':'adap017','experimenter':'billy'}
pardict.update(psyCurveChangeReward)
pardict.update({'trialsPerBlock':150})
pardict.update({'lowFreq':7000,'highFreq':17000})
adap017reward = pardict.copy()



#######################################################################################################
#######################################################################################################


pardict = {'subject':'adap020','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update(frequencySet6to19)
pardict.update({'lowFreq':6200,'midFreq':12000,'highFreq':19200})
pardict.update({'currentBlock':'low_boundary'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.01})
pardict.update(fixIntensity)
pardict.update({'punishTimeError':4})
pardict.update({'trialsPerBlock':250})
adap020 = pardict.copy()

pardict = {'subject':'adap024','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'currentBlock':'high_boundary'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
#pardict.update(fixIntensity)
pardict.update({'punishTimeError':4})
pardict.update({'trialsPerBlock':300})
adap024 = pardict.copy()

pardict = {'subject':'adap021','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'currentBlock':'high_boundary'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.03})
#pardict.update(fixIntensity)
pardict.update({'punishTimeError':4})
pardict.update({'trialsPerBlock':300})
adap021 = pardict.copy()

