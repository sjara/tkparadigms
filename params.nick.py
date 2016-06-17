hm4d002 = {'targetDuration':0.2,
           'isiMin':1.9,
           'isiMax':1.9} #, 'outcomeMode':'simulated'

noisetest = {'stimDur':0.1, 
             'isiMin':0.5,
             'isiMax':1,
             'randomMode':'Ordered',
             'soundMode':'Noise',
             'minInt':70,
             'maxInt':70,
             'numInt':1,
             'experimenter' : 'santiago',
             'subject':'pinp013'}

test060 = {'stimDur':0.1,
           'isiMax': 2,
           'soundMode' : 'Chord',
           'subject':'pinp013',
           'experimenter' : 'santiago'}

test077noise = {'stimDur':0.01,
           'isiMin':0.5,
           'isiMax': 1,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test077freq = {'stimDur':0.5,
           'isiMin':1,
           'isiMax':2,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Chord',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test075noise = {'stimDur':0.01,
           'isiMin':0.5,
           'isiMax': 1,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test075freq = {'stimDur':0.5,
           'isiMin':1,
           'isiMax':2,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Chord',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test080noise = {'stimDur':0.05,
           'isiMin':0.5,
           'isiMax': 1,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test080freq = {'stimDur':0.5,
           'isiMin':1,
           'isiMax':2,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Chord',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test082noise = {'stimDur':0.05,
           'isiMin':0.5,
           'isiMax': 1,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test082freq = {'stimDur':0.5,
           'isiMin':1,
           'isiMax':2,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Chord',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test019noise = {'stimDur':0.05,
           'isiMin':0.5,
           'isiMax': 1,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'billy'}

test019freq = {'stimDur':0.2,
           'isiMin':0.5,
           'isiMax':1,
           'minInt':60,
           'maxInt':60,
           'soundMode' : 'Chord',
           'subject':'pinp013',
           'experimenter' : 'billy'}

ratClicks = {'stimDur':0.01,
           'isiMin':0.5,
           'isiMax': 1,
           'minInt':60,
           'maxInt':60,
           'noiseAmp':2.0,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'santiago'}


ratClicksFixed = {'stimDur':0.01,
           'isiMin':1.9,
           'isiMax': 1.9,
           'minInt':60,
           'maxInt':60,
           'noiseAmp':2.0,
           'soundMode' : 'Noise',
           'subject':'pinp013',
           'experimenter' : 'santiago'}


lasertrain = {'stimDur':0.01,
               'isiMean':1,
               'isiHalfRange': 0,
               'noiseAmp':0.05,
               'stimType' : 'LaserTrain',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'pinp013',
               'experimenter' : 'nick'}

noisebursts = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0.01,
               'noiseAmp':0.35,
               'stimType' : 'Noise',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'pinp013',
               'experimenter' : 'nick'}

laserpulse = {'stimDur':0.1,
               'isiMean':0.9,
               'isiHalfRange': 0,
               'noiseAmp':0.05,
               'stimType' : 'Laser',
               'minFreq':2000,
               'maxFreq':30000,
               'minInt':40,
               'maxInt':70,
               'numInt':4,
               'subject':'pinp013',
               'experimenter' : 'nick'}


tuningCurve = {'stimDur':0.1,
               'isiMean':0.8,
               'isiHalfRange': 0.1,
               'noiseAmp':0.05,
               'stimType' : 'Sine',
               'minFreq':2000,
               'maxFreq':40000,
               'minInt':30,
               'maxInt':60,
               'numInt':4,
               'subject':'pinp013',
               'experimenter' : 'nick'}

tuningAM = {'subject':'pinp013', 'experimenter':'nick', 
            'minFreq':4, 'maxFreq':128, 'numTones':11, 
            'stimType':'AM', 'stimDur':0.5,
            'noiseAmp':0.5, #The new noise amp is 0.5 to get 20mV RMS - 2015-12-20 Nick
            'isiMin':1, 'isiMax':2}