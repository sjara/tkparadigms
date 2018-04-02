'''
Change detection head-fixed task.
'''

import time
import numpy as np
from PySide import QtGui
from taskontrol.core import paramgui
from taskontrol.core import arraycontainer
from taskontrol.plugins import templates
from taskontrol.plugins import soundclient
from taskontrol.plugins import speakercalibration
from taskontrol.settings import rigsettings



LONGTIME = 100

class Paradigm(templates.ParadigmGoNoGo):
    def __init__(self,parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.params['stimPreDurationMean'] = paramgui.NumericParam('Stim pre duration mean',value=1.2,
                                                            units='s',group='Timing parameters')
        self.params['stimPreDurationHalfRange'] = paramgui.NumericParam('+/-',value=0.6,
                                                            units='s',group='Timing parameters')
        self.params['stimPreDuration'] = paramgui.NumericParam('Stim pre duration',value=0,
                                                               enabled=False, decimals=3,
                                                               units='s',group='Timing parameters')
        self.params['stimPostDuration'] = paramgui.NumericParam('Stim post duration',value=0.8,
                                                                units='s',group='Timing parameters')
        self.params['timeOut'] = paramgui.NumericParam('Time out duration',value=0,
                                                       units='s',group='Timing parameters')
        self.params['interTrialInterval'] = paramgui.NumericParam('Inter-trial interval',value=0,
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

        self.params['outcomeMode'] = paramgui.MenuParam('Outcome mode',
                                                        ['on_run','on_stim_change',
                                                         'on_correct_stop'],
                                                         value=2, group='Task modes')
        taskModes = self.params.layout_group('Task modes')
        
        self.params['nValid'] = paramgui.NumericParam('N valid',value=0,
                                                      units='',enabled=False,
                                                      group='Report')
        self.params['nRewarded'] = paramgui.NumericParam('N rewarded',value=0,
                                                         units='',enabled=False,
                                                         group='Report')
        reportParams = self.params.layout_group('Report')

        # -- Add graphical widgets to main window --
        self.centralWidget = QtGui.QWidget()
        layoutMain = QtGui.QHBoxLayout()
        layoutCol1 = QtGui.QVBoxLayout()
        layoutCol2 = QtGui.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.dispatcherView)

        layoutCol2.addWidget(timingParams)
        layoutCol2.addWidget(soundParams)
        layoutCol2.addWidget(taskModes)
        layoutCol2.addWidget(reportParams)

        self.centralWidget.setLayout(layoutMain)
        self.setCentralWidget(self.centralWidget)

        # -- Add variables for storing results --
        maxNtrials = 4000 # Preallocating space for each vector makes things easier
        self.results = arraycontainer.Container()
        #self.results.labels['rewardSide'] = {'left':0,'right':1}
        #self.results['rewardSide'] = np.random.randint(2,size=maxNtrials)
        #self.results.labels['choice'] = {'left':0,'right':1,'none':2}
        #self.results['choice'] = np.empty(maxNtrials,dtype=int)
        self.results.labels['outcome'] = {'hit':1, 'miss':2, 'falseAlarm':3,'correctRejection':4,
                                          'earlyStop':5, 'freeReward':6, 'aborted':7}
        self.results['outcome'] = np.empty(maxNtrials,dtype=int)
        # Saving as bool creates an 'enum' vector, so I'm saving as 'int'
        self.results['valid'] = np.zeros(maxNtrials,dtype='int8') # redundant but useful
        self.results['timeTrialStart'] = np.empty(maxNtrials,dtype=float)
        self.results['timeRun'] = np.empty(maxNtrials,dtype=float)
        self.results['timeStop'] = np.empty(maxNtrials,dtype=float)
        self.results['timePreStim'] = np.empty(maxNtrials,dtype=float)
        self.results['timePostStim'] = np.empty(maxNtrials,dtype=float)
        #self.results['timeLick'] = np.empty(maxNtrials,dtype=float)

        # -- Load parameters from a file --
        self.params.from_file(paramfile,paramdictname)

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
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial>0:
            self.calculate_results(nextTrial-1)
            self.params.update_history()

        # Set stim pre duration
        randNum = (2*np.random.random(1)[0]-1) # In range [-1,1)
        stimPreDuration = self.params['stimPreDurationMean'].get_value() + \
            self.params['stimPreDurationHalfRange'].get_value()*randNum
        self.params['stimPreDuration'].set_value(stimPreDuration)

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
        outcomeMode = self.params['outcomeMode'].get_string()
        self.sm.reset_transitions()
        if outcomeMode == 'on_run':
            raise ValueError('Option on_run is not implemented yet.')
        elif outcomeMode == 'on_stim_change':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForRun'},
                              outputsOff=['centerLED', 'rightLED'])
            self.sm.add_state(name='waitForRun', statetimer=LONGTIME,
                              transitions={'Win':'playPreStimulus'})
            self.sm.add_state(name='playPreStimulus', statetimer=stimPreDur,
                              transitions={'Tup':'playPostStimulus', 'Wout':'earlyStop'},
                              serialOut=self.stimPreSoundID)
            self.sm.add_state(name='playPostStimulus', statetimer=0.1,
                              transitions={'Tup':'freeReward'},
                              serialOut=self.stimPostSoundID)
            self.sm.add_state(name='freeReward', statetimer=0,
                              transitions={'Tup':'reward'})
            self.sm.add_state(name='reward', statetimer=0.04,
                              transitions={'Tup':'stopReward'},
                              outputsOn=['rightWater'])
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'interTrialInterval'},
                              outputsOff=['rightWater'])
            self.sm.add_state(name='earlyStop', statetimer=0,
                              transitions={'Tup':'punish'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='punish', statetimer=timeOut,
                              transitions={'Tup':'interTrialInterval'})
            self.sm.add_state(name='interTrialInterval', statetimer=interTrialInterval+stimPostDur,
                              transitions={'Tup':'readyForNextTrial'})
        elif outcomeMode == 'on_correct_stop':
            self.sm.add_state(name='startTrial', statetimer=0,
                              transitions={'Tup':'waitForRun'},
                              outputsOff=['centerLED', 'rightLED'])
            self.sm.add_state(name='waitForRun', statetimer=LONGTIME,
                              transitions={'Win':'playPreStimulus'})
            self.sm.add_state(name='playPreStimulus', statetimer=stimPreDur,
                              transitions={'Tup':'playPostStimulus', 'Wout':'falseAlarm'},
                              serialOut=self.stimPreSoundID)
            self.sm.add_state(name='playPostStimulus', statetimer=stimPostDur,
                              transitions={'Tup':'miss', 'Wout':'hit'},
                              serialOut=self.stimPostSoundID)
            self.sm.add_state(name='hit', statetimer=0,
                              transitions={'Tup':'reward'})
            self.sm.add_state(name='reward', statetimer=0.04,
                              transitions={'Tup':'stopReward'},
                              outputsOn=['rightWater'], serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='stopReward', statetimer=0,
                              transitions={'Tup':'interTrialInterval'},
                              outputsOff=['rightWater'])
            self.sm.add_state(name='miss', statetimer=0,
                              transitions={'Tup':'punish'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='falseAlarm', statetimer=0,
                              transitions={'Tup':'punish'},
                              serialOut=soundclient.STOP_ALL_SOUNDS)
            self.sm.add_state(name='punish', statetimer=timeOut,
                              transitions={'Tup':'interTrialInterval'})
            self.sm.add_state(name='interTrialInterval', statetimer=interTrialInterval+stimPostDur,
                              transitions={'Tup':'readyForNextTrial'})

        self.prepare_sounds()

        self.dispatcherModel.set_state_matrix(self.sm)
        self.dispatcherModel.ready_to_start_trial()
        #print(self.sm) ### DEBUG


    def calculate_results(self,trialIndex):
        eventsThisTrial = self.dispatcherModel.events_one_trial(trialIndex)
    	# -- Check if it was a valid trial --
    	if self.sm.statesNameToIndex['playPostStimulus'] in eventsThisTrial[:,2]:
        	self.params['nValid'].add(1)
                self.results['valid'][trialIndex] = 1

        lastEvent = eventsThisTrial[-1,:]
        outcomeMode = self.params['outcomeMode'].get_string()
        if lastEvent[1]==-1 and lastEvent[2]==0:
            self.results['outcome'][trialIndex] = self.results.labels['outcome']['aborted']
        else:
            if outcomeMode == 'on_run':
                raise ValueError('Option on_run is not implemented yet.')
            elif outcomeMode == 'on_stim_change':
                if self.sm.statesNameToIndex['freeReward'] in eventsThisTrial[:,2]:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['freeReward']
                    self.params['nRewarded'].add(1)
                elif self.sm.statesNameToIndex['earlyStop'] in eventsThisTrial[:,2]:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['earlyStop']
            elif outcomeMode == 'on_correct_stop':
                if self.sm.statesNameToIndex['hit'] in eventsThisTrial[:,2]:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['hit']
                    self.params['nRewarded'].add(1)
                elif self.sm.statesNameToIndex['miss'] in eventsThisTrial[:,2]:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['miss']
                elif self.sm.statesNameToIndex['falseAlarm'] in eventsThisTrial[:,2]:
                    self.results['outcome'][trialIndex] = self.results.labels['outcome']['falseAlarm']

        #print('--- OUTCOME [{}]: {} ---'.format(trialIndex,self.results['outcome'][trialIndex])) # DEBUG


if __name__ == '__main__':
    (app,paradigm) = paramgui.create_app(Paradigm)
