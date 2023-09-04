"""
This file defines the parameters to use for each subject.
"""

# --- Cooperation task ---

coopStage1 = {'taskMode':'auto_lights','barrierType': 'perforated_10_mm' ,'waitTime':3, 'pokesPerMouse': 1, 'rewardFrequency': 1}
coopStage2 = {'taskMode':'cooperate_lights','barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 1, 'rewardFrequency': 3, "activatePokeIncrement":"True", "numberOfPokeAddPerMouse":3, "thresholdForIncrementPoke":10}
coopStage3 = {'taskMode':'cooperate_lights', 'barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 10, 'rewardFrequency': 3}
coopStage4 = {'taskMode':'cooperate', 'barrierType': 'perforated_10_mm', 'waitTime':0.5, 'pokesPerMouse': 10,'rewardFrequency': 3}

coop016x017 = {'subject':'coop016x017', 'experimenter':'juan', **coopStage4, 'barrierType': 'solid', 'rewardFrequency': 2 }
coop018x019 = {'subject':'coop018x019', 'experimenter':'juan', **coopStage4, 'pokesPerMouse': 15}
coop022x023 = {'subject':'coop022x023', 'experimenter':'juan', **coopStage4, 'barrierType': 'solid', 'rewardFrequency': 2, 'pokesPerMouse': 5}
coop024x025 = {'subject':'coop024x025', 'experimenter':'juan', **coopStage4,'barrierType': 'perforated_10_mm','pokesPerMouse': 10,'rewardFrequency': 2 }
coop026x027 = {'subject':'coop026x027', 'experimenter':'juan', **coopStage4,'barrierType': 'solid', 'pokesPerMouse': 10, 'rewardFrequency': 2} 
coop028x029 = {'subject':'coop028x029', 'experimenter':'juan', **coopStage1,}