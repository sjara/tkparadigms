"""
Two-alternative choice for head-fixed with two lick ports (right/left).
"""

import numpy as np
import sys
import os
import glob
from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import paramgui as messenger
from taskontrol import utils
from taskontrol.plugins import manualcontrol
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
import time


LONGTIME = 100
MAX_N_TRIALS = 8000

SOUND_DIR = rigsettings.SPEECH_SOUNDS_PATH

SOUND_FILENAME_FORMAT = 'syllable_{0}x_vot{1:03.0f}_ft{2:03.0f}.wav'  # From speechsynth.py
FREQFACTOR_PATTERN = r'_(\d{1})x_'
VOT_PATTERN = r'_vot(\d{3})_'
FT_PATTERN = r'_ft(\d{3}).'

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

        self.name = 'headfixed_speech'

        self.soundFiles = []
        #self.targetSoundID = {}  # Keys are filenames, items are integers to be used as soundID
        self.freqFactor = 0
        self.possibleVOT = 0
        self.possibleFT = 0
        
        # -- Create an empty statematrix --
        self.sm = statematrix.StateMatrix(inputs=rigsettings.INPUTS, outputs=rigsettings.OUTPUTS,
                                          readystate='readyForNextTrial')

        # -- Create dispatcher --
        smServerType = rigsettings.STATE_MACHINE_TYPE
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType,interval=0.1)
        #self.dispatcherView = dispatcher.DispatcherGUI(model=self.dispatcherModel)

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
        self.params['soundsFolder'] = paramgui.StringParam('Sounds folder', value=SOUND_DIR,
                                                           enabled=False, group='Session info')
        self.get_sound_files()  # Defines self.soundFiles, self.possibleVOT and self.possibleFT
        self.sessionInfo = self.params.layout_group('Session info')

        self.params['timeWaterValve'] = paramgui.NumericParam('Time valve',value=timeWaterValve,
                                                                units='s',group='Water delivery')
        waterDelivery = self.params.layout_group('Water delivery')

        
        self.params['targetDuration'] = paramgui.NumericParam('Target duration',value=0,
                                                              decimals=3, enabled=False,
                                                              units='s',group='Timing parameters')
        self.params['lickingPeriod'] = paramgui.NumericParam('Licking period',value=1.5,
                                                        units='s',group='Timing parameters')
        self.params['rewardAvailability'] = paramgui.NumericParam('Reward availability',value=1,
                                                        units='s',group='Timing parameters')
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter trial interval (ITI)',value=0,
                                                                  units='s',group='Timing parameters',
                                                                  decimals=3, enabled=False)
        self.params['addedITI'] = paramgui.NumericParam('Added ITI',value=0,
                                                                  units='s',group='Timing parameters',
                                                                  decimals=3, enabled=False)
        self.params['interTrialIntervalMean'] = paramgui.NumericParam('ITI mean',value=2.5,
                                                        units='s',group='Timing parameters')
        self.params['interTrialIntervalHalfRange'] = paramgui.NumericParam('ITI +/-',value=1,
                                                        units='s',group='Timing parameters')
        #self.params['punishTimeOut'] = paramgui.NumericParam('Time out (punish)',value=1,
        #                                                units='s',group='Timing parameters')
        #self.params['timeLEDon'] = paramgui.NumericParam('Time LED on',value=1,
        #                                                units='s',group='Timing parameters')
        self.params['syncLight'] = paramgui.MenuParam('Sync light',
                                                       ['off', 'leftLED', 'centerLED', 'rightLED'],
                                                       value=0, group='Timing parameters')
        self.params['syncLightDuration'] = paramgui.NumericParam('Sync light duration',value=0,
                                                        units='s',group='Timing parameters')
        self.params['delayFromSyncLightOnset'] = paramgui.NumericParam('Delay from sync light on',value=0,
                                                                units='s',group='Timing parameters',
                                                                decimals=3, enabled=False)
        timingParams = self.params.layout_group('Timing parameters')


        self.params['psycurveMode'] = paramgui.MenuParam('PsyCurve Mode',
                                                         ['off','uniform','extreme80pc'],
                                                         value=0,group='Psychometric parameters')
        self.params['psycurveNsteps'] = paramgui.MenuParam('PsyCurve N steps', ['4','6'],
                                                           value=0,group='Psychometric parameters')
        psychometricParams = self.params.layout_group('Psychometric parameters')


        self.params['relevantFeature'] = paramgui.MenuParam('Relevant feature',
                                                            ['spectral', 'temporal', 'none'],
                                                            value=0,group='Categorization parameters')
        self.params['irrelevantFeatureMode'] = paramgui.MenuParam('Irrelevant feature mode',
                                                                  ['fix_to_min', 'fix_to_max',
                                                                   'random', 'matrix_border'],
                                                                  value=0,group='Categorization parameters')
        #self.params['soundActionMode'] = paramgui.MenuParam('Sound-action mode',
        #                                                    ['low_left','high_left'],
        #                                                    value=0,group='Categorization parameters')
        categorizationParams = self.params.layout_group('Categorization parameters')


        
        self.params['targetVOTpercent'] = paramgui.NumericParam('Target VOT percent', value=0, decimals=0,
                                                                units='percentage', enabled=False,
                                                                group='Sound parameters')
        self.params['targetFTpercent'] = paramgui.NumericParam('Target FT percent', value=0, decimals=0,
                                                                units='percentage', enabled=False,
                                                                group='Sound parameters')
        self.params['targetIntensityMode'] = paramgui.MenuParam('Intensity mode',
                                                                ['fixed','randMinus20'],
                                                                value=0,group='Sound parameters')
        self.params['targetMaxIntensity'] = paramgui.NumericParam('Max intensity',value=70,
                                                                  units='dB-SPL',group='Sound parameters')
        self.params['targetIntensity'] = paramgui.NumericParam('Intensity',value=0.0,units='dB-SPL',
                                                               enabled=False,group='Sound parameters')
        self.params['targetAmplitude'] = paramgui.NumericParam('Target amplitude',value=0.0,units='[0-1]',
                                                        enabled=False,decimals=4,group='Sound parameters')
        self.params['soundLocation'] = paramgui.MenuParam('Sound location',
                                                          ['binaural', 'left', 'right'],
                                                          value=0, group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')

        '''
        self.params['highFreq'] = paramgui.NumericParam('High frequency', value=13000, units='Hz',
                                                        group='Sound parameters')
        self.params['lowFreq'] = paramgui.NumericParam('Low frequency', value=6000, units='Hz',
                                                        group='Sound parameters')
        self.params['targetFrequency'] = paramgui.NumericParam('Target frequency', value=0,
                                                               decimals=0, units='Hz', enabled=False,
                                                               group='Sound parameters')
        self.params['highAMrate'] = paramgui.NumericParam('High mod rate',value=32,
                                                        units='Hz',group='Sound parameters')
        self.params['lowAMrate'] = paramgui.NumericParam('Low mod rate',value=8,
                                                        units='Hz',group='Sound parameters')
        self.params['targetAMrate'] = paramgui.NumericParam('Target AM rate', value=0,
                                                               decimals=1, units='Hz', enabled=False,
                                                               group='Sound parameters')
        self.params['targetCloudStrength'] = paramgui.NumericParam('Target cloud strength', value=0,
                                                               decimals=0, units='[-100,100]', enabled=False,
                                                               group='Sound parameters')
        self.params['highAMdepth'] = paramgui.NumericParam('High AM depth', value=100, units='',
                                                           group='Sound parameters')
        self.params['lowAMdepth'] = paramgui.NumericParam('Low AM depth', value=0, units='',
                                                          group='Sound parameters')
        self.params['targetAMdepth'] = paramgui.NumericParam('Target AM depth', value=0,
                                                             decimals=0, units='', enabled=False,
                                                             group='Sound parameters')
        self.params['targetFMslope'] = paramgui.NumericParam('Target FM slope', value=0,
                                                             decimals=2, units='', enabled=False,
                                                             group='Sound parameters')
        self.params['startFreq'] = paramgui.NumericParam('FM start frequency', value=0, units='Hz', decimals=0,
                                                         enabled=False, group='Sound parameters')
        self.params['targetDuration'] = paramgui.NumericParam('Target duration', value=0.5, units='s',
                                                              group='Sound parameters')
        self.params['targetIntensity'] = paramgui.NumericParam('Target intensity', value=50,
                                                               units='dB-SPL', enabled=True,
                                                               group='Sound parameters')
        self.params['targetAmplitude'] = paramgui.NumericParam('Target amplitude',value=0.0,
                                                               units='[0-1]', enabled=False,
                                                               decimals=4, group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')
        '''

        
        self.params['punishmentSound'] = paramgui.MenuParam('Punishment Sound Type',
        						    ['white_noise', 'chord'], value = 0,
        						    group = 'Punishment parameters', enabled=False)
        self.params['punishmentFrequency'] =paramgui.NumericParam('Punishment frequency', value=13000,
                                                                  units='Hz', enabled=False,
                                                                  group='Punishment parameters')
        self.params['punishmentIntensity'] = paramgui.NumericParam('Punishment intensity',value=70,
                                                              units='dB-SPL',enabled=True,
                                                              group='Punishment parameters')
        self.params['punishmentDuration'] = paramgui.NumericParam('Punishment duration',value=0.1,
                                                        units='s', group='Punishment parameters')
        punishmentParams = self.params.layout_group('Punishment parameters')

        self.params['lickBeforeStimOffset'] = paramgui.MenuParam('Lick before stim offset',
                                                           ['reward','ignore','abort','punish'], value=0,
                                                           group='Choice parameters')
        self.params['rewardSideMode'] = paramgui.MenuParam('Reward side mode',
                                                           ['random','toggle','onlyL','onlyR',
                                                            'repeat_mistake'], value=0,
                                                           group='Choice parameters')
        self.params['rewardSide'] = paramgui.MenuParam('Reward side', ['left','right'], value=0,
                                                       enabled=False, group='Choice parameters')
        self.params['taskMode'] = paramgui.MenuParam('Task mode',
                                                     ['water_after_sound','water_on_lick',
                                                      'lick_on_stim','discriminate_stim'],
                                                     value=0, group='Choice parameters')
        choiceParams = self.params.layout_group('Choice parameters')

        
        '''
        self.params['stimType'] = paramgui.MenuParam('Stim type',
                                                     ['sound_and_light', 'sound_only', 'light_only'],
                                                     value=1, group='General parameters')
        self.params['soundType'] = paramgui.MenuParam('Sound type',
                                                      ['chords', 'AM_rate','AM_depth','AM_vs_chord',
                                                       'tone_cloud', 'FM_direction'],
                                                      value=0,group='General parameters')
        self.params['psycurveMode'] = paramgui.MenuParam('PsyCurve Mode',
                                                         ['off', 'uniform', 'mid_and_extreme'],
                                                         value=0,group='General parameters')
        self.params['psycurveNsteps'] = paramgui.NumericParam('N steps',value=6,decimals=0,
                                                              group='General parameters')
        generalParams = self.params.layout_group('General parameters')
        '''

        self.params['nHitsLeft'] = paramgui.NumericParam('Hits L',value=0, enabled=False,
                                                             units='trials',group='Report')
        self.params['nHitsRight'] = paramgui.NumericParam('Hits R',value=0, enabled=False,
                                                             units='trials',group='Report')
        self.params['nErrorsLeft'] = paramgui.NumericParam('Errors L',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nErrorsRight'] = paramgui.NumericParam('Errors R',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nFalseAlarmsLeft'] = paramgui.NumericParam('False alarms L',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nFalseAlarmsRight'] = paramgui.NumericParam('False alarms R',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nEarlyLicksLeft'] = paramgui.NumericParam('Early licks L',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nEarlyLicksRight'] = paramgui.NumericParam('Early licks R',value=0, enabled=False,
                                                      units='trials',group='Report')       
        '''
        self.params['nFalseAlarms'] = paramgui.NumericParam('False alarms',value=0, enabled=False,
                                                      units='trials',group='Report')
        '''
        self.params['nMissesLeft'] = paramgui.NumericParam('Misses L',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nMissesRight'] = paramgui.NumericParam('Misses R',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nLicksLeft'] = paramgui.NumericParam('Licks L',value=0, enabled=False,
                                                      units='trials',group='Report')
        self.params['nLicksRight'] = paramgui.NumericParam('Licks R',value=0, enabled=False,
                                                      units='trials',group='Report')
        reportInfo = self.params.layout_group('Report')


        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()
        layoutCol3 = QtWidgets.QVBoxLayout()
        layoutCol4 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)
        layoutMain.addLayout(layoutCol3)
        layoutMain.addLayout(layoutCol4)

        layoutCol1.addWidget(self.singleDrop)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.saveData)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addStretch()
        layoutCol1.addWidget(self.dispatcher.widget)

        layoutCol2.addWidget(self.manualControl)
        layoutCol2.addStretch()
        layoutCol2.addWidget(reportInfo)
 
        layoutCol3.addWidget(soundParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(psychometricParams)
        layoutCol3.addStretch()
        layoutCol3.addWidget(categorizationParams)
        layoutCol3.addWidget(waterDelivery)
        layoutCol3.addStretch()

        layoutCol4.addWidget(punishmentParams)
        layoutCol4.addStretch()
        layoutCol4.addWidget(timingParams)
        layoutCol4.addStretch()
        layoutCol4.addWidget(choiceParams)
        #layoutCol4.addStretch()
        #layoutCol4.addWidget(generalParams)
        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = MAX_N_TRIALS # Preallocating space for each vector makes things easier
        self.results = utils.EnumContainer()
        self.results.labels['outcome'] = {'hit':1, 'error':0,'falseAlarm':3, 'miss':2, 'none':-1, 'punishments': 4}
        self.results['outcome'] = np.empty(maxNtrials,dtype=int)
        self.results.labels['choice'] = {'left':0,'right':1,'none':2}
        self.results['choice'] = np.empty(maxNtrials,dtype=int)
        
        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

        # -- Load speaker calibration --
        #self.sineCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_SINE)
        #self.chordCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        #self.noiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        self.spkNoiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_CALIBRATION_NOISE)
        try:
            self.spkVowelCal = speakercalibration.VowelCalibration(rigsettings.SPEAKER_CALIBRATION_VOWEL)
            self.VOWEL_CALIBRATION = True
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.warning(self, "WARNING!",
                                          "This rig has not been calibrated for speech sounds.")
            self.VOWEL_CALIBRATION = False

        # -- Connect to sound server and define sounds --
        print('Conecting to soundserver...')
        print('***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****') ### DEBUG
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.soundClient.start()

        self.targetSoundID = 1
        self.punishSoundID = 3   

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
        
    def prepare_punish_sound(self, punishmentSound, soundParam):
        punishmentIntensity = self.params['punishmentIntensity'].get_value()
        punishmentDuration = self.params['punishmentDuration'].get_value()
        if punishmentSound =='chord':
            punishmentFrequency = soundParam
            punishmentAmp = self.chordCal.find_amplitude(punishmentFrequency,punishmentIntensity).mean()
            s3 = {'type':'chord', 'frequency':punishmentFrequency, 'duration':punishmentDuration,
                  'amplitude':punishmentAmp, 'ntones':12, 'factor':1.2}
        elif punishmentSound == 'white_noise':
            #modDepth = soundParam        
            punishmentAmp = self.spkNoiseCal.find_amplitude(punishmentIntensity).mean()
            #modFrequency = 10
            s3 = {'type':'noise', 'duration':punishmentDuration, 'amplitude':punishmentAmp} 
        self.soundClient.set_sound(self.punishSoundID,s3)         


    def get_sound_files(self):
        import re
        soundFolder = self.params['soundsFolder'].get_value()
        self.soundFiles = glob.glob(os.path.join(soundFolder,'*.wav'))
        nFiles = len(self.soundFiles)
        eachVOT = np.empty(nFiles, dtype=int)
        eachFT = np.empty(nFiles, dtype=int)
        self.soundIDdict = {}
        for indsf, oneFile in enumerate(self.soundFiles):
            self.soundIDdict[oneFile] = indsf+1
            self.soundIDdict[indsf] = oneFile
            eachVOT[indsf] = re.search(VOT_PATTERN, oneFile).group(1)
            eachFT[indsf] = re.search(FT_PATTERN, oneFile).group(1)
        self.possibleVOT = np.unique(eachVOT)
        self.possibleFT = np.unique(eachFT)
        self.freqFactor = re.search(FREQFACTOR_PATTERN, oneFile).group(1)


    def prepare_target_sound(self, soundFilename):
        soundLocation = self.params['soundLocation'].get_string()
        if self.params['targetIntensityMode'].get_string() == 'randMinus20':
            possibleIntensities = self.params['targetMaxIntensity'].get_value()+\
                                  np.array([-20,-15,-10,-5,0])
            targetIntensity = possibleIntensities[np.random.randint(len(possibleIntensities))]
        else:
            targetIntensity = self.params['targetMaxIntensity'].get_value()
        self.params['targetIntensity'].set_value(targetIntensity)
        if self.VOWEL_CALIBRATION:
            targetAmp = self.spkVowelCal.find_amplitude(targetIntensity).mean()
        else:
            # FIXME: currently I am averaging calibration from both speakers (not good)
            targetFrequency = 10000
            targetAmp = self.spkCal.find_amplitude(targetFrequency,targetIntensity).mean()
        self.params['targetAmplitude'].set_value(targetAmp)
        if soundLocation == 'left':
            soundDict = {'type':'fromfile', 'filename':soundFilename, 'amplitude':[targetAmp, 0]}
        elif soundLocation == 'right':
            soundDict = {'type':'fromfile', 'filename':soundFilename, 'amplitude':[0, targetAmp]}
        else:
            soundDict = {'type':'fromfile', 'filename':soundFilename, 'amplitude':targetAmp}
        thisSound = self.soundClient.set_sound(self.targetSoundID, soundDict)
        self.params['targetDuration'].set_value(thisSound.get_duration())
        
    '''
    def prepare_target_sound(self, soundType, soundParam):
        """
        The meaning of soundParam depends on the soundType. For example:
        for soundType='chords', soundParam is the target frequency,
        for soundType='AM_depth', soundParam is the modulation depth.
        """
        #targetFrequency = 6000
        targetIntensity = self.params['targetIntensity'].get_value()
        targetDuration = self.params['targetDuration'].get_value()
        # FIXME: currently I am averaging calibration from both speakers (not good)
        if soundType == 'chords':
            targetFrequency = soundParam
            targetAmp = self.chordCal.find_amplitude(targetFrequency,targetIntensity).mean()
            s1 = {'type':'chord', 'frequency':targetFrequency, 'duration':targetDuration,
                  'amplitude':targetAmp, 'ntones':12, 'factor':1.2}
        elif soundType == 'AM_rate':
            targetRate = soundParam
            modDepth = 100
            self.params['targetAMdepth'].set_value(modDepth)
            targetAmp = self.noiseCal.find_amplitude(targetIntensity).mean()
            s1 = {'type':'AM', 'modFrequency':targetRate, 'duration':targetDuration,
                  'modDepth':modDepth, 'amplitude':targetAmp}
        elif soundType == 'AM_depth':
            modDepth = soundParam
            targetAmp = self.noiseCal.find_amplitude(targetIntensity).mean()
            modFrequency = 10
            self.params['targetAMrate'].set_value(modFrequency)
            s1 = {'type':'AM', 'modFrequency':modFrequency, 'duration':targetDuration,
                  'modDepth':modDepth, 'amplitude':targetAmp}
        if soundType == 'tone_cloud':
            cloudStrength = soundParam  # A value bewteen -100 and 100
            highestFreq = self.params['highFreq'].get_value()
            lowestFreq = self.params['lowFreq'].get_value()
            factorToMidpoint = np.power(highestFreq/lowestFreq,1/6)
            centerHighThird = highestFreq/factorToMidpoint
            centerLowThird = lowestFreq*factorToMidpoint
            s1 = {'type':'toneCloud', 'duration':targetDuration, 'amplitude':0,
                  'freqRange':[lowestFreq,highestFreq], 'nFreq':18, 'toneDuration':0.03,
                  'toneOnsetAsync': 0.01, 'strength':soundParam}
            freqEachTone = np.logspace(*np.log10(s1['freqRange']), s1['nFreq'])
            calibArray = self.sineCal.find_amplitudes(freqEachTone, targetIntensity).mean(axis=1)
            s1.update({'amplitude':1, 'calibration':calibArray})
            targetAmp = 0 # Set to zero since it doesn't mean anything in this case
        elif soundType == 'FM_direction':
            targetFMslope = soundParam  # [-1,1]
            highFreq = self.params['highFreq'].get_value()
            lowFreq = self.params['lowFreq'].get_value()
            midFreq = np.sqrt(lowFreq*highFreq)
            halfRange = highFreq/midFreq
            frequencyStart = np.exp( np.log(midFreq) - targetFMslope*np.log(halfRange) )
            frequencyEnd = np.exp( np.log(midFreq) + targetFMslope*np.log(halfRange) )
            self.params['startFreq'].set_value(frequencyStart)
            targetAmp = self.sineCal.find_amplitude(midFreq, targetIntensity).mean()
            s1 = {'type':'FM', 'frequencyStart':frequencyStart, 'frequencyEnd':frequencyEnd,
                  'duration':targetDuration, 'amplitude':targetAmp}
        self.params['targetAmplitude'].set_value(targetAmp)
        self.soundClient.set_sound(self.targetSoundID,s1)
    '''
        
    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.params.update_history(nextTrial-1)
            self.calculate_results(nextTrial-1)
            lastTrialWasRewarded = self.results['outcome'][nextTrial-1] == \
                                   self.results.labels['outcome']['hit']
        else:
            lastTrialWasRewarded = True

        # -- Prepare next trial --
        targetDuration = self.params['targetDuration'].get_value()
        taskMode = self.params['taskMode'].get_string()
        rewardAvailability = self.params['rewardAvailability'].get_value()
        punishmentDuration = self.params['punishmentDuration'].get_value()  
        punishmentFrequency = self.params['punishmentFrequency'].get_value()
        
        timeWaterValve = self.params['timeWaterValve'].get_value()
        interTrialIntervalMean = self.params['interTrialIntervalMean'].get_value()
        interTrialIntervalHalfRange = self.params['interTrialIntervalHalfRange'].get_value()
        addedITI = self.params['addedITI'].get_value()
        randNum = (2*np.random.random(1)[0]-1)
        interTrialInterval = interTrialIntervalMean + randNum*interTrialIntervalHalfRange + addedITI
        self.params['interTrialInterval'].set_value(interTrialInterval)
        lickingPeriod = self.params['lickingPeriod'].get_value()
        lickBeforeStimOffset = self.params['lickBeforeStimOffset'].get_string()

        lastRewardSide = self.params['rewardSide'].get_string()
        rewardSideMode = self.params['rewardSideMode'].get_string()
        possibleSides = ['left','right']
        if rewardSideMode=='toggle':
            if lastRewardSide=='left':
                nextRewardSide = 'right'
            else:
                nextRewardSide = 'left'
        elif rewardSideMode=='random':
            nextRewardSide = possibleSides[np.random.randint(2)]
        elif rewardSideMode=='repeat_mistake':
            if lastTrialWasRewarded:
                nextRewardSide = possibleSides[np.random.randint(2)]
            else:
                nextRewardSide = lastRewardSide
        elif rewardSideMode=='onlyL':
                nextRewardSide = 'left'
        elif rewardSideMode=='onlyR':
                nextRewardSide = 'right'
        self.params['rewardSide'].set_string(nextRewardSide)

        if nextRewardSide=='left':
            rewardedEvent = 'Lin'
            punishedEvent = 'Rin'
            rewardOutput = 'leftWater'
            targetLED = 'leftLED'
        elif nextRewardSide=='right':
            rewardedEvent = 'Rin'
            punishedEvent = 'Lin'
            rewardOutput = 'rightWater'
            targetLED = 'rightLED'
        
        # -- Prepare sound --
        relevantFeature = self.params['relevantFeature'].get_string()
        if relevantFeature == 'spectral':
            targetPercentageParam = self.params['targetFTpercent']
            irrelevantParam = self.params['targetVOTpercent']
        elif relevantFeature == 'temporal':
            targetPercentageParam = self.params['targetVOTpercent']
            irrelevantParam = self.params['targetFTpercent']
        elif relevantFeature == 'none':
            self.params['irrelevantFeatureMode'].set_string('matrix_border')
            targetPercentageParam = self.params['targetFTpercent']
            irrelevantParam = self.params['targetVOTpercent']
        else:
            raise ValueError(f'Relevant feature "{relevantFeature}" not implemented')

        psycurveMode = self.params['psycurveMode'].get_string()
        psycurveNsteps = int(self.params['psycurveNsteps'].get_string())
        if psycurveMode=='off':
            if nextRewardSide=='left':
                targetPercentage = 0
            elif nextRewardSide=='right':
                targetPercentage = 100
        elif psycurveMode=='uniform':
            randIndex = np.random.randint(psycurveNsteps//2)
            possibleValues = np.round(np.linspace(0, 100, psycurveNsteps)).astype(int)
            if nextRewardSide=='left':
                targetPercentage = possibleValues[randIndex]
            elif nextRewardSide=='right':
                targetPercentage = possibleValues[randIndex+psycurveNsteps//2]
        elif psycurveMode=='extreme80pc':
            # -- It assumes 6 possible values. 80% trials on extremes, 20% on the rest --
            randIndex = np.flatnonzero(np.random.multinomial(1,[0.8, 0.1, 0.1]))[0]
            if nextRewardSide=='left':
                targetPercentage = randIndex*20
            elif nextRewardSide=='right':
                targetPercentage = (5-randIndex)*20
        targetPercentageParam.set_value(targetPercentage)

        irrelevantFeatureMode = self.params['irrelevantFeatureMode'].get_string()
        if irrelevantFeatureMode=='fix_to_min':
            irrelevantParam.set_value(0)
        elif irrelevantFeatureMode=='fix_to_max':
            irrelevantParam.set_value(100)
        elif irrelevantFeatureMode=='random':
            if psycurveMode=='off':
                psycurveNsteps = 2
            possibleIrrelValues = np.round(np.linspace(0, 100, psycurveNsteps)).astype(int)
            irrelevantFeaturePercent = np.random.choice(possibleIrrelValues, 1)[0]
            irrelevantParam.set_value(irrelevantFeaturePercent)
        elif irrelevantFeatureMode=='matrix_border':
            # NOTE: this mode overwrites values for targetPercentage
            self.params['relevantFeature'].set_string('none')
            if psycurveMode=='off':
                psycurveNsteps = 2
            possibleValuesEither = np.round(np.linspace(0, 100, psycurveNsteps)).astype(int)
            valsVOT, valsFT = np.meshgrid(possibleValuesEither, possibleValuesEither)
            border = lambda arr: np.concatenate([arr[0,:-1], arr[:-1,-1],
                                                 arr[-1,::-1], arr[-2:0:-1,0]])
            borderVOT = border(valsVOT)
            borderFT = border(valsFT)
            pairInd = np.random.randint(len(borderVOT))
            self.params['targetVOTpercent'].set_value(borderVOT[pairInd])
            self.params['targetFTpercent'].set_value(borderFT[pairInd])

        VOTpc = self.params['targetVOTpercent'].get_value()
        FTpc = self.params['targetFTpercent'].get_value()
        filename = SOUND_FILENAME_FORMAT.format(self.freqFactor, VOTpc, FTpc)

        soundFolder = self.params['soundsFolder'].get_value()
        soundKey = os.path.join(soundFolder, filename)

        '''
        psycurveMode = self.params['psycurveMode'].get_string()
        lowFreq = self.params['lowFreq'].get_value()
        highFreq = self.params['highFreq'].get_value()
        lowAMrate = self.params['lowAMrate'].get_value()
        highAMrate = self.params['highAMrate'].get_value()
        nSteps = self.params['psycurveNsteps'].get_value()
        possibleFreqs = np.logspace(np.log10(lowFreq), np.log10(highFreq), nSteps)
        possibleAMrates = np.logspace(np.log10(lowAMrate), np.log10(highAMrate), nSteps)
        possibleStrengths = np.linspace(-100, 100, nSteps)
        freqBoundary = np.sqrt(lowFreq*highFreq)
        leftFreqInds = np.flatnonzero(possibleFreqs<freqBoundary)
        rightFreqInds = np.flatnonzero(possibleFreqs>freqBoundary)

        if nextRewardSide=='left':
            self.params['rewardSide'].set_string('left')
            rewardedEvent = 'Lin'
            punishedEvent = 'Rin'
            rewardOutput = 'leftWater'
            targetLED = 'leftLED'
            targetAMdepth = self.params['lowAMdepth'].get_value()
            targetFMslope = -1
            if psycurveMode=='uniform':
                freqIndex = np.random.randint(len(leftFreqInds))
                strengthIndex = np.random.randint(int(nSteps/2))
                # FIXME: temporary hack to enable psychometric during FM
                if self.params['soundType'].get_string()=='FM_direction':
                    #possibleFMslopes = np.linspace(1, -1, nSteps) # This was used until 2021-10-21
                    possibleFMslopes = np.linspace(-1, 1, nSteps) # This was enabled on 2021-10-22
                    randIndex = np.random.randint(nSteps//2) # WARNING: nSteps needs to be even
                    targetFMslope = possibleFMslopes[randIndex]
            elif psycurveMode=='mid_and_extreme':
                freqSubset = [0, nSteps//2-1] 
                freqIndex = freqSubset[np.random.randint(len(freqSubset))]
            else:
                freqIndex = 0  # Lowest freq
                strengthIndex = 0  # strength=-100 (100% low)
        elif nextRewardSide=='right':
            self.params['rewardSide'].set_string('right')
            rewardedEvent = 'Rin'
            punishedEvent = 'Lin'
            rewardOutput = 'rightWater'
            targetLED = 'rightLED'
            targetAMdepth = self.params['highAMdepth'].get_value()
            targetFMslope = 1
            if psycurveMode=='uniform':
                freqIndex = np.random.randint(len(rightFreqInds))+len(leftFreqInds)
                strengthIndex = np.random.randint(int(nSteps/2)) + int(nSteps/2)
                # FIXME: temporary hack to enable psychometric during FM
                if self.params['soundType'].get_string()=='FM_direction':
                    #possibleFMslopes = np.linspace(1, -1, nSteps) # This was used until 2021-10-21
                    possibleFMslopes = np.linspace(-1, 1, nSteps) # This was enabled on 2021-10-22
                    randIndex = np.random.randint(nSteps//2) # WARNING: nSteps needs to be even
                    targetFMslope = possibleFMslopes[randIndex + (nSteps//2)]
            elif psycurveMode=='mid_and_extreme':
                freqSubset = [nSteps//2, nSteps-1] 
                freqIndex = freqSubset[np.random.randint(len(freqSubset))]
            else:
                freqIndex = -1 # Highest freq
                strengthIndex = -1  # strength=100 (100% high)

        targetFrequency = possibleFreqs[freqIndex]
        targetAMrate = possibleAMrates[freqIndex]
        targetCloudStrength = possibleStrengths[strengthIndex]
        soundType = self.params['soundType'].get_string()
        if soundType == 'chords':
            self.params['targetFrequency'].set_value(targetFrequency)
            self.prepare_target_sound(soundType, targetFrequency)
        elif soundType == 'AM_rate':
            self.params['targetAMrate'].set_value(targetAMrate)
            self.prepare_target_sound(soundType, targetAMrate)
        elif soundType == 'AM_depth':
            self.params['targetAMdepth'].set_value(targetAMdepth)
            self.prepare_target_sound(soundType, targetAMdepth)
        elif soundType == 'AM_vs_chord':
            if nextRewardSide=='left':
                targetAMdepth = self.params['lowAMdepth'].get_value()
                self.params['targetAMdepth'].set_value(targetAMdepth)
                self.prepare_target_sound('AM_depth', targetAMdepth)
            if nextRewardSide=='right':
                self.params['targetFrequency'].set_value(highFreq)
                self.prepare_target_sound('chords', targetFrequency)
        elif soundType == 'tone_cloud':
            self.params['targetCloudStrength'].set_value(targetCloudStrength)
            self.prepare_target_sound(soundType, targetCloudStrength)
        elif soundType == 'FM_direction':
            self.params['targetFMslope'].set_value(targetFMslope)
            self.prepare_target_sound(soundType, targetFMslope)
        '''
        
        punishmentSound = self.params['punishmentSound'].get_string()           
        if punishmentSound == 'chord':
            self.params['punishmentFrequency'].set_value(punishmentFrequency)
            self.prepare_punish_sound(punishmentSound, punishmentFrequency)
        elif punishmentSound == 'white_noise':
            self.prepare_punish_sound(punishmentSound, None)
        punishsoundOutput = self.punishSoundID

        #delayToSyncLight = self.params['delayToSyncLight'].get_value()
        syncLightDuration = self.params['syncLightDuration'].get_value()
        syncLightPortStr = self.params['syncLight'].get_string()
        if syncLightPortStr=='off':
            syncLightPort = []
        else:
            syncLightPort = [syncLightPortStr]
        self.params['delayFromSyncLightOnset'].set_value(interTrialInterval)
        
        '''
        stimType = self.params['stimType'].get_string()
        if (stimType=='sound_and_light') | (stimType=='sound_only'):
            soundOutput = self.targetSoundID
            stimOutput = stimSync
        else:
            soundOutput = soundclient.STOP_ALL_SOUNDS
            stimOutput = stimSync
        if (stimType=='sound_and_light') | (stimType=='light_only'):
            lightOutput = [targetLED]
            stimOutput = stimSync + ['leftLED','rightLED']
        else:
            lightOutput = []
        '''
        # Sound only
        soundOutput = self.targetSoundID
        stimOutput = stimSync
        lightOutput = []

        self.prepare_target_sound(soundKey)
       
        self.sm.reset_transitions()

        if taskMode == 'water_after_sound':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'delayPeriod'})
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval,
                              transitions={'Tup':'playTarget'})
            if lickBeforeStimOffset=='punish':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Lin':'earlyLickL', 'Rin': 'earlyLickR',
                                               'Tup': 'reward'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='ignore' or 'abort' or 'reward':
            	self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Tup':'reward'},
                                  serialOut=soundOutput)            
            else:
                raise ValueError(f'Lick mode: "{lickBeforeStimOffset}" has not been implemented')
            self.sm.add_state(name='earlyLickL', statetimer=0, 
            		       transitions={'Tup': 'punishment'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='earlyLickR', statetimer=0, 
            		       transitions={'Tup': 'punishment'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='punishment', statetimer=punishmentDuration,
                              transitions={'Tup': 'readyForNextTrial'},
            		       serialOut= punishsoundOutput)
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=[rewardOutput])
            self.sm.add_state(name='lickingPeriod', statetimer=lickingPeriod,
                              transitions={'Tup':'readyForNextTrial'})
            # -- A few empty states necessary to avoid errors when changing taskMode --
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='error')            
            self.sm.add_state(name='miss')            
            self.sm.add_state(name='falseAlarmL')            
            self.sm.add_state(name='falseAlarmR')
        elif taskMode == 'water_on_lick':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForLick'},
                              outputsOff=['centerLED'])
            self.sm.add_state(name='waitForLick', statetimer=LONGTIME,
                              transitions={rewardedEvent:'reward'})
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput]+lightOutput,
                              serialOut=soundOutput)
            self.sm.add_state(name='stopReward', statetimer=interTrialInterval,
                              transitions={'Tup':'readyForNextTrial'},
                              outputsOff=[rewardOutput]+lightOutput)
            # -- A few empty states necessary to avoid errors when changing taskMode --
            self.sm.add_state(name='hit')            
            self.sm.add_state(name='error')            
            self.sm.add_state(name='miss')            
            self.sm.add_state(name='falseAlarmL')            
            self.sm.add_state(name='falseAlarmR')            
        elif taskMode == 'lick_on_stim':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'syncLightOn'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='syncLightOn', statetimer=syncLightDuration,
                              transitions={'Tup':'syncLightOff'},
                              outputsOn=syncLightPort)
            self.sm.add_state(name='syncLightOff', statetimer=0,
                              transitions={'Tup':'delayPeriod'},
                              outputsOff=syncLightPort)
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval-syncLightDuration,
                              transitions={'Lin':'falseAlarmL', 'Rin':'falseAlarmR',
                                           'Tup':'playTarget'})
            if lickBeforeStimOffset=='reward':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={rewardedEvent:'hit', 'Tup':'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='ignore':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Tup':'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='abort':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Lin':'falseAlarmL', 'Rin':'falseAlarmR',
                                               'Tup':'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='punish':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Lin':'earlyLickL', 'Rin': 'earlyLickR',
                                               'Tup': 'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            else:
                raise ValueError(f'Lick mode: "{lickBeforeStimOffset}" has not been implemented')
            self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                              transitions={rewardedEvent:'hit', punishedEvent:'error', 'Tup':'miss'},
                              outputsOff=['centerLED','rightLED','leftLED']+stimOutput)
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'},
                              outputsOff=['centerLED','rightLED','leftLED']+stimOutput)
            self.sm.add_state(name='error', statetimer=0,
                              transitions={'Tup':'waitForLick'},
                              outputsOff=['centerLED','rightLED','leftLED']+stimOutput)            
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='falseAlarmL', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='falseAlarmR', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)    
            self.sm.add_state(name='earlyLickL', statetimer=0, 
            		       transitions={'Tup': 'punishment'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='earlyLickR', statetimer=0, 
            		       transitions={'Tup': 'punishment'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='punishment', statetimer=punishmentDuration,
                              transitions={'Tup': 'readyForNextTrial'},
            		       serialOut= punishsoundOutput)
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=[rewardOutput])
            self.sm.add_state(name='lickingPeriod', statetimer=lickingPeriod,
                              transitions={'Tup':'readyForNextTrial'})
        elif taskMode == 'discriminate_stim':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'syncLightOn'},
                              outputsOff=['centerLED','rightLED','leftLED'])
            self.sm.add_state(name='syncLightOn', statetimer=syncLightDuration,
                              transitions={'Tup':'syncLightOff'},
                              outputsOn=syncLightPort)
            self.sm.add_state(name='syncLightOff', statetimer=0,
                              transitions={'Tup':'delayPeriod'},
                              outputsOff=syncLightPort)
            self.sm.add_state(name='delayPeriod', statetimer=interTrialInterval-syncLightDuration,
                              transitions={'Lin':'falseAlarmL', 'Rin':'falseAlarmR','Tup':'playTarget'})
            if lickBeforeStimOffset=='reward':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={rewardedEvent:'hit', punishedEvent:'error',
                                               'Tup':'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='ignore':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={punishedEvent:'error', 'Tup':'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='abort':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Lin':'falseAlarmL', 'Rin':'falseAlarmR',
                                               'Tup':'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            elif lickBeforeStimOffset=='punish':
                self.sm.add_state(name='playTarget', statetimer=targetDuration,
                                  transitions={'Lin':'earlyLickL', 'Rin': 'earlyLickR',
                                               'Tup': 'waitForLick'},
                                  outputsOn=lightOutput+stimOutput, serialOut=soundOutput)
            else:
                raise ValueError(f'Lick mode: "{lickBeforeStimOffset}" has not been implemented')
            self.sm.add_state(name='waitForLick', statetimer=rewardAvailability,
                              transitions={rewardedEvent:'hit', punishedEvent:'error',
                                           'Tup':'miss'},
                              outputsOff=['centerLED','rightLED','leftLED']+stimOutput)
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'},
                              outputsOff=['centerLED','rightLED','leftLED']+stimOutput)            
            self.sm.add_state(name='error', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=['centerLED','rightLED','leftLED']+stimOutput)            
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'})
            self.sm.add_state(name='falseAlarmL', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)            
            self.sm.add_state(name='falseAlarmR', statetimer=0,
                              transitions={'Tup':'readyForNextTrial'},
                              serialOut=soundclient.STOP_ALL_SOUNDS) 
            self.sm.add_state(name='earlyLickL', statetimer=0, 
            		       transitions={'Tup': 'punishment'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='earlyLickR', statetimer=0, 
            		       transitions={'Tup': 'punishment'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)     
            self.sm.add_state(name='punishment', statetimer=punishmentDuration,
                              transitions={'Tup': 'readyForNextTrial'},
            		       serialOut= punishsoundOutput)     
            self.sm.add_state(name='reward', statetimer=timeWaterValve,
                              transitions={'Tup':'stopReward'},
                              outputsOn=[rewardOutput])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'lickingPeriod'},
                              outputsOff=[rewardOutput])
            self.sm.add_state(name='lickingPeriod', statetimer=lickingPeriod,
                              transitions={'Tup':'readyForNextTrial'})

        #print(self.sm) ### DEBUG
        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def calculate_results(self,trialIndex):
        # NOTE: Changes to graphical parameters (like nHits) are saved before calling
        #       this method. Therefore, those set here will be saved on the next trial.

        #taskModeLabels = self.params['taskMode'].get_items()
        #firstTrialModeInd = self.params.history['taskMode'][0]
        #if taskModeLabels[firstTrialModeInd] == 'water_on_lick':
        #    self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']

        lastRewardSide = self.params['rewardSide'].get_string()
        eventsThisTrial = self.dispatcher.events_one_trial(trialIndex)
        statesThisTrial = eventsThisTrial[:,2]
        if self.params['taskMode'].get_string() in ['lick_on_stim', 'discriminate_stim', 'water_after_sound']:
            if self.sm.statesNameToIndex['hit'] in statesThisTrial:
                self.params['addedITI'].set_value(0)
                if lastRewardSide=='left':
                    self.params['nHitsLeft'].add(1)
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
                    self.results['choice'][trialIndex] = self.results.labels['choice']['left']
                else:
                    self.params['nHitsRight'].add(1)
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
                    self.results['choice'][trialIndex] = self.results.labels['choice']['right']
            elif self.sm.statesNameToIndex['error'] in statesThisTrial:
                self.params['addedITI'].set_value(self.params['lickingPeriod'].get_value())
                if lastRewardSide=='left':
                    self.params['nErrorsLeft'].add(1)
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['error']
                    self.results['choice'][trialIndex] = self.results.labels['choice']['right']
                else:
                    self.params['nErrorsRight'].add(1)
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['error']
                    self.results['choice'][trialIndex] = self.results.labels['choice']['left']
            elif self.sm.statesNameToIndex['falseAlarmL'] in statesThisTrial:
                self.params['addedITI'].set_value(self.params['lickingPeriod'].get_value())
                self.params['nFalseAlarmsLeft'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['falseAlarm']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']
            elif self.sm.statesNameToIndex['falseAlarmR'] in statesThisTrial:
                self.params['addedITI'].set_value(self.params['lickingPeriod'].get_value())
                self.params['nFalseAlarmsRight'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['falseAlarm']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']  
            elif self.sm.statesNameToIndex['earlyLickL'] in statesThisTrial:
                self.params['addedITI'].set_value(self.params['lickingPeriod'].get_value())
                self.params['nEarlyLicksLeft'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['punishments']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']
            elif self.sm.statesNameToIndex['earlyLickR'] in statesThisTrial:
                self.params['addedITI'].set_value(self.params['lickingPeriod'].get_value())
                self.params['nEarlyLicksRight'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['punishments']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']
            elif self.sm.statesNameToIndex['miss'] in statesThisTrial:
                self.params['addedITI'].set_value(self.params['lickingPeriod'].get_value())
                if lastRewardSide=='left':
                    self.params['nMissesLeft'].add(1)
                else:
                    self.params['nMissesRight'].add(1)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']
            else:
                # This may happen if changing from one taskMode to another
                self.params['addedITI'].set_value(0)
                self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
                self.results['choice'][trialIndex] = self.results.labels['choice']['none']
        else:
            # -- For any other task modes (like water_on_lick)
            self.results['outcome'][trialIndex] = self.results.labels['outcome']['none']
            self.results['choice'][trialIndex] = self.results.labels['choice']['none']
        # -- Estimate number of licks --
        eventCodesThisTrial = eventsThisTrial[:,1]
        nLicksLeftThisTrial = np.sum(eventCodesThisTrial==self.sm.eventsDict['Lin'])
        nLicksRightThisTrial = np.sum(eventCodesThisTrial==self.sm.eventsDict['Rin'])
        self.params['nLicksLeft'].add(nLicksLeftThisTrial)
        self.params['nLicksRight'].add(nLicksRightThisTrial)

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

