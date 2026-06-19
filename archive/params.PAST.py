'''
Parameters used for animals that do not exist anymore
'''

shapingMode = {'lowFreq':5000,'midFreq':11000,'highFreq':24000, 'currentBlock':'mid_boundary','targetIntensityMode':'fixed'}


# -- Angie's mice --
test071 = shapingMode.copy()
test071.update({'subject':'test071','experimenter':'santiago'})

test070 = shapingMode.copy()
test070.update({'subject':'test070','experimenter':'santiago'})

test069 = shapingMode.copy()
test069.update({'subject':'test069','experimenter':'santiago'})

test068 = shapingMode.copy()
test068.update({'subject':'test068','experimenter':'santiago'})

test067 = shapingMode.copy()
test067.update({'subject':'test067','experimenter':'santiago'})

test066 = shapingMode.copy()
test066.update({'subject':'test066','experimenter':'santiago'})

test065 = shapingMode.copy()
test065.update({'subject':'test065','experimenter':'santiago'})

test064 = shapingMode.copy()
test064.update({'subject':'test064','experimenter':'santiago'})


# -- Santiago's audStr lesions --
psyCurveMidBound = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                    'currentBlock':'mid_boundary','psycurveMode':'uniform'}

test012 = psyCurveMidBound.copy()
test012.update({'subject':'test012','experimenter':'santiago'})
test012.update({'trialsPerBlock':2000,'currentBlock':'mid_boundary','psycurveMode':'uniform'})

test020 = psyCurveMidBound.copy()
test020.update({'subject':'test020','experimenter':'santiago'})
test020.update({'trialsPerBlock':2000,'currentBlock':'mid_boundary','psycurveMode':'uniform'})
