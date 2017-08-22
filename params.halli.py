'''
Define parameters for different subjects
'''

frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}

# ======== Adaptive frequency discrimination task ========
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
psyCurveMode = {'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'currentBlock':'mid_boundary',
                           'punishTimeEarly':0, 'punishSoundAmplitude':0, 'psycurveMode':'uniform'}

# ======== Parameters for each animal =========

pardict = {'subject':'adap062','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap062 = pardict.copy()

pardict = {'subject':'adap063','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap063 = pardict.copy()

pardict = {'subject':'adap064','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap064 = pardict.copy()

pardict = {'subject':'adap065','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap065 = pardict.copy()

pardict = {'subject':'adap066','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(requireCorrectMode)
pardict.update({'antibiasMode':'repeat_mistake'})
adap066 = pardict.copy()

pardict = {'subject':'adap067','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap067 = pardict.copy()

pardict = {'subject':'adap068','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap068 = pardict.copy()

pardict = {'subject':'adap069','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap069 = pardict.copy()

pardict = {'subject':'adap070','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap070 = pardict.copy()

pardict = {'subject':'adap071','experimenter':'halli'}
pardict.update(frequencySet6to19)
pardict.update(basicDiscriminationMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap071 = pardict.copy()
