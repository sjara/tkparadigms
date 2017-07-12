subject = 'band030'

noiseburst = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'stimType' : 'Noise',
               'minInt':60,
               'maxInt':60,
               'numInt':1,
               'subject':subject,
               'experimenter' : 'anna'}

lasernoiseburst = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'stimType' : 'laser_sound',
               'minAmp':60,
               'maxAmp':60,
               'numAmps':1,
               'laserFrontOverhang':0.1,
               'laserBackOverhang':0.1,
               'subject':subject,
               'experimenter' : 'anna'}

noiseAmps = {'stimDur':0.5,
           'isiMean':1.0,
           'isiHalfRange':0.1,
           'minFreq':32,
           'maxFreq':32,
           'numTones':1,
           'minInt':30,
           'maxInt':70,
           'numInt':5,
           'stimType' : 'AM',
           'subject':subject,
           'experimenter' : 'anna'}

tuningCurve = {'stimDur':0.1,
           'isiMean':0.8,
           'isiHalfRange':0.1,
           'minInt':40,
           'maxInt':60,
	       'numInt':2,
           'stimType' : 'Sine',
           'subject':subject,
           'experimenter' : 'anna'}

AM = 	  {'stimDur':0.5,
           'isiMean':1.0,
           'isiHalfRange':0.1,
           'minFreq':4,
           'maxFreq':64,
           'numTones':5,
           'minInt':60,
           'maxInt':60,
           'numInt':1,
           'stimType' : 'AM',
           'subject':subject,
           'experimenter' : 'anna'}


bandwidth = {'experimenter':'anna',
             'subject':subject,
             'minAmp':50,
             'maxAmp':70,
             'isiMean':1.5,
             'isiHalfRange':0.1,
             'minBand':0.25,
             'maxBand':4.0,
             'numBands':5}

laserBandwidth = {'experimenter':'anna',
             'subject':subject,
             'minAmp':70,
             'maxAmp':70,
             'numAmps':1,
             'isiMean':1.7,
             'isiHalfRange':0.1,
             'minBand':0.25,
             'maxBand':4.0,
             'numBands':5,
             'laserFrontOverhang':0.1,
             'laserBackOverhang':0.1,
             'stimType':'laser_band_AM'}

laserPulse = {'experimenter':'anna',
             'subject':subject,
             'stimDur':0.1,
             'isiMean':0.9,
             'isiHalfRange': 0,
             'stimType' : 'Laser'}

laserTrain = {'experimenter':'anna',
             'subject':subject,
             'stimDur':0.01,
             'isiMean':1,
             'isiHalfRange': 0,
             'noiseAmp':0.05,
             'stimType' : 'LaserTrain'}
