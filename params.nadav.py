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

bandEasySNR = {'outcomeMode':'only_if_correct', 'threshMode':'linear', 'minSNR':10, 'maxSNR':20, 'numSNRs':3, 
               'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
               'bandMode':'uniform', 'minBand':0.25, 'maxBand':1.0, 'numBands':2, 'includeWhite':'yes',
               'soundMode':'off_on_withdrawal','noiseMode':'max_only'}

bilateralLaser = {'laserMode':'random'}

# -- bandwidth mice --

pardict = {'subject': 'band046', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band046 = pardict.copy()

pardict = {'subject': 'band047', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band047 = pardict.copy()

pardict = {'subject': 'band048', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band048 = pardict.copy()

pardict = {'subject': 'band049', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band049 = pardict.copy()

pardict = {'subject': 'band050', 'experimenter': 'nadav'}
pardict.update(onlyIfCorrectMultipleBandwidths)
band050 = pardict.copy()

pardict = {'subject': 'band051', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
pardict.update(bilateralLaser)
band051 = pardict.copy()

pardict = {'subject': 'band052', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band052 = pardict.copy()

pardict = {'subject': 'band053', 'experimenter': 'nadav'}
pardict.update(bandEasySNR)
band053 = pardict.copy()

pardict = {'subject': 'band065', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
band065 = pardict.copy()

pardict = {'subject': 'band066', 'experimenter': 'nadav'}
pardict.update(directMode)
band066 = pardict.copy()

pardict = {'subject': 'band067', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
band067 = pardict.copy()

pardict = {'subject': 'band068', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
band068 = pardict.copy()

pardict = {'subject': 'band069', 'experimenter': 'nadav'}
pardict.update(nextCorrectDel)
band069 = pardict.copy()

pardict = {'subject': 'band070', 'experimenter': 'nadav'}
pardict.update(nextCorrectNoDel)
band070 = pardict.copy()

pardict = {'subject': 'band071', 'experimenter': 'nadav'}
pardict.update(nextCorrectDel)
band071 = pardict.copy()
