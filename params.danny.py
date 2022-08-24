# Chords

lowestfirst3chord = {'experimenter':'danny', 'interTrialIntervalMean':10,
           'interTrialIntervalHalfRange':2, 'preDurationMean':7, 'preDurationHalfRange':0,
           'totalStimDuration':12, 'fadeIn':2, 'maxFreq':15000, 'minFreq':4000,
           'nFreqs':3, 'minFreqRatio':1.00, 'soundIntensity':70}
  #^previously: dbtest1
             
lowestfirst6chord = {'experimenter':'danny', 'interTrialIntervalMean':10,
           'interTrialIntervalHalfRange':2, 'preDurationMean':7, 'preDurationHalfRange':0,
           'totalStimDuration':12, 'fadeIn':2, 'maxFreq':15000, 'minFreq':4000,
           'nFreqs':6, 'minFreqRatio':1.00, 'soundIntensity':70}
  #^previously: dbtest2             

highestfirst6chord = {'experimenter':'danny', 'interTrialIntervalMean':10,
           'interTrialIntervalHalfRange':2, 'preDurationMean':7, 'preDurationHalfRange':0,
           'totalStimDuration':12, 'fadeIn':2, 'maxFreq':15000, 'minFreq':4000,
           'nFreqs':6, 'minFreqRatio':1.00, 'soundIntensity':70}
  #^previously: dbtest3            

random6chord = {'experimenter':'danny', 'maxFreq':15000, 'minFreq':4000, 'numTones':6,
           'minInt':70, 'maxInt':70, 'numInt':1, 'stimDur':5,'isiMean':10, 'isiHalfRange':1,
           'randomMode':'Random', 'stimType':'Chord'} 
  #^previously: dbtest4 
  
#Pure Tones

pureTone20sec = {'experimenter':'danny', 'maxFreq':6000, 'minFreq':6000, 'numTones':1,
           'minInt':70, 'maxInt':70, 'numInt':1, 'stimDur':20,'isiMean':20, 'isiHalfRange':0,
           'randomMode':'Random', 'stimType':'Sine', 'syncLight':'centerLED',
           'syncLightMode':'from_stim_offset', 'syncLightDuration':0.5,
           'delayToSyncLight':0}           

# Amplitude Modulated Sounds

AMrandom3rate = {'soundType':'AM_rate', 'soundSetMode':'random', 'minFreq':4, 'maxFreq':12,
           'nFreqs':3,'experimenter':'danny', 'interTrialIntervalMean':10,  'preDurationMean':7,
           'fadeIn':2, 'totalStimDuration':12, 'minFreqRatio':1.00, 'soundIntensity':85}
           
AMpreExtreme3rate = {'soundType':'AM_rate', 'soundSetMode':'pre_extreme', 'minFreq':4, 'maxFreq':12,
           'nFreqs':3,'experimenter':'danny', 'interTrialIntervalMean':10,  'preDurationMean':7,
           'fadeIn':2, 'totalStimDuration':12, 'minFreqRatio':1.00, 'soundIntensity':85}
           
           
AM20sec = {'experimenter':'danny', 'maxFreq':12, 'minFreq':12, 'numTones':1,
           'minInt':85, 'maxInt':85, 'numInt':1, 'stimDur':20,'isiMean':20, 'isiHalfRange':0,
           'randomMode':'Random', 'stimType':'AM', 'syncLight':'centerLED',
           'syncLightMode':'from_stim_offset', 'syncLightDuration':0.5,
           'delayToSyncLight':0} 

AM20secControl = {'experimenter':'danny', 'maxFreq':12, 'minFreq':12, 'numTones':1,
           'minInt':0, 'maxInt':0, 'numInt':1, 'stimDur':20,'isiMean':20, 'isiHalfRange':0,
           'randomMode':'Random', 'stimType':'AM', 'syncLight':'centerLED',
           'syncLightMode':'from_stim_offset', 'syncLightDuration':0.5,
           'delayToSyncLight':0} 
           
AM20secRandomIntensity = {'experimenter':'danny', 'maxFreq':12, 'minFreq':12, 'numTones':1,
           'minInt':20, 'maxInt':85, 'numInt':4, 'stimDur':20,'isiMean':20, 'isiHalfRange':0,
           'randomMode':'Random', 'stimType':'AM', 'syncLight':'centerLED',
           'syncLightMode':'from_stim_offset', 'syncLightDuration':0.5,
           'delayToSyncLight':0}           
           
