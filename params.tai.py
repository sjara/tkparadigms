'''
Parameters for photoinactivation during freq discrimination task (photostim_freq_discrim.py)
'''

frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}

psyCurvePhotoInactivation = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                             'currentBlock':'mid_boundary','psycurveMode':'uniform',
                             'laserFrontOverhang':0.05, 'laserBackOverhang':0.1,
                             'percentLaserTrialLeft':0.3, 'percentLaserTrialRight':0, }

pardict = {'subject':'adap038','experimenter':'tai'}
pardict.update(frequencySet6to19)
pardict.update(psyCurvePhotoInactivation)
adap038 = pardict.copy()

pardict = {'subject':'adap031','experimenter':'tai'}
pardict.update(frequencySet6to19)
pardict.update(psyCurvePhotoInactivation)
adap031 = pardict.copy()

pardict = {'subject':'adap031','experimenter':'tai'}
pardict.update(frequencySet6to19)
pardict.update(psyCurvePhotoInactivation)
adap031_interval = pardict.copy()
