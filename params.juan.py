"""
This file defines the parameters to use for each subject.
"""

# --- Cooperation task ---

coopStage1 = {'taskMode':'auto_lights','barrierType': 'perforated_10_mm' ,'waitTime':3, 'pokesPerMouse': 1, 'rewardFrequency': 1}
coopStage2 = {'taskMode':'cooperate_lights','barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 1, 'rewardFrequency': 3 }
coopStage3 = {'taskMode':'cooperate_lights', 'barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 10, 'rewardFrequency': 3}
coopStage4 = {'taskMode':'cooperate', 'barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 10,'rewardFrequency': 2}

coop016x017 = {'subject':'coop016x017', 'experimenter':'juan', **coopStage4}
coop018x019 = {'subject':'coop018x019', 'experimenter':'juan', **coopStage4, 'rewardFrequency': 3, 'pokesPerMouse': 15}
coop022x023 = {'subject':'coop022x023', 'experimenter':'juan', **coopStage4}
coop024x025 = {'subject':'coop024x025', 'experimenter':'juan', **coopStage2, 'pokesPerMouse': 7, "activatePokeIncrement":"True", "targetPokesPerMouse": 10, "numberOfPokeAddPerMouse":3, "thresholdForIncrementPoke":10}
coop026x027 = {'subject':'coop026x027', 'experimenter':'juan', **coopStage3, 'pokesPerMouse': 10, "activatePokeIncrement":"False", "targetPokesPerMouse": 10, "numberOfPokeAddPerMouse":3, "thresholdForIncrementPoke":10} 