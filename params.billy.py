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

switchBlocksMode = {'punishTimeError':4, 'delayToTargetMean':0.2}

#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(basicDiscriminationMode)

# ======== Cued discrimination task ========
cuedSidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
cuedDirectMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}




# -- Cued discrimination task --

pardict = {'subject':'cued000','experimenter':'santiago'} # FOR TESTING
#pardict.update(directMode)
pardict.update({'outcomeMode':'on_next_correct'})
pardict.update({'lowFreq':1000,'midFreq':2000,'highFreq':4000})
#pardict.update({'delayToTargetMean':0.5})
#pardict.update({'automationMode':'increase_delay'})
pardict.update({'psycurveMode':'off'})
cued000 = pardict.copy()

pardict = {'subject':'cued001','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update({'psycurveMode':'single_target'})
pardict.update({'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed'})
cued001 = pardict.copy()

pardict = {'subject':'cued002','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update({'psycurveMode':'single_target'})
pardict.update({'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed'})
cued002 = pardict.copy()

pardict = {'subject':'cued003','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update({'psycurveMode':'single_target'})
pardict.update({'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed'})
cued003 = pardict.copy()

pardict = {'subject':'cued004','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update({'psycurveMode':'single_target'})
pardict.update({'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed'})
cued004 = pardict.copy()

pardict = {'subject':'cued005','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update({'psycurveMode':'single_target'})
pardict.update({'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed'})
cued005 = pardict.copy()

pardict = {'subject':'cued006','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update({'psycurveMode':'single_target'})
pardict.update({'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed'})
cued006 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --
latestMiceMode = sidesDirectMode

pardict = {'subject':'adap006','experimenter':'santiago'}
pardict.update(latestMiceMode)
pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap006 = pardict.copy()

pardict = {'subject':'adap007','experimenter':'santiago'}
pardict.update(latestMiceMode)
pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap007 = pardict.copy()

pardict = {'subject':'adap008','experimenter':'santiago'}
pardict.update(latestMiceMode)
pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap008 = pardict.copy()

pardict = {'subject':'adap009','experimenter':'santiago'}
pardict.update(latestMiceMode)
pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap009 = pardict.copy()

pardict = {'subject':'adap010','experimenter':'santiago'}
pardict.update(latestMiceMode)
pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap010 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --

pardict = {'subject':'adap001','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap001 = pardict.copy()

pardict = {'subject':'adap002','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap002 = pardict.copy()

pardict = {'subject':'adap003','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap003 = pardict.copy()

pardict = {'subject':'adap004','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
# NOTE: there was a mistake here and this mouse was trained in 3 vs 16
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap004 = pardict.copy()

pardict = {'subject':'adap005','experimenter':'santiago'}
#pardict.update(directMode)
#pardict.update(increaseDelayMode)
#pardict.update(switchDailyMode)
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap005 = pardict.copy()

# -- Adaptive categorization, psychometric and switching --

pardict = {'subject':'test089','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'low_boundary'})
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
test089 = pardict.copy()

pardict = {'subject':'test088','experimenter':'santiago'}
#pardict.update(switchDailyMode)
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'low_boundary'})
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
test088 = pardict.copy()

pardict = {'subject':'test087','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update(frequencySet6to19)
pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
test087 = pardict.copy()


pardict = {'subject':'test085','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
test085 = pardict.copy()





################################################################################################################################

test086frequency = {'lowFreq':9920,'midFreq':11000,'highFreq':12038}
test053frequency = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}
fixIntensity = {'targetIntensityMode':'fixed','targetMaxIntensity':50}

pardict = {'subject':'test086','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(test086frequency)
pardict.update(fixIntensity)
pardict.update({'punishTimeEarly':0,'punishSoundAmplitude':0.01})
test086 = pardict.copy()

pardict = {'subject':'test053','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
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

