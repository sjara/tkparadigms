"""
Two-alternative choice for head-fixed with two lick ports (right/left).
"""

import sys
import numpy as np
from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import utils
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
import time


LONGTIME = 100
MAX_N_TRIALS = 8000

PUNISHMENT_DURATION = 0.5

class Paradigm(QtWidgets.QMainWindow):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.name = 'detectiongonogo'

        # -- Create an empty statematrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS, outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Create dispatcher --
        smServerType = rigsettings.STATE_MACHINE_TYPE
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)

        # -- Module for saving data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR, remotedir=rigsettings.REMOTE_DIR)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)
        timeWaterValve = 0.03
        self.singleDrop = manualcontrol.SingleDrop(self.dispatcher.statemachine, timeWaterValve)
        
        # -- Define graphical parameters --
        self.params = paramgui.Container()
        self.params['trainer'] = paramgui.StringParam('Trainer (initials)',
                                                      value='',
                                                      group='Session info')
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                           value='experimenter',
                                                           group='Session info')
        self.params['subject'] = paramgui.StringParam('Subject',value='subject',
                                                      group='Session info')
        self.sessionInfo = self.params.layout_group('Session info')

        self.params['timeWaterValve'] = paramgui.NumericParam('Time valve',value=timeWaterValve,
                                                                units='s',group='Water delivery')
        #self.params['timeWaterValvesS'] = paramgui.NumericParam('Time valves S',value=0.03,
        #                                                        units='s',group='Water delivery')
        waterDelivery = self.params.layout_group('Water delivery')
       
        self.params['rewardAvailability'] = paramgui.NumericParam('Reward availability',value=1,
                                                        units='s',group='Timing parameters')
        self.params['interTrialIntervalMean'] = paramgui.NumericParam('ITI mean',value=2,
                                                        units='s',group='Timing parameters')
        self.params['interTrialIntervalHalfRange'] = paramgui.NumericParam('ITI +/-',value=0,
                                                        units='s',group='Timing parameters')
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter trial interval (ITI)',value=0,
                                                                  units='s',group='Timing parameters',
                                                                  decimals=3, enabled=False)
        self.params['preDurationMean'] = paramgui.NumericParam('Pre duration mean', value=1.0, units='s',
                                                              group='Timing parameters')
        self.params['preDurationHalfRange'] = paramgui.NumericParam('Pre duration +/-',
                                                                    value=0, units='s',
                                                                    group='Timing parameters')
        self.params['totalStimDuration'] = paramgui.NumericParam('Total duration', value=2.0, units='s',
                                                              group='Timing parameters')
        self.params['preDuration'] = paramgui.NumericParam('Pre duration', value=0, units='s',
                                                           group='Timing parameters', decimals=3,
                                                           enabled=False)
        self.params['postDuration'] = paramgui.NumericParam('Post duration', value=0, units='s',
                                                            group='Timing parameters', decimals=3,
                                                            enabled=False)
        self.params['fadeIn'] = paramgui.NumericParam('Fade in', value=1.0, units='s',
                                                       group='Timing parameters', decimals=3)
        timingParams = self.params.layout_group('Timing parameters')

        
        self.params['maxFreq'] = paramgui.NumericParam('Max frequency', value=13000, units='Hz',
                                                        group='Sound parameters')
        self.params['minFreq'] = paramgui.NumericParam('Min frequency', value=6000, units='Hz',
                                                        group='Sound parameters')
        self.params['nFreqs'] = paramgui.NumericParam('N frequencies', value=2, units='',
                                                        group='Sound parameters')
        self.params['minFreqRatio'] = paramgui.NumericParam('Min freq ratio', value=1.01, units='',
                                                        group='Sound parameters')
        self.params['preFreq'] = paramgui.NumericParam('Pre frequency', value=0,
                                                               decimals=0, units='Hz', enabled=False,
                                                               group='Sound parameters')
        self.params['postFreq'] = paramgui.NumericParam('Post frequency', value=0,
                                                               decimals=0, units='Hz', enabled=False,
                                                               group='Sound parameters')
        self.params['soundIntensity'] = paramgui.NumericParam('Sound intensity', value=50, units='dB-SPL',
                                                        enabled=True, group='Sound parameters')
        self.params['preSoundAmplitude'] = paramgui.NumericParam('Pre sound amplitude',value=0.0,
                                                                 units='[0-1]', enabled=False,
                                                                 decimals=4, group='Sound parameters')
        self.params['postSoundAmplitude'] = paramgui.NumericParam('Post sound amplitude',value=0.0,
                                                                  units='[0-1]',enabled=False,
                                                                  decimals=4, group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')

        '''
        self.params['rewardSideMode'] = paramgui.MenuParam('Reward side mode',
                                                           ['random','toggle','onlyL','onlyR'], value=0,
                                                           group='Choice parameters')
        self.params['rewardSide'] = paramgui.MenuParam('Reward side', ['left','right'], value=0,
                                                       enabled=False, group='Choice parameters')
        choiceParams = self.params.layout_group('Choice parameters')
        '''
        
        self.params['syncLight'] = paramgui.MenuParam('Sync light port',
                                                       ['off', 'leftLED', 'centerLED', 'rightLED'],
                                                       value=2, group='General parameters')
        self.params['activeLickPort'] = paramgui.MenuParam('Active lick port',
                                                       ['left', 'center', 'right'],
                                                       value=0, group='General parameters')
        self.params['punishMode'] = paramgui.MenuParam('Punishment',
                                                       ['none', 'noise'], enabled=False,
                                                       value=0, group='General parameters')
        self.params['punishIntensity'] = paramgui.NumericParam('Noise intensity',
                                                               value=60, units='dB-SPL',
                                                               group='General parameters')
        self.params['stimType'] = paramgui.MenuParam('Stim type',
                                                     ['sound_only', 'light_only','sound_and_light'],
                                                     value=0,group='General parameters',
                                                     enabled=False)
        '''
        self.params['psycurveMode'] = paramgui.MenuParam('PsyCurve Mode',
                                                         ['off','uniform'],
                                                         value=0,group='General parameters')
        self.params['psycurveNsteps'] = paramgui.NumericParam('N steps',value=6,decimals=0,
                                                              group='General parameters')
        '''
        self.params['taskMode'] = paramgui.MenuParam('Task mode',
                                                     ['water_on_lick','water_on_change',
                                                      'wait_for_change',
                                                      'lick_after_change'],
                                                     value=3, group='General parameters')
        generalParams = self.params.layout_group('General parameters')

        self.params['nHits'] = paramgui.NumericParam('Hits',value=0, enabled=False,
                                                             units='trials',group='Report')
        self.params['nFalseAlarms'] = paramgui.NumericParam('False alarms',value=0, enabled=False,
                                                            units='trials',group='Report')
        self.params['nMisses'] = paramgui.NumericParam('Misses',value=0, enabled=False,
                                                       units='trials',group='Report')
        self.params['nCorrectRejects'] = paramgui.NumericParam('Correct rejects',value=0, enabled=False,
                                                       units='trials',group='Report')
        self.params['nLicks'] = paramgui.NumericParam('Licks',value=0, enabled=False,
                                                      units='licks',group='Report')
        reportInfo = self.params.layout_group('Report')


        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.singleDrop)
        layoutCol1.addStretch()
        layoutCol1.addWidget(waterDelivery)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addStretch()
        layoutCol1.addWidget(reportInfo)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)

        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(timingParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(soundParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(generalParams)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = MAX_N_TRIALS # Preallocating space for each vector makes things easier
        self.results = utils.EnumContainer()
        self.results.labels['outcome'] = {'hit':1, 'error':0,'falseAlarm':3, 'miss':2, 'none':-1}
        self.results['outcome'] = np.empty(maxNtrials,dtype=int)
        #self.results.labels['choice'] = {'left':0,'right':1,'none':2}
        #self.results['choice'] = np.empty(maxNtrials,dtype=int)
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

        # -- Load speaker calibration --
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)

        # -- Connect to sound server and define sounds --
        print('Conecting to soundserver...')
        print('***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****') ### DEBUG
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.preSoundID = 1
        self.postSoundID = 2
        self.punishSoundID = 3
        self.soundClient.start()
      
        # -- Connect signals from dispatcher --
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect messenger --
        self.messagebar = paramgui.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect('Created window')

        # -- Connect signals to messenger
        self.saveData.logMessage.connect(self.messagebar.collect)
        self.dispatcher.logMessage.connect(self.messagebar.collect)

        # -- Connect other signals --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

    def _show_message(self,msg):
        self.statusBar().showMessage(str(msg))
        print(msg)

    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcher,
                               self.sm, self.results],
                              self.dispatcher.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def prepare_sounds(self):
        #targetFrequency = 6000
        soundIntensity = self.params['soundIntensity'].get_value()
        # FIXME: currently I am averaging calibration from both speakers (not good)
        preFreq = self.params['preFreq'].get_value()
        postFreq = self.params['postFreq'].get_value()
        preSoundAmp = self.spkCal.find_amplitude(preFreq,soundIntensity).mean()
        postSoundAmp = self.spkCal.find_amplitude(postFreq,soundIntensity).mean()
        self.params['preSoundAmplitude'].set_value(preSoundAmp)
        self.params['postSoundAmplitude'].set_value(postSoundAmp)
        preDuration = self.params['preDuration'].get_value()
        postDuration = self.params['postDuration'].get_value()
        fadeIn = self.params['fadeIn'].get_value()
        sPre = {'type':'chord', 'frequency':preFreq, 'ntones':12, 'factor':1.2,
                'duration':preDuration, 'amplitude':preSoundAmp, 'fadein':fadeIn}
        sPost = {'type':'chord', 'frequency':postFreq, 'ntones':12, 'factor':1.2,
                 'duration':postDuration, 'amplitude':postSoundAmp} #, 'delay':preDuration}
        self.soundClient.set_sound(self.preSoundID, sPre)
        self.soundClient.set_sound(self.postSoundID,sPost)

        # -- Prepare punishment noise --
        punishIntensity = self.params['punishIntensity'].get_value()
        targetAmp = self.noiseCal.find_amplitude(punishIntensity).mean()
        sNoise = {'type':'noise', 'duration': PUNISHMENT_DURATION, 'amplitude':targetAmp}
        self.soundClient.set_sound(self.punishSoundID,sNoise)
        
       
    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, etc) --
        if nextTrial>0:
            self.params.update_history(nextTrial-1)
            self.calculate_results(nextTrial-1)
            
        # -- Prepare next trial --
        taskMode = self.params['taskMode'].get_string()
        rewardAvailability = self.params['rewardAvailability'].get_value()
        timeWaterValve = self.params['timeWaterValve'].get_value()
        
        preDurationMean = self.params['preDurationMean'].get_value()
        preDurationHalfRange = self.params['preDurationHalfRange'].get_value()
        totalStimDuration = self.params['totalStimDuration'].get_value()
        randNum = (2*np.random.random(1)[0]-1)
        preDuration = preDurationMean + randNum*preDurationHalfRange
        self.params['preDuration'].set_value(preDuration)
        postDuration = self.params['totalStimDuration'].get_value() - preDuration
        self.params['postDuration'].set_value(postDuration)
        
        interTrialIntervalMean = self.params['interTrialIntervalMean'].get_value()
        interTrialIntervalHalfRange = self.params['interTrialIntervalHalfRange'].get_value()
        randNum = (2*np.random.random(1)[0]-1)
        interTrialInterval = interTrialIntervalMean + randNum*interTrialIntervalHalfRange
        self.params['interTrialInterval'].set_value(interTrialInterval)


        
        '''
        psycurveMode = self.params['psycurveMode'].get_string()
        lowFreq = self.params['lowFreq'].get_value()
        highFreq = self.params['highFreq'].get_value()
        nFreqs = self.params['psycurveNsteps'].get_value()
        freqsAll = np.logspace(np.log10(lowFreq),np.log10(highFreq),nFreqs)
        freqBoundary = np.sqrt(lowFreq*highFreq)
        leftFreqInds = np.flatnonzero(freqsAll<freqBoundary)
        rightFreqInds = np.flatnonzero(freqsAll>freqBoundary)
        '''

        maxFreq = self.params['maxFreq'].get_value()
        minFreq = self.params['minFreq'].get_value()
        nFreqs = self.params['nFreqs'].get_value()
        allFreq = np.logspace(np.log10(minFreq),np.log10(maxFreq),nFreqs)
        randPre = np.random.randint(nFreqs)  # Which sound will be the "pre" sound
        preFreq = allFreq[randPre]
        minRatio = self.params['minFreqRatio'].get_value() # Min ratio between pre and post frequency
        possiblePostBool = np.logical_or( (preFreq/allFreq)>=minRatio, (allFreq/preFreq)>=minRatio )
        possiblePostInds = np.flatnonzero(possiblePostBool)
        #print('=======================================')
        #print(possiblePostInds)
        if len(possiblePostInds)==0:
            self.dispatcher.widget.stop()
            raise ValueError('There are no frequencies in the set range far enough'+\
                             ' from {:0.0f} Hz given the min freq ratio.'.format(allFreq[randPre]))
        randPost = np.random.choice(possiblePostInds)
        #allFreq = [minFreq, maxFreq]
        #randPre = np.random.randint(2)  # Which sound will be the "pre" sound

        activePort = self.params['activeLickPort'].get_string()
        activeInput = activePort[0].upper()+'in'  # To produce Cin, Lin, Rin
        activeValve = activePort+'Water'
        activeLED = activePort+'LED'

        syncLightPortStr = self.params['syncLight'].get_string()
        if syncLightPortStr=='off':
            syncLightPort = []
        else:
            syncLightPort = [syncLightPortStr]

        catchTrial = False
        if catchTrial:
            postFreq = preFreq
            stateAfterPre = 'morePre'
            timeInWaitForLick = rewardAvailability
            timeInPost = postDuration
            timeInMorePost = 0
            stateAfterPost = 'waitForLick'
        else:
            postFreq = allFreq[randPost]
            stateAfterPre = 'playPost'
            timeInWaitForLick = max(0,rewardAvailability-postDuration)
            timeInMorePost = max(0,postDuration-rewardAvailability)
            timeInPost = postDuration-timeInMorePost
            if rewardAvailability > postDuration:
                # If rewardAvailability > postDuration, finish post and go to waitForLick
                stateAfterPost = 'waitForLick'
            else:
                # If rewardAvailability < postDuration, make post shorter
                # (but continue playing sound) and go to morePost (with no reward)
                stateAfterPost = 'morePost'

        if self.params['punishMode'].get_string()=='noise':
            stateAfterFA = 'punish'
        else:
            stateAfterFA = 'readyForNextTrial'
        
        self.params['preFreq'].set_value(preFreq)
        self.params['postFreq'].set_value(postFreq)
        self.prepare_sounds()

        self.sm.reset_transitions()
        if taskMode == 'water_on_lick':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForLick'},
                              outputsOff=[activeLED])
            self.sm.add_state(name='waitForLick', statetimer=LONGTIME,
                              transitions={activeInput:'preSound'})
            self.sm.add_state(name='preSound', statetimer=preDuration,
                              transitions={'Tup':'reward'},
                              serialOut=self.preSoundID)
            #self.sm.add_state(name='reward', statetimer=postDuration,
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'postSound'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='postSound', statetimer=postDuration,
                              transitions={'Tup':'stopReward'},
                              outputsOff=[activeValve],
                              serialOut=self.postSoundID)
            self.sm.add_state(name='stopReward', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'})
            # -- A few empty states necessary to avoid errors when changing taskMode --
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='miss')            
            self.sm.add_state(name='falseAlarm')
            self.sm.add_state(name='correctReject')            
        elif taskMode == 'water_on_change':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={'Tup':'playPre'})
            self.sm.add_state(name='playPre', statetimer=preDuration-timeWaterValve,
                              transitions={'Tup':'reward'},
                              serialOut=self.preSoundID)
            self.sm.add_state(name='playPost', statetimer=timeInPost,
                              transitions={'Tup':stateAfterPost},
                              outputsOn = syncLightPort,
                              serialOut=self.postSoundID)
            self.sm.add_state(name='morePost', statetimer=timeInMorePost,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'playPost'},
                              outputsOff=[activeValve])
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='miss')            
            self.sm.add_state(name='falseAlarm')
            self.sm.add_state(name='correctReject')            
        elif taskMode == 'wait_for_change':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={'Tup':'playPre', activeInput:'earlyResponse'})
            self.sm.add_state(name='earlyResponse', statetimer=0,
                              transitions={'Tup':'delayPeriod'})
            self.sm.add_state(name='playPre', statetimer=preDuration-timeWaterValve,
                              transitions={'Tup':'reward', activeInput:'falseAlarm'},
                              serialOut=self.preSoundID)
            self.sm.add_state(name='playPost', statetimer=timeInPost,
                              transitions={'Tup':stateAfterPost},
                              outputsOn = syncLightPort,
                              serialOut=self.postSoundID)
            self.sm.add_state(name='morePost', statetimer=timeInMorePost,
                              transitions={'Tup':'miss'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                              transitions={'Tup':'miss'})
            self.sm.add_state(name='falseAlarm', statetimer=0,
                              transitions={'Tup':stateAfterFA},
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='miss', statetimer=postDuration,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='punish', statetimer=PUNISHMENT_DURATION,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=['centerLED','rightLED','leftLED'],
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'playPost'},
                              outputsOff=[activeValve])
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='correctReject')            
        elif taskMode == 'lick_after_change':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={'Tup':'playPre', activeInput:'earlyResponse'})
            self.sm.add_state(name='earlyResponse', statetimer=0,
                              transitions={'Tup':'delayPeriod'})
            self.sm.add_state(name='playPre', statetimer=preDuration,
                              transitions={'Tup':stateAfterPre, activeInput:'falseAlarm'},
                              serialOut=self.preSoundID)
            self.sm.add_state(name='morePre', statetimer=postDuration,
                              transitions={'Tup':'waitForLick'},
                              serialOut=self.postSoundID)
            self.sm.add_state(name='playPost', statetimer=timeInPost,
                              transitions={activeInput:'hit', 'Tup':stateAfterPost},
                              outputsOn = syncLightPort,
                              serialOut=self.postSoundID)
            self.sm.add_state(name='morePost', statetimer=timeInMorePost,
                              outputsOff=['centerLED','rightLED','leftLED'],
                              transitions={'Tup':'miss'})
            self.sm.add_state(name='waitForLick', statetimer=timeInWaitForLick,
                              transitions={activeInput:'hit', 'Tup':'miss'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'},
                              outputsOff=['centerLED','rightLED','leftLED'],
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='falseAlarm', statetimer=0,
                              transitions={'Tup':stateAfterFA},
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='punish', statetimer=PUNISHMENT_DURATION,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=['centerLED','rightLED','leftLED'],
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[activeValve])
            self.sm.add_state(name='correctReject')            
        #print(self.sm) ### DEBUG
        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def calculate_results(self,trialIndex):
        # NOTE: Changes to graphical parameters (like nHits) are saved before calling
        #       this method. Therefore, those set here will be saved on the next trial.

        eventsThisTrial = self.dispatcher.events_one_trial(trialIndex)
        statesThisTrial = eventsThisTrial[:,2]
        if self.params['taskMode'].get_string() in ['lick_after_change', 'water_on_change',
                                                    'wait_for_change']:
            if self.sm.statesNameToIndex['hit'] in statesThisTrial:
                self.params['nHits'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
            elif self.sm.statesNameToIndex['falseAlarm'] in statesThisTrial:
                self.params['nFalseAlarms'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['falseAlarm']
            elif self.sm.statesNameToIndex['miss'] in statesThisTrial:
                self.params['nMisses'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
            else:
                # This may happen if changing from one taskMode to another
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
        else:
            # -- For any other task modes (like water_on_lick)
            self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
            
        # -- Estimate number of licks --
        eventCodesThisTrial = eventsThisTrial[:,1]
        activePort = self.params['activeLickPort'].get_string()
        activeInput = activePort[0].upper()+'in'  # To produce Cin, Lin, Rin
        nLicksThisTrial = np.sum(eventCodesThisTrial==self.sm.eventsDict[activeInput])
        self.params['nLicks'].add(nLicksThisTrial)
            
    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcher.die()
        event.accept()

if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)

