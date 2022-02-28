
stage0 = { 'experimenter':'haziq', 
           'outcomeMode':'sides_direct', 'delayToTargetMean':0}
           
stage1 = { 'experimenter':'haziq', 
           'outcomeMode':'direct', 'delayToTargetMean':0}
           
stage2 = { 'experimenter':'haziq', 
           'outcomeMode':'on_next_correct', 'delayToTargetMean':0.01,
           'delayToTargetHalfRange':0.0, 'automationMode':'increase_delay'}
           
stage3 = { 'experimenter':'haziq', 
           'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
           'delayToTargetHalfRange':0.05, 'psycurveMode':'off',
           'maxNtrials':500}

stage4 = {'experimenter':'haziq', 
           'outcomeMode':'only_if_correct', 'delayToTargetMean':0.2,
           'delayToTargetHalfRange':0.05, 'psycurveMode':'uniform',
           'maxNtrials':500}

pamo009 = {'subject':'pamo009',
          }
pamo010 = {'subject':'pamo010',
          }
pamo011 = {'subject':'pamo011',
          }
pamo012 = {'subject':'pamo012',
          }
pamo013 = {'subject':'pamo013',
          }
pamo014 = {'subject':'pamo014',
          }
pamo015 = {'subject':'pamo015',
          }
pamo016 = {'subject':'pamo016',
          }    
pamo017 = {'subject':'pamo017',
          }
pamo018 = {'subject':'pamo018',
          }
pamo019 = {'subject':'pamo019',
          }
pamo020 = {'subject':'pamo020',
          }
pamo021 = {'subject':'pamo021',
          }
pamo022 = {'subject':'pamo022',
          }
pamo023 = {'subject':'pamo023',
          }
pamo024 = {'subject':'pamo024',
          }
pamo025 = {'subject':'pamo025',
          }
pamo026 = {'subject':'pamo026',
          }          

pamo009.update(stage4)
pamo010.update(stage4)
pamo011.update(stage4)
pamo012.update(stage4)
pamo013.update(stage4)
pamo014.update(stage4)
pamo015.update(stage4)
pamo016.update(stage3)
pamo017.update(stage4)
pamo018.update(stage3)
pamo019.update(stage3)
pamo020.update(stage4)
pamo021.update(stage4)
pamo022.update(stage4)
pamo023.update(stage4)
pamo024.update(stage4)
pamo025.update(stage4) 
pamo026.update(stage4)

