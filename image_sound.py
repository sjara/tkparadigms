"""
Simple paradigm that presents a sound on every trial.
"""

import numpy as np
from qtpy import QtCore 
from qtpy import QtWidgets 
from taskontrol import rigsettings
from taskontrol import paramgui
from taskontrol import savedata
from taskontrol import statematrix
from taskontrol import dispatcher
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import imagesoundclient
from taskontrol.plugins import speakercalibration
import time
import random


class Paradigm(QtWidgets.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):
        super().__init__(parent)

        self.name = 'timedimagesound'

        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Module for saving data --
        self.saveData = savedata.SaveData(rigsettings.DATA_DIR, remotedir=rigsettings.REMOTE_DIR)

        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Add parameters --
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

        # -- Trial timing parameters --
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter trial interval (ITI)',value=1.0,
                                                                  units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')

        # -- Sound parameters --
        self.params['soundFrequency'] = paramgui.NumericParam('Sound frequency', value=1000,
                                                               decimals=0, units='Hz',
                                                               group='Sound parameters')
        self.params['soundDuration'] = paramgui.NumericParam('Sound duration', value=0.1, units='s',
                                                              group='Sound parameters')
        self.params['soundIntensity'] = paramgui.NumericParam('Sound intensity', value=60, units='dB-SPL',
                                                        enabled=True, group='Sound parameters')
        self.params['soundAmplitude'] = paramgui.NumericParam('Sound amplitude',value=0.0,units='[0-1]',
                                                        enabled=False, decimals=4, group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')

        # -- Image Params --
        self.params['lightIntensity'] = paramgui.NumericParam('Intensity of light (%)',value=100,
                                                              decimals=2,units='percent',group='Image parameters')
        self.params['xOuterSize'] = paramgui.NumericParam('Size of image array (x)', value = 4,
                                                       decimals=0, units='pixels',group='Image parameters')
        self.params['yOuterSize'] = paramgui.NumericParam('Size of image array (y)', value = 4,
                                                       decimals=0, units='pixels',group='Image parameters')
        
        self.params['xInnerSize'] = paramgui.NumericParam('Subregion size (x)', value = 0,
                                                       decimals=0, units='pixels',group='Image parameters')
        self.params['yInnerSize'] = paramgui.NumericParam('Subregion size (y)', value = 0,
                                                       decimals=0, units='pixels',group='Image parameters')
        
        self.params['xInnerInd'] = paramgui.NumericParam('Subregion i-index', value = 0,
                                                       decimals=0, units='pixels',group='Image parameters')
        self.params['yInnerInd'] = paramgui.NumericParam('Subregion j-index', value = 0,
                                                       decimals=0, units='pixels',group='Image parameters')
        
        self.params['currentI'] = paramgui.NumericParam('Current i-index', value = 0,
                                                       decimals=0,units='index',group='Image parameters')
        self.params['currentJ'] = paramgui.NumericParam('Current j-index', value = 0,
                                                       decimals=0,units='index',group='Image parameters')
        self.params['randomMode'] = paramgui.MenuParam('Presentation Mode',
                                                         ['Ordered','Random'],
                                                         value=1,group='Image parameters')
        
        imageParams = self.params.layout_group('Image parameters')
        

        # -- Create dispatcher --
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)

        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(self.dispatcher.widget)
        
        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(timingParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(soundParams)
        layoutCol2.addStretch()
        layoutCol2.addWidget(imageParams)


        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Center in screen --
        paramgui.center_on_screen(self)

        # -- Load speaker calibration --
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)

        # -- Connect to sound server --
        self.soundClient = imagesoundclient.SoundClient()
        self.soundID = 1
        self.imageID = 64
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

    '''
    def _center_in_screen(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    '''
    
    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcher, self.sm],
                              self.dispatcher.currentTrial,
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def prepare_sound(self):
        soundIntensity = self.params['soundIntensity'].get_value()
        soundDuration = self.params['soundDuration'].get_value()
        # FIXME: currently I am averaging calibration from both speakers (not good)
        soundFrequency = self.params['soundFrequency'].get_value()
        soundAmp = self.spkCal.find_amplitude(soundFrequency,soundIntensity).mean()
        s1 = {'type':'tone', 'frequency':soundFrequency, 'duration':soundDuration,
              'amplitude':soundAmp}
        self.params['soundAmplitude'].set_value(soundAmp)
        self.soundClient.set_sound(self.soundID, s1)

    def prepare_image(self, nextTrial=0):
        
        intensity = self.params['lightIntensity'].get_value()/100
        dimsOuter = (self.params['xOuterSize'].get_value(),self.params['yOuterSize'].get_value())
        dimsInner = (self.params['xInnerSize'].get_value(),self.params['yInnerSize'].get_value())
        dimsTotal = (max(dimsOuter[0],dimsOuter[0]*dimsInner[0]),max(dimsOuter[1],dimsOuter[1]*dimsInner[1]))
        img = np.zeros(dimsTotal, dtype=float)
        
        if dimsOuter == dimsTotal:
            currentI = (nextTrial%(dimsTotal[0]*dimsTotal[1]))//dimsTotal[1]
            currentJ = nextTrial%dimsTotal[1]
            img[currentI, currentJ] = intensity

        else:
            xInnerInd = self.params['xInnerInd'].get_value()
            yInnerInd = self.params['yInnerInd'].get_value()
            currentI = (nextTrial%(dimsInner[0]*dimsInner[1]))//dimsInner[1]
            currentJ = nextTrial%dimsInner[1]

            imStart = (xInnerInd*dimsInner[0],yInnerInd*dimsInner[1])
            imEnd = (xInnerInd*dimsInner[0] + dimsInner[0],yInnerInd*dimsInner[1] + dimsInner[1])
            innerImg = np.zeros(dimsInner,dtype=float)
            
            innerImg[currentI,currentJ] = intensity

            img[imStart[0]:imEnd[0],imStart[1]:imEnd[1]] = innerImg

        self.params['currentI'].set_value(currentI)
        self.params['currentJ'].set_value(currentJ)
        self.soundClient.set_image(self.imageID, img)
        
    def prepare_next_trial(self, nextTrial):
        if nextTrial>0:
            self.params.update_history(nextTrial-1)
        soundDuration = self.params['soundDuration'].get_value()
        interTrialInterval = self.params['interTrialInterval'].get_value()
        self.prepare_sound()

        # -- Prepare the next image to show --
        self.prepare_image(nextTrial)
        
        self.sm.reset_transitions()
        self.sm.add_state(name='startTrial', statetimer=0,
                          transitions={'Tup':'showImage'},
                          outputsOff=['centerLED'])
        self.sm.add_state(name='showImage', statetimer=0,
                          transitions={'Tup':'playSound'},
                          outputsOn=['centerLED'],
                          serialOut=self.imageID)
        self.sm.add_state(name='playSound', statetimer=soundDuration,
                          transitions={'Tup':'ITI', 'Cin':'ITI',
                                       'Lin':'ITI', 'Rin':'ITI'},
                          serialOut=self.soundID)
        self.sm.add_state(name='ITI', statetimer=interTrialInterval,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=['centerLED'],
                          serialOut=imagesoundclient.STOP_ALL_SOUNDS)
        '''
        self.sm.add_state(name='stopSound', statetimer=0,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=['centerLED'],
                          serialOut=soundclient.STOP_ALL_SOUNDS)
        '''
        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtWidgets.QMainWindow, which explains
        its camelCase naming.
        '''
        self.soundClient.shutdown()
        self.dispatcher.die()
        event.accept()


if __name__ == "__main__":
    (app, paradigm) = paramgui.create_app(Paradigm)

