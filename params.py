'''
Define parameters for different subjects
'''

test000 = {'targetDuration':0.2, 'targetIntensityMode':'fixed',
           'targetMaxIntensity':80,
           'highFreq':2100, 'midFreq':1400,'lowFreq':1000, 'trialsPerBlock':3,
           'punishSoundAmplitude':0.1} #, 'outcomeMode':'simulated'

test001 = {'delayToTarget':0.333, 'value1':88, 'value2':99}
test002 = {'value1':77, 'value2':88, 'value3':99}


sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}
increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.05,'targetMaxIntensity':80,'lowFreq':4000,'highFreq':13000}

#onNextCorrectMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05,
#                   'currentBlock':'mid_boundary', 'targetDuration':0.1,'targetMaxIntensity':80,'lowFreq':4000,'highFreq':13000}
#onNextCorrectMode = {'currentBlock':'mid_boundary','lowFreq':3000,'highFreq':16000}
#onNextCorrectMode = {'currentBlock':'low_boundary','trialsPerBlock':1000}
#switchDailyMode = {'trialsPerBlock':2000,'punishTimeError':4}
#switchDailyMode = {'trialsPerBlock':2000,'punishTimeError':4,'currentBlock':'mid_boundary','lowFreq':5000,'midFreq':11000,'highFreq':24000}

psyCurveMidBound = {'trialsPerBlock':2000,'punishTimeError':4,'lowFreq':5000,'midFreq':11000,'highFreq':24000,
                    'currentBlock':'mid_boundary','psycurveMode':'uniform'}

shapingMode = {'lowFreq':5000,'midFreq':11000,'highFreq':24000, 'currentBlock':'mid_boundary','targetIntensityMode':'fixed'}


switchDailyMode = {'trialsPerBlock':2000,'punishTimeError':4,'lowFreq':5000,'midFreq':11000,'highFreq':24000, 
                   'delayToTargetMean':0.2, 'currentBlock':'high_boundary'}

switchBlocksMode = {'punishTimeError':4, 'delayToTargetMean':0.2}



test089 = sidesDirectMode.copy()
test089.update({'subject':'test089','experimenter':'santiago', 'lowFreq':5000,'midFreq':11000,'highFreq':24000})

test088 = sidesDirectMode.copy()
test088.update({'subject':'test088','experimenter':'santiago', 'lowFreq':5000,'midFreq':11000,'highFreq':24000})

test087 = sidesDirectMode.copy()
test087.update({'subject':'test087','experimenter':'santiago', 'lowFreq':5000,'midFreq':11000,'highFreq':24000})

test086 = sidesDirectMode.copy()
test086.update({'subject':'test086','experimenter':'santiago', 'lowFreq':5000,'midFreq':11000,'highFreq':24000})

test085 = sidesDirectMode.copy()
test085.update({'subject':'test085','experimenter':'santiago', 'lowFreq':5000,'midFreq':11000,'highFreq':24000})


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


test011 = switchBlocksMode.copy()
test011.update({'subject':'test011','experimenter':'santiago'})
test011.update({'currentBlock':'high_boundary','trialsPerBlock':200,'trainer':''})

test012 = switchBlocksMode.copy()
test012.update({'subject':'test012','experimenter':'santiago'})
test012.update({'trialsPerBlock':2000,'currentBlock':'mid_boundary','psycurveMode':'uniform'})

test013 = switchBlocksMode.copy()
test013.update({'subject':'test013','experimenter':'santiago'})
test013.update({'trialsPerBlock':2000,'currentBlock':'mid_boundary','psycurveMode':'uniform'})

test014 = switchBlocksMode.copy()
test014.update({'subject':'test014','experimenter':'santiago'})
test014.update({'trialsPerBlock':2000,'currentBlock':'mid_boundary','psycurveMode':'uniform'})

test015 = switchBlocksMode.copy()
test015.update({'subject':'test015','experimenter':'santiago'})
test015.update({'currentBlock':'low_boundary','trialsPerBlock':200,'trainer':''})

test016 = switchBlocksMode.copy()
test016.update({'subject':'test016','experimenter':'santiago'})
test016.update({'currentBlock':'low_boundary','trialsPerBlock':200,'trainer':''})

test017 = switchBlocksMode.copy()
test017.update({'subject':'test017','experimenter':'santiago'})
test017.update({'currentBlock':'low_boundary','trialsPerBlock':200,'trainer':''})

test018 = switchBlocksMode.copy()
test018.update({'subject':'test018','experimenter':'santiago'})
test018.update({'currentBlock':'low_boundary','trialsPerBlock':200,'trainer':''})

test019 = switchBlocksMode.copy()
#test019.update({'subject':'test019','experimenter':'santiago', 'currentBlock':'low_boundary', 'trialsPerBlock':1000})
test019.update({'subject':'test019','experimenter':'santiago'})

test020 = switchBlocksMode.copy()
test020.update({'subject':'test020','experimenter':'santiago'})
test020.update({'trialsPerBlock':2000,'currentBlock':'mid_boundary','psycurveMode':'uniform'})


test050 = switchDailyMode.copy()
test050.update({'subject':'test050','experimenter':'santiago'})

test051 = switchDailyMode.copy()
test051.update({'subject':'test051','experimenter':'santiago'})

test052 = switchDailyMode.copy()
test052.update({'subject':'test052','experimenter':'santiago'})

test053 = switchDailyMode.copy()
test053.update({'subject':'test053','experimenter':'santiago'})

test054 = switchDailyMode.copy()
test054.update({'subject':'test054','experimenter':'santiago'})

test055 = switchDailyMode.copy()
test055.update({'subject':'test055','experimenter':'santiago'})

test056 = switchDailyMode.copy()
test056.update({'subject':'test056','experimenter':'santiago'})

test057 = switchDailyMode.copy()
test057.update({'subject':'test057','experimenter':'santiago'})

test058 = switchDailyMode.copy()
test058.update({'subject':'test058','experimenter':'santiago'})

test059 = switchDailyMode.copy()
test059.update({'subject':'test059','experimenter':'santiago'})

