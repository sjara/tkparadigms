'''
Define parameters for different subjects.
'''

sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0}
directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0}
directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0}
increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                     'automationMode':'increase_delay', 'punishTimeEarly':0, 'punishSoundAmplitude':0}
requireCorrectMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
                      'punishTimeEarly':0, 'punishSoundAmplitude':0}

# ======== Parameters for each animal =========

pardict = {'subject':'bili001','experimenter':'cora'}
pardict.update({'relevantFeature':'spectral'})
pardict.update(requireCorrectMode)
pardict.update({'antibiasMode':'repeat_mistake'})
bili001 = pardict.copy()

pardict = {'subject':'bili002','experimenter':'cora'}
pardict.update({'relevantFeature':'temporal'})
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili002 = pardict.copy()

pardict = {'subject':'bili003','experimenter':'cora'}
pardict.update({'relevantFeature':'spectral'})
pardict.update(increaseDelayMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili003 = pardict.copy()

pardict = {'subject':'bili004','experimenter':'cora'}
pardict.update({'relevantFeature':'temporal'})
pardict.update(increaseDelayMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili004 = pardict.copy()

pardict = {'subject':'bili005','experimenter':'cora'}
pardict.update({'relevantFeature':'spectral'})
pardict.update(requireCorrectMode)
pardict.update({'antibiasMode':'repeat_mistake'})
bili005 = pardict.copy()

pardict = {'subject':'bili006','experimenter':'cora'}
pardict.update({'relevantFeature':'temporal'})
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili006 = pardict.copy()

pardict = {'subject':'bili007','experimenter':'cora'}
pardict.update({'relevantFeature':'spectral'})
pardict.update(requireCorrectMode)
pardict.update({'antibiasMode':'repeat_mistake'})
bili007 = pardict.copy()



