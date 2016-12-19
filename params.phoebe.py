'''
Defines parameters for different subjects
'''

test000 = {'targetDuration':0.2, 'targetIntensityMode':'fixed',
           'targetMaxIntensity':80,
           'highFreq':2100, 'midFreq':1400,'lowFreq':1000, 'trialsPerBlock':3,
           'punishSoundAmplitude':0.1} #, 'outcomeMode':'simulated'

frequencySet6to19 = {'lowFreq':6200, 'highFreq':19200}
### 'punishTimeEarly':0.5,'punishSoundAmplitude':0.05

noFailMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.06, 'delayToGoSignal':0, 'punishSoundAmplitude':0}

shortDelayToTarget = {'delayToTargetMean':0.05, 'delayToTargetHalfRange':0.02}

learnDiscrimMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.02, 'delayToTargetHalfRange':0, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.075, 'delayToGoSignal':0, 'punishSoundAmplitude':0}

increaseDelayGoMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.02, 'delayToTargetHalfRange':0.0, 'automationMode':'increase_delay_go',
                        'targetDuration':0.1, 'delayToGoSignal':0.0, 'punishSoundAmplitude':0}

basicDiscriminationModeShortDelay = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.05, 'delayToTargetHalfRange':0.02, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.1, 'delayToGoSignal':0.1, 'punishSoundAmplitude':0}

increaseDelayGoMode2 = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.02, 'delayToTargetHalfRange':0.0, 'automationMode':'increase_delay_go',
                        'targetDuration':0.1, 'delayToGoSignal':0.05, 'punishSoundAmplitude':0}

basicDiscriminationModeShortDelaytoTarget = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.05, 'delayToTargetHalfRange':0.02, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.1, 'delayToGoSignal':0.2, 'punishSoundAmplitude':0}

basicDiscriminationMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.1, 'delayToGoSignal':0.2, 'punishSoundAmplitude':0}

psycurveDebiasMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.02, 'delayToTargetHalfRange':0, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.1, 'delayToGoSignal':0.05, 'punishSoundAmplitude':0}

psyCurveModeShortDelay = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.05, 'delayToTargetHalfRange':0.02, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.1, 'delayToGoSignal':0.08, 'psycurveMode':'uniform', 'punishSoundAmplitude':0}

psyCurveMode = {'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'automationMode':'off', 'currentBlock':'mid_boundary', 'targetDuration':0.1, 'delayToGoSignal':0.4, 'psycurveMode':'uniform', 'punishSoundAmplitude':0}

                           ###punishTimeEarly':0.5,'punishSoundAmplitude':0.05


pardict = {'subject': 'gosi001', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(basicDiscriminationModeShortDelay)
gosi001 = pardict.copy()

pardict = {'subject': 'gosi002', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(basicDiscriminationModeShortDelay)
gosi002 = pardict.copy()

pardict = {'subject': 'gosi003', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(basicDiscriminationModeShortDelaytoTarget)
gosi003 = pardict.copy()

pardict = {'subject': 'gosi004', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(basicDiscriminationModeShortDelay)
gosi004 = pardict.copy()

pardict = {'subject': 'gosi005', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(noFailMode)
gosi005 = pardict.copy()

pardict = {'subject': 'gosi006', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(basicDiscriminationModeShortDelay)
gosi006 = pardict.copy()

pardict = {'subject': 'gosi007', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(basicDiscriminationModeShortDelay)
gosi007 = pardict.copy()

pardict = {'subject': 'gosi008', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(basicDiscriminationModeShortDelaytoTarget)
gosi008 = pardict.copy()

pardict = {'subject': 'gosi009', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(basicDiscriminationModeShortDelaytoTarget)
gosi009 = pardict.copy()

pardict = {'subject': 'gosi010', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(psyCurveMode)
gosi010 = pardict.copy()

pardict = {'subject': 'gosi011', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(learnDiscrimMode)
gosi011 = pardict.copy()

pardict = {'subject': 'gosi012', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'off-on'})
pardict.update(basicDiscriminationModeShortDelay)
gosi012 = pardict.copy()

pardict = {'subject': 'gosi013', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(basicDiscriminationModeShortDelaytoTarget)
gosi013 = pardict.copy()

pardict = {'subject': 'gosi014', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(basicDiscriminationModeShortDelay)
gosi014 = pardict.copy()

pardict = {'subject': 'gosi015', 'experimenter': 'phoebe', 'trainer': 'pp'}
pardict.update(frequencySet6to19)
pardict.update({'goSignalMode':'on-off'})
pardict.update(noFailMode)
gosi015 = pardict.copy()


