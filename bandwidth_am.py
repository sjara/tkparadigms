'''
Presents bandwidth-limited white noise, amplitude modulated and centered at characteristic frequency.
Bandwidth is varied between trials.

Anna Lakunina and Santiago Jaramillo

TODO:
- add back ability to present laser with short noise bursts
- allow laser to be presented after sound onset
'''

from PySide import QtGui
from taskontrol.core import dispatcher
from taskontrol.core import paramgui
from taskontrol.core import savedata
from taskontrol.settings import rigsettings
reload(rigsettings)
from taskontrol.core import statematrix
from taskontrol.plugins import speakercalibration
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
    laserSync = ['outBit2',''] # Sync signal for laser
else:
    laserSync = ['centerLED'] # Use center LED during emulation
    
# dictionary of indices for params so indexing is not so confusing!
paramIndex = {'bandwidth':0,
             'amplitude':1,
             'harmonics':2,
             'laser':3,
             'SNR':4}

TONE_NOISE_DIFF = 15.0 #hardcoded difference in pure tone and noise amplitude that makes the tone have the same power as its corresponding frequency in the noise


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

        # -- Create the speaker calibration objects
        self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)
        self.toneCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_SINE)

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
                                                       group='Sound Parameters')
        self.params['maxAmp'] = paramgui.NumericParam('Max noise amplitude (dB)',
                                                       value=60,
                                                       group='Sound Parameters')
        self.params['numAmps'] = paramgui.NumericParam('Number of Amplitudes',
                                                       value=2,
                                                       group='Sound Parameters')
        self.params['minBand'] = paramgui.NumericParam('Minimum bandwidth (octaves)',
                                                       value=0.25,
                                                       group='Sound Parameters')
        self.params['maxBand'] = paramgui.NumericParam('Maximum bandwidth (octaves)',
                                                       value=2.0,
                                                       group='Sound Parameters')
        self.params['numBands'] = paramgui.NumericParam('Number of bandwidths',
                                                       value=4,
                                                       group='Sound Parameters')
        # -- Added extremes as separate option in case we want to add other stim types (unmodulated white noise) --
        self.params['whiteNoise'] = paramgui.MenuParam('Add white noise to bandwidths?',
                                                         ['yes', 'no'],
                                                         value=0,group='Sound Parameters')
        self.params['pureTone'] = paramgui.MenuParam('Add pure tone to bandwidths?',
                                                         ['yes', 'no'],
                                                         value=1,group='Sound Parameters')
        self.params['soundType'] = paramgui.MenuParam('Sound type',
                                                         ['full_spectrum', 'harmonics', 'both'],
                                                         value=0,group='Sound Parameters')
        self.params['stimDur'] = paramgui.NumericParam('Stimulus Duration (s)',
                                                        value=1.0,
                                                        group='Sound Parameters')
        self.params['isiMean'] = paramgui.NumericParam('Interstimulus interval mean (s)',
                                                       value=2,
                                                       group='Sound Parameters')
        self.params['isiHalfRange'] = paramgui.NumericParam('+/-',
                                                      value=1,
                                                      group='Sound Parameters')
        self.params['randomMode'] = paramgui.MenuParam('Presentation Mode',
                                                         ['Ordered','Random'],
                                                         value=1,group='Sound Parameters')
        soundParams = self.params.layout_group('Sound Parameters')
        
        self.params['signalType'] = paramgui.MenuParam('Include pure tone signal?',
                                                         ['yes', 'no'],
                                                         value=1,group='Signal Parameters')
        self.params['minSNR'] = paramgui.NumericParam('Minimum signal to noise',value=10, decimals=0,
                                                        units='dB',group='Signal Parameters')
        self.params['maxSNR'] = paramgui.NumericParam('Maximum signal to noise',value=20,decimals=0,
                                                        units='dB',group='Signal Parameters')
        self.params['numSNRs'] = paramgui.NumericParam('Number of SNRs', value=3, decimals=0, units='dB', group='Signal Parameters')
        signalParams = self.params.layout_group('Signal Parameters')
        
        self.params['laserPercent'] = paramgui.MenuParam('Percentage of trials with laser',
                                                         ['0%', '50%', '100%'],
                                                         value=1,group='Laser Parameters')
        self.params['laserType'] = paramgui.MenuParam('Laser colour',
                                                         ['blue', 'green'],
                                                         value=1,group='Laser Parameters')
        self.params['laserFrontOverhang'] = paramgui.NumericParam('Laser Front Overhang',value=0,
                                                           group='Laser Parameters',
                                                           decimals=1)
        self.params['laserBackOverhang'] = paramgui.NumericParam('Laser Back Overhang',value=0,
                                                           group='Laser Parameters',
                                                           decimals=1)
        laserParams = self.params.layout_group('Laser Parameters')
        
        self.params['currentAmp'] = paramgui.NumericParam('Current Amplitude',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=1)
        self.params['currentBand'] = paramgui.NumericParam('Current Bandwidth',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=2)
        self.params['currentSNR'] = paramgui.NumericParam('Current SNR',value=0.0,decimals=1,
                                                        units='dB', enabled=False, group='Current Trial')
        self.params['laserTrial'] = paramgui.NumericParam('Laser Trial?',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=0)
        self.params['harmTrialType'] = paramgui.NumericParam('Harmonics Trial?',value=0,
                                                           enabled=False,
                                                           group='Current Trial',
                                                           decimals=0)
        trialParams = self.params.layout_group('Current Trial')

        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)


        # -- Create an empty state matrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS,
                                          outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Module for saving the data --
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
        layoutCol1.addWidget(trialParams)

        self.clearButton = QtGui.QPushButton('Clear Stim List', self)
        self.clearButton.clicked.connect(self.clear_tone_list)
        layoutCol1.addWidget(self.clearButton)

        layoutCol2.addWidget(sessionParams)  #Add the parameter GUI to column 2
        layoutCol2.addWidget(soundParams)
        layoutCol2.addWidget(signalParams)
        layoutCol2.addWidget(laserParams)

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
        
        if numBands>1:
            bandList = self.logscale(minBand, maxBand, numBands)
        elif numBands==1:
            bandList = maxBand #FIXME: using max band if num bands is 1
        
        if self.params['soundType'].get_string() == 'full_spectrum':
            if self.params['whiteNoise'].get_string() == 'yes':
                bandList = np.concatenate((bandList, [np.inf]))
                
        if self.params['pureTone'].get_string() == 'yes':
            bandList = np.concatenate((bandList, [0]))

        minAmp = self.params['minAmp'].get_value()
        maxAmp = self.params['maxAmp'].get_value()
        numAmps = self.params['numAmps'].get_value()

        ampList = np.linspace(minAmp, maxAmp, num=numAmps)
        
        if self.params['laserPercent'].get_string() == '0%':
            lasList = [0]
        elif self.params['laserPercent'].get_string() == '50%':
            lasList = [0,1]
        elif self.params['laserPercent'].get_string() == '100%':
            lasList = [1]
            
        if self.params['soundType'].get_string() == 'full_spectrum':
            harmList = [0]
        elif self.params['soundType'].get_string() == 'harmonics':
            harmList = [1]
        elif self.params['soundType'].get_string() == 'both':
            harmList = [0,1]
            
        if self.params['signalType'].get_string() == 'yes':
            minSNR = self.params['minSNR'].get_value()
            maxSNR = self.params['maxSNR'].get_value()
            numSNR = self.params['numSNRs'].get_value()
    
            SNRList = np.linspace(minSNR, maxSNR, num=numSNR)
            SNRList = np.concatenate((SNRList, [-np.inf]))
        elif self.params['signalType'].get_string() == 'no':
            SNRList = [-np.inf]
        
        # -- Make a tuple list of all of the products of the parameter lists --
        fullList = list(itertools.product(bandList, ampList, harmList, lasList, SNRList))
        productList = [i for i in fullList if not(i[paramIndex['bandwidth']]==0 and i[paramIndex['harmonics']]==1)] #remove duplicate pure tone trials
            
        # -- If in random presentation mode, shuffle the list of products --
        randomMode = self.params['randomMode'].get_string()
        if randomMode == 'Random':
            random.shuffle(productList)

        # -- Set the sound parameter list to the product list

        self.soundParamList = productList
        
        print productList




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

        # -- Set stim to appropriate laser (not during emulation) --
        if len(laserSync)>1:
            if self.params['laserType'].get_string() == 'blue':
                laserSync[1] = 'stim1'
            if self.params['laserType'].get_string() == 'green':
                laserSync[1] = 'stim2'
            

        # -- Prepare the sound using randomly chosen parameters from parameter lists --

        stimDur = self.params['stimDur'].get_value()
        charFreq = self.params['charFreq'].get_value()
        modRate = self.params['modRate'].get_value()
        trialAmp = self.noiseCal.find_amplitude(self.trialParams[paramIndex['amplitude']])[0]
        trialBand = self.trialParams[paramIndex['bandwidth']]

        # -- Determine the sound presentation mode and prepare the appropriate sound --

        if self.trialParams[paramIndex['bandwidth']] == 0:
            noise = {'type':'tone_AM', 'duration':stimDur, 'amplitude':trialAmp/16.0, 'frequency':charFreq, 'modRate':modRate, 'ntones':1, 'factor':1}
        elif np.isinf(self.trialParams[paramIndex['bandwidth']]):
            noise = {'type':'AM', 'modFrequency':modRate, 'duration':stimDur, 'amplitude':trialAmp}
        else:
            if self.trialParams[paramIndex['harmonics']] == 1:
                noise = {'type':'tone_AM', 'duration':stimDur, 'amplitude':trialAmp/16.0, 'frequency':charFreq, 'modRate':modRate, 'ntones':int(trialBand)+1, 'factor':2**(int(trialBand)/2)}
            else:
                noise = {'type':'band_AM', 'duration':stimDur, 'amplitude':trialAmp, 'frequency':charFreq, 'modRate':modRate, 'octaves':trialBand}

        signalAmp = self.toneCal.find_amplitude(charFreq, self.trialParams[paramIndex['amplitude']]+self.trialParams[paramIndex['SNR']]-TONE_NOISE_DIFF)
        signal = {'type':'tone', 'frequency': charFreq, 'duration':stimDur, 'amplitude': signalAmp}
        #noise = {'type':'band', 'duration':stimDur, 'amplitude':trialAmp, 'frequency':charFreq, 'octaves':trialBand}
