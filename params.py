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
#increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
#                     'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.05}

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

# ======== Reward change task ========

psyCurveChangeReward = {'punishTimeError':4,
                     'delayToTargetMean':0.2,
                     'currentBlock':'same_reward',
                     'psycurveMode':'uniform',
                     'automationMode':'same_right_left',
                     'punishTimeEarly':0.5,
                     'punishTimeError':2,
                     'punishSoundAmplitude':0,
                     'trialsPerBlock':200,
                     'baseWaterValveL':0.015,
                     'baseWaterValveR':0.015,
                     'factorWaterValveL':4,
                     'factorWaterValveR':4}


# ======== Parameters for each animal =========


# -- Frequency discrimination (some LowLeft, some LowRight) --
adap05xModeLowLeft = basicDiscriminationMode.copy() #This mode is for low frequency going left
adap05xModeLowLeft.update({'soundActionMode':'low_left', 'punishTimeEarly':0, 'punishSoundAmplitude':0})
adap05xModeLowLeft.update({'delayToTargetMean':0.15})
#adap05xModeLowLeft.update({'antibiasMode':'repeat_mistake'})
adap05xModeLowRight = basicDiscriminationMode.copy() #This mode is for low frequency going right
adap05xModeLowRight.update({'soundActionMode':'high_left', 'punishTimeEarly':0, 'punishSoundAmplitude':0})
adap05xModeLowRight.update({'delayToTargetMean':0.15})
#adap05xModeLowRight.update({'antibiasMode':'repeat_mistake'})


adap05xMode = {'delayToTargetMean':0.15, 'punishTimeEarly':0, 'punishSoundAmplitude':0}


pardict = {'subject':'adap048','experimenter':'lan'}
#pardict.update(basicDiscriminationMode)
pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
pardict.update({'lowFreq':8600,'highFreq':19200,'psycurveMode':'uniform','psycurveNfreq':6})
pardict.update({'targetIntensityMode':'fixed'})
pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowLeft)
#pardict.update(adap05xMode)
pardict.update({'delayToTargetMean':0.1,'delayToTargetHalfRange':0.02,'punishSoundAmplitude':0.015})
pardict.update({'soundActionMode':'low_left'})
adap048 = pardict.copy()

pardict = {'subject':'adap049','experimenter':'lan'}
pardict.update(basicDiscriminationMode)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowRight)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'high_left'})
adap049 = pardict.copy()

