# -- dictionaries of params for different stages --

sidesDirectMode = {'outcomeMode':'sides_direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

directMode = {'outcomeMode':'direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

nextCorrectNoDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only' }

nextCorrectDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.1, 'delayToTargetHalfRange':0.05 }

nextCorrectDel2 = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

outcomeOnlyifCorrect= {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

outcomeOnlyifCorrect2= {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

# -- bandwidth mice --

pardict = {'subject': 'band046', 'experimenter': 'nadav'}
pardict.update(directMode)
band046 = pardict.copy()

pardict = {'subject': 'band047', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band047 = pardict.copy()

pardict = {'subject': 'band048', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band048 = pardict.copy()

pardict = {'subject': 'band049', 'experimenter': 'nadav'}
pardict.update(directMode)
band049 = pardict.copy()

pardict = {'subject': 'band050', 'experimenter': 'nadav'}
pardict.update(directMode)
band050 = pardict.copy()

pardict = {'subject': 'band051', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band051 = pardict.copy()

pardict = {'subject': 'band052', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band052 = pardict.copy()

pardict = {'subject': 'band053', 'experimenter': 'nadav'}
pardict.update(directMode)
band053 = pardict.copy()
