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
                     'targetIntensityMode':'fixed',}
amDiscrimStage4 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
                   'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60}
amDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed',}
freqDiscrimStage3 = {{'experimenter':'sara','soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed',}
freqDiscrimBiasCorr = {'experimenter':'sara','soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed',}
freqDiscrimStage4 = {'experimenter':'sara', 'soundTypeMode': 'tones', 'outcomeMode':'only_if_correct', 'psycurveMode':'uniform', 
                   'psycurveNsteps':'6', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60}

sole048 = {'subject':'sole048', **freqDiscrimStage3}
sole049 = {'subject':'sole049', **amDiscrimStage4}
sole050 = {'subject':'sole050', **freqDiscrimStage3}
sole051 = {'subject':'sole051', **amDiscrimStage4}
sole052 = {'subject':'sole052', **amDiscrimStage3}
sole053 = {'subject':'sole053', **amDiscrimStage4}
sole054 = {'subject':'sole054', **amDiscrimStage4}
sole055 = {'subject':'sole055', **amDiscrimStage4}
sole056 = {'subject':'sole056', **amDiscrimStage3}
sole057 = {'subject':'sole057', **amDiscrimStage4}
sole058 = {'subject':'sole058', **amDiscrimStage4}
sole059 = {'subject':'sole059', **amDiscrimBiasCorr}
sole060 = {'subject':'sole060', **amDiscrimStage3}
sole061 = {'subject':'sole061', **amDiscrimStage4}
sole062 = {'subject':'sole062', **amDiscrimStage2}
sole064 = {'subject':'sole064', **amDiscrimStage2}
sole065 = {'subject':'sole065', **amDiscrimStage2}
sole067 = {'subject':'sole067', **amDiscrimStage2}
