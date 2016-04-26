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
                     'punishTimeEarly':0.5,'punishSoundAmplitude':0.05}

basicDiscriminationMode = {'delayToTargetMean':0.2,'currentBlock':'mid_boundary',
                           'punishTimeEarly':0.5,'punishSoundAmplitude':0.05}

psyCurveMidBound = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                    'currentBlock':'mid_boundary','psycurveMode':'uniform'}

switchDailyMode = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2}

switchBlocksMode = {'punishTimeError':4, 'delayToTargetMean':0.2}


# ======== Cued discrimination task ========
cuedSidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
cuedDirectMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}

# ======== Parameters for each animal =========

# -- New adap animals
pardict = {'subject':'adap026','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(basicDiscriminationMode)
adap026 = pardict.copy()

pardict = {'subject':'adap027','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(basicDiscriminationMode)
adap027 = pardict.copy()

pardict = {'subject':'adap028','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(basicDiscriminationMode)
adap028 = pardict.copy()

pardict = {'subject':'adap029','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(basicDiscriminationMode)
adap029 = pardict.copy()

pardict = {'subject':'adap030','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(basicDiscriminationMode)
adap030 = pardict.copy()

# -- D1:Chr2 adaptive categorization, psychometric and switching --
#d1pi2 = basicDiscriminationMode

pardict = {'subject':'d1pi008','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
d1pi008 = pardict.copy()

pardict = {'subject':'d1pi009','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
d1pi009 = pardict.copy()

pardict = {'subject':'d1pi010','experimenter':'santiago'}
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
d1pi010 = pardict.copy()

pardict = {'subject':'d1pi011','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
d1pi011 = pardict.copy()

pardict = {'subject':'d1pi012','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
d1pi012 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --
adap5 = switchDailyMode

pardict = {'subject':'adap021','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap021 = pardict.copy()

pardict = {'subject':'adap022','experimenter':'santiago'}
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap022 = pardict.copy()

pardict = {'subject':'adap023','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap023 = pardict.copy()

pardict = {'subject':'adap024','experimenter':'santiago'}
pardict.update(adap5)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
pardict.update({'delayToTargetMean':0.1})
adap024 = pardict.copy()

pardict = {'subject':'adap025','experimenter':'santiago'}
pardict.update(adap5)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
pardict.update({'delayToTargetMean':0.1})
adap025 = pardict.copy()






# -- Amplitude modulation discrimination (amod) mice --
# amodMice_kindergarden = {'outcomeMode':'direct'}
# amodMice_smart = {'outcomeMode':'on_next_correct'}
amodMice_regularTask = {'outcomeMode':'only_if_correct'}
amodMice_regularTask.update({'punishTimeError':2})


pardict = {'subject':'amod002','experimenter':'nick'}
pardict.update(amodMice_regularTask)
pardict.update({'psycurveMode':'uniform'})
pardict.update({'soundTypeMode':'mixed_chords'})
amod002 = pardict.copy()

pardict = {'subject':'amod003','experimenter':'nick'}
pardict.update(amodMice_regularTask)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'psycurveMode':'uniform'})
pardict.update({'soundTypeMode':'mixed_chords'})
amod003 = pardict.copy()

pardict = {'subject':'amod004','experimenter':'nick'}
pardict.update(amodMice_regularTask)
pardict.update({'psycurveMode':'uniform','highModFreq':64})
pardict.update({'lowSoundFreq':5000,'highSoundFreq':12000})
# pardict.update({'highModFreq':64})
pardict.update({'soundTypeMode':'mixed_tones'})
amod004 = pardict.copy()

# -- Drd1::ChR2 mice. Frequency discrimination task --

pardict = {'subject':'d1pi003','experimenter':'santiago'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMidBound)
#pardict.update({'antibiasMode':'repeat_mistake'})
d1pi003 = pardict.copy()

pardict = {'subject':'d1pi004','experimenter':'santiago'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
d1pi004 = pardict.copy()

pardict = {'subject':'d1pi005','experimenter':'santiago'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMidBound)
#pardict.update({'antibiasMode':'repeat_mistake'})
d1pi005 = pardict.copy()

pardict = {'subject':'d1pi006','experimenter':'santiago'}
pardict.update(frequencySet6to19)
pardict.update(directMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
d1pi006 = pardict.copy()


# -- Cued discrimination task --
#cuedMiceMode = {'targetMaxIntensity':30, 'cueIntensity':40, 'targetIntensityMode':'fixed','psycurveMode':'single_target'}
#cuedMiceMode = {'targetMaxIntensity':40, 'cueIntensity':40, 'targetIntensityMode':'fixed', 'psycurveMode':'off'}
cuedMiceMode = {'targetMaxIntensity':40, 'cueIntensity':40, 'targetIntensityMode':'fixed', 'psycurveMode':'two_cues_psy'}

pardict = {'subject':'cued000','experimenter':'santiago'} # FOR TESTING
#pardict.update(directMode)
pardict.update({'outcomeMode':'on_next_correct'})
pardict.update({'lowFreq':1000,'midFreq':2000,'highFreq':4000})
#pardict.update({'delayToTargetMean':0.5})
#pardict.update({'automationMode':'increase_delay'})
pardict.update({'psycurveMode':'two_cues_psy'})
cued000 = pardict.copy()

pardict = {'subject':'cued001','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update(cuedMiceMode)
cued001 = pardict.copy()

pardict = {'subject':'cued002','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update(cuedMiceMode)
cued002 = pardict.copy()

pardict = {'subject':'cued003','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update(cuedMiceMode)
cued003 = pardict.copy()

pardict = {'subject':'cued004','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update(cuedMiceMode)
cued004 = pardict.copy()

pardict = {'subject':'cued005','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update(cuedMiceMode)
cued005 = pardict.copy()

pardict = {'subject':'cued006','experimenter':'santiago'}
pardict.update({'outcomeMode':'only_if_correct'})
pardict.update(frequencySet5to24)
pardict.update(cuedMiceMode)
cued006 = pardict.copy()

# -- Adaptive categorization, psychometric and switching --
adap4 = basicDiscriminationMode
#adap4.update({'delayToTargetMean':0.2})

pardict = {'subject':'adap016','experimenter':'santiago'}
#pardict.update(switchBlocksMode)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap016 = pardict.copy()

pardict = {'subject':'adap017','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap017 = pardict.copy()

pardict = {'subject':'adap018','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap018 = pardict.copy()

pardict = {'subject':'adap019','experimenter':'santiago'}
#pardict.update(switchBlocksMode)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap019 = pardict.copy()

pardict = {'subject':'adap020','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap020 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --
adap3 = psyCurveMidBound
adap3.update({'delayToTargetMean':0.2})

pardict = {'subject':'adap011','experimenter':'santiago'}
pardict.update(adap3)
pardict.update(frequencySet6to19)
#pardict.update({'lowFreq':5000,'midFreq':9000,'highFreq':16000})
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap011 = pardict.copy()

pardict = {'subject':'adap012','experimenter':'santiago'}
pardict.update(adap3)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap012 = pardict.copy()

pardict = {'subject':'adap013','experimenter':'santiago'}
pardict.update(adap3)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap013 = pardict.copy()

pardict = {'subject':'adap014','experimenter':'santiago'}
pardict.update(adap3)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap014 = pardict.copy()

pardict = {'subject':'adap015','experimenter':'santiago'}
pardict.update(adap3)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap015 = pardict.copy()



# -- Adaptive categorization, psychometric and switching --
adap2 = switchBlocksMode

pardict = {'subject':'adap006','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet5to24)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap006 = pardict.copy()

pardict = {'subject':'adap007','experimenter':'santiago'}
#pardict.update(basicDiscriminationMode)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet5to24)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap007 = pardict.copy()

pardict = {'subject':'adap008','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet5to24)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap008 = pardict.copy()

pardict = {'subject':'adap009','experimenter':'santiago'}
#pardict.update(basicDiscriminationMode)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet5to24)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap009 = pardict.copy()

pardict = {'subject':'adap010','experimenter':'santiago'}
pardict.update(adap2)
pardict.update(frequencySet5to24)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap010 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --
#firstAdapMice = {'automationMode':'increase_delay','delayToTargetMean':0.1,'delayToTargetHalfRange':0,
#                 'trialsPerBlock':2000}
firstAdapMice = {'punishTimeError':4, 'delayToTargetMean':0.2,'trialsPerBlock':300}

frequencySet6to15 = {'lowFreq':6200,'midFreq':11000,'highFreq':15000}

frequencySet6to10 = {'lowFreq':6200,'midFreq':8000,'highFreq':10000}#This is for adap002

pardict = {'subject':'adap001','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap001 = pardict.copy()

pardict = {'subject':'adap002','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to10)
pardict.update({'punishTimeError':2})
pardict.update({'targetIntensityMode':'fixed','targetMaxIntensity':50})
pardict.update({'punishTimeEarly':0.2,'punishSoundAmplitude':0.05})
adap002 = pardict.copy()

pardict = {'subject':'adap003','experimenter':'santiago'}
pardict.update(firstAdapMice)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap003 = pardict.copy()

pardict = {'subject':'adap004','experimenter':'santiago'}
pardict.update(firstAdapMice)
pardict.update(frequencySet6to19)
# NOTE: there was a mistake here and this mouse was trained in 3 vs 16
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
adap004 = pardict.copy()

pardict = {'subject':'adap005','experimenter':'santiago'}
#pardict.update(directMode)
#pardict.update(increaseDelayMode)
#pardict.update(switchDailyMode)
#pardict.update(switchBlocksMode)
pardict.update(psyCurveMidBound)
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
pardict.update(frequencySet6to19)
#pardict.update(frequencySet5to24)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
test087 = pardict.copy()

pardict = {'subject':'test086','experimenter':'santiago'}
pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
test086 = pardict.copy()

pardict = {'subject':'test085','experimenter':'santiago'}
#pardict.update(switchBlocksMode)
#pardict.update({'currentBlock':'high_boundary'})
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
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
#pardict.update(switchBlocksMode)
pardict.update(psyCurveMidBound)
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
