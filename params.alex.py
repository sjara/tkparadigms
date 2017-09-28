sidesDirectMode = {'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}

directMode = {'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                   'currentBlock':'mid_boundary'}

increaseDelayMode = {'outcomeMode':'on_next_correct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0,
                     'currentBlock':'mid_boundary', 'automationMode':'increase_delay', 'targetDuration':0.05,
                     'punishTimeEarly':0.5,'punishSoundAmplitude':0.05}

basicDiscriminationMode = {'delayToTargetMean':0.2,'currentBlock':'mid_boundary',
                           'punishTimeEarly':0,'punishSoundAmplitude':0.0}

psyCurveMidBound = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                    'currentBlock':'mid_boundary','psycurveMode':'uniform'}

frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}

pardict = {'subject': 'adap058', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
adap058 = pardict.copy()

pardict = {'subject': 'adap059', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap059 = pardict.copy()

pardict = {'subject': 'adap060', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap060 = pardict.copy()

pardict = {'subject': 'adap061', 'experimenter': 'alex', 'trainer': ''}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
#pardict.update({'antibiasMode':'repeat_mistake'})
adap061 = pardict.copy()


# ephys params
subject = 'dapa006'

tuningCurve = {'stimDur':0.1,
           'minInt':50,
           'maxInt':70,
	       'numInt':2,
	       'isiMean':0.8,
	       'isiHalfRange':0.1,
           'stimType' : 'Sine',
           'subject':subject,
           'experimenter' : 'alex'}

laserTuningCurve = {'stimDur:0.1',
                    'minInt':50,
                    'maxInt':70,
                    'numInt':2,
                    'isiMean':0.8,
                    'isiHalfRange':0.1,
                    'stimType':'SineLaser',
                    'subject':subject,
                    'experimenter':'alex'}

noisetest = {'stimDur':0.1,
             'isiMean':0.9,
             'isiHalfRange':0.01,
             'randomMode':'Ordered',
             'soundMode':'Noise',
             'minInt':70,
             'maxInt':70,
             'numInt':1,
             'experimenter' : 'alex',
             'subject':subject}
