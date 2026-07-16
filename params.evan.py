"""
This file defines the parameters for taskontrol paradigms.
"""

lowtoneTrains70 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':3000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}
              
lowtoneTrains80 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':3000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':80, 'maxInt':80}

midtoneTrains70 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':15500, 'maxFreq':15500, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}

midtoneTrains80 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':15500, 'maxFreq':15500, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':80, 'maxInt':80}

hightoneTrains70 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':28000, 'maxFreq':28000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}
              
hightoneTrains80 = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':28000, 'maxFreq':28000, 'numTones':1, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':80, 'maxInt':80}
              
intensitytoneTrains = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':28000, 'numTones':3, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':80, 'numInt':2}
              
toneTrains = {'subject':'imag02X', 'experimenter':'Willgaston', 
              'minFreq':3000, 'maxFreq':32000, 'numTones':3, 
              'stimType':'ToneTrain', 'stimDur':0.5,
              'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70}

widefieldMapping = {'subject':'imag03X', 'experimenter':'Evan', 
              'sessionID':'12121212', 'nMaxTrials':285, 
              'freq1':3000,'intensity1':75, 'freq2':15500,
              'intensity2':70, 'freq3':28000,'intensity3':80,
              'stimDuration':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 
              'stimType':'ToneTrain'}
              
              
              
tuningFreqTrain = {'subject':'imag022','experimenter':'evan', 'minFreq':2000, 'maxFreq':40000,
                   'numTones':16, 'stimType':'ToneTrain', 'stimDur':0.5, 'isiMean':1.2,
                   'isiHalfRange':0.2, 'minInt':60, 'maxInt':60, 'numInt':1}

tuningAM = {'subject':'imag022','experimenter':'evan', 'minFreq':4, 'maxFreq':128, 'numTones':11,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2, 'minInt':60,
            'maxInt':60}

repeatAM = {'subject':'imag022','experimenter':'evan', 'minFreq':8, 'maxFreq':8, 'numTones':1,
            'stimType':'AM', 'stimDur':0.5, 'isiMean':2.0, 'isiHalfRange':0.0, 'minInt':60,
            'maxInt':60}

tuningFreq = {'subject':'imag022','experimenter':'evan', 'minFreq':2000, 'maxFreq':40000,
              'numTones':16, 'stimType':'Sine', 'stimDur':0.5, 'isiMean':1.2, 'isiHalfRange':0.2,
              'minInt':70, 'maxInt':70, 'numInt':1}

natSounds = {'subject':'imag03X','experimenter':'evan', 'outcomeMode':'passive_exposure',
                         'delayToTargetMean':3.5, 'delayToTargetHalfRange':0.5,
                         'targetMaxIntensity':70,'soundLocation':'left'}


#toneTrains80LHH = {'subject':'imag02X', 'experimenter':'Willgaston', 
#              'minFreq':3000, 'maxFreq':32000, 'numTones':3, 
#              'stimType':'ToneTrain', 'stimDur':0.5,
#              'isiMean':1.2, 'isiHalfRange':0.2,
#              'minInt':80, 'maxInt':80}

#AMsounds = {'subject':'test000', 'experimenter':'Lizeth', 
#              'minFreq':8, 'maxFreq':16, 'numTones':2, 
#              'stimType':'AM', 'stimDur':1,
#              'isiMean':1.5, 'isiHalfRange':0.2,
#              'minInt':65, 'maxInt':65}

