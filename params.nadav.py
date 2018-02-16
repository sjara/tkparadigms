# -- dictionaries of params for different stages --

sidesDirectMode = {'outcomeMode':'sides_direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

directMode = {'outcomeMode':'direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

nextCorrectNoDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only' }

nextCorrectDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.1, 'delayToTargetHalfRange':0.05 }

nextCorrectDel2 = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

outcomeOnlyifCorrect= {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05 }

outcomeOnlyifCorrectOffOnWithdrawal = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 
                        'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 
                        'bandMode':'white_only',
                        'soundMode':'off_on_withdrawal'}

onlyIfCorrectMultipleBandwidths = {'outcomeMode':'only_if_correct', 'threshMode':'max_only', 'maxSNR':20, 
                        'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 
                        'bandMode':'uniform', 'minBand':0.25, 'maxBand':1.0, 'numBands':2, 'includeWhite':'yes',
                        'soundMode':'off_on_withdrawal'}

# -- bandwidth mice --

pardict = {'subject': 'band046', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band046 = pardict.copy()

pardict = {'subject': 'band047', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band047 = pardict.copy()

pardict = {'subject': 'band048', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band048 = pardict.copy()

pardict = {'subject': 'band049', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band049 = pardict.copy()

pardict = {'subject': 'band050', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band050 = pardict.copy()

pardict = {'subject': 'band051', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band051 = pardict.copy()

pardict = {'subject': 'band052', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band052 = pardict.copy()

pardict = {'subject': 'band053', 'experimenter': 'nadav'}
pardict.update(outcomeOnlyifCorrect)
band053 = pardict.copy()