pardict = {'subject':'adap050','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowLeft)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'low_left'})
#pardict.update({'delayToTargetMean':0.05, 'automationMode':'increase_delay', 'allowEarlyWithdrawal':'on'})
adap050 = pardict.copy()

pardict = {'subject':'adap051','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowRight)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'high_left'})
adap051 = pardict.copy()

pardict = {'subject':'adap052','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowLeft)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'low_left'})
adap052 = pardict.copy()

pardict = {'subject':'adap053','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowRight)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'high_left'})
adap053 = pardict.copy()

pardict = {'subject':'adap054','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowLeft)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'low_left'})
#pardict.update({'delayToTargetMean':0.05, 'automationMode':'increase_delay', 'allowEarlyWithdrawal':'on'})
adap054 = pardict.copy()

pardict = {'subject':'adap055','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowRight)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'high_left'})
adap055 = pardict.copy()

pardict = {'subject':'adap056','experimenter':'lan'}
pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
pardict.update({'lowFreq':7300,'highFreq':16300,'psycurveMode':'uniform','psycurveNfreq':6})
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowLeft)
#pardict.update(adap05xMode)
pardict.update({'targetIntensityMode':'fixed'})
pardict.update({'delayToTargetMean':0.13,'delayToTargetHalfRange':0.02})
pardict.update({'soundActionMode':'low_left'})
adap056 = pardict.copy()

pardict = {'subject':'adap057','experimenter':'lan'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap05xModeLowRight)
pardict.update(adap05xMode)
pardict.update({'soundActionMode':'high_left'})
adap057 = pardict.copy()

pardict = {'subject': 'adap058', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
adap058 = pardict.copy()

pardict = {'subject': 'adap059', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap059 = pardict.copy()

pardict = {'subject': 'adap060', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap060 = pardict.copy()

pardict = {'subject': 'adap061', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap061 = pardict.copy()

pardict = {'subject': 'adap067', 'experimenter': 'jardon', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
pardict.update({'delayToTargetMean':0.15,'targetIntensityMode':'fixed'})
#pardict.update({'antibiasMode':'repeat_mistake'})
adap067 = pardict.copy()

pardict = {'subject': 'adap071', 'experimenter': 'jardon', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap071 = pardict.copy()


# -- Go-signal mice (and some moved to reward-change) --
psyCurveGoSignal = {'outcomeMode':'only_if_correct', 'delayToTargetHalfRange':0.05, 'delayToTargetMean':0.1,
                    'currentBlock':'mid_boundary', 'targetDuration':0.1,
                    'psycurveMode':'off', 'punishSoundAmplitude':0}
# 'delayToGoSignal':0, 'psycurveMode':'uniform',

pardict = {'subject': 'gosi001', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi001 = pardict.copy()

pardict = {'subject': 'gosi002', 'experimenter': 'stacy', 'trainer': ''}
#pardict.update(psyCurveChangeReward)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi002 = pardict.copy()

pardict = {'subject': 'gosi003', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi003 = pardict.copy()

pardict = {'subject': 'gosi004', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi004 = pardict.copy()

pardict = {'subject': 'gosi005', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi005 = pardict.copy()

pardict = {'subject': 'gosi006', 'experimenter': 'stacy', 'trainer': ''}
#pardict.update(psyCurveChangeReward)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi006 = pardict.copy()

pardict = {'subject': 'gosi007', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi007 = pardict.copy()

pardict = {'subject': 'gosi008', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi008 = pardict.copy()

pardict = {'subject': 'gosi009', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi009 = pardict.copy()

pardict = {'subject': 'gosi010', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi010 = pardict.copy()

pardict = {'subject': 'gosi011', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi011 = pardict.copy()

pardict = {'subject': 'gosi012', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'off-on'})
#pardict.update(psyCurveGoSignal)
gosi012 = pardict.copy()

pardict = {'subject': 'gosi013', 'experimenter': 'stacy', 'trainer': ''}
#pardict.update(psyCurveChangeReward)
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi013 = pardict.copy()

pardict = {'subject': 'gosi014', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi014 = pardict.copy()

pardict = {'subject': 'gosi015', 'experimenter': 'stacy', 'trainer': ''}
pardict.update(psyCurveChangeReward)
pardict.update(frequencySet6to19)
#pardict.update({'goSignalMode':'on-off'})
#pardict.update(psyCurveGoSignal)
gosi015 = pardict.copy()



'''
psyCurveChangeReward = {'punishTimeError':4,
                     'delayToTargetMean':0.1,
                     'currentBlock':'same_reward',
                     'psycurveMode':'uniform',
                     'automationMode':'same_left_right',
                     'punishTimeEarly':0.5,
                     'punishTimeError':2,
                     'punishSoundAmplitude':0.05}
'''



# -- bandwidth mice (tone detection task) --

bandSidesDirectMode = {'outcomeMode':'sides_direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

bandDirectMode = {'outcomeMode':'direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

bandNextCorrectNoDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only' }

bandNextCorrectIntDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only',
                          'delayToTargetMean':0.15, 'delayToTargetHalfRange':0.05 }

bandNextCorrectFinDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only',
                          'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1 }

bandOnlyCorrect = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 
                   'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1 }

bandOnlyifCorrectOffOnWithdrawal = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 
                        'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1, 
                        'bandMode':'white_only',
                        'soundMode':'off_on_withdrawal'}

bandOnlyCorrectIntMode = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'uniform',
                          'minBand':2.0, 'maxBand':4.0, 'numBands':2, 'includeWhite':'yes',
                          'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1,
                          'soundMode':'off_on_withdrawal'}

bandOnlyCorrectHardMode = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'uniform',
                          'minBand':0.25, 'maxBand':4.0, 'numBands':5, 'includeWhite':'yes',
                          'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1,
                          'soundMode':'off_on_withdrawal'}
bandPreSNR = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'max_only',
                          'maxBand':1.0, 'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1,
                          'soundMode':'off_on_withdrawal'}
bandEasySNR = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':5, 'maxSNR':20, 'numSNRs':4, 'bandMode':'max_only',
                          'maxBand':1.0, 'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1,
                          'soundMode':'off_on_withdrawal'}
bandEasySNR2BW = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':10, 'maxSNR':20, 'numSNRs':3, 
               'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1,
               'bandMode':'uniform', 'minBand':0.25, 'maxBand':0.25, 'numBands':1, 'includeWhite':'yes',
               'soundMode':'off_on_withdrawal','noiseMode':'max_only'}
bandSNR = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':-5, 'maxSNR':15, 'numSNRs':5, 'bandMode':'max_only',
                          'maxBand':1.0, 'delayToTargetMean':0.3, 'delayToTargetHalfRange':0.1,
                          'soundMode':'off_on_withdrawal'}

bandBilateralLaser = {'nOnsetsToUse':'1', 'laserOnsetFromSoundOnset1':0, 'laserDuration':0.6, 'laserMode':'random'}
bandUnilateralLaser = {'nOnsetsToUse':'1', 'laserOnsetFromSoundOnset1':0, 'laserDuration':0.6, 'stimMode':'mixed_all', 'fractionTrialsLaser':0.45, 'laserMode':'random'}
bandOnsets = {'nOnsetsToUse':'3', 'laserDuration':0.2,'fractionTrialsLaser':0.45}
threeNoiseThreshMode = {'noiseMode':'uniform', 'minNoiseAmp':30, 'maxNoiseAmp':40, 'numAmps':3}
oneNoiseThreshMode = {'noiseMode':'max_only', 'maxNoiseAmp':40}

pardict = {'subject': 'band090', 'experimenter': 'anna'}
pardict.update(bandEasySNR2BW)
#pardict.update({'antibiasMode':'repeat_mistake'})
band090 = pardict.copy()

pardict = {'subject': 'band091', 'experimenter': 'anna'}
pardict.update(bandEasySNR2BW)
pardict.update(bandBilateralLaser)
band091 = pardict.copy()

pardict = {'subject': 'band093', 'experimenter': 'anna'}
pardict.update(bandEasySNR2BW)
pardict.update(bandBilateralLaser)
#pardict.update({'antibiasMode':'repeat_mistake'})
band093 = pardict.copy()

pardict = {'subject': 'band105', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band105 = pardict.copy()

pardict = {'subject': 'band106', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band106 = pardict.copy()

pardict = {'subject': 'band107', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band107 = pardict.copy()

pardict = {'subject': 'band108', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band108 = pardict.copy()

pardict = {'subject': 'band109', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band109 = pardict.copy()

pardict = {'subject': 'band110', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band110 = pardict.copy()

pardict = {'subject': 'band111', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band111 = pardict.copy()

pardict = {'subject': 'band112', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band112 = pardict.copy()

pardict = {'subject': 'band113', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band113 = pardict.copy()

pardict = {'subject': 'band114', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band114 = pardict.copy()

pardict = {'subject': 'band115', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band115 = pardict.copy()

pardict = {'subject': 'band116', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band116 = pardict.copy()

pardict = {'subject': 'band117', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band117 = pardict.copy()

pardict = {'subject': 'band118', 'experimenter': 'anna'}
pardict.update(bandOnlyifCorrectOffOnWithdrawal)
#pardict.update({'antibiasMode':'repeat_mistake'})
band118 = pardict.copy()

pardict = {'subject': 'band119', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
#pardict.update({'antibiasMode':'repeat_mistake'})
band119 = pardict.copy()

pardict = {'subject': 'band120', 'experimenter': 'anna'}
pardict.update(bandOnlyCorrect)
pardict.update({'antibiasMode':'repeat_mistake'})
band120 = pardict.copy()




# -- adaptive frequency discrimination --

#adap03xMode = basicDiscriminationMode #increaseDelayMode
adap03xMode = psyCurveMidBound   #basicDiscriminationMode #increaseDelayMode
adap03xMode.update({'punishSoundAmplitude': 0})
#adap03xMode.update({'antibiasMode':'repeat_mistake'})
adap04xModeLowLeft = basicDiscriminationMode.copy() #This mode is for low frequency going left
adap04xModeLowLeft.update({'soundActionMode':'low_left', 'punishSoundAmplitude':0})
#adap04xModeLowLeft.update({'antibiasMode':'repeat_mistake'})
adap04xModeLowRight = basicDiscriminationMode.copy() #This mode is for low frequency going right
adap04xModeLowRight.update({'soundActionMode':'high_left', 'punishSoundAmplitude':0})
#adap04xModeLowRight.update({'antibiasMode':'repeat_mistake'})

pardict = {'subject':'adap041','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap04xModeLowLeft)
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'low_left', 'punishSoundAmplitude':0})
adap041 = pardict.copy()

pardict = {'subject':'adap042','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap04xModeLowLeft)
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'low_left', 'punishSoundAmplitude':0})
adap042 = pardict.copy()

pardict = {'subject':'adap043','experimenter':'lan'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap04xModeLowLeft)
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'low_left', 'punishSoundAmplitude':0})
adap043 = pardict.copy()

pardict = {'subject':'adap044','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap04xModeLowRight)
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'high_left', 'punishSoundAmplitude':0})
adap044 = pardict.copy()

pardict = {'subject':'adap045','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap04xModeLowRight)
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'high_left', 'punishSoundAmplitude':0})
adap045 = pardict.copy()

pardict = {'subject':'adap046','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(adap04xModeLowRight)
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'high_left', 'punishSoundAmplitude':0})
adap046 = pardict.copy()

pardict = {'subject':'adap047','experimenter':'lan'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(psyCurveMidBound)
pardict.update({'soundActionMode':'high_left', 'punishSoundAmplitude':0})
#pardict.update(adap04xModeLowRight)
adap047 = pardict.copy()


pardict = {'subject':'adap040','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap040 = pardict.copy()

pardict = {'subject':'adap039','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap039 = pardict.copy()

pardict = {'subject':'adap038','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap038 = pardict.copy()

pardict = {'subject':'adap037','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap037 = pardict.copy()

pardict = {'subject':'adap036','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap036 = pardict.copy()

pardict = {'subject':'adap035','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap035 = pardict.copy()

pardict = {'subject':'adap034','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap034 = pardict.copy()

pardict = {'subject':'adap033','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap033 = pardict.copy()

pardict = {'subject':'adap032','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap032 = pardict.copy()

pardict = {'subject':'adap031','experimenter':'santiago'}
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(adap03xMode)
adap031 = pardict.copy()


# -- adap026-030 --
pardict = {'subject':'adap026','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
# pardict.update(basicDiscriminationMode)
adap026 = pardict.copy()

pardict = {'subject':'adap027','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
# pardict.update(basicDiscriminationMode)
adap027 = pardict.copy()

pardict = {'subject':'adap028','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
# pardict.update(basicDiscriminationMode)
adap028 = pardict.copy()

pardict = {'subject':'adap029','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
# pardict.update(basicDiscriminationMode)
adap029 = pardict.copy()

pardict = {'subject':'adap030','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
# pardict.update({'antibiasMode':'repeat_mistake'})
# pardict.update(basicDiscriminationMode)
adap030 = pardict.copy()


# -- D1:Chr2 adaptive categorization, psychometric and switching --
# D1:Chr2 on reward change discrimination psychometric curve
d1pi1 = basicDiscriminationMode
d1pi2 = psyCurveMidBound 
d1pi1.update({'punishTimeError':2})

pardict = {'subject':'d1pi018','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi2)
d1pi018 = pardict.copy()

pardict = {'subject':'d1pi019','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi2)
d1pi019 = pardict.copy()

pardict = {'subject':'d1pi020','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi2)
d1pi020 = pardict.copy()

pardict = {'subject':'d1pi008','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(psyCurveMidBound)
d1pi008 = pardict.copy()

pardict = {'subject':'d1pi011','experimenter':'lan'}
pardict.update(frequencySet4to13)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(psyCurveMidBound)
pardict.update({'psycurveMode':'uniform'})
pardict.update({'delayToTargetMean':0.1,'delayToTargetHalfRange':0.02,})
pardict.update({'targetDuration':0.08})
pardict.update({'targetMaxIntensity':53})
pardict.update({'targetIntensityMode':'fixed'})
d1pi011 = pardict.copy()

pardict = {'subject':'d1pi013','experimenter':'lan'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi1)
d1pi013 = pardict.copy()

pardict = {'subject':'d1pi014','experimenter':'santiago'}
#pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update(d1pi1)
pardict.update({'lowFreq':7300,'highFreq':16300,'psycurveMode':'uniform','psycurveNfreq':6,'currentBlock':'mid_boundary'})
pardict.update({'targetMaxIntensity':52,'targetIntensityMode':'fixed'})
pardict.update({'delayToTargetMean':0.15, 'delayToTargetHalfRange':0.05})
pardict.update({'punishSoundAmplitude':0.015,'punishTimeError':2})
d1pi014 = pardict.copy()

pardict = {'subject':'d1pi015','experimenter':'santiago'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi1)
d1pi015 = pardict.copy()

pardict = {'subject':'d1pi016','experimenter':'santiago'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi1)
d1pi016 = pardict.copy()

pardict = {'subject':'d1pi017','experimenter':'santiago'}
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update(d1pi1)
d1pi017 = pardict.copy()


#pardict = {'subject':'d1pi008','experimenter':'santiago'}
#pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
#pardict.update(psyCurveChangeReward)
#pardict.update({'lowFreq':6200,'highFreq':19200})
#d1pi008 = pardict.copy()

pardict = {'subject':'d1pi009','experimenter':'santiago'}
#pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
pardict.update(psyCurveChangeReward)
pardict.update({'lowFreq':6200,'highFreq':19200})
d1pi009 = pardict.copy()

pardict = {'subject':'d1pi010','experimenter':'santiago'}
#pardict.update(basicDiscriminationMode)
#pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
pardict.update(psyCurveChangeReward)
pardict.update({'lowFreq':6200,'highFreq':19200})
d1pi010 = pardict.copy()

#pardict = {'subject':'d1pi011','experimenter':'santiago'}
#pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
#pardict.update(frequencySet3to16)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
#pardict.update(psyCurveChangeReward)
#pardict.update({'lowFreq':3000,'highFreq':16000})
#d1pi011 = pardict.copy()

pardict = {'subject':'d1pi012','experimenter':'santiago'}
#pardict.update(psyCurveMidBound)
#pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
#pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
#pardict.update({'delayToTargetMean':0.1})
pardict.update(psyCurveChangeReward)
pardict.update({'lowFreq':6200,'highFreq':19200})
d1pi012 = pardict.copy()


# -- Adaptive categorization, psychometric and switching --
adap5 = switchDailyMode

# pardict = {'subject':'adap021','experimenter':'santiago'}
# pardict.update(switchBlocksMode)
# pardict.update(frequencySet6to19)
# #pardict.update({'antibiasMode':'repeat_mistake'})
# pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
# adap021 = pardict.copy()

#adap021
pardict = {'subject':'adap021','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
adap021 = pardict.copy()

pardict = {'subject':'adap022','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
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
pardict.update(switchBlocksMode)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
pardict.update({'delayToTargetMean':0.1})
adap024 = pardict.copy()

pardict = {'subject':'adap025','experimenter':'santiago'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
pardict.update({'punishTimeEarly':0.5,'punishSoundAmplitude':0.05})
pardict.update({'delayToTargetMean':0.1})
adap025 = pardict.copy()






# -- Amplitude modulation discrimination (amod) mice --
amodMice_modulationSidesDirect = {'outcomeMode':'sides_direct', 'soundTypeMode':'amp_mod'}
amodMice_modulationDirect = {'outcomeMode':'direct', 'soundTypeMode':'amp_mod'}
# amodMice_smart = {'outcomeMode':'on_next_correct'}

amodMice_modulationOnNextCorrect = {'outcomeMode':'on_next_correct', 'soundTypeMode':'amp_mod'}
amodMice_modulationOnlyIfCorrect = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod'}
amodMice_mixed_tones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones'}

amodMice_regularTask = {'outcomeMode':'only_if_correct'}
amodMice_regularTask.update({'punishTimeError':2})

### new improved amod parameters ###
amodSidesDirect = {'outcomeMode':'sides_direct', 'soundTypeMode':'amp_mod'}
amodDirect = {'outcomeMode':'direct', 'soundTypeMode':'amp_mod'}
amodNextCorrectAM = {'outcomeMode':'on_next_correct', 'soundTypeMode':'amp_mod'}
amodIfCorrectAM = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod'}
amodPsycurveAM = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod', 'psycurveMode':'uniform'}

amodIfCorrectTones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'tones', 'targetIntensityMode':'randMinus20'}

amodPsycurveTones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'tones', 'psycurveMode':'uniform','targetIntensityMode':'randMinus20'}

amodIfCorrectMixed = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones','targetIntensityMode':'randMinus20'}

amodPsycurveMixed = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones', 'psycurveMode':'uniform', 'targetIntensityMode':'randMinus20'}



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

# pardict = {'subject':'amod004','experimenter':'nick'}
# pardict.update(amodMice_regularTask)
# pardict.update({'psycurveMode':'uniform','highModFreq':64})
# pardict.update({'lowSoundFreq':5000,'highSoundFreq':12000})
# # pardict.update({'highModFreq':64})
# pardict.update({'soundTypeMode':'mixed_tones'})
# amod004 = pardict.copy()

pardict = {'subject':'amod004','experimenter':'nick'}
pardict.update(amodMice_regularTask)
pardict.update({'psycurveMode':'uniform'})
pardict.update({'soundTypeMode':'mixed_chords'})
amod004 = pardict.copy()

## -- New Amod mice --
## Starting on direct mode with amp mod only

pardict = {'subject':'amod006','experimenter':'nick'}
pardict.update(amodPsycurveMixed)
pardict.update({'lowSoundFreq':7000,'highSoundFreq':12000})
pardict.update({'lowModFreq': 4, 'highModFreq':64})
amod006 = pardict.copy()

pardict = {'subject':'amod007','experimenter':'nick'}
pardict.update({'lowSoundFreq':7000,'highSoundFreq':12000})
pardict.update({'lowModFreq': 4, 'highModFreq':64})
pardict.update(amodPsycurveMixed)
amod007 = pardict.copy()

pardict = {'subject':'amod008','experimenter':'nick'}
pardict.update({'lowSoundFreq':7000,'highSoundFreq':12000})
pardict.update({'lowModFreq': 4, 'highModFreq':64})
pardict.update(amodPsycurveMixed)
amod008 = pardict.copy()

pardict = {'subject':'amod009','experimenter':'nick'}
pardict.update({'lowSoundFreq':7000,'highSoundFreq':12000})
pardict.update({'lowModFreq': 4, 'highModFreq':64})
pardict.update(amodPsycurveMixed)
amod009 = pardict.copy()

pardict = {'subject':'amod010','experimenter':'nick'}
pardict.update({'lowSoundFreq':7000,'highSoundFreq':12000})
pardict.update({'lowModFreq': 4, 'highModFreq':64})
pardict.update(amodPsycurveMixed)
amod010 = pardict.copy()



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

