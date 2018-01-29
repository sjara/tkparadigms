# -- dictionaries of params for different stages --

sidesDirectMode = {'outcomeMode':'sides_direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

directMode = {'outcomeMode':'direct', 'threshMode': 'max_only', 'maxSNR': 20, 'bandMode': 'white_only'}

nextCorrectNoDel = {'outcomeMode':'on_next_correct', 'threshMode':'max_only', 'maxSNR':20, 'bandMode':'white_only' }


# -- bandwidth mice --

pardict = {'subject': 'band046', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band046 = pardict.copy()

pardict = {'subject': 'band047', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band047 = pardict.copy()

pardict = {'subject': 'band048', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band048 = pardict.copy()

pardict = {'subject': 'band049', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band049 = pardict.copy()

pardict = {'subject': 'band050', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band050 = pardict.copy()

pardict = {'subject': 'band051', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band051 = pardict.copy()

pardict = {'subject': 'band052', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band052 = pardict.copy()

pardict = {'subject': 'band053', 'experimenter': 'nadav'}
pardict.update(sidesDirectMode)
band053 = pardict.copy()
