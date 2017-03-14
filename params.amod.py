amodSidesDirect = {'outcomeMode':'sides_direct', 'soundTypeMode':'amp_mod'}
amodDirect = {'outcomeMode':'direct', 'soundTypeMode':'amp_mod'}
amodNextCorrectAM = {'outcomeMode':'on_next_correct', 'soundTypeMode':'amp_mod'}
amodIfCorrectAM = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod'}
amodPsycurveAM = {'outcomeMode':'only_if_correct', 'soundTypeMode':'amp_mod', 'psycurveMode':'uniform'}
amodIfCorrectTones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'tones'}
amodPsycurveTones = {'outcomeMode':'only_if_correct', 'soundTypeMode':'tones', 'psycurveMode':'uniform'}
amodIfCorrectMixed = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones'}
amodPsycurveMixed = {'outcomeMode':'only_if_correct', 'soundTypeMode':'mixed_tones', 'psycurveMode':'uniform'}


pardict = {'subject':'amod011','experimenter':'nick'}
# pardict.update(amodPsycurveAM)
pardict.update(amodIfCorrectTones)
pardict.update({'punishTimeError':4})
amod011 = pardict.copy()

pardict = {'subject':'amod012','experimenter':'nick'}
# pardict.update(amodPsycurveMixed)
pardict.update(amodIfCorrectMixed)
# pardict.update({'antibiasMode':'repeat_mistake'})
amod012 = pardict.copy()

pardict = {'subject':'amod013','experimenter':'nick'}
# pardict.update(amodPsycurveMixed)
pardict.update(amodIfCorrectMixed)
# pardict.update({'antibiasMode':'repeat_mistake'})
amod013 = pardict.copy()

pardict = {'subject':'amod014','experimenter':'nick'}
# pardict.update(amodPsycurveMixed)
pardict.update(amodIfCorrectMixed)
# pardict.update({'antibiasMode':'repeat_mistake'})
amod014 = pardict.copy()

