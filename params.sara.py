# Parameters for paradigms used by Sara

# === Amplitude Modulation (freely moving) ===
amDiscrimStage0 = {'experimenter':'sara', 'outcomeMode':'sides_direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'targetDuration': 0.1}
amDiscrimStage1 = {'experimenter':'sara', 'outcomeMode':'direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'targetDuration': 0.1}
amDiscrimStage2 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'automationMode':'increase_duration', 
                     'targetMaxIntensity':60,'targetIntensityMode':'fixed', 'targetDuration': 0.1 }
amDiscrimStage21 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'automationMode':'increase_duration', 
                     'targetMaxIntensity':60,'targetIntensityMode':'fixed', 'targetDuration': 0.25 }
amDiscrimStage3 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'targetDuration': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
amDiscrimStage4 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
                   'psycurveNfreq':6, 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60, 'punishTimeEarly': 0.2, 
                   'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
amDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'targetDuration': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}

freqDiscrimStage3 = {'experimenter':'sara','soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'targetDuration': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
freqDiscrimBiasCorr = {'experimenter':'sara','soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'targetDuration': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
freqDiscrimStage4 = {'experimenter':'sara', 'soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
                   'psycurveNfreq':6, 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60, 'punishTimeEarly': 0.2, 'targetDuration': 0.2, 
                    'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}

mixedTasks = {'experimenter':'sara', 'soundTypeMode': 'mixed_tones', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
              'psycurveNfreq':6, 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60, 'punishTimeEarly': 0.2, 'targetDuration': 0.2, 
              'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}

sole048 = {'subject':'sole048', **amDiscrimStage3}
sole049 = {'subject':'sole049', **amDiscrimStage4}
sole050 = {'subject':'sole050', **amDiscrimStage3}
sole053 = {'subject':'sole053', **amDiscrimStage4}
sole054 = {'subject':'sole054', **amDiscrimStage3}
sole056 = {'subject':'sole056', **amDiscrimStage4}
sole059 = {'subject':'sole059', **freqDiscrimStage3}
sole062 = {'subject':'sole062', **amDiscrimBiasCorr}
sole064 = {'subject':'sole064', **amDiscrimStage3}
sole065 = {'subject':'sole065', **amDiscrimStage3}
sole067 = {'subject':'sole067', **amDiscrimStage4}
sole068 = {'subject':'sole068', **amDiscrimStage3}
sole069 = {'subject':'sole069', **amDiscrimBiasCorr}
sole070 = {'subject':'sole070', **amDiscrimStage3}
sole071 = {'subject':'sole071', **amDiscrimStage3}
sole072 = {'subject':'sole072', **amDiscrimStage2}
sole073 = {'subject':'sole073', **amDiscrimStage2}
sole074 = {'subject':'sole074', **amDiscrimStage1}
sole075 = {'subject':'sole075', **amDiscrimStage2}
sole076 = {'subject':'sole076', **amDiscrimStage2}
sole077 = {'subject':'sole077', **amDiscrimStage2}
test000 = {'subject':'test000', **amDiscrimStage2}
