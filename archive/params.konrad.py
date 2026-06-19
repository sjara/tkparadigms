subject = 'chad'

noiseburst = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'stimType' : 'Noise',
               'minInt':60,
               'maxInt':60,
               'numInt':1,
               'subject':subject,
               'experimenter' : 'konrad'}

rlf = {'stimDur':0.1,
       'isiMean':0.9,
       'isiHalfRange': 0.01,
       'stimType' : 'Noise',
       'minInt':30,
       'maxInt':70,
       'numInt':9,
       'subject':subject,
       'experimenter' : 'konrad'}

lasertrain = {'stimDur':0.01,
               'isiMean':1,
               'isiHalfRange': 0,
               'stimType' : 'LaserTrain',
               'subject':subject,
               'experimenter' : 'konrad'}


laserpulse = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0,
               'stimType' : 'Laser',
               'subject':subject,
               'experimenter' : 'konrad'}

tc = {'stimDur':0.1,
      'isiMean':0.8,
      'isiHalfRange': 0.1,
      'stimType' : 'Sine',
      'minFreq':2000,
      'maxFreq':40000,
      'numTones':16,
      'minInt':70,
      'maxInt':70,
      'numInt':1,
      'subject':subject,
      'experimenter' : 'konrad'}

am = {'subject':subject,
      'experimenter':'konrad',
      'minFreq':4,
      'maxFreq':128,
      'numTones':11,
      'minInt':60,
      'maxInt':60,
      'numInt':1,
      'stimType':'AM',
      'stimDur':0.5,
      'isiMean':1,
      'isiHalfRange':0.1}

oddball = {'subject':subject,
      'experimenter':'konrad',
      'standardFreq':0,
      'oddballFreq':0,
      'oddballProb':0.1,
      'soundIntensity':0,
      'soundDuration':0.1,
      'isiMean':0.2,
      'isiHalfRange':0,
      'stimDuration':0.1,
      'sequenceMode':'Oddball',
      'stimType':'Sine'}
