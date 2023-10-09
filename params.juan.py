"""
This file defines the parameters to use for each subject.
"""

# --- Cooperation task ---

coopStage1 = {'taskMode':'auto_lights','barrierType': 'perforated_10_mm' ,'waitTime':3, 'pokesPerMouse': 1, 'rewardFrequency': 1}
coopStage2 = {'taskMode':'cooperate_lights','barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 1, 'rewardFrequency': 3, "activatePokeIncrement":"True", "numberOfPokeAddPerMouse":3, "thresholdForIncrementPoke":10}
coopStage3 = {'taskMode':'cooperate_lights', 'barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 10, 'rewardFrequency': 3}
coopStage4 = {'taskMode':'cooperate', 'barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 10,'rewardFrequency': 3}

'''
Barrier type:
            ["perforated_5_mm","perforated_10_mm", "solid", "transparent_holes", "transparent_no_holes", "no_barrier"]
'''
coop022x023 = {'subject':'coop022x023', 'experimenter':'juan', **coopStage4, 'barrierType': 'transparent_no_holes', 'rewardFrequency': 2, 'pokesPerMouse': 10, 'rigLight':'off'}
coop024x025 = {'subject':'coop024x025', 'experimenter':'juan', **coopStage4,'barrierType': 'perforated_10_mm','pokesPerMouse': 10,'rewardFrequency': 2, 'rigLight':'on'}
coop026x027 = {'subject':'coop026x027', 'experimenter':'juan', **coopStage4,'barrierType': 'perforated_10_mm', 'pokesPerMouse': 10, 'rewardFrequency': 2, 'rigLight':'on'} 
coop028x029 = {'subject':'coop028x029', 'experimenter':'juan', **coopStage3, 'barrierType': 'perforated_10_mm', "activatePokeIncrement":"False", 'pokesPerMouse': 10, 'targetPokesPerMouse':10, 'rewardFrequency': 3}