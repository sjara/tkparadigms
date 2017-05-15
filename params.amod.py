#amod and mixed paradigms
amodSidesDirect = {'outcomeMode':'sides_direct', 'soundTypeMode':'amp_mod'}
amodDirect = {'outcomeMode':'direct', 'soundTypeMode':'amp_mod'}
amodNextCorrectAM = {'outcomeMode':'on_next_correct', 'soundTypeMode':'amp_mod'}
amodIfCorrectAM = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod'}
amodPsycurveAM = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod', 'psycurveMode':'uniform'}
amodIfCorrectTones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'tones'}
amodPsycurveTones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'tones', 'psycurveMode':'uniform'}
amodIfCorrectMixed = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones'}
amodPsycurveMixed = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones', 'psycurveMode':'uniform'}
amodPsycurveChords = {'outcomeMode':'only_if_correct', 'soundTypeMode':'chords', 
                  'psycurveMode':'uniform', 'psycurveNfreq':8, 'highSoundFreq':19200, 
                  'lowSoundFreq':6200}
amodLaserPsycurveChords = {'outcomeMode':'only_if_correct', 'soundTypeMode':'chords', 
                  'psycurveMode':'uniform', 'psycurveNfreq':6, 'laserMode':'random', 
                  'laserProbability':0.2, 'laserDuration':0.6, 'highSoundFreq':19200, 
                  'lowSoundFreq':6200}

#adaptive freq discrim paradigms
psyCurveMidBound = {'trialsPerBlock':2000,'punishTimeError':4,'delayToTargetMean':0.2,
                    'currentBlock':'mid_boundary','psycurveMode':'uniform'}
frequencySet6to19 = {'lowFreq':6200,'midFreq':11000,'highFreq':19200}

#laser params addition to psyCurveMidBound for use with photostim_intervals_freq_discrim.py
laserPsycurve = {'laserDuration':0.6, 'laserOnsetFromSoundOnset1':0, 'fractionTrialsEachLaserMode':0.2}

pardict = {'subject':'amod011','experimenter':'nick'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
# pardict.update(amodIfCorrectMixed)
amod011 = pardict.copy()

pardict = {'subject':'amod012','experimenter':'nick'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
pardict.update(laserPsycurve)
# pardict.update(amodIfCorrectMixed)
# pardict.update({'antibiasMode':'repeat_mistake'})
amod012 = pardict.copy()

pardict = {'subject':'amod013','experimenter':'nick'}
pardict.update(psyCurveMidBound)
pardict.update(frequencySet6to19)
pardict.update(laserPsycurve)
pardict.update({'delayToTargetMean':0.1})
# pardict.update(amodIfCorrectMixed)
amod013 = pardict.copy()

pardict = {'subject':'amod014','experimenter':'nick'}
pardict.update(amodPsycurveMixed)
pardict.update({'laserMode':'random', 'laserProbability':0.2, 'laserDuration':0.6})
# pardict.update(amodIfCorrectMixed)
# pardict.update({'antibiasMode':'repeat_mistake'})
amod014 = pardict.copy()

