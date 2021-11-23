"""
Params for Sean.
"""
"""Params for Sean"""

FM_stage_one = {'outcomeMode': 'sides_direct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'on',
                'antibiasMode': 'off',
                'automationMode': 'off',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_two = {'outcomeMode': 'direct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'on',
                'antibiasMode': 'off',
                'automationMode': 'off',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_three = {'outcomeMode': 'on_next_correct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'on',
                'antibiasMode': 'off',
                'automationMode': 'off',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_three2 = {'outcomeMode': 'on_next_correct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'off',
                'antibiasMode': 'off',
                'automationMode': 'off',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_four = {'outcomeMode': 'on_next_correct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'off',
                'antibiasMode': 'off',
                'automationMode': 'increase_delay',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_five = {'outcomeMode': 'only_if_correct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'off',
                'antibiasMode': 'on',
                'delayToTargetmean':0.3,
                'automationMode': 'off',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_six = {'outcomeMode': 'only_if_correct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'off',
                'antibiasMode': 'off',
                'delayToTargetmean':0.3,
                'automationMode': 'off',
                'psycurveMode': 'off',
                'experimenter': 'sean'}

FM_stage_seven = {'outcomeMode': 'only_if_correct',
                'activePort': 'both',
                'allowEarlyWithdrawal': 'off',
                'antibiasMode': 'off',
                'delayToTargetmean':0.3,
                'automationMode': 'off',
                'psycurveMode': 'uniform',
                'experimenter': 'sean'}

FM_stage_eight = {'outcomeMode': 'only_if_correct',
                  'activePort': 'both',
                  'allowEarlyWithdrawal':'off',
                  'antibiasMode': 'off',
                  'delayToTargetmean':0.3,
                  'automationMode': 'off',
                  'psycurveMode': 'controls',
                  'experimenter': 'sean'}


pals020 = {'subject':'pals020',
           'experimenter': 'angelica',
           'taskMode': 'water_on_sound',
           'rewardSideMode': 'random',
           'soundType':'chords',
           }

frem001 = {'subject':'frem001',
          }

frem002 = {'subject':'frem002',
          }

frem003 = {'subject':'frem003',
          }

frem004 = {'subject':'frem004',
          }

frem005 = {'subject':'frem005',
          }

frem001.update(FM_stage_seven)
frem002.update(FM_stage_eight)
frem003.update(FM_stage_eight)
frem004.update(FM_stage_eight)
frem005.update(FM_stage_eight)
