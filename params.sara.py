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
                   'psycurveNsteps':'8', 'delayToTargetMean':0.2, 'delayToTargetHalfRange':0.05, 'targetIntensityMode':'fixed', 'targetMaxIntensity':60}
amDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'antibiasMode':'repeat_mistake','delayToTargetMean':0.2,
                     'delayToTargetHalfRange':0.05, 'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,
                     'targetIntensityMode':'fixed',}

sole048 = {'subject':'sole048', **amDiscrimStage3}
sole049 = {'subject':'sole049', **amDiscrimStage3}
sole050 = {'subject':'sole050', **amDiscrimBiasCorr}
sole051 = {'subject':'sole051', **amDiscrimStage3}
sole052 = {'subject':'sole052', **amDiscrimStage3}
sole053 = {'subject':'sole053', **amDiscrimStage3}
sole054 = {'subject':'sole054', **amDiscrimBiasCorr}
sole055 = {'subject':'sole055', **amDiscrimStage3}
sole056 = {'subject':'sole056', **amDiscrimBiasCorr}
sole057 = {'subject':'sole057', **amDiscrimStage0}
sole058 = {'subject':'sole058', **amDiscrimStage0}
sole059 = {'subject':'sole059', **amDiscrimStage0}
sole060 = {'subject':'sole060', **amDiscrimStage0}
sole061 = {'subject':'sole061', **amDiscrimStage0}
