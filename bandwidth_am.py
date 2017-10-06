'''
Presents bandwidth-limited white noise, amplitude modulated and centered at characteristic frequency.
Bandwidth is varied between trials.

Anna Lakunina and Santiago Jaramillo
'''

from PySide import QtGui
from taskontrol.core import dispatcher
from taskontrol.core import paramgui
from taskontrol.core import savedata
from taskontrol.settings import rigsettings
from taskontrol.core import statematrix
from taskontrol.plugins import speakercalibration
from taskontrol.plugins import speakernoisecalibration as noisecalibration
from taskontrol.plugins import manualcontrol
import numpy as np
import itertools
import random
from taskontrol.plugins import soundclient
import time

# class clearButton(QtGui.QPushButton):
#    def __init__(self, parent=None):
#        super(OutputButton, self).__init__('Clear Tone List')
#        self.clicked.connect(self.clear_tone_list)

if rigsettings.OUTPUTS.has_key('outBit1'):
    trialStartSync = ['outBit1'] # Sync signal for trial-start.
else:
    trialStartSync = []
if rigsettings.OUTPUTS.has_key('outBit0'):
    stimSync = ['outBit0'] # Sync signal for sound stimulus
else:
    stimSync = []
if rigsettings.OUTPUTS.has_key('outBit2'):
    laserSync = ['outBit2','stim2'] # Sync signal for laser
else:
    laserSync = ['centerLED'] # Use center LED during emulation



