'''
Define parameters for different subjects.
'''

sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0}
directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0}
increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                     'automationMode':'increase_delay', 'punishTimeEarly':0, 'punishSoundAmplitude':0}
requireCorrectMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
                      'punishTimeEarly':0, 'punishSoundAmplitude':0}
psyCurveMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
                'punishTimeEarly':0, 'punishSoundAmplitude':0, 'psycurveMode':'extreme80pc'}
activeMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
              'punishTimeEarly':0, 'punishSoundAmplitude':0, 'psycurveMode':'uniform', 'maxNtrials':750}
passiveMode = {'outcomeMode':'on_any_poke', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
              'punishTimeEarly':0, 'punishSoundAmplitude':0, 'psycurveMode':'uniform', 'maxNtrials':750}
passiveModeExtremes = {'outcomeMode':'on_any_poke', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.1,
                       'punishTimeEarly':0, 'punishSoundAmplitude':0, 'maxNtrials':750}

# ======== Parameters for each animal =========

# -- Test mouse --
pardict = {'subject':'bili000','experimenter':'santiago'}
#pardict.update(activeMode)
pardict.update(passiveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili000 = pardict.copy()

###bili016-024 (PV-ChR2)

pardict = {'subject':'bili016','experimenter':'erin'}
pardict.update(activeMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili016 = pardict.copy()

pardict = {'subject':'bili017','experimenter':'erin'}
pardict.update(activeMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili017 = pardict.copy()

pardict = {'subject':'bili018','experimenter':'erin'}
pardict.update(activeMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili018 = pardict.copy()

pardict = {'subject':'bili019','experimenter':'erin'}
pardict.update(activeMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili019 = pardict.copy()

pardict = {'subject':'bili020','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili020 = pardict.copy()

pardict = {'subject':'bili021','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili021 = pardict.copy()

pardict = {'subject':'bili022','experimenter':'erin'}
pardict.update(activeMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili022 = pardict.copy()

pardict = {'subject':'bili023','experimenter':'erin'}
pardict.update(passiveMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili023 = pardict.copy()

pardict = {'subject':'bili024','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili024 = pardict.copy()

# -----

pardict = {'subject':'bili025','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili025 = pardict.copy()

pardict = {'subject':'bili026','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili026 = pardict.copy()

pardict = {'subject':'bili027','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili027 = pardict.copy()

pardict = {'subject':'bili028','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili028 = pardict.copy()

pardict = {'subject':'bili029','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili029 = pardict.copy()

pardict = {'subject':'bili030','experimenter':'erin'}
pardict.update(requireCorrectMode)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili030 = pardict.copy()

pardict = {'subject':'bili031','experimenter':'erin'}
pardict.update(passiveModeExtremes)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili031 = pardict.copy()

pardict = {'subject':'bili032','experimenter':'erin'}
pardict.update(passiveModeExtremes)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili032 = pardict.copy()

pardict = {'subject':'bili033','experimenter':'erin'}
pardict.update(passiveModeExtremes)
#pardict.update({'antibiasMode':'repeat_mistake'})
bili033 = pardict.copy()

