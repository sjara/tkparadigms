'''
Create a frequency discrimination 2AFC paradigm (with laser photostimulation)
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
import time
import numpy as np

LONGTIME = 100

class Paradigm(templates.Paradigm2AFC):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        # -- Performance dynamics plot --
        performancedynamicsplot.set_pg_colors(self)
        self.myPerformancePlot = performancedynamicsplot.PerformanceDynamicsPlot(nTrials=400,winsize=10)

         # -- Add parameters --
        self.params['timeWaterValveL'] = paramgui.NumericParam('Time valve left',value=0.03,
                                                               units='s',group='Water delivery')
        self.params['timeWaterValveC'] = paramgui.NumericParam('Time valve center',value=0.03,
                                                               units='s',group='Water delivery')
        self.params['timeWaterValveR'] = paramgui.NumericParam('Time valve right',value=0.03,
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

        self.params['delayToTargetMean'] = paramgui.NumericParam('Mean delay to target',value=0.2,
                                                        units='s',group='Timing parameters')
        self.params['delayToTargetHalfRange'] = paramgui.NumericParam('+/-',value=0,
                                                        units='s',group='Timing parameters')
        self.params['delayToTarget'] = paramgui.NumericParam('Delay to target',value=0.3,
                                                        units='s',group='Timing parameters',
                                                        enabled=False,decimals=3)
        self.params['targetDuration'] = paramgui.NumericParam('Target duration',value=0.1,
                                                        units='s',group='Timing parameters')
        self.params['rewardAvailability'] = paramgui.NumericParam('Reward availability',value=4,
                                                        units='s',group='Timing parameters')
        self.params['punishTimeError'] = paramgui.NumericParam('Punishment (error)',value=0,
                                                        units='s',group='Timing parameters')
        self.params['punishTimeEarly'] = paramgui.NumericParam('Punishment (early)',value=0,
                                                        units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')


        self.params['psycurveMode'] = paramgui.MenuParam('PsyCurve Mode',
                                                         ['off','uniform'],
                                                         value=0,group='Psychometric parameters')
        self.params['psycurveNfreq'] = paramgui.NumericParam('N frequencies',value=8,decimals=0,
                                                             group='Psychometric parameters')
        psychometricParams = self.params.layout_group('Psychometric parameters')


        self.params['automationMode'] = paramgui.MenuParam('Automation Mode',
                                                           ['off','increase_delay'],
                                                           value=0,group='Automation')
        self.params['goSignalMode'] = paramgui.MenuParam('Go signal mode',
                                                        ['on-off','off-on'],
                                                         value=0,group='Automation')
        automationParams = self.params.layout_group('Automation')

        self.params['highFreq'] = paramgui.NumericParam('High freq',value=16000,
                                                        units='Hz',group='Sound parameters')
        #self.params['midFreq'] = paramgui.NumericParam('Middle freq',value=7000,
        #                                                units='Hz',group='Sound parameters')
        self.params['lowFreq'] = paramgui.NumericParam('Low freq',value=3000,
                                                        units='Hz',group='Sound parameters')
        self.params['targetFrequency'] = paramgui.NumericParam('Target freq',value=0,decimals=0,
                                                        units='Hz',enabled=False,group='Sound parameters')
        self.params['targetIntensityMode'] = paramgui.MenuParam('Intensity mode',
                                                               ['fixed','randMinus20'],
                                                               value=1,group='Sound parameters')
        # This intensity corresponds to the intensity of each component of the chord
        self.params['targetMaxIntensity'] = paramgui.NumericParam('Max intensity',value=50,
                                                        units='dB-SPL',group='Sound parameters')
        self.params['targetIntensity'] = paramgui.NumericParam('Intensity',value=0.0,units='dB-SPL',
                                                        enabled=False,group='Sound parameters')
        self.params['targetAmplitude'] = paramgui.NumericParam('Target amplitude',value=0.0,units='[0-1]',
                                                        enabled=False,decimals=4,group='Sound parameters')
        self.params['punishSoundAmplitude'] = paramgui.NumericParam('Punish amplitude',value=0.01,
                                                              units='[0-1]',enabled=True,
                                                              group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')

        self.params['nValid'] = paramgui.NumericParam('N valid',value=0,
                                                      units='',enabled=False,
                                                      group='Report')
        self.params['nRewarded'] = paramgui.NumericParam('N rewarded',value=0,
                                                         units='',enabled=False,
                                                         group='Report')
        reportParams = self.params.layout_group('Report')

        
        # Photostim params
        self.params['laserDuration'] = paramgui.NumericParam('Laser duration',value=0.1,
                                                             units='s',group='Stimulation times')
        self.params['laserOnset'] = paramgui.NumericParam('Laser onset',value=np.nan,
                                                          units='s',enabled=False,group='Stimulation times')
        self.params['trialType'] = paramgui.MenuParam('Trial Type', 
                                                      ['no_laser','laser_onset1','laser_onset2',
                                                       'laser_onset3'],
                                                      value=0, enabled=False, group='Stimulation times')
        self.params['laserOnsetFromSoundOnset1'] = paramgui.NumericParam('Laser onset 1 (from sound)',value=-0.1,
                                                             units='s',group='Stimulation times')
        self.params['laserOnsetFromSoundOnset2'] = paramgui.NumericParam('Laser onset 2 (from sound)',value=0,
                                                             units='s',group='Stimulation times')
        self.params['laserOnsetFromSoundOnset3'] = paramgui.NumericParam('Laser onset 3 (from sound)',value=0.1,
                                                             units='s',group='Stimulation times')
        #self.params['laserOnsetFromCenterOut'] = paramgui.NumericParam('Laser onset 3 (from Cout)',value=0,
        #                                                     units='s',group='Stimulation times')
        self.params['nOnsetsToUse'] = paramgui.MenuParam('Onsets to use', 
                                                         ['0','1','2','3'],
                                                         value=0, group='Stimulation times')
        # -- Percent trials each laser type. Remaining trials will be no laser.
        self.params['fractionTrialsEachLaserMode'] = paramgui.NumericParam('Fraction trials each type',value=0.25,
                                                            units='',group='Stimulation times')
        '''
        self.params['stimFreq'] = paramgui.MenuParam('Stim Freq', 
                                                      ['continuous','20','5'],
                                                      value=0, group='Stimulation times',
                                                      enabled=False)
        self.params['stimMode'] = paramgui.MenuParam('Stim Mode',
                                                     ['Unilateral','Bilateral', 'Mixed'],
                                                     value=2,group='Stimulation times')
        '''
        photostimParams = self.params.layout_group('Stimulation times')


        # -- Generic session parameters --
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
        layoutCol2.addWidget(psychometricParams)
        layoutCol2.addStretch()

        layoutCol3.addWidget(timingParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(photostimParams)
        layoutCol3.addStretch()

        layoutCol4.addWidget(automationParams)
        layoutCol3.addStretch()
        layoutCol4.addWidget(soundParams)
        layoutCol3.addStretch()
        layoutCol4.addWidget(reportParams)
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
        '''
        highFreq = self.params['highFreq'].get_value()
        lowFreq = self.params['lowFreq'].get_value()
        stimDur = self.params['targetDuration'].get_value()
        s1 = {'type':'tone', 'frequency':lowFreq, 'duration':stimDur, 'amplitude':0.01}
        s2 = {'type':'tone', 'frequency':highFreq, 'duration':stimDur, 'amplitude':0.01}
        self.soundClient.set_sound(1,s1)
        self.soundClient.set_sound(2,s2)
        '''

        '''
        # This code was moved to the method prepare_punish_sound()
        punishSoundAmplitude = self.params['punishSoundAmplitude'].get_value()
        sNoise = {'type':'noise', 'duration':0.5, 'amplitude':punishSoundAmplitude}
        self.punishSoundID = 127
        self.soundClient.set_sound(self.punishSoundID,sNoise)
        '''
        self.punishSoundID = 127
        self.soundClient.start()

        # -- Prepare first trial --
        #self.prepare_next_trial(0)
       
    def prepare_punish_sound(self):
        punishSoundAmplitude = self.params['punishSoundAmplitude'].get_value()
        sNoise = {'type':'noise', 'duration':0.5, 'amplitude':punishSoundAmplitude}
        self.soundClient.set_sound(self.punishSoundID,sNoise)
        
    def prepare_target_sound(self,targetFrequency):
        if self.params['targetIntensityMode'].get_string() == 'randMinus20':
            possibleIntensities = self.params['targetMaxIntensity'].get_value()+\
                                  np.array([-20,-15,-10,-5,0])
            targetIntensity = possibleIntensities[np.random.randint(len(possibleIntensities))]
        else:
            targetIntensity = self.params['targetMaxIntensity'].get_value()
        self.params['targetIntensity'].set_value(targetIntensity)
                
        spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION)

        # FIXME: currently I am averaging calibration from both speakers (not good)
        targetAmp = spkCal.find_amplitude(targetFrequency,targetIntensity).mean()
        self.params['targetAmplitude'].set_value(targetAmp)

        stimDur = self.params['targetDuration'].get_value()
        s1 = {'type':'chord', 'frequency':targetFrequency, 'duration':stimDur,
              'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        self.soundClient.set_sound(1,s1)

        '''
        #amplitudeFactor = [0.25,0.5,1]
        #possibleAmplitudes = self.params['targetMaxAmplitude'].get_value()*np.array(amplitudeFactor)
        #targetAmplitude = possibleAmplitudes[np.random.randint(len(possibleAmplitudes))]

        #targetAmplitude = 0.01
        #self.params['targetAmplitude'].set_value(targetAmplitude)

        highFreq = self.params['highFreq'].get_value()
        midFreq = self.params['midFreq'].get_value()
        lowFreq = self.params['lowFreq'].get_value()
        stimDur = self.params['targetDuration'].get_value()
        
        spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION)
        ampLow = spkCal.find_amplitude(lowFreq,targetIntensity).mean()
        ampMid = spkCal.find_amplitude(midFreq,targetIntensity).mean()
        ampHigh = spkCal.find_amplitude(highFreq,targetIntensity).mean()
        
        self.params['targetAmplitudeLow'].set_value(ampLow)
        self.params['targetAmplitudeMid'].set_value(ampMid)
        self.params['targetAmplitudeHigh'].set_value(ampHigh)
        
        #s1 = {'type':'tone', 'frequency':lowFreq, 'duration':stimDur, 'amplitude':ampLow}
        #s2 = {'type':'tone', 'frequency':highFreq, 'duration':stimDur, 'amplitude':ampHigh}
        s1 = {'type':'chord', 'frequency':lowFreq, 'duration':stimDur,
              'amplitude':ampLow, 'ntones':12, 'factor':1.2}
        #s2 = {'type':'chord', 'frequency':highFreq, 'duration':stimDur,
        #      'amplitude':ampHigh, 'ntones':12, 'factor':1.2}
        self.soundClient.set_sound(1,s1)
        #self.soundClient.set_sound(2,s2)
        '''

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

        # === Prepare next trial ===
        self.execute_automation()
        nextCorrectChoice = self.results['rewardSide'][nextTrial]

        # -- Prepare sound --
        highFreq = self.params['highFreq'].get_value()
        #midFreq = self.params['midFreq'].get_value()
        lowFreq = self.params['lowFreq'].get_value()
        psycurveMode = self.params['psycurveMode'].get_string()
        if psycurveMode=='off':
            if nextCorrectChoice==self.results.labels['rewardSide']['left']:
                targetFrequency = lowFreq
            elif nextCorrectChoice==self.results.labels['rewardSide']['right']:
                targetFrequency = highFreq
        elif psycurveMode=='uniform':
            nFreqs = self.params['psycurveNfreq'].get_value()
            freqsAll = np.logspace(np.log10(lowFreq),np.log10(highFreq),nFreqs)
            freqBoundary = np.sqrt(lowFreq*highFreq)
            # -- NOTE: current implementation does not present points at the psych boundary -- 
            leftFreqInds = np.flatnonzero(freqsAll<freqBoundary)
            rightFreqInds = np.flatnonzero(freqsAll>freqBoundary)
            if nextCorrectChoice==self.results.labels['rewardSide']['left']:
                randindex = np.random.randint(len(freqsAll[leftFreqInds]))
                targetFrequency = freqsAll[leftFreqInds][randindex]
                #targetFrequency = np.random.choice(freqsAll[leftFreqInds])
            elif nextCorrectChoice==self.results.labels['rewardSide']['right']:
                randindex = np.random.randint(len(freqsAll[rightFreqInds]))
                targetFrequency = freqsAll[rightFreqInds][randindex]
                #targetFrequency = np.random.choice(freqsAll[rightFreqInds])
            pass
        self.params['targetFrequency'].set_value(targetFrequency)
        self.prepare_target_sound(targetFrequency)
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

        soundID = 1  # The appropriate sound has already been prepared and sent to server with ID=1
        targetDuration = self.params['targetDuration'].get_value()
        if rigsettings.OUTPUTS.has_key('outBit1'):
            trialStartOutput = ['outBit1'] # Sync signal for trial-start.
        else:
            trialStartOutput = []
        if rigsettings.OUTPUTS.has_key('outBit0'):
            stimOutput = ['outBit0'] # Sync signal for stimulus
        else:
            stimOutput = []

        '''
        #set laser trial type and laser output
        percentLaserTrialLeft = self.params['percentLaserTrialLeft'].get_value()
        percentLaserTrialRight = self.params['percentLaserTrialRight'].get_value()
        percentLaserTrials = percentLaserTrialLeft+percentLaserTrialRight
        laserTrialType = np.random.choice([0,1,2],size=1,p=[1-percentLaserTrials,percentLaserTrialLeft,percentLaserTrialRight])[0] #extract the first element of the resulting one-element numpy array
        #if laserTrialType: 
        laserFrontOverhang = self.params['laserFrontOverhang'].get_value()
        laserBackOverhang = self.params['laserBackOverhang'].get_value()
        if rigsettings.OUTPUTS.has_key('stim1') and rigsettings.OUTPUTS.has_key('stim2'):
            if laserTrialType==1:  #left laser on
                laserOutput = ['stim1'] #left laser 
                trialType='laser_left'
            elif laserTrialType==2: #right laser on
                laserOutput = ['stim2'] #right laser
                trialType='laser_right'
            elif laserTrialType==0: #no laser trial
                laserOutput = []
                trialType='no_laser'
        else: #In case rig output is not set up to present laser
            laserOutput = []
            trialType='no_laser'
        '''

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

        # -- Define times (delay to target, punishments, etc) --
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        delayToTarget = self.params['delayToTargetMean'].get_value() + \
            self.params['delayToTargetHalfRange'].get_value()*randNum
        self.params['delayToTarget'].set_value(delayToTarget)
        rewardAvailability = self.params['rewardAvailability'].get_value()
        punishTimeError = self.params['punishTimeError'].get_value()
        punishTimeEarly = self.params['punishTimeEarly'].get_value()

        # -- Define the type of trial to present --
        nOnsetsToUse = int(self.params['nOnsetsToUse'].get_string())
        fractionTrialsEachLaserMode = self.params['fractionTrialsEachLaserMode'].get_value()
        fractionTrialsLaser = np.tile(fractionTrialsEachLaserMode,nOnsetsToUse)
        fractionNoLaser = 1-np.sum(fractionTrialsLaser)
        fractionTrials = np.append(fractionNoLaser,fractionTrialsLaser)
        #np.random.choice(['no_laser','laser_onset1','laser_onset2','laser_onset3'],p=fractionTrials)
        trialTypeInd = np.random.choice(nOnsetsToUse+1, size=1, p=fractionTrials)[0]
        self.params['trialType'].set_value(trialTypeInd)
        if trialTypeInd>0:
            laserOutput = ['stim1']
        else:
            laserOutput = []
            
        possibleLaserOnsets = [np.nan,
                               self.params['laserOnsetFromSoundOnset1'].get_value(),
                               self.params['laserOnsetFromSoundOnset2'].get_value(),
                               self.params['laserOnsetFromSoundOnset3'].get_value()]
        laserDuration = self.params['laserDuration'].get_value()
        laserOnset = possibleLaserOnsets[trialTypeInd]  # Laser onset w.r.t sound onset
        self.params['laserOnset'].set_value(laserOnset)
        laserOffset = laserOnset+laserDuration          # Laser offset w.r.t sound onset

        if self.params['goSignalMode'].get_string()=='on-off':
            firstSignalTransitionOn = ['centerLED']
            firstSignalTransitionOff = []
            secondSignalTransitionOn = []
            secondSignalTransitionOff = ['centerLED']
        elif self.params['goSignalMode'].get_string()=='off-on':
            firstSignalTransitionOn = []
            firstSignalTransitionOff = ['centerLED']
            secondSignalTransitionOn = ['centerLED']
            secondSignalTransitionOff = []
        else:
            print 'This mode is not implemented'
            raise
        
        # -- Set state matrix --
        outcomeMode = self.params['outcomeMode'].get_string()
        if outcomeMode=='simulated':
            stimOutput.append(ledOutput)
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=1,
                              transitions={'Tup':'playStimulus'})
            self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                              transitions={'Tup':'reward'},
                              outputsOn=stimOutput,serialOut=soundID,
                              outputsOff=trialStartOutput)
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
                              transitions={'Cin':'playStimulus',correctSidePort:'playStimulus'},
                              outputsOn=firstSignalTransitionOn,
                              outputsOff=firstSignalTransitionOff)
            self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                              transitions={'Tup':'reward'},
                              serialOut=soundID,
                              outputsOn=stimOutput+secondSignalTransitionOn,
                              outputsOff=trialStartOutput+secondSignalTransitionOff)
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput],
                              outputsOff=stimOutput)
            self.sm.add_state(name='stopReward', statetimer=1,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput])
        elif outcomeMode=='direct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'playStimulus'},
                              outputsOn=['centerLED'])
            self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                              transitions={'Tup':'reward'},
                              outputsOn=stimOutput,serialOut=soundID,
                              outputsOff=trialStartOutput+['centerLED'])
            self.sm.add_state(name='reward', statetimer=rewardDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput],
                              outputsOff=stimOutput)
            self.sm.add_state(name='stopReward', statetimer=1,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput])
        elif outcomeMode=='on_next_correct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                              transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
            self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                              transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                              outputsOn=stimOutput, serialOut=soundID,
                              outputsOff=trialStartOutput)
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
            self.sm.add_state(name='earlyWithdrawal', statetimer=punishTimeEarly,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=stimOutput,serialOut=self.punishSoundID)
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

        # -----------------------------------------------------------------------------
        # Laser stim only works in 'only_if_correct' mode!
        # -----------------------------------------------------------------------------
        elif outcomeMode=='only_if_correct':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForCenterPoke'},
                              outputsOn=trialStartOutput)
            self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                              transitions={'Cin':'delayPeriod'},
                              outputsOff=laserOutput)


            if self.params['trialType'].get_string()=='no_laser':
                self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                                  transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
                self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                                  transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                                  outputsOn=stimOutput, serialOut=soundID,
                                  outputsOff=trialStartOutput)
                self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                  transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                               'Tup':'noChoice'},
                                  outputsOff=stimOutput)
            else:  # -- Trials with laser --

                # *** FIXME *** Make sure you solve the boundary conditions (<0 or <=0 ?)
                
                # NOTE: Santiago decided to make write each case separately for clarity,
                #       even though some states are the same across some conditions.
                # NOTE: We always need a state called "playStimulus" to be used calculate_results()
                #       This state sometimes corresponds to preLaser, duringLaser or postLaser.
                # NOTE: Similarly, we always need a state called "waitForSidePoke" right before the choice.
                #       This state sometimes corresponds to waitForSideDuringLaser.
                if (laserOnset<0) and (laserOffset<=0):
                    #  SOUND:  ........|XXXXXXX|........
                    #  LASER:  ...ooo...................
                    self.sm.add_state(name='delayPeriod', statetimer=delayToTarget+laserOnset,
                                      transitions={'Tup':'delayDuringLaser','Cout':'waitForCenterPoke'})
                    self.sm.add_state(name='delayDuringLaser', statetimer=laserDuration,
                                      transitions={'Tup':'delayPostLaser','Cout':'waitForCenterPoke'},
                                      outputsOn=laserOutput)
                    self.sm.add_state(name='delayPostLaser', statetimer=-laserOnset-laserDuration,
                                      transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'},
                                      outputsOff=laserOutput)
                    self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                                      transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                                      outputsOn=stimOutput, serialOut=soundID,
                                      outputsOff=trialStartOutput)
                    self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                      transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                                   'Tup':'noChoice'})
                elif (laserOnset<0) and (laserOffset<=targetDuration):
                    #  SOUND:  ........|XXXXXXX|........
                    #  LASER:  ...ooooooooo.............
                    self.sm.add_state(name='delayPeriod', statetimer=delayToTarget+laserOnset,
                                      transitions={'Tup':'delayDuringLaser','Cout':'waitForCenterPoke'})
                    self.sm.add_state(name='delayDuringLaser', statetimer=-laserOnset,
                                      transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'},
                                      outputsOn=laserOutput)
                    self.sm.add_state(name='playStimulus', statetimer=laserOffset,
                                      transitions={'Tup':'playStimPostLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=stimOutput, serialOut=soundID,
                                      outputsOff=trialStartOutput)
                    self.sm.add_state(name='playStimPostLaser', statetimer=targetDuration-laserOffset,
                                      transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                                      outputsOff=laserOutput)
                    self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                      transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                                   'Tup':'noChoice'})
                elif (laserOnset<0) and (laserOffset>targetDuration):
                    #  SOUND:  ........|XXXXXXX|........
                    #  LASER:  ....ooooooooooooooooo....
                    self.sm.add_state(name='delayPeriod', statetimer=delayToTarget+laserOnset,
                                      transitions={'Tup':'delayDuringLaser','Cout':'waitForCenterPoke'})
                    self.sm.add_state(name='delayDuringLaser', statetimer=-laserOnset,
                                      transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'},
                                      outputsOn=laserOutput)
                    self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                                      transitions={'Tup':'waitForSideDuringLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=stimOutput, serialOut=soundID,
                                      outputsOff=trialStartOutput)
                    self.sm.add_state(name='waitForSideDuringLaser', statetimer=laserOffset-targetDuration,
                                      transitions={'Tup':'waitForSidePoke'})
                    self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                      transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                                   'Tup':'noChoice'},
                                      outputsOff=laserOutput)
                elif (laserOnset>=0) and (laserOnset<=targetDuration) and (laserOffset<=targetDuration):
                    #  SOUND:  ........|XXXXXXX|........
                    #  LASER:  ..........oooo...........
                    self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                                      transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
                    self.sm.add_state(name='playStimulus', statetimer=laserOnset,
                                      transitions={'Tup':'playStimDuringLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=stimOutput, serialOut=soundID,
                                      outputsOff=trialStartOutput)
                    self.sm.add_state(name='playStimDuringLaser', statetimer=laserDuration,
                                      transitions={'Tup':'playStimPostLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=laserOutput)
                    self.sm.add_state(name='playStimPostLaser', statetimer=targetDuration-laserOffset,
                                      transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                                      outputsOff=laserOutput)
                    self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                      transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                                   'Tup':'noChoice'})
                elif (laserOnset>=0) and (laserOnset<=targetDuration) and (laserOffset>targetDuration):
                    #  SOUND:  ........|XXXXXXX|........
                    #  LASER:  ............oooooooooo...
                    self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                                      transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
                    self.sm.add_state(name='playStimulus', statetimer=laserOnset,
                                      transitions={'Tup':'playStimDuringLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=stimOutput, serialOut=soundID,
                                      outputsOff=trialStartOutput)
                    self.sm.add_state(name='playStimDuringLaser', statetimer=targetDuration-laserOnset,
                                      transitions={'Tup':'waitForSideDuringLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=laserOutput)
                    self.sm.add_state(name='waitForSideDuringLaser', statetimer=laserOffset-targetDuration,
                                      transitions={'Tup':'waitForSidePoke'})
                    self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                      transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                                   'Tup':'noChoice'},
                                      outputsOff=laserOutput)
                else:
                    #  SOUND:  ........|XXXXXXX|........
                    #  LASER:  ...................oooo..
                    self.sm.add_state(name='delayPeriod', statetimer=delayToTarget,
                                      transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
                    self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                                      transitions={'Tup':'waitForSidePreLaser','Cout':'earlyWithdrawal'},
                                      outputsOn=stimOutput, serialOut=soundID,
                                      outputsOff=trialStartOutput)
                    self.sm.add_state(name='waitForSidePreLaser', statetimer=laserOnset-targetDuration,
                                      transitions={'Tup':'waitForSideDuringLaser'})
                    self.sm.add_state(name='waitForSideDuringLaser', statetimer=laserDuration,
                                      transitions={'Tup':'waitForSidePoke'})
                    self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                      transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                                   'Tup':'noChoice'},
                                      outputsOff=laserOutput)
                    
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
            self.sm.add_state(name='earlyWithdrawal', statetimer=punishTimeEarly,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=stimOutput+laserOutput,serialOut=self.punishSoundID)
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


            '''
            if (laserFrontOverhang >= 0) & (laserBackOverhang >= 0):
                self.sm.add_state(name='startTrial', statetimer=0,
                                  transitions={'Tup':'waitForCenterPoke'},
                                  outputsOn=trialStartOutput)
                self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                                  transitions={'Cin':'delayPreLaser'},
                                  outputsOff=laserOutput)
                self.sm.add_state(name='delayPreLaser', statetimer=delayToTarget-laserFrontOverhang,
                                  transitions={'Tup':'delayPosLaser','Cout':'waitForCenterPoke'})
                self.sm.add_state(name='delayPosLaser', statetimer=laserFrontOverhang,
                                  transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'}, 
                                  outputsOn=laserOutput)

                # Note that 'delayPeriod' may happen several times in a trial, so
                # trialStartOutput off here would only meaningful for the first time in the trial.
                self.sm.add_state(name='playStimulus', statetimer=targetDuration,
                                  transitions={'Tup':'laserPosSound','Cout':'earlyWithdrawal'},
                                  outputsOn=stimOutput, serialOut=soundID,
                                  outputsOff=trialStartOutput)
                self.sm.add_state(name='laserPosSound', statetimer=laserBackOverhang,
                                  transitions={'Tup':'waitForSidePoke'},
                                  outputsOff=stimOutput) #The assumption here is that the mouse doesn't get to side port before Tup!
                self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                  transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                               'Tup':'noChoice'},
                                  outputsOff=laserOutput)

            elif (laserFrontOverhang < 0) & (laserBackOverhang >= 0):
                self.sm.add_state(name='startTrial', statetimer=0,
                                  transitions={'Tup':'waitForCenterPoke'},
                                  outputsOn=trialStartOutput)
                self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                                  transitions={'Cin':'delayPreLaser'})
                ###naming of this state is not ideal, it should be 'delayPeriod', this is a hack so that calculate_results works.
                self.sm.add_state(name='delayPreLaser', statetimer=delayToTarget,
                                  transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
                self.sm.add_state(name='playStimulus', statetimer=(-1*laserFrontOverhang),
                                  transitions={'Tup':'laserDuringSound','Cout':'earlyWithdrawal'},
                                  outputsOn=stimOutput, serialOut=soundID,
                                  outputsOff=trialStartOutput)
                
                self.sm.add_state(name='laserDuringSound', statetimer=targetDuration+laserFrontOverhang,
                                  transitions={'Tup':'laserPosSound','Cout':'earlyWithdrawal'},
                                  outputsOn=laserOutput)
                
                self.sm.add_state(name='laserPosSound', statetimer=laserBackOverhang,
                                  transitions={'Tup':'waitForSidePoke'}, 
                                  outputsOff=stimOutput) #The assumption here is that the mouse doesn't get to side port before Tup!

                self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                  transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                               'Tup':'noChoice'},
                                  outputsOff=laserOutput)

            elif (laserFrontOverhang >= 0) & (laserBackOverhang < 0):
                self.sm.add_state(name='startTrial', statetimer=0,
                                  transitions={'Tup':'waitForCenterPoke'},
                                  outputsOn=trialStartOutput)
                self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                                  transitions={'Cin':'delayPreLaser'},
                                  outputsOff=laserOutput)
                self.sm.add_state(name='delayPreLaser', statetimer=delayToTarget-laserFrontOverhang,
                                  transitions={'Tup':'delayPosLaser','Cout':'waitForCenterPoke'})
                self.sm.add_state(name='delayPosLaser', statetimer=laserFrontOverhang,
                                  transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'}, 
                                  outputsOn=laserOutput)

                self.sm.add_state(name='playStimulus', statetimer=targetDuration+laserBackOverhang,
                                  transitions={'Tup':'soundPosLaser','Cout':'earlyWithdrawal'},
                                  outputsOn=stimOutput, serialOut=soundID,
                                  outputsOff=trialStartOutput)

                self.sm.add_state(name='soundPosLaser', statetimer=(-1*laserBackOverhang),
                                  transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                                  outputsOff=laserOutput)

                self.sm.add_state(name='waitForSidePoke', statetimer=rewardAvailability,
                                  transitions={'Lin':'choiceLeft','Rin':'choiceRight',
                                               'Tup':'noChoice'},
                                  outputsOff=stimOutput)
            
            elif (laserFrontOverhang < 0) & (laserBackOverhang < 0):
                self.sm.add_state(name='startTrial', statetimer=0,
                                  transitions={'Tup':'waitForCenterPoke'},
                                  outputsOn=trialStartOutput)
                self.sm.add_state(name='waitForCenterPoke', statetimer=LONGTIME,
                                  transitions={'Cin':'delayPreLaser'})
                ###naming of this state is not ideal, it should be 'delayPeriod', this is a hack so that calculate_results works
                self.sm.add_state(name='delayPreLaser', statetimer=delayToTarget,
                                  transitions={'Tup':'playStimulus','Cout':'waitForCenterPoke'})
                self.sm.add_state(name='playStimulus', statetimer=(-1*laserFrontOverhang),
                                  transitions={'Tup':'laserDuringSound','Cout':'earlyWithdrawal'},
                                  outputsOn=stimOutput, serialOut=soundID,
                                  outputsOff=trialStartOutput)
                
                self.sm.add_state(name='laserDuringSound', statetimer=delayToTarget+laserFrontOverhang+laserBackOverhang,
                                  transitions={'Tup':'soundPosLaser','Cout':'earlyWithdrawal'},
                                  outputsOn=laserOutput)
                
                self.sm.add_state(name='soundPosLaser', statetimer=(-1*laserBackOverhang),
                                  transitions={'Tup':'waitForSidePoke','Cout':'earlyWithdrawal'},
                                  outputsOff=laserOutput)

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
            self.sm.add_state(name='earlyWithdrawal', statetimer=punishTimeEarly,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=stimOutput+laserOutput,
                              serialOut=self.punishSoundID)
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
        '''

            
        else:
            raise TypeError('outcomeMode={0} has not been implemented'.format(outcomeMode))
        print self.sm ### DEBUG
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
            targetStateID = self.sm.statesNameToIndex['playStimulus']
            targetEventInd = np.flatnonzero(statesThisTrial==targetStateID)[0]
            self.results['timeTarget'][trialIndex] = eventsThisTrial[targetEventInd,0]

            # -- Find center poke-in time --
            if outcomeModeString in ['only_if_correct']:
                seqCin = [self.sm.statesNameToIndex['waitForCenterPoke'],
                          self.sm.statesNameToIndex['delayPeriod'],
                          self.sm.statesNameToIndex['playStimulus']]
            elif outcomeModeString in ['on_next_correct']:
                seqCin = [self.sm.statesNameToIndex['waitForCenterPoke'],
                          self.sm.statesNameToIndex['delayPeriod'],
                          self.sm.statesNameToIndex['playStimulus']]
            elif outcomeModeString in ['simulated','sides_direct','direct']:
                seqCin = [self.sm.statesNameToIndex['waitForCenterPoke'],
                          self.sm.statesNameToIndex['playStimulus']]
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
                    if self.sm.statesNameToIndex['earlyWithdrawal'] in eventsThisTrial[:,2]:
                        self.results['outcome'][trialIndex] = \
                            self.results.labels['outcome']['invalid']
                    elif self.sm.statesNameToIndex['punish'] in eventsThisTrial[:,2]:
                        self.results['outcome'][trialIndex] = \
                            self.results.labels['outcome']['error']
            	# -- Check if it was a valid trial --
            	if self.sm.statesNameToIndex['waitForSidePoke'] in eventsThisTrial[:,2]:
                	self.params['nValid'].add(1)
                        self.results['valid'][trialIndex] = 1

    def execute_automation(self):
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


