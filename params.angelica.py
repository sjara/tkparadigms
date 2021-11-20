"""
Params for Angelica.
"""

AM_stage_zero = {'outcomeMode':'sides_direct',
                'delayToTargetMean':0,
                'delayToTargetHalfRange':0,
                'experimenter': 'angelica'
               }

AM_stage_one = {'outcomeMode':'direct',
                'delayToTargetMean':0.0,
                'delayToTargetHalfRange':0.0,
                'experimenter': 'angelica'}

AM_stage_two = {'outcomeMode':'on_next_correct',
                'delayToTargetMean':0.0,
                'delayToTargetHalfRange':0.0,
                'automationMode': 'increase_delay',
                'experimenter': 'angelica'}

AM_stage_three = {'outcomeMode':'only_if_correct',
                'delayToTargetMean':0.2,
                'delayToTargetHalfRange':0.05,
                'experimenter': 'angelica'}

bias_correction_stage = {'outcomeMode':'only_if_correct',
                'delayToTargetMean':0.2,
                'delayToTargetHalfRange':0.05,
                'antibiasMode': 'repeat_mistake',
                'experimenter': 'angelica'}

AM_stage_four = {'outcomeMode':'only_if_correct',
                'delayToTargetMean':0.2,
                'delayToTargetHalfRange':0.05,
                 'psycurveMode': 'uniform',
                'experimenter': 'angelica'}


pals015 = {'subject':'pals015',
           'experimenter': 'angelica',
           'taskMode': 'water_on_sound',
           'rewardSideMode': 'random',
           'soundType':'chords',
           }

amod015 = {'subject':'amod015',
          }

amod016 = {'subject':'amod016',
          }

amod017 = {'subject':'amod017',
          }

amod018 = {'subject':'amod018',
          }

amod019 = {'subject':'amod019',
          }

amod020 = {'subject':'amod020',
          }

amod015.update(AM_stage_four)
amod016.update(AM_stage_three)
amod017.update(bias_correction_stage)
amod018.update(AM_stage_three)
amod019.update(AM_stage_four)
amod020.update(AM_stage_four)

# python am_discrimination.py params.angelica.py amod015
