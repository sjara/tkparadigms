subject = 'pinp024'

noiseburst = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'stimType' : 'Noise',
               'minInt':60,
               'maxInt':60,
               'numInt':1,
               'subject':subject,
               'experimenter' : 'nick'}

rlf = {'stimDur':0.1,
       'isiMean':0.9,
       'isiHalfRange': 0.01,
       'stimType' : 'Noise',
       'minInt':30,
       'maxInt':70,
       'numInt':9,
       'subject':subject,
       'experimenter' : 'nick'}

lasertrain = {'stimDur':0.01,
               'isiMean':1,
               'isiHalfRange': 0,
               'stimType' : 'LaserTrain',
               'subject':subject,
               'experimenter' : 'nick'}


laserpulse = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0,
               'stimType' : 'Laser',
               'subject':subject,
               'experimenter' : 'nick'}

tc = {'stimDur':0.1,
      'isiMean':0.8,
      'isiHalfRange': 0.1,
      'stimType' : 'Sine',
      'minFreq':2000,
      'maxFreq':40000,
      'minInt':15,
      'maxInt':70,
      'numInt':12,
      'subject':subject,
      'experimenter' : 'nick'}

am = {'subject':subject,
      'experimenter':'nick',
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
