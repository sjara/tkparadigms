
stage0 = {'experimenter':'haziq', 
          'outcomeMode':'sides_direct', 'delayToTargetMean':0}
           
stage1 = { 'experimenter':'haziq', 
           'outcomeMode':'direct', 'delayToTargetMean':0}
           
stage2 = { 'experimenter':'haziq', 
           'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
           'delayToTargetHalfRange':0.0, 'automationMode':'increase_delay',
           'maxNtrials':400}

stage3 = { 'experimenter':'haziq', 
           'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
           'delayToTargetHalfRange':0.05, 'psycurveMode':'off',
           'maxNtrials':500}

stage4 = {'experimenter':'haziq', 
           'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
           'delayToTargetHalfRange':0.05, 'psycurveMode':'uniform',
           'maxNtrials':500}
           
stage5 = {'experimenter':'haziq', 
           'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
           'delayToTargetHalfRange':0.05, 'psycurveMode':'controls',
           'maxNtrials':500}

antibias = {'antibiasMode':'repeat_mistake'}

pamo009 = {'subject':'pamo009', **stage5}
pamo010 = {'subject':'pamo010', **stage5}
pamo011 = {'subject':'pamo011', **stage5}
pamo012 = {'subject':'pamo012', **stage5}
pamo013 = {'subject':'pamo013', **stage5}
pamo014 = {'subject':'pamo014', **stage5}
pamo015 = {'subject':'pamo015', **stage5}
pamo016 = {'subject':'pamo016', **stage5}
pamo017 = {'subject':'pamo017', **stage5}
pamo018 = {'subject':'pamo018', **stage5}
pamo019 = {'subject':'pamo019', **stage5}
pamo020 = {'subject':'pamo020', **stage5}
pamo021 = {'subject':'pamo021', **stage5}
pamo022 = {'subject':'pamo022', **stage5}
pamo023 = {'subject':'pamo023', **stage5}
pamo024 = {'subject':'pamo024', **stage5}
pamo025 = {'subject':'pamo025', **stage5}
pamo026 = {'subject':'pamo026', **stage5}

pamo027 = {'subject':'pamo027', **stage4}
pamo028 = {'subject':'pamo028', **stage4}
pamo029 = {'subject':'pamo029', **stage4}
pamo030 = {'subject':'pamo030', **stage4}
pamo031 = {'subject':'pamo031', **stage4}
pamo032 = {'subject':'pamo032', **stage4}
pamo033 = {'subject':'pamo033', **stage4}
pamo034 = {'subject':'pamo034', **stage4}
pamo035 = {'subject':'pamo035', **stage4}
pamo036 = {'subject':'pamo036', **stage4}
pamo037 = {'subject':'pamo037', **stage4}
pamo038 = {'subject':'pamo038', **stage4}
pamo039 = {'subject':'pamo039', **stage4}
pamo040 = {'subject':'pamo040', **stage4}
pamo041 = {'subject':'pamo041', **stage4}

pamo042 = {'subject':'pamo042', **stage3}
pamo043 = {'subject':'pamo043', **stage3, **antibias}
pamo044 = {'subject':'pamo044', **stage3}
pamo045 = {'subject':'pamo045', **stage3}
pamo046 = {'subject':'pamo046', **stage3}
pamo047 = {'subject':'pamo047', **stage3}
pamo048 = {'subject':'pamo048', **stage3}
pamo049 = {'subject':'pamo049', **stage3, **antibias}
pamo050 = {'subject':'pamo050', **stage3}
pamo051 = {'subject':'pamo051', **stage3}
pamo052 = {'subject':'pamo052', **stage3}
pamo053 = {'subject':'pamo053', **stage3}
pamo054 = {'subject':'pamo054', **stage3}
pamo055 = {'subject':'pamo055', **stage3}
pamo056 = {'subject':'pamo056', **stage3}
pamo057 = {'subject':'pamo057', **stage3}
pamo058 = {'subject':'pamo058', **stage3}
pamo059 = {'subject':'pamo059', **stage3, **antibias}

