subject = 'pals002'
experimenter = 'isabella'

noiseburst = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'stimType' : 'Noise',
               'minInt':60,
               'maxInt':60,
               'numInt':1,
               'subject':subject,
               'experimenter' : experimenter}

tuningTest = {'stimDur':0.1,
               'minInt':60,
               'maxInt':60,
               'numInt':1,
               'isiMean':0.6,
               'isiHalfRange':0.1,
               'stimType' : 'Sine',
               'subject':subject,
               'experimenter' : experimenter}

am = {'subject':subject,
      'experimenter':experimenter,
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
      
chord = {'subject':subject,
      'experimenter':experimenter,
      'minFreq':6000,
      'maxFreq':13000,
      'numTones':8,
      'minInt':60,
      'maxInt':60,
      'numInt':1,
      'stimType':'Chord',
      'stimDur':0.2,
      'isiMean':2}
            

