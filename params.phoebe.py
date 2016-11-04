'''
Defines parameters for different subjects
'''

test000 = {'targetDuration':0.2, 'targetIntensityMode':'fixed',
           'targetMaxIntensity':80,
           'highFreq':2100, 'midFreq':1400,'lowFreq':1000, 'trialsPerBlock':3,
           'punishSoundAmplitude':0.1} #, 'outcomeMode':'simulated'

frequencySet6to19 = {'lowFreq':6200, 'highFreq':19200}
### 'punishTimeEarly':0.5,'punishSoundAmplitude':0.05

shortDelayToTarget = {'delayToTargetMean':0.05, 'delayToTargetHalfRange':0.02}

increaseDelayGoMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0.1, 'delayToTargetHalfRange':0.05,
                       'automationMode':'increase_delay_go', 'targetDuration':0.1, 'delayToGoSignal':0}

basicDiscriminationMode = {'delayToTargetMean':0.2,'currentBlock':'mid_boundary',
                           'punishTimeEarly':0.5,'punishSoundAmplitude':0.05}


pardict = {'subject': 'gosi001', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
gosi001 = pardict.copy()

pardict = {'subject': 'gosi002', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
gosi002 = pardict.copy()

pardict = {'subject': 'gosi003', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
gosi003 = pardict.copy()

pardict = {'subject': 'gosi004', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
gosi004 = pardict.copy()

pardict = {'subject': 'gosi005', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi005 = pardict.copy()

pardict = {'subject': 'gosi006', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi006 = pardict.copy()

pardict = {'subject': 'gosi007', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi007 = pardict.copy()

pardict = {'subject': 'gosi008', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi008 = pardict.copy()

pardict = {'subject': 'gosi009', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi009 = pardict.copy()

pardict = {'subject': 'gosi010', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi010 = pardict.copy()

pardict = {'subject': 'gosi011', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi011 = pardict.copy()

pardict = {'subject': 'gosi012', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(increaseDelayGoMode)
gosi012 = pardict.copy()

pardict = {'subject': 'gosi013', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
gosi013 = pardict.copy()

pardict = {'subject': 'gosi014', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
pardict.update(shortDelayToTarget)
gosi014 = pardict.copy()

pardict = {'subject': 'gosi015', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(increaseDelayGoMode)
pardict.update(shortDelayToTarget)
gosi015 = pardict.copy()


