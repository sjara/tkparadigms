"""
Params for Angelica.
"""

AM_stage_one = {'taskMode': 'water_on_sound',
                'rewardSideMode': 'random',
                'soundType':'AM_depth',
                'experimenter': 'isabella'}

AM_stage_two = {'taskMode': 'lick_on_stim',
                'lickBeforeStimOffset': 'ignore',
                'rewardSideMode': 'repeat_mistake',
                'soundType': 'AM_depth',
                'experimenter': 'isabella'}

AM_stage_three = {'taskMode': 'discriminate_stim',
                  'lickBeforeStimOffset': 'ignore',
                  'rewardSideMode': 'repeat_mistake',
                  'soundType': 'AM_depth',
                  'experimenter': 'isabella'}

AM_stage_four = {'taskMode': 'discriminate_stim',
                 'rewardSideMode': 'random',
                 'soundType': 'AM_depth',
                 'experimenter': 'isabella'}


pals015 = {'subject':'pals015',
           'experimenter': 'angelica',
           'taskMode': 'water_on_sound',
           'rewardSideMode': 'random',
           'soundType':'chords',
           }

amod015 = {'subject':'amod015',
           'experimenter': 'angelica',
          }
amod015.update(AM_stage_one)

# python am_discrimination.py params.angelica.py amod015
