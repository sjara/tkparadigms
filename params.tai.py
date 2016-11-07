'''
Parameters for photoinactivation during freq discrimination task (photostim_freq_discrim.py)
'''

frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}

psyCurvePhotoInactivation = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                             'currentBlock':'mid_boundary','psycurveMode':'uniform',
                             'laserFrontOverhang':0.05, 'laserBackOverhang':0.1,
                             'percentLaserTrialLeft':0.3, 'percentLaserTrialRight':0, }

#Params for paradigm 'photostim_interval_freq_discrim.py' that Santiago wrote for presenting laser at three different times
psyCurvePhotoInactivation_interval = {'delayToTargetHalfRange':0.05,'punishTimeError':4,
					'psycurveMode':'uniform','laserDuration':0.1,
					'laserOnsetFromSoundOnset1':-0.1,'laserOnsetFromSoundOnset2':0,
					'laserOnsetFromSoundOnset3':0.1,'nOnsetsToUse':'3',
					'fractionTrialsEachLaserMode':0.25}

pardict = {'subject':'adap038','experimenter':'tai'}
pardict.update(frequencySet6to19)
pardict.update(psyCurvePhotoInactivation)
adap038 = pardict.copy()

#params for adap031 in paradigm 'photostim_freq_discrim.py'
pardict = {'subject':'adap031','experimenter':'tai'}
pardict.update(frequencySet6to19)
pardict.update(psyCurvePhotoInactivation)
adap031 = pardict.copy()

#params for adap031 in paradigm 'photostim_interval_freq_discrim.py'
pardict = {'subject':'adap031','experimenter':'tai'}
pardict.update(frequencySet6to19)
pardict.update(psyCurvePhotoInactivation_interval)
adap031_interval = pardict.copy()
