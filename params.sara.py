# Parameters for paradigms used by Sara

# === Amplitude Modulation (freely moving) ===
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
             

sole048 = {'subject':'sole048', **freqDiscrimBiasCorr}
sole049 = {'subject':'sole049', **amDiscrimStage4}
sole050 = {'subject':'sole050', **freqDiscrimStage3}
sole053 = {'subject':'sole053', **amDiscrimStage4}
sole054 = {'subject':'sole054', **amDiscrimStage3}
sole056 = {'subject':'sole056', **amDiscrimStage4}
sole059 = {'subject':'sole059', **freqDiscrimStage3}
sole062 = {'subject':'sole062', **amDiscrimBiasCorr}
sole064 = {'subject':'sole064', **amDiscrimStage3}
sole065 = {'subject':'sole065', **amDiscrimStage3}
sole067 = {'subject':'sole067', **amDiscrimStage4}
sole068 = {'subject':'sole068', **amDiscrimBiasCorr}
sole069 = {'subject':'sole069', **amDiscrimStage3}
sole070 = {'subject':'sole070', **amDiscrimStage3}
sole071 = {'subject':'sole071', **amDiscrimBiasCorr}
sole072 = {'subject':'sole072', **amDiscrimBiasCorr0}
sole073 = {'subject':'sole073', **amDiscrimStage03}
sole074 = {'subject':'sole074', **amDiscrimStage03}
sole075 = {'subject':'sole075', **amDiscrimBiasCorr0}
sole076 = {'subject':'sole076', **amDiscrimBiasCorr0}
sole077 = {'subject':'sole077', **amDiscrimStage03}
test000 = {'subject':'test000', **amDiscrimStage2}
