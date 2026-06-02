# Parameters for paradigms used by Sara

# === Amplitude Modulation and frequency discrimination (freely moving) ===
amDiscrimStage0 = {'experimenter':'sara', 'outcomeMode':'sides_direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60,'targetIntensityMode':'fixed',
                   'targetDuration': 0.5, 'visibleLightMode':'center'}

amDiscrimStage1 = {'experimenter':'sara', 'outcomeMode':'direct', 'delayToTargetMean':0, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.5, 'visibleLightMode':'center'}

amDiscrimStage2 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'on', 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.5, 'visibleLightMode':'center'}

amDiscrimStage20 = {'experimenter':'sara', 'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.1, 'automationMode':'increase_duration', 'lightMode': 'on', 'lightOffset': 'side_poke'}

amDiscrimStage21 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                    'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                    'targetDuration': 0.25, 'automationMode':'increase_duration', 'lightMode': 'on', 'lightOffset': 'side_poke'}
                     
amDiscrimStage3 = {'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5,
                   'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 'automationMode': 'increase_delay'}


amDiscrimStage03 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.3}

amDiscrimStage4 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.5, 'psycurveMode':'uniform', 'psycurveNfreq':6}

amDiscrimStage41 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.2, 'psycurveMode':'uniform', 'psycurveNfreq':6,  'visibleLightMode':'center'}


amDiscrimStage04 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.3, 'psycurveMode':'uniform', 'psycurveNfreq':6}
                   
amDiscrimBiasCorr = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 'allowEarlyWithdrawal':'on', 'punishTimeError':0,
                             'punishTimeEarly':0.2, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed', 'targetDuration':0.3, 'antibiasMode':'repeat_mistake'}

amDiscrimBiasCorr0 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                     'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                     'targetDuration': 0.3, 'antibiasMode':'repeat_mistake'}
                    
freqDiscrimStage3 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.1, 'delayToTargetHalfRange':0,
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

amDiscrimStage03 = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.3}

amDiscrimStage3LaserOn = {'experimenter':'sara', 'outcomeMode':'only_if_correct', 'delayToTargetMean':0.01, 'delayToTargetHalfRange':0, 
                   'allowEarlyWithdrawal':'off', 'punishTimeEarly': 0.2, 'punishSoundIntensity':60, 'targetMaxIntensity':60, 'targetIntensityMode':'fixed',
                   'targetDuration': 0.3, 'visibleLightMode':'center'}
changedStage3 = {'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.01, 'delayToTargetHalfRange': 0, 'targetDuration': 0.5,
                 'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                 'lowAMrate': 4, 'highAMrate': 128, 'visibleLightMode':'all'}
amDiscrimStage22 = {'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'on', 'lightOffset': 'side_poke', 'automationMode': 'increase_delay'}
amDiscrimBiasCorr22 = {'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.1, 'delayToTargetHalfRange': 0, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'on', 'lightOffset': 'side_poke', 'automationMode': 'increase_delay'}
amDiscrimStage3LedDelay = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay'}

amDiscrimStage3LedDelayStop1 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.3}
amDiscrimStage3LedDelayStop2 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.32}
amDiscrimStage3LedDelayStop3 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.34}
amDiscrimStage3LedDelayStop4 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.36}
amDiscrimStage3LedDelayStop5 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.38}
amDiscrimStage3LedDelayStop6 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.4}
amDiscrimStage3LedDelayStop7 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.42}
amDiscrimStage3LedDelayStop8 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.44}
amDiscrimStage3LedDelayStop9 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.46}
amDiscrimStage3LedDelayStop10 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.48}
amDiscrimStage3LedDelayStop11 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.49}
amDiscrimStage3LedDelayStop12 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.495}
amDiscrimStage3LedDelayStop13 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.496}
amDiscrimStage3LedDelayStop14 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.497}
amDiscrimStage3LedDelayStop15 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.498}
amDiscrimStage3LedDelayStop16 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.499}
amDiscrimStage3LedDelayStop17 = { 'experimenter': 'sara', 'outcomeMode': 'only_if_correct', 'delayToTargetMean': 0.2, 'delayToTargetHalfRange': 0.02, 'targetDuration': 0.5, 
                       'allowEarlyWithdrawal': 'on', 'punishTimeEarly': 0, 'punishTimeError': 0, 'targetMaxIntensity': 60, 'targetIntensityMode': 'fixed', 
                       'lightMode': 'delayed', 'lightOffset': 'side_poke', 'automationMode': 'increase_light_delay', 'maxDelayToLight': 0.5}


sole072 = {'subject':'sole072', **amDiscrimStage3LedDelayStop10}
sole074 = {'subject':'sole074', **amDiscrimStage3LedDelayStop17}
sole076 = {'subject':'sole076', **amDiscrimStage3LedDelayStop17}
sole077 = {'subject':'sole077', **amDiscrimStage3LedDelayStop17}
sole078 = {'subject':'sole078', **amDiscrimStage3LedDelayStop12}
sole079 = {'subject':'sole079', **amDiscrimStage3LedDelayStop17}
sole080 = {'subject':'sole080', **amDiscrimStage3LedDelayStop11}
sole081 = {'subject':'sole081', **amDiscrimStage3LedDelayStop1}
sole082 = {'subject':'sole082', **amDiscrimStage3LedDelayStop8}
sole083 = {'subject':'sole083', **amDiscrimStage3}
sole084 = {'subject':'sole084', **amDiscrimStage3}
sole086 =  {'subject':'sole086', **amDiscrimStage0}
test000 = {'subject':'test000', **amDiscrimStage3LedDelay}
