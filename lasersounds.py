from PySide import QtGui
from taskontrol.core import dispatcher
from taskontrol.core import paramgui
from taskontrol.core import savedata
from taskontrol.settings import rigsettings
from taskontrol.core import statematrix
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import soundclient
import numpy as np
import time

if rigsettings.OUTPUTS.has_key('outBit1'):
    trialStartSync = ['outBit1'] # Sync signal for trial-start.
else:
    trialStartSync = []
if rigsettings.OUTPUTS.has_key('outBit0'):
    stimSync = ['outBit0'] # Sync signal for sound stimulus
else:
    stimSync = []
if rigsettings.OUTPUTS.has_key('outBit2'):
    laserSync = ['outBit2','stim1'] # Sync signal for laser
else:
    laserSync = ['centerLED'] # Use center LED during emulation

class Paradigm(QtGui.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):

        '''
        Set up the taskontrol core modules, add parameters to the GUI, and 
        initialize the sound server.
        '''

        super(Paradigm, self).__init__(parent)

        self.name = 'lasersounds'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the speaker calibration object
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION)

        # -- Create dispatcher --
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,
                                                     interval=0.1)

        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Add parameters --
        self.params = paramgui.Container()

        #Info about the experiment
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='santiago',
                                                            group='Experiment Info')
        self.params['subject'] = paramgui.StringParam('Subject',value='test030',
                                                       group='Experiment Info')

        self.params['mode'] = paramgui.MenuParam('Mode',
                                                ['Random','Interleaved','Sound','Laser'],
                                                value=0,group='Experiment Info')
        
        #Timing parameters
        self.params['laserDelay'] = paramgui.NumericParam('Delay to Laser Onset (s)',
                                                        value=0.1,
                                                        group='Timing Parameters')
        self.params['laserFrontOverhang'] = paramgui.NumericParam('Laser onset to sound onset (s)',
                                                        value=0.05,
                                                        group='Timing Parameters')
        self.params['laserBackOverhang'] = paramgui.NumericParam('Sound offset to laser offset (s)',
                                                        value=0.05,
                                                        group='Timing Parameters')
        self.params['soundDuration'] = paramgui.NumericParam('Sound Duration (s)',
                                                        value=0.1,
                                                        group='Timing Parameters')
        self.params['itiMean'] = paramgui.NumericParam('Inter-trial interval mean (s)',
                                                        value=0.5,
                                                        group='Timing Parameters')
        self.params['itiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=0.25,
                                                      group='Timing Parameters')


        #Info about the sounds
        self.params['soundType'] = paramgui.MenuParam('Sound Type',
                                                         ['Sine','Chord','Noise'],
                                                         value=2,group='Sound Parameters')
        self.params['targetFreq'] = paramgui.NumericParam('Frequency (Hz)',
                                                        value=5000,
                                                        group='Sound Parameters')
        self.params['noiseAmp'] = paramgui.NumericParam('Amplitude in Noise-Mode',
                                                       value=0.3,
                                                       group='Sound Parameters')
        self.params['toneInt'] = paramgui.NumericParam('Target Intensity for Sine and Chord (dB SPL)',
                                                       value=70,
                                                       group='Sound Parameters')


        #Info about the current trial
        self.params['laserTrial'] = paramgui.NumericParam('Laser Trial',
                                                            value=0,
                                                            enabled=False,
                                                            group='Current Trial')

        
        infoParams = self.params.layout_group('Experiment Info')
        timingParams = self.params.layout_group('Timing Parameters')
        soundParams = self.params.layout_group('Sound Parameters')
        currentTrialParams = self.params.layout_group('Current Trial')
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)


        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Module for savng the data -- 

        self.saveData = savedata.SaveData(rigsettings.DATA_DIR,
                                          remotedir=rigsettings.REMOTE_DIR)
        self.saveData.checkInteractive.setChecked(True)

        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout() #Create a main layout and two columns
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()
        layoutCol3 = QtGui.QVBoxLayout()


        layoutMain.addLayout(layoutCol1) #Add the columns to the main layout
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)

        layoutCol1.addWidget(self.dispatcherView) #Add the dispatcher to col1
        layoutCol1.addWidget(self.saveData)
        layoutCol2.addWidget(infoParams)  #Add info parameters to column 2
        layoutCol2.addWidget(soundParams)  #Add info parameters to column 2
        layoutCol3.addWidget(timingParams)  #Add timing parameters to column 3
        layoutCol3.addWidget(currentTrialParams)  #Add current trial parameters to column 3

        self.centralWidget.setLayout(layoutMain) #Assign the layouts to the main window
        self.setCentralWidget(self.centralWidget)

        # -- Connect signals from dispatcher --
        
        #prepare_next_trial is sent whenever the dispatcher reaches the end of 
        #the current trial. 
        self.dispatcherModel.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect the save data button --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

        print "Connecting to sound server"
        print '***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****'        
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()

        self.laserInterleavedSwitch=1

    def prepare_next_trial(self, nextTrial):
        '''
        Prepare the target sound, send state matrix to the statemachine, and 
        update the list of GUI parameters so that we can save the history of the
        frequency, intensity, and amplitude parameters for each trial. 
        '''

        if nextTrial > 0:  ## Do not update the history before the first trial
            self.params.update_history()

        self.sm.reset_transitions()

        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        iti = self.params['itiMean'].get_value() + \
              self.params['itiHalfRange'].get_value()*randNum


        soundDuration = self.params['soundDuration'].get_value()
        trialFreq = self.params['targetFreq'].get_value()
        trialIntensity = self.params['toneInt'].get_value()
        targetAmp = self.spkCal.find_amplitude(trialFreq,
                                               trialIntensity)[1]  
                                               #Only calibrated right speaker
        noiseAmp = self.params['noiseAmp'].get_value()

        # -- Determine the sound presentation mode and prepare the appropriate sound
        soundType = self.params['soundType'].get_string()
        
        if soundType == 'Sine':
            sound = {'type':'tone', 'duration':soundDuration, 
                     'amplitude':targetAmp, 'frequency':trialFreq}
        elif soundType == 'Chord':
            sound = {'type':'chord', 'frequency':trialFreq, 'duration':soundDuration,
                  'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        elif soundType == 'Noise':
            sound = {'type':'noise', 'duration':soundDuration,
                     'amplitude':noiseAmp}


        mode = self.params['mode'].get_string()

        if mode=='Random':
            soundOutput=stimSync
            serialOutput = 1
            if np.random.random(1)>=0.5:
                laserOutput=laserSync
                self.params['laserTrial'].set_value(1)
            else:
                laserOutput=[]
                self.params['laserTrial'].set_value(0)


        elif mode=='Interleaved':
            soundOutput=stimSync
            serialOutput = 1
            if self.laserInterleavedSwitch==1:
                laserOutput=laserSync
                self.params['laserTrial'].set_value(1)
                self.laserInterleavedSwitch=0
            elif self.laserInterleavedSwitch==0:
                laserOutput=[]
                self.params['laserTrial'].set_value(0)
                self.laserInterleavedSwitch=1
                    
        elif mode=='Sound':
            soundOutput=stimSync
            serialOutput = 1
            laserOutput=[]
            self.params['laserTrial'].set_value(0)

        elif mode=='Laser':
            soundOutput=[]
            serialOutput = 0
            laserOutput=laserSync
            self.params['laserTrial'].set_value(1)
            

        self.soundClient.set_sound(1,sound)

        #Get the timing parameters
        delayToLaser = self.params['laserDelay'].get_value()
        laserFrontOverhang = self.params['laserFrontOverhang'].get_value()
        laserBackOverhang = self.params['laserBackOverhang'].get_value()
        

        # -- Prepare the state transition matrix --
        self.sm.add_state(name='startTrial', statetimer = delayToLaser,  
                          transitions={'Tup':'laserFrontOverhang'})
        self.sm.add_state(name='laserFrontOverhang', statetimer=laserFrontOverhang, 
                          transitions={'Tup':'soundOn'},
                          outputsOn=laserOutput)
        self.sm.add_state(name='soundOn', statetimer = soundDuration,
                          transitions={'Tup':'laserBackOverhang'},
                          outputsOn=soundOutput,
                          serialOut=serialOutput) 
        self.sm.add_state(name='laserBackOverhang', statetimer = laserBackOverhang,
                          transitions={'Tup':'iti'},
                          outputsOff=soundOutput) 
        self.sm.add_state(name='iti', statetimer = iti,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=laserOutput) 

        
        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()


    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcherModel,
                               self.sm],
                              self.dispatcherModel.currentTrial,
                              experimenter=self.params['experimenter'].get_value(),
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
        self.dispatcherModel.die()
        event.accept()
                           
if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(Paradigm)