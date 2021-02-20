"""
Create a paradigm for calibrating the amount of water delivered.
"""

from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import utils
from taskontrol.plugins import manualcontrol


class WaterCalibration(QtWidgets.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None, dummy=False):
        super(WaterCalibration, self).__init__(parent)

        self.name = '2afc'

        # -- Read settings --
        if dummy:
            smServerType = 'dummy'
        else:
            smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Module for saving data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR)

        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Add parameters --
        self.params = paramgui.Container()
        '''
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                           value='experimenter',
                                                           group='Session info')
        self.params['subject'] = paramgui.StringParam('Subject',value='subject',
                                                      group='Session info')
        self.sessionInfo = self.params.layout_group('Session info')
        '''

        self.params['timeWaterValveL'] = paramgui.NumericParam('Time valve left',value=0.04,
                                                               units='s',group='Valves times')
        #self.params['timeWaterValveC'] = paramgui.NumericParam('Time valve center',value=0.04,
        #                                                       units='s',group='Valves times')
        self.params['timeWaterValveR'] = paramgui.NumericParam('Time valve right',value=0.04,
                                                               units='s',group='Valves times')
        valvesTimes = self.params.layout_group('Valves times')

        self.params['waterVolumeL'] = paramgui.NumericParam('Water volume left',value=0,
                                                               units='ml',group='Water volume')
        #self.params['waterVolumeC'] = paramgui.NumericParam('Water volume center',value=0,
        #                                                       units='ml',group='Water volume')
        self.params['waterVolumeR'] = paramgui.NumericParam('Water volume right',value=0,
                                                               units='ml',group='Water volume')
        waterVolume = self.params.layout_group('Water volume')

        self.params['offTime'] = paramgui.NumericParam('Time between',value=0.5,
                                                       units='s',group='Schedule')
        self.params['nDeliveries'] = paramgui.NumericParam('N deliveries',value=2,
                                                       units='',group='Schedule')
        self.params['nDelivered'] = paramgui.NumericParam('N delivered',value=0,
                                                       units='',group='Schedule')
        self.params['nDelivered'].set_enabled(False)
        schedule = self.params.layout_group('Schedule')


        # -- Create dispatcher --
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)
 
        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)

        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()
        layoutCol3 = QtWidgets.QVBoxLayout()

        layoutCol1.addWidget(self.saveData)
        #layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(self.dispatcher.widget)

        layoutCol2.addWidget(valvesTimes)
        layoutCol2.addStretch()
        layoutCol2.addWidget(self.manualControl)

        layoutCol3.addWidget(waterVolume)
        layoutCol3.addStretch()
        layoutCol3.addWidget(schedule)

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables storing results --
        self.results = utils.EnumContainer()

        # -- Connect signals from dispatcher --
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)
        self.dispatcher.timerTic.connect(self._timer_tic)

        # -- Connect messenger --
        self.messagebar = paramgui.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect('Created window')

        # -- Connect signals to messenger
        self.saveData.logMessage.connect(self.messagebar.collect)
        self.dispatcher.logMessage.connect(self.messagebar.collect)

        # -- Connect other signals --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        # -- Center in screen --
        paramgui.center_on_screen(self)

        # -- Prepare first trial --
        # - No need to prepare here. Dispatcher sends a signal when pressing Start -
        #self.prepare_next_trial(0)
        

    def _show_message(self,msg):
        self.statusBar().showMessage(str(msg))
        print(msg)

    def _timer_tic(self,etime,lastEvents):
        pass

    def save_to_file(self):
        pass

    def prepare_next_trial(self, nextTrial):
        print('============ Prearing trial {0} ==========='.format(self.dispatcher.currentTrial))
        self.sm.reset_transitions()
        valveTimeR = self.params['timeWaterValveR'].get_value()
        #valveTimeR = self.params['timeWaterValveR'].get_value()

        self.sm.add_state(name='startTrial', statetimer=0,
                          transitions={'Tup':'valveOnL'})
        self.sm.add_state(name='valveOnL',
                          statetimer=self.params['timeWaterValveL'].get_value(),
                          transitions={'Tup':'valveOffL'},
                          outputsOn={'leftLED','leftWater'})
        self.sm.add_state(name='valveOffL',
                          statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'valveOnR'},
                          outputsOff={'leftLED','leftWater'})
        self.sm.add_state(name='valveOnR',
                          statetimer=self.params['timeWaterValveR'].get_value(),
                          transitions={'Tup':'valveOffR'},
                          outputsOn={'rightLED','rightWater'})
        self.sm.add_state(name='valveOffR',
                          statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff={'rightLED','rightWater'})
        pass
        print(self.sm) ### DEBUG
        self.dispatcher.set_state_matrix(self.sm)

        if self.params['nDelivered'].get_value() < self.params['nDeliveries'].get_value():
            self.dispatcher.ready_to_start_trial()
            self.params['nDelivered'].set_value(int(self.params['nDelivered'].get_value())+1)
        else:
            self.dispatcher.widget.stop()
            self.params['nDelivered'].set_value(0)

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        self.dispatcher.die()
        event.accept()

if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(WaterCalibration)
