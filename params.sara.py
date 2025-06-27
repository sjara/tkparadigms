# Parameters for paradigms used by Sara

# === Amplitude Modulation (freely moving) ===
amDiscrimStage0 = {'experimenter':'sara', 'outcomeMode':'sides_direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed',}
amDiscrimStage1 = {'experimenter':'sara', 'outcomeMode':'direct', 'delayToTargetMean':0,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed',}
amDiscrimStage2 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
                     'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'automationMode':'increase_delay', 
                     'targetMaxIntensity':60,'targetIntensityMode':'fixed',}
amDiscrimStage3 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
amDiscrimStage4 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
                   'psycurveNfreq':6, 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60, 'punishTimeEarly': 0.2, 
                   'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
amDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}

freqDiscrimStage3 = {'experimenter':'sara','soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
freqDiscrimBiasCorr = {'experimenter':'sara','soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}
freqDiscrimStage4 = {'experimenter':'sara', 'soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
                   'psycurveNfreq':60, 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60, 'punishTimeEarly': 0.2,
                    'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}

mixedTasks = {'experimenter':'sara', 'soundTypeMode': 'mixed_tones', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
              'psycurveNfreq':6, 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60, 'punishTimeEarly': 0.2, 
              'punishSoundIntensity':60, 'allowEarlyWithdrawal': 'off'}

sole048 = {'subject':'sole048', **amDiscrimStage4}
sole049 = {'subject':'sole049', **amDiscrimStage4}
sole050 = {'subject':'sole050', **amDiscrimBiasCorr}
sole051 = {'subject':'sole051', **mixedTasks}
sole052 = {'subject':'sole052', **amDiscrimStage4}
sole053 = {'subject':'sole053', **amDiscrimStage4}
sole054 = {'subject':'sole054', **amDiscrimStage4}
sole055 = {'subject':'sole055', **amDiscrimStage3}
sole056 = {'subject':'sole056', **freqDiscrimStage3}
sole057 = {'subject':'sole057', **amDiscrimBiasCorr}
sole058 = {'subject':'sole058', **amDiscrimBiasCorr}
sole059 = {'subject':'sole059', **freqDiscrimStage3}
sole060 = {'subject':'sole060', **amDiscrimStage3}
sole061 = {'subject':'sole061', **amDiscrimStage4}
sole062 = {'subject':'sole062', **freqDiscrimStage4}
sole064 = {'subject':'sole064', **amDiscrimStage4}
sole065 = {'subject':'sole065', **amDiscrimStage4}
sole067 = {'subject':'sole067', **amDiscrimBiasCorr}
sole068 = {'subject':'sole068', **amDiscrimStage3}
sole069 = {'subject':'sole069', **amDiscrimStage3}
sole070 = {'subject':'sole070', **amDiscrimStage3}
