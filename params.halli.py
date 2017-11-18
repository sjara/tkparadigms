'''
Define parameters for different subjects
'''

frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}

# ======== Method 1: Adaptive frequency discrimination task ========
sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                     'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.1,
                     'allowEarlyWithdrawal':'on','punishTimeEarly':0, 'punishSoundAmplitude':0}
requireCorrectMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
                      'currentBlock':'mid_boundary', 'targetDuration':0.1,
                      'allowEarlyWithdrawal':'on','punishTimeEarly':0, 'punishSoundAmplitude':0}
basicDiscriminationMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                           'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                           'punishTimeEarly':0.5, 'punishSoundAmplitude':50}
psyCurveMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                'punishTimeEarly':0.5, 'punishSoundAmplitude':50, 'psycurveMode':'uniform'}

# ======== Method 2: Adaptive frequency discrimination task ========
M2sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
M2directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
M2requireCorrectMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.075, 'delayToTargetHalfRange':0.025,
                      'currentBlock':'mid_boundary', 'targetDuration':0.1,
                      'allowEarlyWithdrawal':'on','punishTimeEarly':0, 'punishSoundAmplitude':0}
M2increaseDelayMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.05, 'delayToTargetHalfRange':0,
                     'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.1,
                     'allowEarlyWithdrawal':'on','punishTimeEarly':0, 'punishSoundAmplitude':0}
M2basicDiscriminationMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                           'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                           'punishTimeEarly':0.5, 'punishSoundAmplitude':50}
M2psyCurveMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                'punishTimeEarly':0.5, 'punishSoundAmplitude':50, 'psycurveMode':'uniform'}

# ======== Method 3: Adaptive frequency discrimination task ========
M3sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
M3directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
M3increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                     'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.1,
                     'allowEarlyWithdrawal':'on','punishTimeEarly':0, 'punishSoundAmplitude':0}
M3requireCorrectMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
                      'currentBlock':'mid_boundary', 'targetDuration':0.1,
                      'allowEarlyWithdrawal':'on','punishTimeEarly':0, 'punishSoundAmplitude':0}
M3basicDiscriminationMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                           'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                           'punishTimeEarly':0.5, 'punishSoundAmplitude':50}
M3psyCurveMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
                'currentBlock':'mid_boundary', 'targetDuration':0.1, 'allowEarlyWithdrawal':'off',
                'punishTimeEarly':0.5, 'punishSoundAmplitude':50, 'psycurveMode':'uniform'}



# ======== Parameters for each animal =========

pardict = {'subject':'adap062','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap062 = pardict.copy()

pardict = {'subject':'adap063','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap063 = pardict.copy()

pardict = {'subject':'adap064','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap064 = pardict.copy()

pardict = {'subject':'adap065','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap065 = pardict.copy()

pardict = {'subject':'adap066','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap066 = pardict.copy()

pardict = {'subject':'adap067','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap067 = pardict.copy()

pardict = {'subject':'adap068','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap068 = pardict.copy()

pardict = {'subject':'adap069','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap069 = pardict.copy()

pardict = {'subject':'adap070','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap070 = pardict.copy()

pardict = {'subject':'adap071','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap071 = pardict.copy()

pardict = {'subject':'adap072','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M2increaseDelayMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap072 = pardict.copy()

pardict = {'subject':'adap073','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M2psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap073 = pardict.copy()

pardict = {'subject':'adap074','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M2basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap074 = pardict.copy()

pardict = {'subject':'adap075','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M2basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap075 = pardict.copy()

pardict = {'subject':'adap076','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap076 = pardict.copy()

pardict = {'subject':'adap077','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M3psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap077 = pardict.copy()

pardict = {'subject':'adap078','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M3psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap078 = pardict.copy()

pardict = {'subject':'adap079','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M3psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap079 = pardict.copy()

pardict = {'subject':'adap080','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M3psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap080 = pardict.copy()

pardict = {'subject':'adap081','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(M3psyCurveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap081 = pardict.copy()
