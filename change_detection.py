'''
Change detection head-fixed task.
'''

import time
import numpy as np
from PySide import QtGui
from taskontrol.core import paramgui
from taskontrol.plugins import templates
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
from taskontrol.settings import rigsettings


LONGTIME = 100

class Paradigm(templates.ParadigmGoNoGo):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.params['stimPreDuration'] = paramgui.NumericParam('Stim pre duration',value=0.4,
                                                            units='s',group='Timing parameters')
        self.params['stimPostDuration'] = paramgui.NumericParam('Stim post duration',value=0.8,
                                                            units='s',group='Timing parameters')
        self.params['timeOut'] = paramgui.NumericParam('Time out duration',value=2,enabled=False,
                                                       units='s',group='Timing parameters')
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter-trial interval',value=1,
                                                       units='s',group='Timing parameters')
        timingParams = self.params.layout_group('Timing parameters')

        self.params['freq1'] = paramgui.NumericParam('Freq 1',value=9000,
                                                            units='Hz',group='Sound parameters')
        self.params['freq2'] = paramgui.NumericParam('Freq 2',value=4000,
                                                            units='Hz',group='Sound parameters')
        self.params['stimPreFreq'] = paramgui.NumericParam('Stim pre freq',value=0,enabled=False,
                                                            units='Hz',group='Sound parameters')
        self.params['stimPostFreq'] = paramgui.NumericParam('Stim post freq',value=0,enabled=False,
                                                            units='Hz',group='Sound parameters')
        self.params['stimIntensity'] = paramgui.NumericParam('Intensity',value=40, units='dB-SPL',
                                                            enabled=True, group='Sound parameters')
        self.params['stimPreAmplitude'] = paramgui.NumericParam('Stim pre amplitude', value=0.0,
                                                            units='[0-1]',decimals=4,
                                                            enabled=False,group='Sound parameters')
        self.params['stimPostAmplitude'] = paramgui.NumericParam('Stim post amplitude', value=0.0,
                                                            units='[0-1]',decimals=4,
                                                            enabled=False,group='Sound parameters')
        soundParams = self.params.layout_group('Sound parameters')

        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout()
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)

        layoutCol1.addWidget(self.dispatcherView)
        layoutCol2.addWidget(self.sessionInfo)
        layoutCol2.addWidget(timingParams)
        layoutCol2.addWidget(soundParams)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Load speaker calibration --
        self.spkCal = speakercalibration.Calibration(rigsettings.SPEAKER_CALIBRATION_CHORD)
        #self.spkNoiseCal = speakercalibration.NoiseCalibration(rigsettings.SPEAKER_NOISE_CALIBRATION)

        # -- Connect to sound server and define sounds --
        print 'Conecting to soundserver...'
        print '***** FIXME: HARDCODED TIME DELAY TO WAIT FOR SERIAL PORT! *****' ### DEBUG
        time.sleep(0.2)
        self.soundClient = soundclient.SoundClient()
        self.stimPreSoundID = 1
        self.stimPostSoundID = 2
        self.soundClient.start()

    def prepare_sounds(self):
        '''
        if self.params['stimIntensityMode'].get_string() == 'randMinus20':
            possibleIntensities = self.params['stimMaxIntensity'].get_value()+\
                                  np.array([-20,-15,-10,-5,0])
            stimIntensity = possibleIntensities[np.random.randint(len(possibleIntensities))]
        else:
            stimIntensity = self.params['stimMaxIntensity'].get_value()
        self.params['stimIntensity'].set_value(stimIntensity)
        '''
        stimIntensity = self.params['stimIntensity'].get_value()
        stimPreFreq = self.params['stimPreFreq'].get_value()
        stimPostFreq = self.params['stimPostFreq'].get_value()

        # FIXME: currently I am averaging calibration from both speakers (not good)
        stimPreAmp = self.spkCal.find_amplitude(stimPreFreq,stimIntensity).mean()
        self.params['stimPreAmplitude'].set_value(stimPreAmp)
        # FIXME: currently I am averaging calibration from both speakers (not good)
        stimPostAmp = self.spkCal.find_amplitude(stimPostFreq,stimIntensity).mean()
        self.params['stimPostAmplitude'].set_value(stimPostAmp)

        stimPreDur = self.params['stimPreDuration'].get_value()
        stimPostDur = self.params['stimPostDuration'].get_value()
        s1 = {'type':'chord', 'frequency':stimPreFreq, 'duration':stimPreDur,
              'amplitude':stimPreAmp, 'ntones':12, 'factor':1.2}
        s2 = {'type':'chord', 'frequency':stimPostFreq, 'duration':stimPostDur,
              'amplitude':stimPostAmp, 'ntones':12, 'factor':1.2}
        self.soundClient.set_sound(self.stimPreSoundID,s1)
        self.soundClient.set_sound(self.stimPostSoundID,s2)


    def prepare_next_trial(self, nextTrial):
        
        freq1 = self.params['freq1'].get_value()
        freq2 = self.params['freq2'].get_value()
        if np.random.randint(2):
            self.params['stimPreFreq'].set_value(freq1)
            self.params['stimPostFreq'].set_value(freq2)
        else:
            self.params['stimPreFreq'].set_value(freq2)
            self.params['stimPostFreq'].set_value(freq1)

        stimPreDur = self.params['stimPreDuration'].get_value()
        stimPostDur = self.params['stimPostDuration'].get_value()
        timeOut = self.params['timeOut'].get_value()
        interTrialInterval = self.params['interTrialInterval'].get_value()
        self.sm.reset_transitions()
        self.sm.add_state(name='startTrial', statetimer=0,
                          transitions={'Tup':'waitForRun'},
                          outputsOff=['centerLED', 'rightLED'])
        self.sm.add_state(name='waitForRun', statetimer=LONGTIME,
                          transitions={'Win':'playPreStimulus'})
        '''
        self.sm.add_state(name='playPreStimulus', statetimer=stimPreDur,
                          transitions={'Tup':'playPostStimulus', 'Wout':'stopStimulus'},
                          serialOut=self.stimPreSoundID)
        '''
        self.sm.add_state(name='playPreStimulus', statetimer=stimPreDur,
                          transitions={'Tup':'playPostStimulus'},
                          serialOut=self.stimPreSoundID)
        self.sm.add_state(name='playPostStimulus', statetimer=0.1,
                          transitions={'Tup':'waterDelivery'},
                          serialOut=self.stimPostSoundID)
        self.sm.add_state(name='waterDelivery', statetimer=0.04,
                          transitions={'Tup':'interTrialInterval'},
                          outputsOn=['rightWater'])
        self.sm.add_state(name='stopStimulus', statetimer=timeOut,
                          transitions={'Tup':'interTrialInterval'},
                          serialOut=soundclient.STOP_ALL_SOUNDS)
        self.sm.add_state(name='interTrialInterval', statetimer=interTrialInterval+stimPostDur,
                          transitions={'Tup':'readyForNextTrial'},
                          outputsOff=['rightWater'])
        self.prepare_sounds()

        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()


if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)
