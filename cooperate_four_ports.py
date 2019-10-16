'''
Cooperate four ports is a paradigm in which two animals must poke simultaneously to obtain reward.
There are two lanes (one for each animal) with one port at each end.
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
'''
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
import time
'''

LONGTIME = 100
MAX_N_TRIALS = 4000

class Paradigm(QtGui.QMainWindow):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.name = 'coop4ports'

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

        self.params['timeWaterValvesN'] = paramgui.NumericParam('Time valves N',value=0.03,
                                                                units='s',group='Water delivery')
        self.params['timeWaterValvesS'] = paramgui.NumericParam('Time valves S',value=0.03,
                                                                units='s',group='Water delivery')
        waterDelivery = self.params.layout_group('Water delivery')
       
        self.params['waitTime'] = paramgui.NumericParam('Wait time',value=3,
                                                        units='s',group='Timing parameters')
        self.params['timeLEDon'] = paramgui.NumericParam('Time LED on',value=1,
                                                        units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')
        self.params['taskMode'] = paramgui.MenuParam('Task mode', ['one_track','cooperate'], value=0,
                                                     group='General parameters')
        generalParams = self.params.layout_group('General parameters')


        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout()
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(self.dispatcherView)

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
        self.results = arraycontainer.Container()
        self.results.labels['outcome'] = {'correct':1,'error':0}
        self.results['outcome'] = np.empty(maxNtrials,dtype=int)
        self.results.labels['activeSide'] = {'north':0,'south':1}
        self.results['activeSide'] = np.empty(maxNtrials,dtype=int)
        self.results['activeSide'][0] = 0
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

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

    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.params.update_history()
            
        # -- Prepare next trial --
        taskMode = self.params['taskMode'].get_string()
        waitTime = self.params['waitTime'].get_value()
        timeLEDon = self.params['timeLEDon'].get_value()
        timeWaterValvesN = self.params['timeWaterValvesN'].get_value()
        timeWaterValvesS = self.params['timeWaterValvesS'].get_value()

        self.sm.reset_transitions()

        if self.results['activeSide'][nextTrial] == self.results.labels['activeSide']['north']:
            port1in = 'N1in'; port2in = 'N2in'
            LED1 = 'N1LED'; LED2 = 'N2LED'
            Water1 = 'N1Water'; Water2 = 'N2Water'
            self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
        else:
            port1in = 'S1in'; port2in = 'S2in'
            LED1 = 'S1LED'; LED2 = 'S2LED'
            Water1 = 'S1Water'; Water2 = 'S2Water'
            self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['north']

        if taskMode == 'one_track':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForPoke'},
                              outputsOff=[LED1,LED2])
            self.sm.add_state(name='waitForPoke', statetimer=LONGTIME,
                              transitions={port1in:'reward', port2in:'reward'})
            self.sm.add_state(name='reward', statetimer=timeWaterValvesN,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[Water1, Water2],
                              outputsOff=[LED1,LED2])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[Water1, Water2])
        elif taskMode == 'cooperate':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForPoke'},
                              outputsOff=[LED1,LED2])
            self.sm.add_state(name='waitForPoke', statetimer=LONGTIME,
                              transitions={port1in:'waitForPort2', port2in:'waitForPort1'})
            self.sm.add_state(name='waitForPort2', statetimer=waitTime,
                              transitions={port2in:'reward', 'Tup':'singlePoke'},
                              outputsOn=[])
            self.sm.add_state(name='waitForPort1', statetimer=waitTime,
                              transitions={port1in:'reward', 'Tup':'singlePoke'},
                              outputsOn=[])
            self.sm.add_state(name='singlePoke', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[LED1,LED2])
            self.sm.add_state(name='reward', statetimer=timeWaterValvesN,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[Water1, Water2, LED1, LED2],
                              outputsOff=[])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'keepLEDon'},
                              outputsOff=[Water1, Water2])
            self.sm.add_state(name='keepLEDon', statetimer=timeLEDon,
                              transitions={'Tup':'turnLEDoff'},
                              outputsOff=[])
            self.sm.add_state(name='turnLEDoff', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[LED1, LED2])
        
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        #self.soundClient.shutdown()
        self.dispatcherModel.die()
        event.accept()

if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)

