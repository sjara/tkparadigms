'''
Detect sound and lick to obtain reward. Used in head-fixed configuration.
'''

import time
import numpy as np
from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import utils
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import performancedynamicsplot
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration


LONGTIME = 100
MAX_N_TRIALS = 8000

if 'outBit1' in rigsettings.OUTPUTS:
    trialStartSync = ['outBit1'] # Sync signal for trial-start.
else:
    trialStartSync = []
if 'outBit0' in rigsettings.OUTPUTS:
    stimSync = ['outBit0'] # Sync signal for sound stimulus
else:
    stimSync = []

class Paradigm(QtWidgets.QMainWindow):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.name = 'detectsound'

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

        self.params['timeWaterValve'] = paramgui.NumericParam('Time valve',value=0.03,
                                                                units='s',group='Water delivery')
        #self.params['timeWaterValvesS'] = paramgui.NumericParam('Time valves S',value=0.03,
        #                                                        units='s',group='Water delivery')
        waterDelivery = self.params.layout_group('Water delivery')
       
        self.params['lickingPeriod'] = paramgui.NumericParam('Licking period',value=1.5,
                                                        units='s',group='Timing parameters')
        self.params['rewardAvailability'] = paramgui.NumericParam('Reward availability',value=1,
                                                        units='s',group='Timing parameters')
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter trial interval (ITI)',value=0,
                                                                  units='s',group='Timing parameters',
                                                                  decimals=3, enabled=False)
        self.params['interTrialIntervalMean'] = paramgui.NumericParam('ITI mean',value=3,
                                                        units='s',group='Timing parameters')
        self.params['interTrialIntervalHalfRange'] = paramgui.NumericParam('ITI +/-',value=1,
                                                        units='s',group='Timing parameters')
        #self.params['punishTimeOut'] = paramgui.NumericParam('Time out (punish)',value=1,
        #                                                units='s',group='Timing parameters')
        #self.params['timeLEDon'] = paramgui.NumericParam('Time LED on',value=1,
        #                                                units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')

        self.params['stimDuration'] = paramgui.NumericParam('Stim duration',value=0.2, units='s',
                                                              group='Sound parameters')
        self.params['targetFrequency'] = paramgui.NumericParam('Target frequency',value=9000, units='Hz',
                                                              group='Sound parameters')
        self.params['distractorFreqDelta'] = paramgui.NumericParam('Distractors freq delta',value=1.2,
                                                                   units='octaves',
                                                                   enabled=True, group='Sound parameters')
        self.params['stimFrequency'] = paramgui.NumericParam('Stim frequency',value=9000, units='Hz',
                                                              group='Sound parameters', enabled=False,
                                                              decimals=1)
        self.params['stimIntensity'] = paramgui.NumericParam('Stim intensity',value=50, units='dB-SPL',
                                                        enabled=True, group='Sound parameters')
        self.params['stimAmplitude'] = paramgui.NumericParam('Stim amplitude',value=0.0,units='[0-1]',
                                                        enabled=False,decimals=4,group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')

        self.params['punishmentType'] = paramgui.MenuParam('Punishment type',
                                                           ['none','noise'],
                                                           value=0, group='Punishment parameters')
        self.params['punishmentIntensity'] = paramgui.NumericParam('Punishment intensity',value=50,
                                                              units='dB-SPL',enabled=True,
                                                              group='Punishment parameters')
        self.params['punishmentDuration'] = paramgui.NumericParam('Punishment duration',value=0.3,
                                                                  units='s', group='Punishment parameters')
        punishmentParams = self.params.layout_group('Punishment parameters')
        
        self.params['taskMode'] = paramgui.MenuParam('Task mode', ['water_after_sound', 'detect_single_sound',
                                                                   'detect_with_distractors',
                                                                   'water_on_lick'],
                                                     value=0, group='General parameters')
        self.params['distractorType'] = paramgui.MenuParam('Distractor type',
                                                           ['lower','higher','lower_and_higher'],
                                                           value=0, group='General parameters')
        self.params['targetTrialRatio'] = paramgui.NumericParam('Target trial ratio',value=0.5,
                                                                enabled=True, group='General parameters')
        self.params['activeLickPort'] = paramgui.MenuParam('Active lick port',
                                                           ['left', 'center', 'right'],
                                                           value=0, group='General parameters')
        self.params['lightMode'] = paramgui.MenuParam('Light mode', ['none','center','all'], value=0,
                                                      group='General parameters', enabled=False)
        self.params['soundType'] = paramgui.MenuParam('Sound type', ['chord', 'tone'], enabled=True, 
                                                      value=0,group='General parameters')
        generalParams = self.params.layout_group('General parameters')

        self.params['nHits'] = paramgui.NumericParam('N hits',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nMisses'] = paramgui.NumericParam('N misses',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nFalseAlarms'] = paramgui.NumericParam('N false alarms',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nCorrectRejects'] = paramgui.NumericParam('N correct rejects',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nEarlyLicks'] = paramgui.NumericParam('N early licks',value=0, enabled=False,
                                                      units='trials',group='Report')
        reportInfo = self.params.layout_group('Report')


        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()
        layoutCol3 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addStretch()
        layoutCol1.addWidget(reportInfo)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)

        layoutCol2.addWidget(self.singleDrop)
        layoutCol2.addStretch()
        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(waterDelivery)
        layoutCol2.addStretch()
        layoutCol2.addWidget(timingParams)
        #layoutCol3.addStretch()

        layoutCol3.addWidget(soundParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(punishmentParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(generalParams)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = MAX_N_TRIALS # Preallocating space for each vector makes things easier
        self.results = utils.EnumContainer()
        self.results.labels['outcome'] = {'hit':1, 'falseAlarm':0, 'miss':2, 'correctReject':3,
                                          'earlyLick':4, 'none':-1}
        self.results['outcome'] = np.empty(maxNtrials, dtype=int)
        self.results['timeTrialStart'] = np.empty(maxNtrials, dtype=float)
        self.results['timeStim'] = np.empty(maxNtrials, dtype=float)
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

        # -- Load speaker calibration --
        self.sineCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_SINE)
        self.chordCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)

        # -- Connect to sound server and define sounds --
        #print('Conecting to soundserver...')
        #print('***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****') ### DEBUG
        #time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.stimSoundID = 1
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

    def prepare_sound(self):
        stimFrequency = self.params['stimFrequency'].get_value()
        stimIntensity = self.params['stimIntensity'].get_value()
        stimDuration = self.params['stimDuration'].get_value()
        soundType = self.params['soundType'].get_string()
        # FIXME: currently I am averaging calibration from both speakers (not good)
        if soundType == 'chord':
            stimAmp = self.chordCal.find_amplitude(stimFrequency,stimIntensity).mean()
            self.params['stimAmplitude'].set_value(stimAmp)
            s1 = {'type':'chord', 'frequency':stimFrequency, 'duration':stimDuration,
                  'amplitude':stimAmp, 'ntones':12, 'factor':1.2}
        elif soundType == 'tone':    
            stimAmp = self.sineCal.find_amplitude(stimFrequency,stimIntensity).mean()
            self.params['stimAmplitude'].set_value(stimAmp)
            s1 = {'type':'tone', 'frequency':stimFrequency, 'duration':stimDuration,
                  'amplitude':stimAmp}
        self.soundClient.set_sound(self.stimSoundID,s1)

        # -- Prepare punishment sound --
        punishmentIntensity = self.params['punishmentIntensity'].get_value()
        punishmentDuration = self.params['punishmentDuration'].get_value()
        punishmentAmp = self.noiseCal.find_amplitude(punishmentIntensity).mean()
        s3 = {'type':'noise', 'duration':punishmentDuration, 'amplitude':punishmentAmp} 
        self.soundClient.set_sound(self.punishSoundID, s3)         

        
    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.params.update_history(nextTrial-1)
            self.calculate_results(nextTrial-1)
            
        # -- Prepare next trial --
        taskMode = self.params['taskMode'].get_string()
        punishmentType = self.params['punishmentType'].get_string() # For false alarms
        targetTrialRatio = self.params['targetTrialRatio'].get_value()
        rewardAvailability = self.params['rewardAvailability'].get_value()
        stimDuration = self.params['stimDuration'].get_value()
        timeWaterValve = self.params['timeWaterValve'].get_value()
        interTrialIntervalMean = self.params['interTrialIntervalMean'].get_value()
        interTrialIntervalHalfRange = self.params['interTrialIntervalHalfRange'].get_value()
        randNum = (2*np.random.random(1)[0]-1)
        interTrialInterval = interTrialIntervalMean + randNum*interTrialIntervalHalfRange
        lickingPeriod = self.params['lickingPeriod'].get_value()
        self.params['interTrialInterval'].set_value(interTrialInterval)

        activePort = self.params['activeLickPort'].get_string()
        self.activeInput = activePort[0].upper()+'in'  # To produce Cin, Lin, Rin
        activeValve = activePort+'Water'
        activeLED = activePort+'LED'

        lightMode = self.params['lightMode'].get_string()
        if lightMode=='none':
            lightOutput = ['']
        if lightMode=='center':
            lightOutput = ['centerLED']
        elif lightMode=='all':
            lightOutput = ['centerLED', 'leftLED','rightLED']

        targetTrial = (np.random.random(1)[0] < targetTrialRatio)

        # -- Define which sound to present --
        targetFrequency = self.params['targetFrequency'].get_value()
        distractorFreqDelta = self.params['distractorFreqDelta'].get_value()
        distractorType = self.params['distractorType'].get_string()
        if taskMode in ['water_after_sound', 'detect_single_sound']:
            stimFrequency = targetFrequency
        elif taskMode == 'detect_with_distractors':
            if targetTrial:
                stimFrequency = targetFrequency
            else:
                distractorPossibleFreq = [targetFrequency / (2**distractorFreqDelta),
                                          targetFrequency * (2**distractorFreqDelta)]
                if distractorType == 'lower':
                    distractorInd = 0
                elif distractorType == 'higher':
                    distractorInd = 1
                elif distractorType == 'lower_and_higher':
                    distractorInd = np.random.randint(2)
                stimFrequency = distractorPossibleFreq[distractorInd]
        self.params['stimFrequency'].set_value(stimFrequency)
        
        self.prepare_sound()
        soundOutput = self.stimSoundID
        
        self.sm.reset_transitions()

        if taskMode == 'water_after_sound':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={self.activeInput: 'earlyLick', 'Tup':'playStim'})
            self.sm.add_state(name='playStim', statetimer=stimDuration,
                              transitions={'Tup':'reward'},
                              serialOut=soundOutput)            
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=[activeValve])
            self.sm.add_state(name='lickingPeriod', statetimer=lickingPeriod,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='earlyLick', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            # -- A few empty states necessary to avoid errors when changing taskMode --
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='miss')            
            self.sm.add_state(name='falseAlarm')            
            self.sm.add_state(name='correctReject')            
        elif taskMode == 'detect_single_sound':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={self.activeInput:'earlyLick', 'Tup':'playStim'})
            self.sm.add_state(name='playStim', statetimer=stimDuration,
                              transitions={self.activeInput:'hit', 'Tup':'waitForLick'},
                              serialOut=soundOutput)
            self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                              transitions={self.activeInput:'hit', 'Tup':'miss'})
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'})            
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='earlyLick', statetimer=0,
                              transitions={'Tup':'lickingPeriod'})            
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=[activeValve])
            self.sm.add_state(name='lickingPeriod', statetimer=lickingPeriod,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='falseAlarm')            
            self.sm.add_state(name='correctReject')            
        elif taskMode == 'detect_with_distractors':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={self.activeInput:'earlyLick', 'Tup':'playStim'})
            if targetTrial:
                self.sm.add_state(name='playStim', statetimer=stimDuration,
                                  transitions={self.activeInput:'hit', 'Tup':'waitForLick'},
                                  serialOut=soundOutput)
                self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                                  transitions={self.activeInput:'hit', 'Tup':'miss'})
            else:
                self.sm.add_state(name='playStim', statetimer=stimDuration,
                                  transitions={self.activeInput:'falseAlarm', 'Tup':'waitForLick'},
                                  serialOut=soundOutput)
                self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                                  transitions={self.activeInput:'falseAlarm', 'Tup':'correctReject'})
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'})            
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='earlyLick', statetimer=0,
                              transitions={'Tup':'lickingPeriod'})
            if punishmentType == 'noise':
                self.sm.add_state(name='falseAlarm', statetimer=0,
                                  transitions={'Tup':'punishment'})            
            else:
                self.sm.add_state(name='falseAlarm', statetimer=0,
                                  transitions={'Tup':'lickingPeriod'})            
            self.sm.add_state(name='correctReject', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=[activeValve])
            self.sm.add_state(name='punishment', statetimer=0.5,
                              transitions={'Tup':'lickingPeriod'}, serialOut=self.punishSoundID)
            self.sm.add_state(name='lickingPeriod', statetimer=lickingPeriod,
                              transitions={'Tup':'readyForNextTrial'})
        if taskMode == 'water_on_lick':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForLick'},
                              outputsOff=['centerLED'])
            self.sm.add_state(name='waitForLick', statetimer=LONGTIME,
                              transitions={'Cin':'reward'})
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[activeValve],
                              serialOut=soundOutput)
            self.sm.add_state(name='stopReward', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[activeValve])
            # -- A few empty states necessary to avoid errors when changing taskMode --
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='miss')            
            self.sm.add_state(name='falseAlarm')            


        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def calculate_results(self,trialIndex):
        taskMode = self.params['taskMode'].get_string()
        eventsThisTrial = self.dispatcher.events_one_trial(trialIndex)
        statesThisTrial = eventsThisTrial[:,2]

        # -- Find beginning of trial --
        startTrialStateID = self.sm.statesNameToIndex['startTrial']
        startTrialInd = np.flatnonzero(statesThisTrial==startTrialStateID)[0]
        self.results['timeTrialStart'][trialIndex] = eventsThisTrial[startTrialInd,0]
        # -- Find time of stim --
        lastEvent = eventsThisTrial[-1,:]
        if lastEvent[1]==-1 and lastEvent[2]==0: # Check if aborted trial
            self.results['timeStim'][trialIndex] = np.nan
        else:
            stimStateID = self.sm.statesNameToIndex['playStim']
            if stimStateID in statesThisTrial:
                stimEventInd = np.flatnonzero(statesThisTrial==stimStateID)[0]
                self.results['timeStim'][trialIndex] = eventsThisTrial[stimEventInd,0]
            else:
                self.results['timeStim'][trialIndex] = np.nan
        
        if taskMode == 'water_after_sound':
            if self.sm.statesNameToIndex['reward'] in statesThisTrial:
               if self.sm.eventsDict[self.activeInput] in eventsThisTrial[:,1]:
                   self.params['nHits'].add(1)
                   self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
               else:
                   self.params['nMisses'].add(1)
                   self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
            elif self.sm.statesNameToIndex['earlyLick'] in statesThisTrial:
                self.params['nEarlyLicks'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['earlyLick']
            else:
                # This should not happen
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
        elif taskMode == 'detect_single_sound':
            if self.sm.statesNameToIndex['hit'] in statesThisTrial:
                self.params['nHits'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
            elif self.sm.statesNameToIndex['miss'] in statesThisTrial:
                self.params['nMisses'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
            elif self.sm.statesNameToIndex['earlyLick'] in statesThisTrial:
                self.params['nEarlyLicks'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['earlyLick']
            else:
                # This should not happen
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
        elif taskMode == 'detect_with_distractors':
            # NOTE: this could be merged with the mode above
            if self.sm.statesNameToIndex['hit'] in statesThisTrial:
                self.params['nHits'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
            elif self.sm.statesNameToIndex['miss'] in statesThisTrial:
                self.params['nMisses'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
            elif self.sm.statesNameToIndex['earlyLick'] in statesThisTrial:
                self.params['nEarlyLicks'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['earlyLick']
            elif self.sm.statesNameToIndex['falseAlarm'] in statesThisTrial:
                self.params['nFalseAlarms'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['falseAlarm']
            elif self.sm.statesNameToIndex['correctReject'] in statesThisTrial:
                self.params['nCorrectRejects'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['correctReject']
            else:
                # This should not happen
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
        
    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtWidgets.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcher.die()
        event.accept()

if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)

