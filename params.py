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
                    'currentBlock':'mid_boundary','psycurveMode':'uniform'}

switchDailyMode = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2}

switchBlocksMode = {'punishTimeError':4, 'delayToTargetMean':0.2}

#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(basicDiscriminationMode)


# -- Cued discrimination task --

pardict = {'subject':'cued000','experimenter':'santiago'} # FOR TESTING
pardict.update(directMode)
pardict.update({'lowFreq':1000,'midFreq':2000,'highFreq':4000})
#pardict.update({'delayToTargetMean':0.5})
pardict.update({'automationMode':'increase_delay'})
cued000 = pardict.copy()

pardict = {'subject':'cued001','experimenter':'santiago'}
pardict.update(directMode)
pardict.update(frequencySet6to19)
#pardict.update({'cuedIntensify':30})
pardict.update({'automationMode':'increase_delay'})
cued001 = pardict.copy()

pardict = {'subject':'cued002','experimenter':'santiago'}
pardict.update(directMode)
pardict.update(frequencySet6to19)
pardict.update({'automationMode':'increase_delay'})
cued002 = pardict.copy()

pardict = {'subject':'cued003','experimenter':'santiago'}
pardict.update(directMode)
pardict.update(frequencySet6to19)
pardict.update({'automationMode':'increase_delay'})
cued003 = pardict.copy()

pardict = {'subject':'cued004','experimenter':'santiago'}
pardict.update(directMode)
pardict.update(frequencySet6to19)
pardict.update({'automationMode':'increase_delay'})
cued004 = pardict.copy()

pardict = {'subject':'cued005','experimenter':'santiago'}
pardict.update(directMode)
pardict.update(frequencySet6to19)
pardict.update({'automationMode':'increase_delay'})
cued005 = pardict.copy()

pardict = {'subject':'cued006','experimenter':'santiago'}
pardict.update(directMode)
pardict.update(frequencySet6to19)
pardict.update({'automationMode':'increase_delay'})
cued006 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --

pardict = {'subject':'adap001','experimenter':'santiago'}
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
adap001 = pardict.copy()

pardict = {'subject':'adap002','experimenter':'santiago'}
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
adap002 = pardict.copy()

pardict = {'subject':'adap003','experimenter':'santiago'}
#pardict.update(directMode)
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
adap003 = pardict.copy()

pardict = {'subject':'adap004','experimenter':'santiago'}
#pardict.update(directMode)
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
# NOTE: there was a mistake here and this mouse was trained in 3 vs 16
adap004 = pardict.copy()

pardict = {'subject':'adap005','experimenter':'santiago'}
#pardict.update(directMode)
#pardict.update(increaseDelayMode)
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
adap005 = pardict.copy()

# -- Adaptive categorization, psychometric and switching --

pardict = {'subject':'test089','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'low_boundary'})
pardict.update(frequencySet6to19)
test089 = pardict.copy()

pardict = {'subject':'test088','experimenter':'santiago'}
pardict.update(switchDailyMode)
#pardict.update({'currentBlock':'low_boundary'})
pardict.update(frequencySet6to19)
test088 = pardict.copy()

pardict = {'subject':'test087','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
test087 = pardict.copy()

pardict = {'subject':'test086','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(frequencySet6to19)
test086 = pardict.copy()

pardict = {'subject':'test085','experimenter':'santiago'}
pardict.update(switchDailyMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(frequencySet6to19)
test085 = pardict.copy()


# -- Trained to switch (then changed to psycurve) --

pardict = {'subject':'test050','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
test050 = pardict.copy()

pardict = {'subject':'test051','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
test051 = pardict.copy()

pardict = {'subject':'test052','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
test052 = pardict.copy()

pardict = {'subject':'test053','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
test053 = pardict.copy()

pardict = {'subject':'test054','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
test054 = pardict.copy()

pardict = {'subject':'test055','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
test055 = pardict.copy()

pardict = {'subject':'test056','experimenter':'santiago'}
#pardict.update(switchDailyMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
test056 = pardict.copy()

pardict = {'subject':'test057','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
test057 = pardict.copy()

pardict = {'subject':'test058','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
pardict.update(frequencySet5to24)
test058 = pardict.copy()

pardict = {'subject':'test059','experimenter':'santiago'}
#pardict.update(psyCurveMidBound)
#pardict.update(switchDailyMode)
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(frequencySet6to19)
test059 = pardict.copy()



# -- First animals. Trained to switch (then changed to psycurve) --

pardict = {'subject':'test011','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet4to13)
test011 = pardict.copy()

pardict = {'subject':'test012','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet4to13)
test012 = pardict.copy()

pardict = {'subject':'test015','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet4to13)
test015 = pardict.copy()

pardict = {'subject':'test016','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet4to13)
test016 = pardict.copy()

pardict = {'subject':'test017','experimenter':'santiago'}
pardict.update(switchDailyMode)
pardict.update(frequencySet4to13)
test017 = pardict.copy()

pardict = {'subject':'test018','experimenter':'santiago'}
#pardict.update(switchDailyMode)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet3to16)
#pardict.update({'currentBlock':'low_boundary'})
test018 = pardict.copy()

pardict = {'subject':'test020','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet4to13)
test020 = pardict.copy()


'''
test011 = psyCurveMidBound.copy()
test011.update({'subject':'test011','experimenter':'santiago'})
test011.update({'currentBlock':'high_boundary','trialsPerBlock':200,'trainer':''})
'''

'''
test050 = psyCurveMidBound.copy()
test050.update({'subject':'test050','experimenter':'santiago'})
'''
'''
test085 = basicDiscriminationMode.copy()
test085.update({'subject':'test085','experimenter':'santiago', 'lowFreq':5000,'midFreq':11000,'highFreq':24000})
'''