class Paradigm(QtGui.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):

        '''
        Set up the taskontrol core modules, add parameters to the GUI, and
        initialize the sound server.
        '''

        super(Paradigm, self).__init__(parent)

        self.name = 'bandwidth_am'

        # -- Read settings --
        smServerType = rigsettings.STATE_MACHINE_TYPE

        # -- Create the noise calibration object
        self.noiseCal = noisecalibration.Calibration(rigsettings.NOISE_CALIBRATION)

        # -- Create dispatcher --
        self.dispatcherModel = dispatcher.Dispatcher(serverType=smServerType,
                                                     interval=0.1)

        self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcherModel.statemachine)

        # -- Add parameters --
        self.params = paramgui.Container()
        self.params['experimenter'] = paramgui.StringParam('Experimenter',
                                                            value='santiago',
                                                            group='Session')
        self.params['subject'] = paramgui.StringParam('Subject',value='test030',
                                                       group='Session')

        self.params['charFreq'] = paramgui.NumericParam('Characteristic Frequency (Hz)',
                                                        value=8000,
                                                        group='Session')
        self.params['modRate'] = paramgui.NumericParam('Modulation rate',
                                                       value=2.0,
                                                       group='Session')
        sessionParams = self.params.layout_group('Session')
        self.params['minAmp'] = paramgui.NumericParam('Min noise amplitude (dB)',
                                                       value=40,
                                                       group='Parameters')
        self.params['maxAmp'] = paramgui.NumericParam('Max noise amplitude (dB)',
                                                       value=60,
                                                       group='Parameters')
        self.params['numAmps'] = paramgui.NumericParam('Number of Amplitudes',
                                                       value=2,
                                                       group='Parameters')

        self.params['stimDur'] = paramgui.NumericParam('Stimulus Duration (s)',
                                                        value=1.0,
                                                        group='Parameters')
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus interval mean (s)',
                                                       value=2,
                                                       group='Parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=1,
                                                      group='Parameters')
        self.params['minBand'] = paramgui.NumericParam('Minimum bandwidth (octaves)',
                                                       value=0.25,
                                                       group='Parameters')
        self.params['maxBand'] = paramgui.NumericParam('Maximum bandwidth (octaves)',
                                                       value=2.0,
                                                       group='Parameters')
        self.params['numBands'] = paramgui.NumericParam('Number of bandwiths',
                                                       value=4,
                                                       group='Parameters')
        self.params['randomMode'] = paramgui.MenuParam('Presentation Mode',
                                                         ['Ordered','Random'],
                                                         value=1,group='Parameters')
        self.params['stimType'] = paramgui.MenuParam('Stim Type',
                                                         ['laser_sound', 'band', 'band_AM', 'band_harmonics_AM', 'laser_band_AM'],
                                                         value=2,group='Parameters')
        # -- Added extremes as separate option in case we want to add other stim types (unmodulated white noise) --
        self.params['extremes'] = paramgui.MenuParam('Add extremes?',
                                                         ['yes', 'no'],
                                                         value=0,group='Parameters')
        self.params['laserFrontOverhang'] = paramgui.NumericParam('Laser Front Overhang',value=0,
                                                           group='Parameters',
                                                           decimals=1)
        self.params['laserBackOverhang'] = paramgui.NumericParam('Laser Back Overhang',value=0,
                                                           group='Parameters',
                                                           decimals=1)
        self.params['currentAmp'] = paramgui.NumericParam('Current Amplitude',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=1)
        self.params['currentBand'] = paramgui.NumericParam('Current Bandwidth',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=2)
        self.params['laserTrial'] = paramgui.NumericParam('Laser Trial?',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=0)
        self.params['harmTrialType'] = paramgui.MenuParam('Harmonics type',['none','ordered','random'],
                                                           value=0,enabled=False,
                                                           group='Current Trial')


        timingParams = self.params.layout_group('Parameters')
        trialParams = self.params.layout_group('Current Trial')

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


        layoutMain.addLayout(layoutCol1) #Add the columns to the main layout
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.dispatcherView) #Add the dispatcher to col1
        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.manualControl)

        self.clearButton = QtGui.QPushButton('Clear Stim List', self)
        self.clearButton.clicked.connect(self.clear_tone_list)
        layoutCol1.addWidget(self.clearButton)

        layoutCol2.addWidget(sessionParams)  #Add the parameter GUI to column 2
        layoutCol2.addWidget(timingParams)  #Add the parameter GUI to column 2
        layoutCol2.addWidget(trialParams)

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
        #soundFreq = self.params['soundFreq'].get_value()

        # -- Initialize the list of trial parameters --
        self.trialParams = []
        self.soundParamList = []

    def populate_sound_params(self):

        '''This function reads the GUI inputs and populates a list of three-item tuples
        containing the frequency, and amplitude for each trial. This function is
        called by prepare_next_trial at the beginning of the experiment and whenever
        we run out of combinations of sounds to present'''

        ## -- Get the parameters --

        minBand = self.params['minBand'].get_value()
        maxBand = self.params['maxBand'].get_value()
        numBands = self.params['numBands'].get_value()

        bandList = self.logscale(minBand, maxBand, numBands)
        if self.params['extremes'].get_string() == 'yes':
            extremes = np.array([0, np.inf])
            if self.params['stimType'].get_string() != 'band_harmonics_AM':
                bandList = np.concatenate((bandList, extremes))

        minAmp = self.params['minAmp'].get_value()
        maxAmp = self.params['maxAmp'].get_value()
        numAmps = self.params['numAmps'].get_value()

        ampList = np.linspace(minAmp, maxAmp, num=numAmps)

        # -- Make a tuple list of all of the products of the three parameter lists
        if self.params['stimType'].get_string() == 'laser_band_AM':
            lasList = [0,1]
            productList = list(itertools.product(bandList, ampList, lasList))
        elif self.params['stimType'].get_string() == 'band_harmonics_AM':
            harmList = [0,1]
            bandList = np.concatenate((bandList, np.zeros(1)))
            fullList = list(itertools.product(bandList, ampList, harmList))
            productList = [i for i in fullList if not(i[0]==0 and i[2]==0)] #remove duplicate pure tone trials
        else:
            productList = list(itertools.product(bandList, ampList))
            
        # -- If in random presentation mode, shuffle the list of products
        randomMode = self.params['randomMode'].get_string()
        if randomMode == 'Random':
            random.shuffle(productList)

        # -- Set the sound parameter list to the product list

        self.soundParamList = productList




    def logscale(self, minFreq, maxFreq, numFreqs):
        '''This function returns a specified number of frequencies
        scaled logarithmically between a minimum and maximum val'''

        slope=(np.log2(maxFreq)-np.log2(minFreq))/(numFreqs-1)
        xVals=range(numFreqs)
        logs=[slope * x + np.log2(minFreq) for x in xVals]
        logs=np.array(logs)
        vals=np.exp2(logs)
        return vals

    def prepare_next_trial(self, nextTrial):

        '''
        Prepare the target sound, send state matrix to the statemachine, and
        update the list of GUI parameters so that we can save the history of the
        frequency, intensity, and amplitude parameters for each trial.
        '''

        if nextTrial > 0:  ## Do not update the history before the first trial
            self.params.update_history()

        self.sm.reset_transitions()

        ## -- Choose an ISI randomly
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        isi = self.params['isiMean'].get_value() + \
              self.params['isiHalfRange'].get_value()*randNum


        # -- Get the sound parameters from the parameter list --
        # -- If the parameter list is empty, populate it  --
        try:
            self.trialParams = self.soundParamList.pop(0) #pop(0) pops from the left
        except IndexError:
            self.populate_sound_params()
            self.trialParams = self.soundParamList.pop(0)



        # -- Prepare the sound using randomly chosen parameters from parameter lists --

        stimDur = self.params['stimDur'].get_value()
        charFreq = self.params['charFreq'].get_value()
        modRate = self.params['modRate'].get_value()
        trialAmp = self.noiseCal.find_amplitude(0, self.trialParams[0])
        trialBand = self.trialParams[0]

        # -- Determine the sound presentation mode and prepare the appropriate sound
        stimType = self.params['stimType'].get_string()

        if (stimType == 'band_AM') or (stimType == 'laser_band_AM'):
            if self.trialParams[0] == 0:
                sound = {'type':'tone_AM', 'duration':stimDur, 'amplitude':trialAmp/16.0, 'frequency':charFreq, 'modRate':modRate, 'ntones':1, 'factor':1}
            elif np.isinf(self.trialParams[0]):
                sound = {'type':'AM', 'modFrequency':modRate, 'duration':stimDur, 'amplitude':trialAmp}
            else:
                sound = {'type':'band_AM', 'duration':stimDur, 'amplitude':trialAmp, 'frequency':charFreq, 'modRate':modRate, 'octaves':trialBand}
        elif stimType == 'band_harmonics_AM':
            if self.trialParams[2] == 1:
                sound = {'type':'tone_AM', 'duration':stimDur, 'amplitude':trialAmp/16.0, 'frequency':charFreq, 'modRate':modRate, 'ntones':int(trialBand)+1, 'factor':2**(int(trialBand)/2)}
            else:
                sound = {'type':'band_AM', 'duration':stimDur, 'amplitude':trialAmp, 'frequency':charFreq, 'modRate':modRate, 'octaves':trialBand}
        elif stimType == 'band':
            sound = {'type':'band', 'duration':stimDur, 'amplitude':trialAmp, 'frequency':charFreq, 'octaves':trialBand}
        elif stimType == 'laser_sound':
            sound = {'type':'noise', 'duration':stimDur, 'amplitude':trialAmp}
        stimOutput = stimSync
        serialOutput = 1
        self.soundClient.set_sound(1,sound)
        if stimType == 'band_harmonics_AM':
            if self.trialParams[2] == 1:
                self.params['harmTrialType'].set_value(1)
            else:
                self.params['harmTrialType'].set_value(0)
        if stimType == 'laser_sound':
            laserOutput=laserSync
        elif stimType == 'laser_band_AM':
            if self.trialParams[2] == 1:
                laserOutput=laserSync
                self.params['laserTrial'].set_value(1)
            else:
                laserOutput=[]
                self.params['laserTrial'].set_value(0)

        self.params['currentBand'].set_value(self.trialParams[0])
        self.params['currentAmp'].set_value(self.trialParams[1])
        
        laserFrontOverhang = self.params['laserFrontOverhang'].get_value()
        laserBackOverhang = self.params['laserBackOverhang'].get_value()

        # -- Prepare the state transition matrix --

        if (stimType == 'laser_band_AM') or (stimType == 'laser_sound'):
            self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,  
                          transitions={'Tup':'laserFrontOverhang'})
            self.sm.add_state(name='laserFrontOverhang', statetimer=laserFrontOverhang, 
                          transitions={'Tup':'soundOn'},
                          outputsOn=laserOutput)
            self.sm.add_state(name='soundOn', statetimer = stimDur,
                          transitions={'Tup':'laserBackOverhang'},
                          outputsOn=stimOutput,
                          serialOut=serialOutput)
            self.sm.add_state(name='laserBackOverhang', statetimer = laserBackOverhang,
                          transitions={'Tup':'iti'},
                          outputsOff=stimOutput)
            self.sm.add_state(name='iti', statetimer = 0.5 * isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=laserOutput) 
        else:
            self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,
                              transitions={'Tup':'soundOn'})
            self.sm.add_state(name='soundOn', statetimer=stimDur,
                              transitions={'Tup':'soundOff'},
                              outputsOn=stimOutput,
                              serialOut=serialOutput)
            self.sm.add_state(name='soundOff', statetimer = 0.5 * isi,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=stimOutput)


        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()

    #def _timer_tic(self, etime, lastEvents):
    #    #timer_tic is sent whenever the dispatcher gets information from the Arduino
    #    pass

    def save_to_file(self):
        '''Triggered by button-clicked signal'''
        self.saveData.to_file([self.params, self.dispatcherModel,
                               self.sm],
                              self.dispatcherModel.currentTrial,
                              experimenter='',
                              subject=self.params['subject'].get_value(),
                              paradigm=self.name)

    def clear_tone_list(self):
        '''Allow the user to clear the list of tones and assign new tones from the GUI'''

        print self.soundParamList
        self.soundParamList = []
        print self.soundParamList

    def closeEvent(self, event):
        '''
        Executed when closing the main window.
        This method is inherited from QtGui.QMainWindow, which explains
        its camelCase naming.
        '''
	self.soundClient.shutdown()
        self.dispatcherModel.die()
        event.accept()

if __name__ == "__main__":
    (app,paradigm) = paramgui.create_app(Paradigm)