#         elif stimType == 'laser_sound':
#             noise = {'type':'noise', 'duration':stimDur, 'amplitude':trialAmp}
        stimOutput = stimSync
        noiseID = 1
        signalID = 2
        self.soundClient.set_sound(1,noise)
        self.soundClient.set_sound(2,signal)

        if self.trialParams[paramIndex['laser']] == 1:
            laserOutput=laserSync
        else:
            laserOutput=[]
            
        self.params['currentBand'].set_value(self.trialParams[paramIndex['bandwidth']])
        self.params['currentAmp'].set_value(self.trialParams[paramIndex['amplitude']])
        self.params['harmTrialType'].set_value(self.trialParams[paramIndex['harmonics']])
        self.params['laserTrial'].set_value(self.trialParams[paramIndex['laser']])
        self.params['currentSNR'].set_value(self.trialParams[paramIndex['SNR']])
        
        laserFrontOverhang = self.params['laserFrontOverhang'].get_value()
        laserBackOverhang = self.params['laserBackOverhang'].get_value()

        # -- Prepare the state transition matrix --

        if self.trialParams[paramIndex['laser']] == 1:
            self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,  
                          transitions={'Tup':'laserFrontOverhang'})
            self.sm.add_state(name='laserFrontOverhang', statetimer=laserFrontOverhang, 
                          transitions={'Tup':'soundOn'},
                          outputsOn=laserOutput)
            if np.isinf(self.trialParams[paramIndex['SNR']]):
                self.sm.add_state(name='soundOn', statetimer = stimDur,
                          transitions={'Tup':'laserBackOverhang'},
                          outputsOn=stimOutput,
                          serialOut=noiseID)
            else:
                self.sm.add_state(name='soundOn', statetimer = 0,
                          transitions={'Tup':'signalOn'},
                          outputsOn=stimOutput,
                          serialOut=noiseID)
                self.sm.add_state(name='signalOn', statetimer = stimDur,
                          transitions={'Tup':'laserBackOverhang'},
                          outputsOn=stimOutput,
                          serialOut=signalID)
            self.sm.add_state(name='laserBackOverhang', statetimer = laserBackOverhang,
                          transitions={'Tup':'iti'},
                          outputsOff=stimOutput)
            self.sm.add_state(name='iti', statetimer = 0.5 * isi,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=laserOutput) 
        else:
            self.sm.add_state(name='startTrial', statetimer = 0.5 * isi,
                              transitions={'Tup':'soundOn'})
            if np.isinf(self.trialParams[paramIndex['SNR']]):
                self.sm.add_state(name='soundOn', statetimer=stimDur,
                              transitions={'Tup':'soundOff'},
                              outputsOn=stimOutput,
                              serialOut=noiseID)
            else:
                self.sm.add_state(name='soundOn', statetimer = 0,
                          transitions={'Tup':'signalOn'},
                          outputsOn=stimOutput,
                          serialOut=noiseID)
                self.sm.add_state(name='signalOn', statetimer = stimDur,
                          transitions={'Tup':'soundOff'},
                          outputsOn=stimOutput,
                          serialOut=signalID)
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
