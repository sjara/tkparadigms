'''
Detect sound and lick to obtain reward. Used in head-fixed configuration.
'''

import numpy as np
from PySide import QtGui 
from taskontrol.core import dispatcher
from taskontrol.core import statematrix
from taskontrol.core import savedata
from taskontrol.core import paramgui
from taskontrol.core import messenger
from taskontrol.core import arraycontainer
from taskontrol.plugins import manualcontrol
from taskontrol.settings import rigsettings

from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
import time


LONGTIME = 100
MAX_N_TRIALS = 4000

class Paradigm(QtGui.QMainWindow):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.name = 'detectsound'

        # -- Create an empty statematrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS, outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Create dispatcher --
        smServerType = rigsettings.STATE_MACHINE_TYPE
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)
        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Module for saving data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR, remotedir=rigsettings.REMOTE_DIR)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcherModel.statemachine)
        
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
       
        self.params['rewardAvailability'] = paramgui.NumericParam('Reward availability',value=1,
                                                        units='s',group='Timing parameters')
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter trial interval (ITI)',value=0,
                                                                  units='s',group='Timing parameters',
                                                                  decimals=3, enabled=False)
        self.params['interTrialIntervalMean'] = paramgui.NumericParam('ITI mean',value=4,
                                                        units='s',group='Timing parameters')
        self.params['interTrialIntervalHalfRange'] = paramgui.NumericParam('ITI +/-',value=2,
                                                        units='s',group='Timing parameters')
        #self.params['punishTimeOut'] = paramgui.NumericParam('Time out (punish)',value=1,
        #                                                units='s',group='Timing parameters')
        #self.params['timeLEDon'] = paramgui.NumericParam('Time LED on',value=1,
        #                                                units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')

        self.params['targetDuration'] = paramgui.NumericParam('Target duration',value=0.2, units='s',
                                                              group='Sound parameters')
        self.params['targetIntensity'] = paramgui.NumericParam('Target intensity',value=50, units='dB-SPL',
                                                        enabled=True, group='Sound parameters')
        self.params['targetAmplitude'] = paramgui.NumericParam('Target amplitude',value=0.0,units='[0-1]',
                                                        enabled=False,decimals=4,group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')
        
        self.params['taskMode'] = paramgui.MenuParam('Task mode', ['water_on_lick','detect_sound'], value=0,
                                                     group='General parameters')
        generalParams = self.params.layout_group('General parameters')

        self.params['nHits'] = paramgui.NumericParam('N hits',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nMisses'] = paramgui.NumericParam('N misses',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nFalseAlarms'] = paramgui.NumericParam('N false alarms',value=0, enabled=False,
                                                      units='trials',group='Report')
        reportInfo = self.params.layout_group('Report')


        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout()
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(reportInfo)
        layoutCol1.addWidget(self.dispatcherView)

        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(waterDelivery)
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
        self.results = arraycontainer.Container()
        self.results.labels['outcome'] = {'hit':1,'falseAlarm':0, 'miss':2, 'none':-1}
        self.results['outcome'] = np.empty(maxNtrials,dtype=int)
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

        # -- Load speaker calibration --
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)

        # -- Connect to sound server and define sounds --
        print 'Conecting to soundserver...'
        print '***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****' ### DEBUG
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.targetSoundID = 1
        self.soundClient.start()
      
        # -- Connect signals from dispatcher --
        self.dispatcherModel.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect messenger --
        self.messagebar = messenger.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect('Created window')

        # -- Connect signals to messenger
        self.saveData.logMessage.connect(self.messagebar.collect)
        self.dispatcherModel.logMessage.connect(self.messagebar.collect)

        # -- Connect other signals --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

    def _show_message(self,msg):
        self.statusBar().showMessage(str(msg))
        print msg

    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcherModel,
                               self.sm, self.results],
                              self.dispatcherModel.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def prepare_target_sound(self):
        targetFrequency = 6000
        targetIntensity = self.params['targetIntensity'].get_value()
        targetDuration = self.params['targetDuration'].get_value()
        # FIXME: currently I am averaging calibration from both speakers (not good)
        targetAmp = self.spkCal.find_amplitude(targetFrequency,targetIntensity).mean()
        self.params['targetAmplitude'].set_value(targetAmp)
        s1 = {'type':'chord', 'frequency':targetFrequency, 'duration':targetDuration,
              'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        self.soundClient.set_sound(self.targetSoundID,s1)

        
    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.params.update_history()
            self.calculate_results(nextTrial-1)
            
        # -- Prepare next trial --
        taskMode = self.params['taskMode'].get_string()
        rewardAvailability = self.params['rewardAvailability'].get_value()
        targetDuration = self.params['targetDuration'].get_value()
        timeWaterValve = self.params['timeWaterValve'].get_value()
        interTrialIntervalMean = self.params['interTrialIntervalMean'].get_value()
        interTrialIntervalHalfRange = self.params['interTrialIntervalHalfRange'].get_value()
        randNum = (2*np.random.random(1)[0]-1)
        interTrialInterval = interTrialIntervalMean + randNum*interTrialIntervalHalfRange
        self.params['interTrialInterval'].set_value(interTrialInterval)
        
        self.sm.reset_transitions()

        if taskMode == 'water_on_lick':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForLick'},
                              outputsOff=['centerLED'])
            self.sm.add_state(name='waitForLick', statetimer=LONGTIME,
                              transitions={'Cin':'reward'})
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=['centerWater','centerLED'],
                              serialOut=self.targetSoundID)
            self.sm.add_state(name='stopReward', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=['centerWater','centerLED'])
        elif taskMode == 'detect_sound':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'},
                              outputsOff=['centerLED'])
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={'Cin':'falseAlarm', 'Tup':'playTarget'})
            self.sm.add_state(name='playTarget', statetimer=targetDuration,
                              transitions={'Cin':'hit', 'Tup':'waitForLick'},
                              outputsOn=['centerLED'],
                              serialOut=self.targetSoundID)
            self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                              transitions={'Cin':'hit', 'Tup':'miss'},
                              outputsOff=['centerLED'])
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'},
                              outputsOff=['centerLED'])            
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='falseAlarm', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})            
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=['centerWater'])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=['centerWater'])


        self.prepare_target_sound()
        
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()

    def calculate_results(self,trialIndex):
        if self.params['taskMode'].get_string()=='detect_sound':
            eventsThisTrial = self.dispatcherModel.events_one_trial(trialIndex)
            statesThisTrial = eventsThisTrial[:,2]
            if self.sm.statesNameToIndex['hit'] in statesThisTrial:
                self.params['nHits'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
            elif self.sm.statesNameToIndex['miss'] in statesThisTrial:
                self.params['nMisses'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
            elif self.sm.statesNameToIndex['falseAlarm'] in statesThisTrial:
                self.params['nFalseAlarms'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['falseAlarm']
            else:
                # This should not happen
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
        
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

