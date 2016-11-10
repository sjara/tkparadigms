'''
Create a comodulation masking release 2AFC paradigm.


* TO DO:
- Check that all parameters are saved
- Check that all times are saved
- Note that outcomeMode (menu) is saved different from labels (e.g., outcome)
- Verify that the choice of last trial is saved properly

'''

import numpy as np
from taskontrol.settings import rigsettings
from taskontrol.core import paramgui
from PySide import QtGui
from taskontrol.core import arraycontainer
from taskontrol.core import utils

from taskontrol.plugins import templates
reload(templates)
from taskontrol.plugins import performancedynamicsplot

from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import speakernoisecalibration as noisecalibration
import time

LONGTIME = 100

class Paradigm(templates.Paradigm2AFC):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        # -- Performance dynamics plot --
        performancedynamicsplot.set_pg_colors(self)
        self.myPerformancePlot = performancedynamicsplot.PerformanceDynamicsPlot(nTrials=400,winsize=10)

         # -- Add parameters --
        self.params['timeWaterValveL'] = paramgui.NumericParam('Time valve left',value=0.03,enabled=False,
                                                               units='s',group='Water delivery')
        self.params['baseWaterValveL'] = paramgui.NumericParam('Base time left',value=0.03,
                                                               units='s',group='Water delivery')
        self.params['factorWaterValveL'] = paramgui.NumericParam('Factor left',value=1,
                                                               units='s',group='Water delivery')
        self.params['timeWaterValveR'] = paramgui.NumericParam('Time valve right',value=0.03,enabled=False,
                                                               units='s',group='Water delivery')
        self.params['baseWaterValveR'] = paramgui.NumericParam('Base time right',value=0.03,
                                                               units='s',group='Water delivery')
        self.params['factorWaterValveR'] = paramgui.NumericParam('Factor right',value=1,
                                                               units='s',group='Water delivery')
        waterDelivery = self.params.layout_group('Water delivery')

        self.params['outcomeMode'] = paramgui.MenuParam('Outcome mode',
                                                        ['sides_direct','direct','on_next_correct',
                                                         'only_if_correct','simulated'],
                                                         value=3,group='Choice parameters')
        self.params['antibiasMode'] = paramgui.MenuParam('Anti-bias mode',
                                                        ['off','repeat_mistake'],
                                                        value=0,group='Choice parameters')
        choiceParams = self.params.layout_group('Choice parameters')

        self.params['delayToTargetMean'] = paramgui.NumericParam('Mean delay to target',value=0.04,
                                                        units='s',group='Timing parameters')
        self.params['delayToTargetHalfRange'] = paramgui.NumericParam('+/-',value=0.0,
                                                        units='s',group='Timing parameters')
        self.params['delayToTarget'] = paramgui.NumericParam('Delay to target',value=0.3,
                                                        units='s',group='Timing parameters',
                                                        enabled=False,decimals=3)
        self.params['targetDuration'] = paramgui.NumericParam('Target duration',value=0.5,
                                                        units='s',group='Timing parameters')
        self.params['rewardAvailability'] = paramgui.NumericParam('Reward availability',value=4,
                                                        units='s',group='Timing parameters')
        self.params['punishTimeError'] = paramgui.NumericParam('Punishment (error)',value=0,
                                                        units='s',group='Timing parameters')
        self.params['punishTimeEarly'] = paramgui.NumericParam('Punishment (early)',value=0,
                                                        units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')

        self.params['automationMode'] = paramgui.MenuParam('Automation Mode',
                                                           ['off','increase_delay','same_left_right','same_right_left','left_right_left'],
                                                           value=0,group='Automation')
        automationParams = self.params.layout_group('Automation')
        
        
        self.params['threshMode'] = paramgui.MenuParam('Threshold Mode',
                                                         ['max_only','uniform'],
                                                         value=0,group='Threshold detection parameters')
        # -- tone intensity refers to difference between tone and masking noise --
        self.params['minSNR'] = paramgui.NumericParam('Minimum signal to noise',value=2, decimals=1,
                                                        units='dB',group='Threshold detection parameters')
        self.params['maxSNR'] = paramgui.NumericParam('Maximum signal to noise',value=20,decimals=0,
                                                        units='dB',group='Threshold detection parameters')
        self.params['numSNRs'] = paramgui.NumericParam('Number of SNRs', value=2, decimals=0, units='dB', group='Threshold detection parameters')
        threshParams = self.params.layout_group('Threshold detection parameters')


        self.params['bandMode'] = paramgui.MenuParam('Bandwidth Mode', ['white_only', 'max_only', 'uniform'], value=0, group='Bandwidth parameters')
        self.params['minBand'] = paramgui.NumericParam('Minimum bandwidth',value=0.25,decimals=2,
                                                        units='octaves',group='Bandwidth parameters')
        self.params['maxBand'] = paramgui.NumericParam('Maximum bandwidth',value=4.0,decimals=2,
                                                        units='octaves',group='Bandwidth parameters')
        self.params['numBands'] = paramgui.NumericParam('Number of bandwidths',
                                                               value=5, decimals=0, group='Bandwidth parameters')
        self.params['includeWhite'] = paramgui.MenuParam('Include white noise?', ['yes', 'no'], value=0, group='Bandwidth parameters')
        bandParams = self.params.layout_group('Bandwidth parameters')
        
        self.params['noiseMode'] = paramgui.MenuParam('Masker amplitude mode', ['max_only', 'uniform'], value=1, group='Masker amplitude parameters')
        # -- power refers to average power of noise stimulus
        self.params['minNoiseAmp'] = paramgui.NumericParam('Minimum noise power',value=30,decimals=0,
                                                        units='dB',group='Masker amplitude parameters')
        self.params['maxNoiseAmp'] = paramgui.NumericParam('Maximum noise power',value=40,decimals=0,
                                                        units='dB',group='Masker amplitude parameters')
        self.params['numAmps'] = paramgui.NumericParam('Number of noise amplitudes',
                                                               value=2, decimals=0, group='Masker amplitude parameters')  
        noiseParams = self.params.layout_group('Masker amplitude parameters')  
            
        self.params['toneFreq'] = paramgui.NumericParam('Tone frequency',value=8000,
                                                        units='Hz',group='Sound parameters')
        self.params['modRate'] = paramgui.NumericParam('Modulation Rate',value=8,
                                                        units='Hz',group='Sound parameters')        
        self.params['punishSoundAmplitude'] = paramgui.NumericParam('Punish amplitude',value=0.01,
                                                              units='[0-1]',enabled=True,
                                                              group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')
        
        self.params['currentBand'] = paramgui.NumericParam('Trial bandwidth',value=0.0,decimals=2,
                                                        units='octaves', enabled=False, group='Current Trial')
        self.params['currentNoiseAmp'] = paramgui.NumericParam('Trial noise power',value=0.0,decimals=0,
                                                        units='dB', enabled=False, group='Current Trial')
        self.params['currentSNR'] = paramgui.NumericParam('Trial SNR',value=0.0,decimals=1,
                                                        units='dB', enabled=False, group='Current Trial')
        trialParams = self.params.layout_group('Current Trial')

        self.params['nValid'] = paramgui.NumericParam('N valid',value=0,
                                                      units='',enabled=False,
                                                      group='Report')
        self.params['nRewarded'] = paramgui.NumericParam('N rewarded',value=0,
                                                         units='',enabled=False,
                                                         group='Report')
        reportParams = self.params.layout_group('Report')


        #
        self.params['experimenter'].set_value('santiago')
        self.params['subject'].set_value('test')

        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QVBoxLayout()
        layoutTop = QtGui.QVBoxLayout()
        layoutBottom = QtGui.QHBoxLayout()
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()
        layoutCol3 = QtGui.QVBoxLayout()
        layoutCol4 = QtGui.QVBoxLayout()

        layoutMain.addLayout(layoutTop)
        #layoutMain.addStretch()
        layoutMain.addSpacing(0)
        layoutMain.addLayout(layoutBottom)

        layoutTop.addWidget(self.mySidesPlot)
        layoutTop.addWidget(self.myPerformancePlot)

        layoutBottom.addLayout(layoutCol1)
        layoutBottom.addLayout(layoutCol2)
        layoutBottom.addLayout(layoutCol3)
        layoutBottom.addLayout(layoutCol4)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(self.dispatcherView)

        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(waterDelivery)
        layoutCol2.addStretch()
        layoutCol2.addWidget(choiceParams)
        layoutCol2.addStretch()

        layoutCol3.addWidget(timingParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(automationParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(trialParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(reportParams)
        layoutCol3.addStretch()
        
        layoutCol4.addWidget(soundParams)
        layoutCol4.addStretch()
        layoutCol4.addWidget(threshParams)
        layoutCol4.addStretch()
        layoutCol4.addWidget(bandParams)
        layoutCol4.addStretch()
        layoutCol4.addWidget(noiseParams)
        layoutCol4.addStretch()

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = 4000 # Preallocating space for each vector makes things easier
        self.results = arraycontainer.Container()
        self.results.labels['rewardSide'] = {'left':0,'right':1}
        self.results['rewardSide'] = np.random.randint(2,size=maxNtrials)
        self.results.labels['choice'] = {'left':0,'right':1,'none':2}
        self.results['choice'] = np.empty(maxNtrials,dtype=int)
        self.results.labels['outcome'] = {'correct':1,'error':0,'invalid':2,
                                          'free':3,'nochoice':4,'aftererror':5,'aborted':6}
        self.results['outcome'] = np.empty(maxNtrials,dtype=int)
        # Saving as bool creates an 'enum' vector, so I'm saving as 'int'
        self.results['valid'] = np.zeros(maxNtrials,dtype='int8') # redundant but useful
        self.results['timeTrialStart'] = np.empty(maxNtrials,dtype=float)
        self.results['timeTarget'] = np.empty(maxNtrials,dtype=float)
        self.results['timeCenterIn'] = np.empty(maxNtrials,dtype=float)
        self.results['timeCenterOut'] = np.empty(maxNtrials,dtype=float)
        self.results['timeSideIn'] = np.empty(maxNtrials,dtype=float)


        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

        # -- Connect to sound server and define sounds --
        print 'Conecting to soundserver...'
        print '***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****' ### DEBUG
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.punishSoundID = 127
        self.soundClient.start()

        # -- Prepare first trial --
        #self.prepare_next_trial(0)

    def prepare_punish_sound(self):
        punishSoundAmplitude = self.params['punishSoundAmplitude'].get_value()
        sNoise = {'type':'noise', 'duration':0.5, 'amplitude':punishSoundAmplitude}
        self.soundClient.set_sound(self.punishSoundID,sNoise)

    def prepare_target_sound(self, band, noiseInt, toneInt):
        spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION)
        # FIXME: currently I am averaging calibration from both speakers (not good)
        stimDur = self.params['targetDuration'].get_value()
        modRate = self.params['modRate'].get_value()
        noiseCal = noisecalibration.Calibration(rigsettings.NOISE_CALIBRATION)
        toneFreq = self.params['toneFreq'].get_value()
        noiseAmp = noiseCal.find_amplitude(1, noiseInt).mean()
        if np.isinf(band):
            s1 = {'type':'AM', 'modFrequency': modRate, 'duration':stimDur, 'amplitude': noiseAmp}
        else:
            s1 = {'type':'band_AM', 'modRate': modRate, 'frequency': toneFreq, 'octaves': band, 'duration': stimDur, 'amplitude': noiseAmp}
        toneAmp = spkCal.find_amplitude(toneFreq, noiseInt+toneInt).mean()
        s2 = {'type':'tone', 'frequency': toneFreq, 'duration':stimDur, 'amplitude': toneAmp}
        self.soundClient.set_sound(1,s1)
        self.soundClient.set_sound(2,s2)


    def prepare_next_trial(self, nextTrial):
        import time
        TicTime = time.time()

        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.params.update_history()
            self.calculate_results(nextTrial-1)
            # -- Apply anti-bias --
            if self.params['antibiasMode'].get_string()=='repeat_mistake':
                if self.results['outcome'][nextTrial-1]==self.results.labels['outcome']['error']:
                    self.results['rewardSide'][nextTrial] = self.results['rewardSide'][nextTrial-1]
            # -- Set current block if switching --
            nValid = self.params['nValid'].get_value()
            ###print '{0} {1} {2}'.format(nValid,trialsPerBlock,np.mod(nValid,trialsPerBlock)) ### DEBUG

        #import pdb; pdb.set_trace() ### DEBUG

        # === Prepare next trial ===
        self.execute_automation()
        nextCorrectChoice = self.results['rewardSide'][nextTrial]

        # -- Define reward for each side --
        factorL = 1
        factorR = 1
        self.params['timeWaterValveL'].set_value(factorL*self.params['baseWaterValveL'].get_value())
        self.params['timeWaterValveR'].set_value(factorR*self.params['baseWaterValveR'].get_value())

        # -- Prepare sound --
        threshMode = self.params['threshMode'].get_string()
        if threshMode=='max_only':
            if nextCorrectChoice==self.results.labels['rewardSide']['left']:
                currentToneInt = -np.inf
            elif nextCorrectChoice==self.results.labels['rewardSide']['right']:
                currentToneInt = self.params['maxSNR'].get_value()
        elif threshMode=='uniform': 
            if nextCorrectChoice==self.results.labels['rewardSide']['left']:
                currentToneInt = -np.inf
            elif nextCorrectChoice==self.results.labels['rewardSide']['right']:
                numSNRs = self.params['numSNRs'].get_value()
                minSNR = self.params['minSNR'].get_value()
                maxSNR = self.params['maxSNR'].get_value()
                allSNRs = np.logspace(np.log2(minSNR), np.log2(maxSNR), numSNRs, base=2.0)
                currentToneInt = np.random.choice(allSNRs)
        if self.params['bandMode'].get_string()=='white_only':
            currentBand = np.inf
        elif self.params['bandMode'].get_string()=='max_only':
            currentBand = self.params['maxBand'].get_value()
        else:
            numBands = self.params['numBands'].get_value()
            minBand = self.params['minBand'].get_value()
            maxBand = self.params['maxBand'].get_value()
            allBands = np.logspace(np.log2(minBand), np.log2(maxBand), numBands, base=2.0)
            if self.params['includeWhite'].get_string()=='yes':
                allBands = np.append(allBands, np.inf)
            currentBand = np.random.choice(allBands)
        if self.params['noiseMode'].get_string()=='max_only':
            currentNoiseAmp = self.params['maxNoiseAmp'].get_value()
        else:
            allNoiseAmps = np.linspace(self.params['minNoiseAmp'].get_value(), self.params['maxNoiseAmp'].get_value(), self.params['numAmps'].get_value())
            currentNoiseAmp = np.random.choice(allNoiseAmps)
        self.params['currentBand'].set_value(currentBand)
        self.params['currentNoiseAmp'].set_value(currentNoiseAmp)
        self.params['currentSNR'].set_value(currentToneInt)
        self.prepare_target_sound(currentBand, currentNoiseAmp, currentToneInt)
        self.prepare_punish_sound()

        # -- Prepare state matrix --
        self.set_state_matrix(nextCorrectChoice)
        self.dispatcherModel.ready_to_start_trial()
        ###print 'Elapsed Time (preparing next trial): ' + str(time.time()-TicTime) ### DEBUG

        # -- Update sides plot --
        self.mySidesPlot.update(self.results['rewardSide'],self.results['outcome'],nextTrial)

        # -- Update performance plot --
        self.myPerformancePlot.update(self.results['rewardSide'],self.results.labels['rewardSide'],
                                      self.results['outcome'],self.results.labels['outcome'],
                                      nextTrial)

    def set_state_matrix(self,nextCorrectChoice):
        self.sm.reset_transitions()

        noiseID = 1  # The appropriate sound has already been prepared and sent to server with ID=1
        toneID = 2
        targetDuration = self.params['targetDuration'].get_value()
        if rigsettings.OUTPUTS.has_key('outBit1'):
            trialStartOutput = ['outBit1'] # Sync signal for trial-start.
        else:
            trialStartOutput = []
        if rigsettings.OUTPUTS.has_key('outBit0'):
            stimOutput = ['outBit0'] # Sync signal for stimulus
        else:
            stimOutput = []
        if nextCorrectChoice==self.results.labels['rewardSide']['left']:
            rewardDuration = self.params['timeWaterValveL'].get_value()
            ledOutput = 'leftLED'
            fromChoiceL = 'reward'
            fromChoiceR = 'punish'
            rewardOutput = 'leftWater'
            correctSidePort = 'Lin'
            #soundID = 1
        elif nextCorrectChoice==self.results.labels['rewardSide']['right']:
            rewardDuration = self.params['timeWaterValveR'].get_value()
            ledOutput = 'rightLED'
            fromChoiceL = 'punish'
            fromChoiceR = 'reward'
            rewardOutput = 'rightWater'
            correctSidePort = 'Rin'
            #soundID = 2
        else:
            raise ValueError('Value of nextCorrectChoice is not appropriate')

        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        delayToTarget = self.params['delayToTargetMean'].get_value() + \
            self.params['delayToTargetHalfRange'].get_value()*randNum
        self.params['delayToTarget'].set_value(delayToTarget)
        rewardAvailability = self.params['rewardAvailability'].get_value()
        punishTimeError = self.params['punishTimeError'].get_value()
        punishTimeEarly = self.params['punishTimeEarly'].get_value()

        # -- Set state matrix --
        outcomeMode = self.params['outcomeMode'].get_string()
        if outcomeMode=='simulated':
            stimOutput.append(ledOutput)
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=1,
                              transitions={'Tup':'playNoiseStimulus'})
            self.sm.add_state(name='playNoiseStimulus', statetimer=0,
                              transitions={'Tup':'playToneStimulus'},
                              outputsOn=stimOutput, serialOut=noiseID,
                              outputsOff=trialStartOutput)
            self.sm.add_state(name='playToneStimulus', statetimer=targetDuration,
                              transitions={'Tup':'reward'}, serialOut=toneID)
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput],
                              outputsOff=stimOutput)
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput])
        elif outcomeMode=='sides_direct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'playNoiseStimulus',correctSidePort:'playNoiseStimulus'})
            self.sm.add_state(name='playNoiseStimulus', statetimer=0,
                              transitions={'Tup':'playToneStimulus'},
                              outputsOn=stimOutput,serialOut=noiseID,
                              outputsOff=trialStartOutput)
            self.sm.add_state(name='playToneStimulus', statetimer=targetDuration,
                              transitions={'Tup':'reward'}, serialOut=toneID)
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput],
                              outputsOff=stimOutput)
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput])
        elif outcomeMode=='direct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'playNoiseStimulus'})
            self.sm.add_state(name='playNoiseStimulus', statetimer=0,
                              transitions={'Tup':'playToneStimulus'},
                              outputsOn=stimOutput,serialOut=noiseID,
                              outputsOff=trialStartOutput)
            self.sm.add_state(name='playToneStimulus', statetimer=targetDuration,
                              transitions={'Tup':'reward'}, serialOut=toneID)
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput],
                              outputsOff=stimOutput)
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput])
        elif outcomeMode=='on_next_correct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                              transitions={'Tup':'playNoiseStimulus','Cout':'waitForCenterPoke'})
            self.sm.add_state(name='playNoiseStimulus', statetimer=0,
                              transitions={'Tup':'playToneStimulus'},
                              outputsOn=stimOutput,serialOut=noiseID,
                              outputsOff=trialStartOutput)
            self.sm.add_state(name='playToneStimulus', statetimer=targetDuration,
                              transitions={'Cout':'waitForSidePoke', 'Tup':'waitForSidePoke'},serialOut=toneID)
            self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                              transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                           'Tup':'noChoice'},
                              outputsOff=stimOutput)
            self.sm.add_state(name='keepWaitForSide', statetimer=rewardAvailability,
                              transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                           'Tup':'noChoice'},
                              outputsOff=stimOutput)
            if correctSidePort=='Lin':
                self.sm.add_state(name='choiceLeft', statetimer=0,
                                  transitions={'Tup':'reward'})
                self.sm.add_state(name='choiceRight', statetimer=0,
                                  transitions={'Tup':'keepWaitForSide'})
            elif correctSidePort=='Rin':
                self.sm.add_state(name='choiceLeft', statetimer=0,
                                  transitions={'Tup':'keepWaitForSide'})
                self.sm.add_state(name='choiceRight', statetimer=0,
                                  transitions={'Tup':'reward'})
            #self.sm.add_state(name='earlyWithdrawal', statetimer=punishTimeEarly,
            #                  transitions={'Tup':'readyForNextTrial'},
            #                  outputsOff=stimOutput,serialOut=self.punishSoundID)
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput])
            self.sm.add_state(name='punish', statetimer=punishTimeError,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='noChoice', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})

        elif outcomeMode=='only_if_correct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                              transitions={'Tup':'playNoiseStimulus','Cout':'waitForCenterPoke'})
            # Note that 'delayPeriod' may happen several times in a trial, so
            # trialStartOutput off here would only meaningful for the first time in the trial.
            self.sm.add_state(name='playNoiseStimulus', statetimer=0,
                              transitions={'Tup':'playToneStimulus'},
                              outputsOn=stimOutput, serialOut=noiseID,
                              outputsOff=trialStartOutput)
            self.sm.add_state(name='playToneStimulus', statetimer=targetDuration,
                              transitions={'Cout':'waitForSidePoke', 'Tup':'waitForSidePoke'}, serialOut=toneID)
            # NOTE: The idea of outputsOff here (in other paradigms) was to indicate the end
            #       of the stimulus. But in this paradigm the stimulus will continue to play.
            self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                              transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                           'Tup':'noChoice'},
                              outputsOff=stimOutput)
            if correctSidePort=='Lin':
                self.sm.add_state(name='choiceLeft', statetimer=0,
                                  transitions={'Tup':'reward'})
                self.sm.add_state(name='choiceRight', statetimer=0,
                                  transitions={'Tup':'punish'})
            elif correctSidePort=='Rin':
                self.sm.add_state(name='choiceLeft', statetimer=0,
                                  transitions={'Tup':'punish'})
                self.sm.add_state(name='choiceRight', statetimer=0,
                                  transitions={'Tup':'reward'})
            #self.sm.add_state(name='earlyWithdrawal', statetimer=punishTimeEarly,
            #                  transitions={'Tup':'readyForNextTrial'},
            #                  outputsOff=stimOutput,serialOut=self.punishSoundID)
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput]+stimOutput)
            self.sm.add_state(name='punish', statetimer=punishTimeError,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='noChoice', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})

        else:
            raise TypeError('outcomeMode={0} has not been implemented'.format(outcomeMode))
        ###print self.sm ### DEBUG
        self.dispatcherModel.set_state_matrix(self.sm)


    def calculate_results(self,trialIndex):
        # -- Find outcomeMode for this trial --
        outcomeModeID = self.params.history['outcomeMode'][trialIndex]
        outcomeModeString = self.params['outcomeMode'].get_items()[outcomeModeID]

        eventsThisTrial = self.dispatcherModel.events_one_trial(trialIndex)
        #print eventsThisTrial
        statesThisTrial = eventsThisTrial[:,2]

        # -- Find beginning of trial --
        startTrialStateID = self.sm.statesNameToIndex['startTrial']
        # FIXME: Next line seems inefficient. Is there a better way?
        startTrialInd = np.flatnonzero(statesThisTrial==startTrialStateID)[0]
        self.results['timeTrialStart'][trialIndex] = eventsThisTrial[startTrialInd,0]
        #print 'TrialStart : {0}'.format(self.results['timeTrialStart'][trialIndex]) ### DEBUG

        # ===== Calculate times of events =====
        # -- Check if it's an aborted trial --
        lastEvent = eventsThisTrial[-1,:]
        if lastEvent[1]==-1 and lastEvent[2]==0:
            self.results['timeTarget'][trialIndex] = np.nan
            self.results['timeCenterIn'][trialIndex] = np.nan
            self.results['timeCenterOut'][trialIndex] = np.nan
            self.results['timeSideIn'][trialIndex] = np.nan
        # -- Otherwise evaluate times of important events --
        else:
            # -- Store time of stimulus --
            targetStateID = self.sm.statesNameToIndex['playNoiseStimulus']
            targetEventInd = np.flatnonzero(statesThisTrial==targetStateID)[0]
            self.results['timeTarget'][trialIndex] = eventsThisTrial[targetEventInd,0]

            # -- Find center poke-in time --
            if outcomeModeString in ['on_next_correct','only_if_correct']:
                seqCin = [self.sm.statesNameToIndex['waitForCenterPoke'],
                          self.sm.statesNameToIndex['delayPeriod'],
                          self.sm.statesNameToIndex['playNoiseStimulus']]
            elif outcomeModeString in ['simulated','sides_direct','direct']:
                seqCin = [self.sm.statesNameToIndex['waitForCenterPoke'],
                          self.sm.statesNameToIndex['playNoiseStimulus']]
            else:
                print 'CenterIn time cannot be calculated for this Outcome Mode.'
            seqPos = np.flatnonzero(utils.find_state_sequence(statesThisTrial,seqCin))
            timeValue = eventsThisTrial[seqPos[0]+1,0] if len(seqPos) else np.nan
            self.results['timeCenterIn'][trialIndex] = timeValue

            # -- Find center poke-out time --
            if len(seqPos):
                cInInd = seqPos[0]+1
                cOutInd = np.flatnonzero(eventsThisTrial[cInInd:,1]==self.sm.eventsDict['Cout'])
                timeValue = eventsThisTrial[cOutInd[0]+cInInd,0] if len(cOutInd) else np.nan
            else:
                timeValue = np.nan
            self.results['timeCenterOut'][trialIndex] = timeValue

            # -- Find side poke time --
            if outcomeModeString in ['on_next_correct','only_if_correct']:
                leftInInd = utils.find_transition(statesThisTrial,
                                                  self.sm.statesNameToIndex['waitForSidePoke'],
                                                  self.sm.statesNameToIndex['choiceLeft'])
                rightInInd = utils.find_transition(statesThisTrial,
                                                   self.sm.statesNameToIndex['waitForSidePoke'],
                                                   self.sm.statesNameToIndex['choiceRight'])
                if len(leftInInd):
                    timeValue = eventsThisTrial[leftInInd[0],0]
                elif len(rightInInd):
                    timeValue = eventsThisTrial[rightInInd[0],0]
                else:
                    timeValue = np.nan
            elif outcomeModeString in ['simulated','sides_direct','direct']:
                timeValue = np.nan
            self.results['timeSideIn'][trialIndex] = timeValue

        # ===== Calculate choice and outcome =====
        # -- Check if it's an aborted trial --
        lastEvent = eventsThisTrial[-1,:]
        if lastEvent[1]==-1 and lastEvent[2]==0:
            self.results['outcome'][trialIndex] = self.results.labels['outcome']['aborted']
            self.results['choice'][trialIndex] = self.results.labels['choice']['none']
        # -- Otherwise evaluate 'choice' and 'outcome' --
        else:
            if outcomeModeString in ['simulated','sides_direct','direct']:
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['free']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']
                self.params['nValid'].add(1)
                self.params['nRewarded'].add(1)
                self.results['valid'][trialIndex] = 1
            if outcomeModeString=='on_next_correct' or outcomeModeString=='only_if_correct':
                if self.sm.statesNameToIndex['choiceLeft'] in eventsThisTrial[:,2]:
                    self.results['choice'][trialIndex] = self.results.labels['choice']['left']
                elif self.sm.statesNameToIndex['choiceRight'] in eventsThisTrial[:,2]:
                    self.results['choice'][trialIndex] = self.results.labels['choice']['right']
                else:
                    self.results['choice'][trialIndex] = self.results.labels['choice']['none']
                    self.results['outcome'][trialIndex] = \
                        self.results.labels['outcome']['nochoice']
                if self.sm.statesNameToIndex['reward'] in eventsThisTrial[:,2]:
                   self.results['outcome'][trialIndex] = \
                        self.results.labels['outcome']['correct']
                   self.params['nRewarded'].add(1)
                   if outcomeModeString=='on_next_correct' and \
                           self.sm.statesNameToIndex['keepWaitForSide'] in eventsThisTrial[:,2]:
                       self.results['outcome'][trialIndex] = \
                           self.results.labels['outcome']['aftererror']
                else:
                    #if self.sm.statesNameToIndex['earlyWithdrawal'] in eventsThisTrial[:,2]:
                    #    self.results['outcome'][trialIndex] = \
                    #        self.results.labels['outcome']['invalid']
                    if self.sm.statesNameToIndex['punish'] in eventsThisTrial[:,2]:
                        self.results['outcome'][trialIndex] = \
                            self.results.labels['outcome']['error']
                # -- Check if it was a valid trial --
                if self.sm.statesNameToIndex['waitForSidePoke'] in eventsThisTrial[:,2]:
                    self.params['nValid'].add(1)
                    self.results['valid'][trialIndex] = 1

    def execute_automation(self):
        '''This executes only some modes. Other modes are use outside this method'''
        automationMode = self.params['automationMode'].get_string()
        nValid = self.params['nValid'].get_value()
        if automationMode=='increase_delay':
            if nValid>0 and not nValid%10:
                self.params['delayToTargetMean'].add(0.010)

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcherModel.die()
        event.accept()

if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)
