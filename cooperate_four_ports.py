'''
Cooperate_four_ports is a paradigm in which two animals must poke simultaneously to obtain reward.
There are two lanes (one for each animal) with one port at each end.

TO DO:
- Store timing of pokes on the wrong side.

'''

import numpy as np
from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import utils
from taskontrol.plugins import manualcontrol

LONGTIME = 100
MAX_N_TRIALS = 4000

class Paradigm(QtWidgets.QMainWindow):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.name = 'coop4ports'

        # -- Create an empty statematrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS, outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial',
                                          extratimers=['lightTimer1','lightTimer2'])

        # -- Create dispatcher --
        smServerType = rigsettings.STATE_MACHINE_TYPE
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)

        # -- Module for saving data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR, remotedir=rigsettings.REMOTE_DIR)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)
        
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

        self.params['timeWaterValves'] = paramgui.NumericParam('Time valves',value=0.03,
                                                                units='s',group='Water delivery')
        #self.params['timeWaterValvesN'] = paramgui.NumericParam('Time valves N',value=0.03,
        #                                                        units='s',group='Water delivery')
        #self.params['timeWaterValvesS'] = paramgui.NumericParam('Time valves S',value=0.03,
        #                                                        units='s',group='Water delivery')
        waterDelivery = self.params.layout_group('Water delivery')
       
        self.params['waitTime'] = paramgui.NumericParam('Wait time',value=3,
                                                        units='s',group='Timing parameters')
        #self.params['timeLEDon'] = paramgui.NumericParam('Time LED on',value=3,
        #                                                 units='s',group='Timing parameters',
        #                                                 enabled=False)
        self.params['ITI'] = paramgui.NumericParam('Inter-trial interval',value=0,
                                                   units='s',group='Timing parameters',
                                                   enabled=True)
        timingParams = self.params.layout_group('Timing parameters')
        self.params['barrierType'] = paramgui.MenuParam('Barrier type', ['perforated','solid',
                                                                         'transparent','no_barrier'],
                                                        value=0, group='General parameters')
        self.params['activeSide'] = paramgui.MenuParam('Active side', ['north','south'], value=0,
                                                        group='General parameters', enabled=False)
        self.params['taskMode'] = paramgui.MenuParam('Task mode', ['one_track','auto_lights',
                                                                   'reward_on_first_poke',
                                                                   'reward_on_last_poke',
                                                                   'cooperate'],
                                                     value=1, group='General parameters')
        self.params['nextPortAfterFail'] = paramgui.MenuParam('Next port after fail',
                                                              ['same','opposite'], value=1,
                                                              group='General parameters', enabled=False)
        generalParams = self.params.layout_group('General parameters')

        self.params['nRewarded1'] = paramgui.NumericParam('N trials rewarded T1',value=0, enabled=False,
                                                         units='trials',group='Report')
        self.params['nRewarded2'] = paramgui.NumericParam('N trials rewarded T2',value=0, enabled=False,
                                                         units='trials',group='Report')
        reportInfo = self.params.layout_group('Report')
        

        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(reportInfo)
        layoutCol1.addWidget(self.dispatcher.widget)

        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(waterDelivery)
        layoutCol2.addStretch()
        layoutCol2.addWidget(timingParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(generalParams)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = MAX_N_TRIALS # Preallocating space for each vector makes things easier
        self.results = utils.EnumContainer()
        self.results.labels['outcome'] = {'aborted':0, 'rewardedBoth':1, 'poke1only':2, 'poke2only':3, 'none':4}
        self.results['outcome'] = np.empty(maxNtrials, dtype=int)
        self.results['timePoke1'] = np.empty(maxNtrials, dtype=float)
        self.results['timePoke2'] = np.empty(maxNtrials, dtype=float)
        #self.results.labels['activeSide'] = {'north':0,'south':1}
        #self.results['activeSide'] = np.empty(maxNtrials,dtype=int)
        #self.results['activeSide'][0] = 0
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

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

    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.params.update_history(nextTrial-1)
            self.calculate_results(nextTrial-1)
            previousOutcome = self.results['outcome'][nextTrial-1]
        else:
            previousOutcome = self.results.labels['outcome']['rewardedBoth']
            
        # -- Prepare next trial --
        taskMode = self.params['taskMode'].get_string()
        nextPortAfterFail = self.params['nextPortAfterFail'].get_string()
        waitTime = self.params['waitTime'].get_value()
        #timeLEDon = self.params['timeLEDon'].get_value()
        interTrialInterval = self.params['ITI'].get_value()
        timeWaterValves = self.params['timeWaterValves'].get_value()
        #timeWaterValvesN = self.params['timeWaterValvesN'].get_value()
        #timeWaterValvesS = self.params['timeWaterValvesS'].get_value()
        activeSide = self.params['activeSide'].get_string()
        
        self.sm.reset_transitions()

        if (activeSide=='north'):
            port1in = 'S1in'; port2in = 'S2in'
            LED1 = 'S1LED'; LED2 = 'S2LED'
            Water1 = 'S1Water'; Water2 = 'S2Water'
            #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
            self.params['activeSide'].set_string('south')
        if (activeSide=='south'):
            port1in = 'N1in'; port2in = 'N2in'
            LED1 = 'N1LED'; LED2 = 'N2LED'
            Water1 = 'N1Water'; Water2 = 'N2Water'
            #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
            self.params['activeSide'].set_string('north')
            
        '''
        switchActiveSide = (previousOutcome==self.results.labels['outcome']['rewarded'])

        if (activeSide=='south' and switchActiveSide) or (activeSide=='north' and not switchActiveSide):
            port1in = 'N1in'; port2in = 'N2in'
            LED1 = 'N1LED'; LED2 = 'N2LED'
            Water1 = 'N1Water'; Water2 = 'N2Water'
            #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
            self.params['activeSide'].set_string('north')
        elif (activeSide=='north' and switchActiveSide) or (activeSide=='south' and not switchActiveSide):
            port1in = 'S1in'; port2in = 'S2in'
            LED1 = 'S1LED'; LED2 = 'S2LED'
            Water1 = 'S1Water'; Water2 = 'S2Water'
            #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['north']
            self.params['activeSide'].set_string('south')
        else:
            raise
        '''

        if taskMode == 'one_track':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForPoke'},
                              outputsOff=[LED1, LED2])
            self.sm.add_state(name='waitForPoke', statetimer=LONGTIME,
                              transitions={port1in:'reward', port2in:'reward'})
            self.sm.add_state(name='reward', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[Water1, Water2],
                              outputsOff=[LED1,LED2])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[Water1, Water2])
        elif taskMode == 'auto_lights':
            #self.params['timeLEDon'].set_value(waitTime)
            self.sm.set_extratimer('lightTimer1', duration=waitTime)
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForAnyPoke'},
                              outputsOff=[LED1, LED2])
            self.sm.add_state(name='waitForAnyPoke', statetimer=waitTime,
                              transitions={port1in:'reward1', port2in:'reward2',
                                           'lightTimer1':'turnLEDoff'},
                              outputsOn=[LED1, LED2],
                              trigger=['lightTimer1'])
            self.sm.add_state(name='reward1', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward1', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water1])
            self.sm.add_state(name='stopReward1', statetimer=0,
                              transitions={'Tup':'waitForPoke2', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water1])
            self.sm.add_state(name='waitForPoke2', statetimer=waitTime,
                              transitions={port2in:'reward2after1', 'lightTimer1':'turnLEDoff'})
            self.sm.add_state(name='reward2after1', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward2after1', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water2])
            self.sm.add_state(name='stopReward2after1', statetimer=0,
                              transitions={'Tup':'keepLEDon', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water2])
            self.sm.add_state(name='reward2', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward2', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water2])
            self.sm.add_state(name='stopReward2', statetimer=0,
                              transitions={'Tup':'waitForPoke1', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water2])
            self.sm.add_state(name='waitForPoke1', statetimer=waitTime,
                              transitions={port1in:'reward1after2', 'lightTimer1':'turnLEDoff'})
            self.sm.add_state(name='reward1after2', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward1after2', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water1])
            self.sm.add_state(name='stopReward1after2', statetimer=0,
                              transitions={'Tup':'keepLEDon', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water1])
            self.sm.add_state(name='keepLEDon', statetimer=waitTime,
                              transitions={'Tup':'turnLEDoff', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water1, Water2])
            self.sm.add_state(name='turnLEDoff', statetimer=0,
                              transitions={'Tup':'iti'},
                              outputsOff=[LED1, LED2, Water1, Water2])
            self.sm.add_state(name='iti', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[LED1, LED2, Water1, Water2])
        elif taskMode == 'reward_on_first_poke':
            #self.params['timeLEDon'].set_value(waitTime)
            self.sm.set_extratimer('lightTimer1', duration=waitTime)
            self.sm.set_extratimer('lightTimer2', duration=waitTime)
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForPoke'},
                              outputsOff=[LED1, LED2])
            self.sm.add_state(name='waitForPoke', statetimer=LONGTIME,
                              transitions={port1in:'reward1', port2in:'reward2'})
            self.sm.add_state(name='reward1', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward1', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water1, LED1, LED2],
                              trigger=['lightTimer1'])
            self.sm.add_state(name='stopReward1', statetimer=0,
                              transitions={'Tup':'waitForPoke2', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water1])
            self.sm.add_state(name='waitForPoke2', statetimer=waitTime,
                              transitions={port2in:'reward2after1', 'lightTimer1':'turnLEDoff'})
            self.sm.add_state(name='reward2after1', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward2after1', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water2])
            self.sm.add_state(name='stopReward2after1', statetimer=0,
                              transitions={'Tup':'keepLEDon', 'lightTimer1':'turnLEDoff'},
                              outputsOff=[Water2])
            self.sm.add_state(name='reward2', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward2', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[Water2, LED1, LED2],
                              trigger=['lightTimer2'])
            self.sm.add_state(name='stopReward2', statetimer=0,
                              transitions={'Tup':'waitForPoke1', 'lightTimer2':'turnLEDoff'},
                              outputsOff=[Water2])
            self.sm.add_state(name='waitForPoke1', statetimer=waitTime,
                              transitions={port1in:'reward1after2', 'lightTimer2':'turnLEDoff'})
            self.sm.add_state(name='reward1after2', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward1after2', 'lightTimer2':'turnLEDoff'},
                              outputsOn=[Water1])
            self.sm.add_state(name='stopReward1after2', statetimer=0,
                              transitions={'Tup':'keepLEDon', 'lightTimer2':'turnLEDoff'},
                              outputsOff=[Water1])
            self.sm.add_state(name='keepLEDon', statetimer=waitTime,
                              transitions={'Tup':'turnLEDoff',
                                           'lightTimer1':'turnLEDoff', 'lightTimer2':'turnLEDoff'},
                              outputsOff=[Water1, Water2])
            self.sm.add_state(name='turnLEDoff', statetimer=0,
                              transitions={'Tup':'iti'},
                              outputsOff=[LED1, LED2, Water1, Water2])
            self.sm.add_state(name='iti', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[LED1, LED2, Water1, Water2])
        elif taskMode == 'reward_on_last_poke':
            #self.params['timeLEDon'].set_value(waitTime)
            self.sm.set_extratimer('lightTimer1', duration=waitTime)
            self.sm.set_extratimer('lightTimer2', duration=waitTime)
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForPoke'},
                              outputsOff=[LED1, LED2])
            self.sm.add_state(name='waitForPoke', statetimer=LONGTIME,
                              transitions={port1in:'waitForPoke2', port2in:'waitForPoke1'})
            self.sm.add_state(name='waitForPoke2', statetimer=waitTime,
                              transitions={port2in:'reward', 'lightTimer1':'turnLEDoff'},
                              outputsOn=[LED1,LED2],
                              trigger=['lightTimer1'])
            self.sm.add_state(name='waitForPoke1', statetimer=waitTime,
                              transitions={port1in:'reward', 'lightTimer2':'turnLEDoff'},
                              outputsOn=[LED1, LED2],
                              trigger=['lightTimer2'])
            self.sm.add_state(name='reward', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward', 'lightTimer1':'turnLEDoff',
                                           'lightTimer2':'turnLEDoff'},
                              outputsOn=[Water1,Water2])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'keepLEDon', 'lightTimer1':'turnLEDoff',
                                           'lightTimer2':'turnLEDoff'},
                              outputsOff=[Water1, Water2])
            self.sm.add_state(name='keepLEDon', statetimer=waitTime,
                              transitions={'Tup':'turnLEDoff',
                                           'lightTimer1':'turnLEDoff', 'lightTimer2':'turnLEDoff'},
                              outputsOff=[Water1, Water2])
            self.sm.add_state(name='turnLEDoff', statetimer=0,
                              transitions={'Tup':'iti'},
                              outputsOff=[LED1, LED2, Water1, Water2])
            self.sm.add_state(name='iti', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[LED1, LED2, Water1, Water2])
        elif taskMode == 'cooperate':
            #self.params['timeLEDon'].set_value(self.params['timeWaterValves'].get_value())
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForPoke'},
                              outputsOff=[LED1, LED2])
            self.sm.add_state(name='waitForPoke', statetimer=LONGTIME,
                              transitions={port1in:'waitForPoke2', port2in:'waitForPoke1'})
            self.sm.add_state(name='waitForPoke2', statetimer=waitTime,
                              transitions={port2in:'reward', 'Tup':'iti'})
            self.sm.add_state(name='waitForPoke1', statetimer=waitTime,
                              transitions={port1in:'reward', 'Tup':'iti'})
            self.sm.add_state(name='reward', statetimer=timeWaterValves,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[Water1, Water2, LED1, LED2])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'iti'},
                              outputsOff=[Water1, Water2, LED1, LED2])
            self.sm.add_state(name='iti', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[LED1, LED2, Water1, Water2])
        
        #print(self.sm)
        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

        
    def calculate_results(self, trialIndex):
        eventsThisTrial = self.dispatcher.events_one_trial(trialIndex)
        statesThisTrial = eventsThisTrial[:,2]
        taskMode = self.params['taskMode'].get_string()
        # -- Check if it's an aborted trial --
        lastEvent = eventsThisTrial[-1,:]
        if lastEvent[1]==-1 and lastEvent[2]==0:
            self.results['outcome'][trialIndex] = self.results.labels['outcome']['aborted']
            self.results['timePoke1'][trialIndex] = np.nan
            self.results['timePoke2'][trialIndex] = np.nan
            return
        if taskMode in ['auto_lights', 'reward_on_first_poke']:
            if (self.sm.statesNameToIndex['reward1'] in statesThisTrial):
                self.params['nRewarded1'].add(1)
                eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['reward1'])[0]
                self.results['timePoke1'][trialIndex] = eventsThisTrial[eventInd,0]
                if (self.sm.statesNameToIndex['reward2after1'] in statesThisTrial):
                    self.params['nRewarded2'].add(1)
                    eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['reward2after1'])[0]
                    self.results['timePoke2'][trialIndex] = eventsThisTrial[eventInd,0]
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['rewardedBoth']
                else:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['poke1only']
                    self.results['timePoke2'][trialIndex] = np.nan
            elif (self.sm.statesNameToIndex['reward2'] in statesThisTrial):
                self.params['nRewarded2'].add(1)
                eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['reward2'])[0]
                self.results['timePoke2'][trialIndex] = eventsThisTrial[eventInd,0]
                if (self.sm.statesNameToIndex['reward1after2'] in statesThisTrial):
                    self.params['nRewarded1'].add(1)
                    self.results['timePoke1'][trialIndex] = eventsThisTrial[eventInd,0]
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['rewardedBoth']
                else:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['poke2only']
                    self.results['timePoke1'][trialIndex] = np.nan
            else:
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
                self.results['timePoke1'][trialIndex] = np.nan
                self.results['timePoke2'][trialIndex] = np.nan
        if taskMode in ['reward_on_last_poke', 'cooperate']:
            if (self.sm.statesNameToIndex['waitForPoke2'] in statesThisTrial):
                eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['waitForPoke2'])[0]
                self.results['timePoke1'][trialIndex] = eventsThisTrial[eventInd,0]
                if (self.sm.statesNameToIndex['reward'] in statesThisTrial):
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['rewardedBoth']
                    self.params['nRewarded1'].add(1)
                    self.params['nRewarded2'].add(1)
                    eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['reward'])[0]
                    self.results['timePoke2'][trialIndex] = eventsThisTrial[eventInd,0]
                else:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['poke1only']
                    self.results['timePoke2'][trialIndex] = np.nan
            elif (self.sm.statesNameToIndex['waitForPoke1'] in statesThisTrial):
                eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['waitForPoke1'])[0]
                self.results['timePoke2'][trialIndex] = eventsThisTrial[eventInd,0]
                if (self.sm.statesNameToIndex['reward'] in statesThisTrial):
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['rewardedBoth']
                    self.params['nRewarded1'].add(1)
                    self.params['nRewarded2'].add(1)
                    eventInd = np.flatnonzero(statesThisTrial==self.sm.statesNameToIndex['reward'])[0]
                    self.results['timePoke1'][trialIndex] = eventsThisTrial[eventInd,0]
                else:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['poke2only']
                    self.results['timePoke1'][trialIndex] = np.nan
            else:
                # -- This should never happen, since a trial requires a poke --
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
                self.results['timePoke1'][trialIndex] = np.nan
                self.results['timePoke2'][trialIndex] = np.nan


    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtWidgets.QMainWindow, which explains
        its camelCase naming.
        '''
        #self.soundClient.shutdown()
        self.dispatcher.die()
        event.accept()

if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)

