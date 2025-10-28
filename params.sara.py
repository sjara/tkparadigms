# Parameters for paradigms used by Sara

# === Amplitude Modulation and frequency discrimination (freely moving) ===
amDiscrimStage0 = {'experimenter':'sara', 'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,'targetIntensityMode':'fixed',
                   'targetDuration': 0.1}

amDiscrimStage1 = {'experimenter':'sara', 'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.1}

amDiscrimStage2 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.1, 'automationMode':'increase_duration' }

amDiscrimStage21 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                    'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                    'targetDuration': 0.25, 'automationMode':'increase_duration'}
                     
amDiscrimStage3 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.2}

amDiscrimStage03 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.3}

amDiscrimStage4 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.2, 'psycurveMode':'uniform', 'psycurveNfreq':6}

amDiscrimStage41 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.2, 'psycurveMode':'uniform', 'psycurveNfreq':6,  'visibleLightMode':'center'}


amDiscrimStage04 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.3, 'psycurveMode':'uniform', 'psycurveNfreq':6}
                   
amDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                     'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                     'targetDuration': 0.2, 'antibiasMode':'repeat_mistake'}

amDiscrimBiasCorr0 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                     'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                     'targetDuration': 0.3, 'antibiasMode':'repeat_mistake'}
                    
freqDiscrimStage3 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0,
                     'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                     'targetDuration': 0.2, 'soundTypeMode': 'tones'}
                                           
freqDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0,
                       'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                       'targetDuration': 0.2, 'antibiasMode':'repeat_mistake', 'soundTypeMode': 'tones'}
                                           
freqDiscrimStage4 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0,
                     'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed', 
                     'targetDuration': 0.2, 'psycurveMode':'uniform', 'psycurveNfreq':6, 'soundTypeMode': 'tones'}                    

mixedTasks = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0,
              'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
              'targetDuration': 0.2, 'psycurveMode':'uniform', 'psycurveNfreq':6, 'soundTypeMode': 'mixed_tones'}

lasorOnAm = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.2, 'psycurveMode':'uniform', 'psycurveNfreq':6, 'laserMode': 'random', 'laserProbability': 0.25, 'laserDuration': 0.3,
                   'visibleLightMode':'center' }
             

sole049 = {'subject':'sole049', **amDiscrimStage4}
sole059 = {'subject':'sole059', **amDiscrimBiasCorr}
sole064 = {'subject':'sole064', **amDiscrimBiasCorr}
sole065 = {'subject':'sole065', **amDiscrimStage3}
sole067 = {'subject':'sole067', **amDiscrimStage3}
sole068 = {'subject':'sole068', **amDiscrimStage41}
sole069 = {'subject':'sole069', **amDiscrimStage3}
sole070 = {'subject':'sole070', **amDiscrimBiasCorr}
sole071 = {'subject':'sole071', **amDiscrimBiasCorr}
sole072 = {'subject':'sole072', **amDiscrimStage03}
sole073 = {'subject':'sole073', **amDiscrimBiasCorr0}
sole074 = {'subject':'sole074', **amDiscrimBiasCorr0}
sole075 = {'subject':'sole075', **amDiscrimStage03}
sole076 = {'subject':'sole076', **amDiscrimStage03}
sole077 = {'subject':'sole077', **amDiscrimStage03}
sole078 = {'subject':'sole078', **amDiscrimBiasCorr0}
sole079 = {'subject':'sole079', **amDiscrimStage03}
sole080 = {'subject':'sole080', **amDiscrimStage03}
test000 = {'subject':'test000', **lasorOnAm}
