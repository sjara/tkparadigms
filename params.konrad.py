'''
Define parameters for different subjects
'''

basicParams = {'trainer':'kb', 'stimPreDuration':1}



# ======== Parameters for each animal =========

pardict = {'subject':'chad000','experimenter':'konrad'}
pardict.update(basicParams)
pardict.update({'freq1':3000, 'timeOut':0.1})
chad000 = pardict.copy()

pardict = {'subject':'chad001','experimenter':'konrad'}
pardict.update(basicParams)
chad001 = pardict.copy()

pardict = {'subject':'chad002','experimenter':'konrad'}
pardict.update(basicParams)
chad002 = pardict.copy()

pardict = {'subject':'chad003','experimenter':'konrad'}
pardict.update(basicParams)
chad003 = pardict.copy()

pardict = {'subject':'chad004','experimenter':'konrad'}
pardict.update(basicParams)
chad004 = pardict.copy()

pardict = {'subject':'chad005','experimenter':'konrad'}
pardict.update(basicParams)
chad005 = pardict.copy()
