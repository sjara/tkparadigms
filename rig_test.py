'''
Test sounds, lights, valves and pokes.
'''

import sys
if sys.version_info.major==3:
    from qtpy import QtWidgets
    from taskontrol import rigsettings
    from taskontrol import dispatcher
    from taskontrol import statematrix
    from taskontrol import savedata
    from taskontrol import paramgui
    from taskontrol import paramgui as messenger
    from taskontrol import utils as arraycontainer
    arraycontainer.Container = arraycontainer.EnumContainer
else:
    from PySide import QtGui as QtWidgets
    from taskontrol.settings import rigsettings
    from taskontrol.core import dispatcher
    from taskontrol.core import statematrix
    from taskontrol.core import savedata
    from taskontrol.core import paramgui
    from taskontrol.core import messenger
    from taskontrol.core import arraycontainer
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import manualcontrol
import numpy as np
import time # For hardcoded waiting time to connect to sound server

centerSoundFile = './center.wav'
leftSoundFile = './left.wav'
rightSoundFile = './right.wav'

class RigTest(QtWidgets.QMainWindow):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(RigTest, self).__init__(parent)

        self.name = 'rigtest'
        smServerType = rigsettings.STATE_MACHINE_TYPE
        
        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')
        # -- Create dispatcher --
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)
        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.WaterControl(self.dispatcherModel.statemachine)
       
        # -- Add parameters --
        self.params = paramgui.Container()
        self.params['timeWaterValveL'] = paramgui.NumericParam('Time valve left', value=0.03,
                                                               units='s', group='Water delivery')
        self.params['timeWaterValveR'] = paramgui.NumericParam('Time valve right', value=0.03,
                                                               units='s', group='Water delivery')
        self.params['offTime'] = paramgui.NumericParam('Time between', value=0.25,
                                                       units='s', group='Schedule')
        self.params['soundDuration'] = paramgui.NumericParam('Sound duration', value=0.26, decimals=2,
                                                             units='s', group='Sound', enabled=False)
        self.params['soundIntensity'] = paramgui.NumericParam('Sound intensity', value=80,
                                                              units='dB-SPL', group='Sound')
        self.params['soundAmplitude'] = paramgui.NumericParam('Avg sound amp', value=1.0, decimals=4,
                                                              units='dB-SPL', group='Sound', enabled=False)
        scheduleGroup = self.params.layout_group('Schedule')
        soundGroup = self.params.layout_group('Sound')
        waterGroup = self.params.layout_group('Water delivery')

        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()
        layoutCol3 = QtWidgets.QVBoxLayout()

        layoutCol1.addWidget(self.dispatcherView)
        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addWidget(scheduleGroup)
        layoutCol3.addWidget(waterGroup)
        layoutCol3.addWidget(soundGroup)

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Connect to sound server and define sounds --
        if sys.version_info.major<3:
            print('Conecting to soundserver...')
            print('***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****') ### DEBUG
            time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundCenterID = 1
        self.soundLeftID = 2
        self.soundRightID = 3
        self.soundClient.start()

        # -- Connect signals from dispatcher --
        self.dispatcherModel.prepareNextTrial.connect(self.prepare_next_trial)
        self.dispatcherModel.timerTic.connect(self._timer_tic)

        # -- Connect messenger --
        self.messagebar = messenger.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect('Created window')

        # -- Connect signals to messenger
        self.dispatcherModel.logMessage.connect(self.messagebar.collect)

        # -- Center in screen --
        #paramgui.center_on_screen(self)

    def _show_message(self,msg):
        self.statusBar().showMessage(str(msg))
        print(msg)

    def _timer_tic(self,etime,lastEvents):
        pass

    def prepare_sounds(self):
        #spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION)
        spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        soundFrequency = 1000
        soundIntensity = self.params['soundIntensity'].get_value()
        soundAmplitude = spkCal.find_amplitude(soundFrequency,soundIntensity)
        self.params['soundAmplitude'].set_value(np.mean(soundAmplitude))
        '''
        soundDuration = self.params['soundDuration'].get_value()
        sNoise = {'type':'noise', 'duration':soundDuration, 'amplitude':soundAmplitude}
        self.soundClient.set_sound(self.soundLeftID,sNoise)
        self.soundClient.set_sound(self.soundRightID,sNoise)
        '''
        sCenter = {'type':'fromfile', 'filename':centerSoundFile,
                 'channel':'both', 'amplitude':soundAmplitude}
        sLeft = {'type':'fromfile', 'filename':leftSoundFile,
                 'channel':'left', 'amplitude':soundAmplitude}
        sRight = {'type':'fromfile', 'filename':rightSoundFile,
                  'channel':'right', 'amplitude':soundAmplitude}
        self.soundClient.set_sound(self.soundCenterID,sCenter)
        self.soundClient.set_sound(self.soundLeftID,sLeft)
        self.soundClient.set_sound(self.soundRightID,sRight)

    def prepare_next_trial(self, nextTrial):
        self.prepare_sounds()
        self.sm.reset_transitions()
        if nextTrial==0:
            self.prepare_automatic_trial() # This will change self.sm
        else:
            eventsLastTrial = self.dispatcherModel.events_one_trial(nextTrial-1)
            # Check if last trial was aborted (by stopping paradigm)
            # FIXME: the -1 (indicating forced transition) should not be hardcoded.
            if eventsLastTrial[-1][1]==-1:
                self.prepare_automatic_trial() # This will change self.sm
            else:
                self.prepare_manual_trial() # This will change self.sm
        #print(self.sm) ### DEBUG
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()
        pass

    def prepare_automatic_trial(self):
        self.sm.add_state(name='startTrial', statetimer=0,
                          transitions={'Tup':'lightOnL'})
        self.sm.add_state(name='lightOnL', statetimer=self.params['timeWaterValveL'].get_value(),
                          transitions={'Tup':'lightOffL'}, outputsOn={'leftLED'})
        self.sm.add_state(name='lightOffL', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'valveOnL'}, outputsOff={'leftLED'})
        self.sm.add_state(name='valveOnL', statetimer=self.params['timeWaterValveL'].get_value(),
                          transitions={'Tup':'valveOffL'}, outputsOn={'leftWater'})
        self.sm.add_state(name='valveOffL', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'soundOnL'},outputsOff={'leftWater'})
        self.sm.add_state(name='soundOnL', statetimer=self.params['soundDuration'].get_value(),
                          transitions={'Tup':'soundOffL'}, serialOut=self.soundLeftID)
        self.sm.add_state(name='soundOffL', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'lightOnR'})
        self.sm.add_state(name='lightOnR', statetimer=self.params['timeWaterValveR'].get_value(),
                          transitions={'Tup':'lightOffR'}, outputsOn={'rightLED'})
        self.sm.add_state(name='lightOffR', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'valveOnR'}, outputsOff={'rightLED'})
        self.sm.add_state(name='valveOnR', statetimer=self.params['timeWaterValveR'].get_value(),
                          transitions={'Tup':'valveOffR'}, outputsOn={'rightWater'})
        self.sm.add_state(name='valveOffR', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'soundOnR'},outputsOff={'rightWater'})
        self.sm.add_state(name='soundOnR', statetimer=self.params['soundDuration'].get_value(),
                          transitions={'Tup':'soundOffR'}, serialOut=self.soundRightID)
        self.sm.add_state(name='soundOffR', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'readyForNextTrial'})

    def prepare_manual_trial(self):
        self.sm.add_state(name='startTrial', statetimer=0,
                          transitions={'Tup':'waitForPoke'})
        self.sm.add_state(name='waitForPoke',statetimer=1000,
                          transitions={'Cin':'soundOnC','Lin':'soundOnL','Rin':'soundOnR'})
        self.sm.add_state(name='soundOnC', statetimer=self.params['soundDuration'].get_value(),
                          transitions={'Tup':'soundOffC'}, serialOut=self.soundCenterID)
        self.sm.add_state(name='soundOffC', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'readyForNextTrial'})
        self.sm.add_state(name='soundOnL', statetimer=self.params['soundDuration'].get_value(),
                          transitions={'Tup':'soundOffL'}, serialOut=self.soundLeftID)
        self.sm.add_state(name='soundOffL', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'readyForNextTrial'})
        self.sm.add_state(name='soundOnR', statetimer=self.params['soundDuration'].get_value(),
                          transitions={'Tup':'soundOffR'}, serialOut=self.soundRightID)
        self.sm.add_state(name='soundOffR', statetimer=self.params['offTime'].get_value(),
                          transitions={'Tup':'readyForNextTrial'})

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtWidgets.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcherModel.die()
        event.accept()

if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(RigTest)
