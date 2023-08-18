"""
Cooperate_four_ports is a paradigm in which two animals must poke simultaneously to obtain reward.
There are two lanes (one for each animal) with one port at each end.

TO DO:
- Store timing of pokes on the wrong side.

"""

import numpy as np
from qtpy import QtWidgets
from taskontrol import rigsettings
from taskontrol import dispatcher
from taskontrol import statematrix
from taskontrol import savedata
from taskontrol import paramgui
from taskontrol import utils
from taskontrol.plugins import manualcontrol

LONGTIME = 100
MAX_N_TRIALS = 4000


class Paradigm(QtWidgets.QMainWindow):
    def __init__(self, parent=None, paramfile=None, paramdictname=None):
        super(Paradigm, self).__init__(parent)

        self.name = "coop4ports"

        # Variable that will be used as a limit
        # A pair of ports of one side cannot be selected more
        # than timesPortSelected in a row
        self.timesPortSelected = 0

        # -- Create an empty statematrix --
        self.sm = statematrix.StateMatrix(
            inputs=rigsettings.INPUTS,
            outputs=rigsettings.OUTPUTS,
            readystate="readyForNextTrial",
            extratimers=["lightTimer1", "lightTimer2"],
        )

        # -- Create dispatcher --
        smServerType = rigsettings.STATE_MACHINE_TYPE
        self.dispatcher = dispatcher.Dispatcher(serverType=smServerType, interval=0.1)

        # -- Module for saving data --
        self.saveData = savedata.SaveData(
            rigsettings.DATA_DIR, remotedir=rigsettings.REMOTE_DIR
        )

        # -- Manual control of outputs --
        self.manualControl = manualcontrol.ManualControl(self.dispatcher.statemachine)

        # -- Define graphical parameters --
        self.params = paramgui.Container()
        self.params["trainer"] = paramgui.StringParam(
            "Trainer (initials)", value="", group="Session info"
        )
        self.params["experimenter"] = paramgui.StringParam(
            "Experimenter", value="experimenter", group="Session info"
        )
        self.params["subject"] = paramgui.StringParam(
            "Subject", value="subject", group="Session info"
        )
        self.sessionInfo = self.params.layout_group("Session info")

        self.params["timeWaterValves"] = paramgui.NumericParam(
            "Time valves", value=0.03, units="s", group="Water delivery"
        )
        self.params["rewardFrequency"] = paramgui.NumericParam(
            "Reward frequency", value=2, units="times", group="Water delivery"
        )
        # self.params['timeWaterValvesN'] = paramgui.NumericParam('Time valves N',value=0.03,
        #                                                        units='s',group='Water delivery')
        # self.params['timeWaterValvesS'] = paramgui.NumericParam('Time valves S',value=0.03,
        #                                                        units='s',group='Water delivery')
        waterDelivery = self.params.layout_group("Water delivery")

        self.params["waitTime"] = paramgui.NumericParam(
            "Wait time", value=0.5, units="s", group="Timing parameters"
        )
        self.params["pokesPerMouse"] = paramgui.NumericParam(
            "Pokes per mouse", value=10, units="pokes", group="Timing parameters"
        )
        ## This name is victim of my poor creativity, it may be changed :)
        self.params["thresholdForIncrementPoke"] = paramgui.NumericParam(
            "Threshold for increase poke",
            value=20,
            units="trials",
            group="Timing parameters",
        )
        
        ## This name is victim of my poor creativity, it may be changed :)
        self.params["numberOfPokeAddPerMouse"] = paramgui.NumericParam(
            "Pokes to add per mouse",
            value=1,
            units="pokes",
            enabled=True,
            group="Timing parameters",
        )

        ## This name is victim of my poor creativity, it may be changed :)
        self.params["targetPokesPerMouse"] = paramgui.NumericParam(
            "Target pokes per mouse",
            value=10,
            units="pokes",
            group="Timing parameters",
        )
        self.params["timeLEDon"] = paramgui.NumericParam(
            "Time LED on",
            value=0.3,
            units="s",
            enabled=False,
            group="Timing parameters",
        )
        self.params["ITI"] = paramgui.NumericParam(
            "Inter-trial interval",
            value=10,
            units="s",
            group="Timing parameters",
            enabled=True,
        )
        self.params["extraTimeITI"] = paramgui.NumericParam(
            "Extra time ITI",
            value=2,
            units="s",
            group="Timing parameters",
            enabled=False,
        )
        timingParams = self.params.layout_group("Timing parameters")
        self.params["barrierType"] = paramgui.MenuParam(
            "Barrier type",
            ["perforated_5_mm","perforated_10_mm", "solid", "transparent_holes", "transparent_no_holes", "no_barrier"],
            value=1,
            group="General parameters",
        )
        self.params["activeSide"] = paramgui.MenuParam(
            "Active side",
            ["north", "south"],
            value=0,
            group="General parameters",
            enabled=False,
        )
        self.params["taskMode"] = paramgui.MenuParam(
            "Task mode",
            [
                "one_track",
                "auto_lights",
                "reward_on_first_poke",
                "reward_on_last_poke",
                "cooperate_lights",
                "cooperate",
            ],
            value=1,
            group="General parameters",
        )

        self.params["activatePokeIncrement"] = paramgui.MenuParam(
            "Activate poke increment",
            ["False", "True"],
            value=0,
            group="General parameters",
            enabled=True,
        )

        self.params["nextPortAfterFail"] = paramgui.MenuParam(
            "Next port after fail",
            ["same", "opposite"],
            value=0,
            group="General parameters",
            enabled=True,
        )

        self.params["ITIAfterFail"] = paramgui.MenuParam(
            "ITI after fail",
            ["False", "True"],
            value=0,
            group="General parameters",
            enabled=True,
        )

        self.params["ITIAfterSuccess"] = paramgui.MenuParam(
            "ITI after success",
            ["False", "True"],
            value=1,
            group="General parameters",
            enabled=True,
        )
        

        self.params["maxPortRepetition"] = paramgui.NumericParam(
            "Max port repetition",
            value=3,
            units="Times",
            group="General parameters",
            enabled=True,
        )
        generalParams = self.params.layout_group("General parameters")

        self.params["nRewarded1"] = paramgui.NumericParam(
            "N trials rewarded T1",
            value=0,
            enabled=False,
            units="trials",
            group="Report",
        )
        self.params["nRewarded2"] = paramgui.NumericParam(
            "N trials rewarded T2",
            value=0,
            enabled=False,
            units="trials",
            group="Report",
        )
        reportInfo = self.params.layout_group("Report")

        # -- Add graphical widgets to main window --
        self.centralWidget = QtWidgets.QWidget()
        layoutMain = QtWidgets.QHBoxLayout()
        layoutCol1 = QtWidgets.QVBoxLayout()
        layoutCol2 = QtWidgets.QVBoxLayout()

        layoutMain.addLayout(layoutCol1)
        layoutMain.addLayout(layoutCol2)

        layoutCol1.addWidget(self.saveData)
        layoutCol1.addWidget(self.sessionInfo)
        layoutCol1.addWidget(reportInfo)
        layoutCol1.addWidget(self.dispatcher.widget)

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
        maxNtrials = (
            MAX_N_TRIALS  # Preallocating space for each vector makes things easier
        )
        self.results = utils.EnumContainer()
        self.results.labels["outcome"] = {
            "aborted": 0,
            "rewardedBoth": 1,
            "poke1only": 2,
            "poke2only": 3,
            "none": 4,
        }
        self.results["outcome"] = np.empty(maxNtrials, dtype=int)
        self.results["timePoke1"] = np.empty(maxNtrials, dtype=float)
        self.results["timePoke2"] = np.empty(maxNtrials, dtype=float)
        self.results["timeTrialStart"] = np.empty(maxNtrials, dtype=float)

        # self.results.labels['activeSide'] = {'north':0,'south':1}
        # self.results['activeSide'] = np.empty(maxNtrials,dtype=int)
        # self.results['activeSide'][0] = 0

        # -- Load parameters from a file --
        self.params.from_file(paramfile, paramdictname)

        # -- Connect signals from dispatcher --
        self.dispatcher.prepareNextTrial.connect(self.prepare_next_trial)

        # -- Connect messenger --
        self.messagebar = paramgui.Messenger()
        self.messagebar.timedMessage.connect(self._show_message)
        self.messagebar.collect("Created window")

        # -- Connect signals to messenger
        self.saveData.logMessage.connect(self.messagebar.collect)
        self.dispatcher.logMessage.connect(self.messagebar.collect)

        # -- Connect other signals --
        self.saveData.buttonSaveData.clicked.connect(self.save_to_file)

    def _show_message(self, msg):
        self.statusBar().showMessage(str(msg))
        print(msg)

    def save_to_file(self):
        """Triggered by button-clicked signal"""
        self.saveData.to_file(
            [self.params, self.dispatcher, self.sm, self.results],
            self.dispatcher.currentTrial,
            experimenter="",
            subject=self.params["subject"].get_value(),
            paradigm=self.name,
        )

    def prepare_next_trial(self, nextTrial):
        # -- Calculate results from last trial (update outcome, choice, etc) --
        if nextTrial > 0:
            self.params.update_history(nextTrial - 1)
            self.calculate_results(nextTrial - 1)
            previousOutcome = self.results["outcome"][nextTrial - 1]
        else:
            previousOutcome = self.results.labels["outcome"]["rewardedBoth"]

        # -- Prepare next trial --
        taskMode: str = self.params["taskMode"].get_string()
        activeSide: str = self.params["activeSide"].get_string()
        nextPortAfterFail = self.params["nextPortAfterFail"].get_string()
        ITIAfterFail = self.params["ITIAfterFail"].get_string()
        ITIAfterSuccess = self.params["ITIAfterSuccess"].get_string()
        activatePokeIncrement = self.params["activatePokeIncrement"].get_string()
        waitTime: float = self.params["waitTime"].get_value()
        timeLEDon: float = self.params["timeLEDon"].get_value()
        interTrialInterval: int = self.params["ITI"].get_value()
        timeWaterValves: float = self.params["timeWaterValves"].get_value()
        nrewarded: int = self.params["nRewarded1"].get_value()
        

        # My creativity is abnormally limited
        thresholdForIncrementPoke: int = self.params[
            "thresholdForIncrementPoke"
        ].get_value()

        # This operation is to make equal the number of pokes each mouse has to do.
        # It has to do with the loop that build the poke's states
        pokesPerMouse: int = self.params["pokesPerMouse"].get_value()
        totalNumberOfPokes: int = (pokesPerMouse * 2) - 1

        targetPokesPerMouse: int = self.params["targetPokesPerMouse"].get_value()
        rewardFrequency = self.params["rewardFrequency"].get_value()
        # timeWaterValvesN = self.params['timeWaterValvesN'].get_value()
        # timeWaterValvesS = self.params['timeWaterValvesS'].get_value()

        ## This is the amount of time extra added if mice are interacting with ports during iti
        ## when iti is going to end.
        # I have not decided what to do with this!!
        # My mind is atrophied .
        extraTimeITI: int = self.params["extraTimeITI"].get_value()
        ##number of pokes to add to pokesPerMouse in order to reach the targetPokesPerMouse
        numberOfPokeAddPerMouse = self.params["numberOfPokeAddPerMouse"].get_value()

        self.sm.reset_transitions()

        # if (activeSide=='north'):
        #     port1in = 'S1in'; port2in = 'S2in'
        #     LED1 = 'S1LED'; LED2 = 'S2LED'
        #     Water1 = 'S1Water'; Water2 = 'S2Water'
        #     #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
        #     self.params['activeSide'].set_string('south')
        # if (activeSide=='south'):
        #     port1in = 'N1in'; port2in = 'N2in'
        #     LED1 = 'N1LED'; LED2 = 'N2LED'
        #     Water1 = 'N1Water'; Water2 = 'N2Water'
        #     #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
        #     self.params['activeSide'].set_string('north')

        """
        switchActiveSide = (previousOutcome==self.results.labels['outcome']['rewarded'])

        if (activeSide=='south' and switchActiveSide) or (activeSide=='north' and not switchActiveSide):
            port1in = 'N1in'; port2in = 'N2in'
            LED1 = 'N1LED'; LED2 = 'N2LED'
            Water1 = 'N1Water'; Water2 = 'N2Water'
            #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['south']
            self.params['activeSide'].set_string('north')
        elif (activeSide=='north' and switchActiveSide) or (activeSide=='south' and not switchActiveSide):
            port1in = 'S1in'; port2in = 'S2in'
            LED1 = 'S1LED'; LED2 = 'S2LED'
            Water1 = 'S1Water'; Water2 = 'S2Water'
            #self.results['activeSide'][nextTrial+1]=self.results.labels['activeSide']['north']
            self.params['activeSide'].set_string('south')
        else:
            raise
        """

        if taskMode == "one_track":

            # Determine if previous trial was successfull
            previousOutcomeSuccessful: bool = (
                previousOutcome == self.results.labels["outcome"]["rewardedBoth"]
            )
            
            # This method is applied to evaluate whether a new side will be chosen
            # Since the meaning of success may vary with each stage of must be applied to each taskMode
            port1in, port2in, LED1, LED2, Water1, Water2 = self.switch_active_side(
                previousOutcomeSuccessful,
                activeSide,
                self.params["activeSide"].get_items(),
                nextPortAfterFail,
            )
            
            self.sm.add_state(
                name="startTrial",
                statetimer=0,
                transitions={"Tup": "waitForPoke"},
                outputsOff=[LED1, LED2],
            )
            self.sm.add_state(
                name="waitForPoke",
                statetimer=LONGTIME,
                transitions={port1in: "reward", port2in: "reward"},
            )
            self.sm.add_state(
                name="reward",
                statetimer=timeWaterValves,
                transitions={"Tup": "stopReward"},
                outputsOn=[Water1, Water2],
                outputsOff=[LED1, LED2],
            )
            self.sm.add_state(
                name="stopReward",
                statetimer=0,
                transitions={"Tup": "readyForNextTrial"},
                outputsOff=[Water1, Water2],
            )        
        elif taskMode == "auto_lights":

            ## This is to flash the lights during iti (turn on/ turn off)
            timesFlashingLightsCounter: int = round(
                (interTrialInterval / timeLEDon) / 2
            )
            timesFlashingLightsBackUp: int = round((extraTimeITI / timeLEDon) / 2)

            # This variable contains the outcomes consider successfull in this taskmode
            successOutcomes: list = ["rewardedBoth", "poke1only", "poke2only"]

            # Evaluate if the last trial was successfull
            previousOutcomeSuccessful: bool = previousOutcome in [
                self.results.labels["outcome"][outcome] for outcome in successOutcomes
            ]

            # This method is applied to evaluate whether a new side will be chosen
            # Since the meaning of success may vary with each stage of must be applied to each taskMode
            port1in, port2in, LED1, LED2, Water1, Water2 = self.switch_active_side(
                previousOutcomeSuccessful,
                activeSide,
                self.params["activeSide"].get_items(),
                nextPortAfterFail,
            )

            self.sm.add_state(
                name="startTrial",
                statetimer=0,
                transitions={"Tup": "iti"},
                outputsOff=[LED1, LED2],
            )
            # Conditional to define if an ITI is applied before the next trial
            if previousOutcomeSuccessful:
                if (self.params["ITIAfterSuccess"].get_items()).index(ITIAfterSuccess) and interTrialInterval:
                    transition_iti = {"Tup":"turnLEDon0"}
                else:
                    transition_iti = {"Tup":"waitForAnyPoke"}
            else:
                if (self.params["ITIAfterFail"].get_items()).index(ITIAfterFail) and interTrialInterval:
                    transition_iti = {"Tup":"turnLEDon0"}
                else:
                    transition_iti = {"Tup":"waitForAnyPoke"}
            
            # Move iti to the beginning so that the iti is applied first
            self.sm.add_state(
                name="iti",
                statetimer=0,
                transitions=transition_iti,
                outputsOff=[LED1, LED2, Water1, Water2],
            )

            # flashing lights for the inter-trial interval period.
            for flash in range(0, timesFlashingLightsCounter):
                # I am trying to keep the flashing lights if the mice are poking
                if flash == (timesFlashingLightsCounter - 1):

                    transitions = {
                        "N1in": "turnLEDonBackUp0",
                        "S1in": "turnLEDonBackUp0",
                        "N2in": "turnLEDonBackUp0",
                        "S2in": "turnLEDonBackUp0",
                        "Tup": "waitForAnyPoke",
                    }
                else:
                    transitions = {"Tup": f"turnLEDon{flash + 1}"}

                self.sm.add_state(
                    name=f"turnLEDon{flash}",
                    statetimer=timeLEDon,
                    transitions={"Tup": f"turnLEDoff{flash}"},
                    outputsOn=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

                self.sm.add_state(
                    name=f"turnLEDoff{flash}",
                    statetimer=(
                        0.5 if flash == (timesFlashingLightsCounter - 1) else timeLEDon
                    ),
                    transitions=transitions,
                    outputsOff=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

            # if the mice are interating with the ports during the flash lights when is gonna end,
            # another second of flashing ligths is applied
            for flashBackUp in range(0, timesFlashingLightsBackUp):
                self.sm.add_state(
                    name=f"turnLEDonBackUp{flashBackUp}",
                    statetimer=timeLEDon,
                    transitions={"Tup": f"turnLEDoffBackUp{flashBackUp}"},
                    outputsOn=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

                self.sm.add_state(
                    name=f"turnLEDoffBackUp{flashBackUp}",
                    statetimer=timeLEDon,
                    transitions={
                        "Tup": (
                            f"turnLEDon{timesFlashingLightsCounter - 2}"
                            if flashBackUp == (timesFlashingLightsBackUp - 1)
                            else f"turnLEDonBackUp{flashBackUp + 1}"
                        )
                    },
                    outputsOff=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

            self.sm.add_state(
                name="waitForAnyPoke",
                statetimer=LONGTIME,
                transitions={
                    port1in: "reward1.0",
                    port2in: "reward2.0",
                },
                outputsOn=[LED1, LED2],
            )
            for reward in range(0, rewardFrequency):

                ## In the last iteration, trasition has to change to continue the flow of the states
                if (reward + 1) == rewardFrequency:
                    stopReward1 = "waitForPoke2"
                    stopReward2 = "waitForPoke1"
                    stopReward2after1 = "turnLEDoff"
                    stopReward1after2 = "turnLEDoff"
                else:
                    stopReward1 = f"reward1.{reward + 1}"
                    stopReward2 = f"reward2.{reward + 1}"
                    stopReward2after1 = f"reward2after1.{reward + 1}"
                    stopReward1after2 = f"reward1after2.{reward + 1}"

                self.sm.add_state(
                    name=f"reward1.{reward}",
                    statetimer=timeWaterValves,
                    transitions={"Tup": f"stopReward1.{reward}"},
                    outputsOn=[Water1],
                )
                self.sm.add_state(
                    name=f"stopReward1.{reward}",
                    statetimer=0,
                    transitions={"Tup": stopReward1},
                    outputsOff=[Water1],
                )
                self.sm.add_state(
                    name=f"reward2after1.{reward}",
                    statetimer=timeWaterValves,
                    transitions={"Tup": f"stopReward2after1.{reward}"},
                    outputsOn=[Water2],
                )
                self.sm.add_state(
                    name=f"stopReward2after1.{reward}",
                    statetimer=0,
                    transitions={"Tup": stopReward2after1},
                    outputsOff=[Water2],
                )
                self.sm.add_state(
                    name=f"reward2.{reward}",
                    statetimer=timeWaterValves,
                    transitions={"Tup": f"stopReward2.{reward}"},
                    outputsOn=[Water2],
                )
                self.sm.add_state(
                    name=f"stopReward2.{reward}",
                    statetimer=0,
                    transitions={"Tup": stopReward2},
                    outputsOff=[Water2],
                )
                self.sm.add_state(
                    name=f"reward1after2.{reward}",
                    statetimer=timeWaterValves,
                    transitions={"Tup": f"stopReward1after2.{reward}"},
                    outputsOn=[Water1],
                )
                self.sm.add_state(
                    name=f"stopReward1after2.{reward}",
                    statetimer=0,
                    transitions={"Tup": stopReward1after2},
                    outputsOff=[Water1],
                )

            self.sm.add_state(
                name="waitForPoke1",
                statetimer=waitTime,
                transitions={port1in: "reward1after2.0", "Tup": "turnLEDoff"},
            )

            self.sm.add_state(
                name="waitForPoke2",
                statetimer=waitTime,
                transitions={port2in: "reward2after1.0", "Tup": "turnLEDoff"},
            )

            # Now this state will be the one that start a new trial
            self.sm.add_state(
                name="turnLEDoff",
                statetimer=1,
                transitions={"Tup": "readyForNextTrial"},
                outputsOff=[LED1, LED2, Water1, Water2],
            )
        elif taskMode == "reward_on_first_poke":

            # This variable contains the outcomes consider successfull in this taskmode
            successOutcomes: list = ["rewardedBoth", "poke1only", "poke2only"]

            # Evaluate if the last trial was successfull
            previousOutcomeSuccessful: bool = previousOutcome in [
                self.results.labels["outcome"][outcome] for outcome in successOutcomes
            ]

            # This method is applied to evaluate whether a new side will be chosen
            # Since the meaning of success may vary with each stage of must be applied to each taskMode
            port1in, port2in, LED1, LED2, Water1, Water2 = self.switch_active_side(
                previousOutcomeSuccessful,
                activeSide,
                self.params["activeSide"].get_items(),
                nextPortAfterFail,
            )
            
            # self.params['timeLEDon'].set_value(waitTime)
            self.sm.set_extratimer("lightTimer1", duration=waitTime)
            self.sm.set_extratimer("lightTimer2", duration=waitTime)
            self.sm.add_state(
                name="startTrial",
                statetimer=0,
                transitions={"Tup": "waitForPoke"},
                outputsOff=[LED1, LED2],
            )
            self.sm.add_state(
                name="waitForPoke",
                statetimer=LONGTIME,
                transitions={port1in: "reward1.0", port2in: "reward2.0"},
            )
            self.sm.add_state(
                name="reward1.0",
                statetimer=timeWaterValves,
                transitions={"Tup": "stopReward1.0", "lightTimer1": "turnLEDoff"},
                outputsOn=[Water1, LED1, LED2],
                trigger=["lightTimer1"],
            )
            self.sm.add_state(
                name="stopReward1.0",
                statetimer=0,
                transitions={"Tup": "waitForPoke2", "lightTimer1": "turnLEDoff"},
                outputsOff=[Water1],
            )
            self.sm.add_state(
                name="waitForPoke2",
                statetimer=waitTime,
                transitions={port2in: "reward2after1.0", "lightTimer1": "turnLEDoff"},
            )
            self.sm.add_state(
                name="reward2after1.0",
                statetimer=timeWaterValves,
                transitions={"Tup": "stopReward2after1.0", "lightTimer1": "turnLEDoff"},
                outputsOn=[Water2],
            )
            self.sm.add_state(
                name="stopReward2after1.0",
                statetimer=0,
                transitions={"Tup": "keepLEDon", "lightTimer1": "turnLEDoff"},
                outputsOff=[Water2],
            )
            self.sm.add_state(
                name="reward2.0",
                statetimer=timeWaterValves,
                transitions={"Tup": "stopReward2.0", "lightTimer1": "turnLEDoff"},
                outputsOn=[Water2, LED1, LED2],
                trigger=["lightTimer2"],
            )
            self.sm.add_state(
                name="stopReward2.0",
                statetimer=0,
                transitions={"Tup": "waitForPoke1", "lightTimer2": "turnLEDoff"},
                outputsOff=[Water2],
            )
            self.sm.add_state(
                name="waitForPoke1",
                statetimer=waitTime,
                transitions={port1in: "reward1after2.0", "lightTimer2": "turnLEDoff"},
            )
            self.sm.add_state(
                name="reward1after2.0",
                statetimer=timeWaterValves,
                transitions={"Tup": "stopReward1after2.0", "lightTimer2": "turnLEDoff"},
                outputsOn=[Water1],
            )
            self.sm.add_state(
                name="stopReward1after2.0",
                statetimer=0,
                transitions={"Tup": "keepLEDon", "lightTimer2": "turnLEDoff"},
                outputsOff=[Water1],
            )
            self.sm.add_state(
                name="keepLEDon",
                statetimer=waitTime,
                transitions={
                    "Tup": "turnLEDoff",
                    "lightTimer1": "turnLEDoff",
                    "lightTimer2": "turnLEDoff",
                },
                outputsOff=[Water1, Water2],
            )
            self.sm.add_state(
                name="turnLEDoff",
                statetimer=0,
                transitions={"Tup": "iti"},
                outputsOff=[LED1, LED2, Water1, Water2],
            )
            self.sm.add_state(
                name="iti",
                statetimer=interTrialInterval,
                transitions={"Tup": "readyForNextTrial"},
                outputsOff=[LED1, LED2, Water1, Water2],
            )
        elif taskMode == "reward_on_last_poke":

            # This variable contains the outcomes consider successfull in this taskmode
            successOutcomes: list = ["rewardedBoth"]

            # Evaluate if the last trial was successfull
            previousOutcomeSuccessful: bool = previousOutcome in [
                self.results.labels["outcome"][outcome] for outcome in successOutcomes
            ]

            # This method is applied to evaluate whether a new side will be chosen
            # Since the meaning of success may vary with each stage of must be applied to each taskMode
            port1in, port2in, LED1, LED2, Water1, Water2 = self.switch_active_side(
                previousOutcomeSuccessful,
                activeSide,
                self.params["activeSide"].get_items(),
                nextPortAfterFail,
            )

            # self.params['timeLEDon'].set_value(waitTime)
            self.sm.set_extratimer("lightTimer1", duration=waitTime)
            self.sm.set_extratimer("lightTimer2", duration=waitTime)
            self.sm.add_state(
                name="startTrial",
                statetimer=0,
                transitions={"Tup": "waitForPoke"},
                outputsOff=[LED1, LED2],
            )
            self.sm.add_state(
                name="waitForPoke",
                statetimer=LONGTIME,
                transitions={port1in: "waitForPoke2", port2in: "waitForPoke1"},
            )
            self.sm.add_state(
                name="waitForPoke2",
                statetimer=waitTime,
                transitions={port2in: "reward", "lightTimer1": "turnLEDoff"},
                outputsOn=[LED1, LED2],
                trigger=["lightTimer1"],
            )
            self.sm.add_state(
                name="waitForPoke1",
                statetimer=waitTime,
                transitions={port1in: "reward", "lightTimer2": "turnLEDoff"},
                outputsOn=[LED1, LED2],
                trigger=["lightTimer2"],
            )
            self.sm.add_state(
                name="reward",
                statetimer=timeWaterValves,
                transitions={
                    "Tup": "stopReward",
                    "lightTimer1": "turnLEDoff",
                    "lightTimer2": "turnLEDoff",
                },
                outputsOn=[Water1, Water2],
            )
            self.sm.add_state(
                name="stopReward",
                statetimer=0,
                transitions={
                    "Tup": "keepLEDon",
                    "lightTimer1": "turnLEDoff",
                    "lightTimer2": "turnLEDoff",
                },
                outputsOff=[Water1, Water2],
            )
            self.sm.add_state(
                name="keepLEDon",
                statetimer=waitTime,
                transitions={
                    "Tup": "turnLEDoff",
                    "lightTimer1": "turnLEDoff",
                    "lightTimer2": "turnLEDoff",
                },
                outputsOff=[Water1, Water2],
            )
            self.sm.add_state(
                name="turnLEDoff",
                statetimer=0,
                transitions={"Tup": "iti"},
                outputsOff=[LED1, LED2, Water1, Water2],
            )
            self.sm.add_state(
                name="iti",
                statetimer=interTrialInterval,
                transitions={"Tup": "readyForNextTrial"},
                outputsOff=[LED1, LED2, Water1, Water2],
            )
        elif taskMode == "cooperate_lights":    

            # Determine if previous trial was successfull
            previousOutcomeSuccessful: bool = (
                previousOutcome == self.results.labels["outcome"]["rewardedBoth"]
            )

            # -- If mice achieve thresholdForIncrementPoke trials the amount of time poking is increased --
            if (self.params["activatePokeIncrement"].get_items()).index(activatePokeIncrement):
                if (
                    (previousOutcomeSuccessful)
                    and (pokesPerMouse < targetPokesPerMouse)
                    and (nrewarded > 0)
                    and (nrewarded % thresholdForIncrementPoke == 0)
                ):
                    update_pokes = pokesPerMouse + numberOfPokeAddPerMouse
                    # Make the number of pokes accumulated equal to the target if the former is greater
                    if update_pokes > targetPokesPerMouse:
                        update_pokes = targetPokesPerMouse
                    else:
                        pass
                    self.params["pokesPerMouse"].set_value(
                        (update_pokes)
                    )
                    pokesPerMouse = self.params["pokesPerMouse"].get_value()
                    
                    # This is for the loop to create pokes states
                    totalNumberOfPokes = (pokesPerMouse * 2) - 1
                else:
                    pass
            else:
                pass

            ## This is to flash the lights during iti (turn on/ turn off)
            timesFlashingLightsCounter: int = round(
                (interTrialInterval / timeLEDon) / 2
            )
            timesFlashingLightsBackUp: int = round((extraTimeITI / timeLEDon) / 2)

            # This method is applied to evaluate whether a new side will be chosen
            # Since the meaning of success may vary with each stage of must be applied to each taskMode
            port1in, port2in, LED1, LED2, Water1, Water2 = self.switch_active_side(
                previousOutcomeSuccessful,
                activeSide,
                self.params["activeSide"].get_items(),
                nextPortAfterFail,
            )

            self.sm.add_state(
                name="startTrial",
                statetimer=0,
                transitions={"Tup": "iti"},
                outputsOff=[LED1, LED2],
            )
            
            # Conditional to define if an ITI is applied before the next trial
            if previousOutcomeSuccessful:
                if (self.params["ITIAfterSuccess"].get_items()).index(ITIAfterSuccess) and interTrialInterval:
                    transition_iti = {"Tup":"turnLEDon0"}
                else:
                    transition_iti = {"Tup":"waitForAnyPoke"}
            else:
                if (self.params["ITIAfterFail"].get_items()).index(ITIAfterFail) and interTrialInterval:
                    transition_iti = {"Tup":"turnLEDon0"}
                else:
                    transition_iti = {"Tup":"waitForAnyPoke"}
            
            # Move iti to the beginning so that the iti is applied first
            self.sm.add_state(
                name="iti",
                statetimer=0,
                transitions=transition_iti,
                outputsOff=[LED1, LED2, Water1, Water2],
            )

            # flashing lights for the inter-trial interval period.
            for flash in range(0, timesFlashingLightsCounter):
                # I am trying to keep the flashing lights if the mice are poking
                if flash == (timesFlashingLightsCounter - 1):

                    transitions = {
                        "N1in": "turnLEDonBackUp0",
                        "S1in": "turnLEDonBackUp0",
                        "N2in": "turnLEDonBackUp0",
                        "S2in": "turnLEDonBackUp0",
                        "Tup": "waitForAnyPoke",
                    }
                else:
                    transitions = {"Tup": f"turnLEDon{flash + 1}"}

                self.sm.add_state(
                    name=f"turnLEDon{flash}",
                    statetimer=timeLEDon,
                    transitions={"Tup": f"turnLEDoff{flash}"},
                    outputsOn=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

                self.sm.add_state(
                    name=f"turnLEDoff{flash}",
                    statetimer=(
                        0.5 if flash == (timesFlashingLightsCounter - 1) else timeLEDon
                    ),
                    transitions=transitions,
                    outputsOff=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

            # if the mice are interating with the ports during the flash lights when is gonna end,
            # another second of flashing ligths is applied
            for flashBackUp in range(0, timesFlashingLightsBackUp):
                self.sm.add_state(
                    name=f"turnLEDonBackUp{flashBackUp}",
                    statetimer=timeLEDon,
                    transitions={"Tup": f"turnLEDoffBackUp{flashBackUp}"},
                    outputsOn=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

                self.sm.add_state(
                    name=f"turnLEDoffBackUp{flashBackUp}",
                    statetimer=timeLEDon,
                    transitions={
                        "Tup": (
                            f"turnLEDon{timesFlashingLightsCounter - 2}"
                            if flashBackUp == (timesFlashingLightsBackUp - 1)
                            else f"turnLEDonBackUp{flashBackUp + 1}"
                        )
                    },
                    outputsOff=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

            self.sm.add_state(
                name="waitForAnyPoke",
                statetimer=LONGTIME,
                transitions={
                    port1in: f"waitForPoke2.0",
                    port2in: f"waitForPoke1.0",
                },
                outputsOn=[LED1, LED2],
            )

            ## This loop is to produce as many pokes as need it to accomplish the amount of time in the ports
            ## the number of pokes depends on the time between each poke and how long mice have to be at ports
            for poke in range(0, totalNumberOfPokes):
                ## In the last iteration, trasition has to change to continue the flow of the states
                if (poke + 1) == totalNumberOfPokes:
                    waitForPoke1: str = "reward0"
                    waitForPoke2: str = "reward0"
                else:
                    waitForPoke1: str = f"waitForPoke1.{poke + 1}"
                    waitForPoke2: str = f"waitForPoke2.{poke + 1}"

                self.sm.add_state(
                    name=f"waitForPoke1.{poke}",
                    statetimer=waitTime,
                    transitions={
                        port1in: waitForPoke2,
                        "Tup": "nextTrial",
                    },
                )
                self.sm.add_state(
                    name=f"waitForPoke2.{poke}",
                    statetimer=waitTime,
                    transitions={
                        port2in: waitForPoke1,
                        "Tup": "nextTrial",
                    },
                )

            for reward in range(0, rewardFrequency):

                ## In the last iteration, trasition has to change to continue the flow of the states
                if (reward + 1) == rewardFrequency:
                    nextReward: str = "nextTrial"
                else:
                    nextReward: str = f"reward{reward + 1}"

                self.sm.add_state(
                    name=f"reward{reward}",
                    statetimer=timeWaterValves,
                    transitions={"Tup": f"stopReward{reward}"},
                    outputsOn=[Water1, Water2],
                )
                self.sm.add_state(
                    name=f"stopReward{reward}",
                    statetimer=0,
                    transitions={"Tup": nextReward},
                    outputsOff=[Water1, Water2],
                )

            self.sm.add_state(
                name="nextTrial",
                statetimer=0,
                transitions={"Tup": "readyForNextTrial"},
                outputsOff=[Water1, Water2],
            )
        elif taskMode == "cooperate":
            ## This is to set a different value to LED during this task
            # self.params["timeLEDon"].set_value(0.2)

            # Determine if previous trial was successfull
            previousOutcomeSuccessful: bool = (
                previousOutcome == self.results.labels["outcome"]["rewardedBoth"]
            )

            # -- If mice achieve thresholdForIncrementPoke trials the amount of time poking is increased --
            if (self.params["activatePokeIncrement"].get_items()).index(activatePokeIncrement):
                if (
                    (previousOutcomeSuccessful)
                    and (pokesPerMouse < targetPokesPerMouse)
                    and (nrewarded > 0)
                    and (nrewarded % thresholdForIncrementPoke == 0)
                ):
                    update_pokes = pokesPerMouse + numberOfPokeAddPerMouse
                    # Make the number of pokes accumulated equal to the target if the former is greater
                    if update_pokes > targetPokesPerMouse:
                        update_pokes = targetPokesPerMouse
                    else:
                        pass
                    self.params["pokesPerMouse"].set_value(
                        (update_pokes)
                    )
                    pokesPerMouse = self.params["pokesPerMouse"].get_value()
                    # This is for the loop to create pokes states
                    totalNumberOfPokes = (pokesPerMouse * 2) - 1
                else:
                    pass
            else:
                pass

            ## This is to flash the lights during iti (turn on/ turn off)
            timesFlashingLightsCounter: int = round(
                (interTrialInterval / timeLEDon) / 2
            )
            timesFlashingLightsBackUp: int = round((extraTimeITI / timeLEDon) / 2)


            # This method is applied to evaluate whether a new side will be chosen
            # Since the meaning of success may vary with each stage of must be applied to each taskMode
            port1in, port2in, LED1, LED2, Water1, Water2 = self.switch_active_side(
                previousOutcomeSuccessful,
                activeSide,
                self.params["activeSide"].get_items(),
                nextPortAfterFail,
            )

            self.sm.add_state(
                name="startTrial",
                statetimer=0,
                transitions={"Tup": "iti"},
                outputsOff=[LED1, LED2],
            )
            # Conditional to define if an ITI is applied before the next trial
            if previousOutcomeSuccessful:
                if (self.params["ITIAfterSuccess"].get_items()).index(ITIAfterSuccess) and interTrialInterval:
                    transition_iti = {"Tup":"turnLEDon0"}
                else:
                    transition_iti = {"Tup":"waitForAnyPoke"}
            else:
                if (self.params["ITIAfterFail"].get_items()).index(ITIAfterFail) and interTrialInterval:
                    transition_iti = {"Tup":"turnLEDon0"}
                else:
                    transition_iti = {"Tup":"waitForAnyPoke"}
            
            # Move iti to the beginning so that the iti is applied first
            self.sm.add_state(
                name="iti",
                statetimer=0,
                transitions=transition_iti,
                outputsOff=[LED1, LED2, Water1, Water2],
            )

            # flashing lights for the inter-trial interval period.
            for flash in range(0, timesFlashingLightsCounter):
                # I am trying to keep the flashing lights if the mice are poking
                if flash == (timesFlashingLightsCounter - 1):

                    transitions = {
                        "N1in": "turnLEDonBackUp0",
                        "S1in": "turnLEDonBackUp0",
                        "N2in": "turnLEDonBackUp0",
                        "S2in": "turnLEDonBackUp0",
                        "Tup": "waitForAnyPoke",
                    }
                else:
                    transitions = {"Tup": f"turnLEDon{flash + 1}"}

                self.sm.add_state(
                    name=f"turnLEDon{flash}",
                    statetimer=timeLEDon,
                    transitions={"Tup": f"turnLEDoff{flash}"},
                    outputsOn=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

                self.sm.add_state(
                    name=f"turnLEDoff{flash}",
                    statetimer=(
                        0.5 if flash == (timesFlashingLightsCounter - 1) else timeLEDon
                    ),
                    transitions=transitions,
                    outputsOff=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

            # if the mice are interating with the ports during the flash lights when is gonna end,
            # another second of flashing ligths is applied
            for flashBackUp in range(0, timesFlashingLightsBackUp):
                self.sm.add_state(
                    name=f"turnLEDonBackUp{flashBackUp}",
                    statetimer=timeLEDon,
                    transitions={"Tup": f"turnLEDoffBackUp{flashBackUp}"},
                    outputsOn=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

                self.sm.add_state(
                    name=f"turnLEDoffBackUp{flashBackUp}",
                    statetimer=timeLEDon,
                    transitions={
                        "Tup": (
                            f"turnLEDon{timesFlashingLightsCounter - 2}"
                            if flashBackUp == (timesFlashingLightsBackUp - 1)
                            else f"turnLEDonBackUp{flashBackUp + 1}"
                        )
                    },
                    outputsOff=["N1LED", "N2LED", "S1LED", "S2LED"],
                )

            self.sm.add_state(
                name="waitForAnyPoke",
                statetimer=LONGTIME,
                transitions={
                    port1in: f"waitForPoke2.0",
                    port2in: f"waitForPoke1.0",
                },
            )

            ## This loop is to produce as many pokes as need it to accomplish the amount of time in the ports
            ## the number of pokes depends on the time between each poke and how long mice have to be at ports
            for poke in range(0, totalNumberOfPokes):

                ## In the last iteration, trasition has to change to continue the flow of the states
                if (poke + 1) == totalNumberOfPokes:
                    waitForPoke1: str = "reward0"
                    waitForPoke2: str = "reward0"
                else:
                    waitForPoke1: str = f"waitForPoke1.{poke + 1}"
                    waitForPoke2: str = f"waitForPoke2.{poke + 1}"

                self.sm.add_state(
                    name=f"waitForPoke1.{poke}",
                    statetimer=waitTime,
                    transitions={
                        port1in: waitForPoke2,
                        "Tup": "turnLEDoff",
                    },
                )
                self.sm.add_state(
                    name=f"waitForPoke2.{poke}",
                    statetimer=waitTime,
                    transitions={
                        port2in: waitForPoke1,
                        "Tup": "turnLEDoff",
                    },
                )

            for reward in range(0, rewardFrequency):

                ## In the last iteration, trasition has to change to continue the flow of the states
                if (reward + 1) == rewardFrequency:
                    nextReward: str = "turnLEDon"
                else:
                    nextReward: str = f"reward{reward + 1}"

                self.sm.add_state(
                    name=f"reward{reward}",
                    statetimer=timeWaterValves,
                    transitions={"Tup": f"stopReward{reward}"},
                    outputsOn=[Water1, Water2],
                )
                self.sm.add_state(
                    name=f"stopReward{reward}",
                    statetimer=0,
                    transitions={"Tup": nextReward},
                    outputsOff=[Water1, Water2],
                )

            self.sm.add_state(
                name="turnLEDon",
                statetimer=timeLEDon,
                transitions={"Tup": "turnLEDoff"},
                outputsOn=[LED1, LED2],
            )
            self.sm.add_state(
                name="turnLEDoff",
                statetimer=0,
                transitions={"Tup": "readyForNextTrial"},
                outputsOff=[LED1, LED2],
            )

        self.dispatcher.set_state_matrix(self.sm)
        self.dispatcher.ready_to_start_trial()

    def switch_active_side(
        self,
        previousOutcomeSuccessful: bool,
        active_side: str,
        sides: list,
        nextPortAfterFail: str,
    ) -> tuple:
        """_summary_
        Function to randomly select a new side available to give a reward.
        Args:
            previousOutcomeSuccessful (bool): If true a new side is selected randomly, otherwise, depending on the value of nextPortAfterFail, it is set the same side or changed.
            active_side (str): Register the last side selected. This is used to have track of how many times the same side is selected.
            sides (list): Sides options in the current paradigm, only two options are available (['north', 'south']).
            nextPortAfterFail (str): Two options ['Same', 'Opposite]. If it is set to 'opossite', after a fail trial the active side is changed to the opposite side. 
                If it is set to 'Same', after a fail trial the same active side is selected.  
        Returns:
            tuple: Return the following variables: port1in (event), port2in (event), LED1, LED2, Water1 , Water2
                that define the events, LEDs, and water ports for next trial.
        """

        # If the last trial was successful, we randomly choose another one
        if previousOutcomeSuccessful:
            # We choose a random index (0=north, 1=south)
            new_active_side = np.random.choice([0, 1])

            # If a side was selected more than n times in a row
            # the active side is changed to the other side
            if active_side == sides[new_active_side]:
                self.timesPortSelected += 1
                if (
                    self.timesPortSelected
                    > self.params["maxPortRepetition"].get_value()
                ):
                    active_side = sides[new_active_side - 1]
                    self.timesPortSelected = 1
            else:
                self.timesPortSelected = 1
                active_side = sides[new_active_side]
        # Select the opposite side after fail if nextPortAfterFail == "opposite"
        elif not (previousOutcomeSuccessful) and (
            nextPortAfterFail == self.params["nextPortAfterFail"].get_items()[1]
        ):
            active_side = sides[sides.index(active_side) - 1]
            self.timesPortSelected = 1

        # Assign variables depending on which side was chosen
        if active_side == "north":
            port1in = "N1in"
            port2in = "N2in"
            LED1 = "N1LED"
            LED2 = "N2LED"
            Water1 = "N1Water"
            Water2 = "N2Water"
        elif active_side == "south":
            port1in = "S1in"
            port2in = "S2in"
            LED1 = "S1LED"
            LED2 = "S2LED"
            Water1 = "S1Water"
            Water2 = "S2Water"

        self.params["activeSide"].set_string(active_side)

        return (port1in, port2in, LED1, LED2, Water1, Water2)

    def calculate_results(self, trialIndex):
        eventsThisTrial = self.dispatcher.events_one_trial(trialIndex)
        statesThisTrial = eventsThisTrial[:, 2]
        taskMode = self.params["taskMode"].get_string()
        # print(self.sm)

        # Save start time of the trial
        startTrialStateID = self.sm.statesNameToIndex["startTrial"]
        startTrialInd = np.flatnonzero(statesThisTrial == startTrialStateID)[0]
        self.results["timeTrialStart"][trialIndex] = eventsThisTrial[startTrialInd, 0]
        # -- Check if it's an aborted trial --
        lastEvent = eventsThisTrial[-1, :]
        if lastEvent[1] == -1 and lastEvent[2] == 0:
            self.results["outcome"][trialIndex] = self.results.labels["outcome"][
                "aborted"
            ]
            self.results["timePoke1"][trialIndex] = np.nan
            self.results["timePoke2"][trialIndex] = np.nan
            return

        if taskMode in ["auto_lights", "reward_on_first_poke"]:
            if self.sm.statesNameToIndex["reward1.0"] in statesThisTrial:
                self.params["nRewarded1"].add(1)
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["reward1.0"]
                )[0]
                self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                if self.sm.statesNameToIndex["reward2after1.0"] in statesThisTrial:
                    self.params["nRewarded2"].add(1)
                    eventInd = np.flatnonzero(
                        statesThisTrial == self.sm.statesNameToIndex["reward2after1.0"]
                    )[0]
                    self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                else:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["poke1only"]
                    self.results["timePoke2"][trialIndex] = np.nan
            elif self.sm.statesNameToIndex["reward2.0"] in statesThisTrial:
                self.params["nRewarded2"].add(1)
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["reward2.0"]
                )[0]
                self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                if self.sm.statesNameToIndex["reward1after2.0"] in statesThisTrial:
                    self.params["nRewarded1"].add(1)
                    self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                else:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["poke2only"]
                    self.results["timePoke1"][trialIndex] = np.nan
            else:
                self.results["outcome"][trialIndex] = self.results.labels["outcome"][
                    "none"
                ]
                self.results["timePoke1"][trialIndex] = np.nan
                self.results["timePoke2"][trialIndex] = np.nan
        elif taskMode in ["reward_on_last_poke"]:
            if self.sm.statesNameToIndex["waitForPoke2"] in statesThisTrial:
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["waitForPoke2"]
                )[0]
                self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                if self.sm.statesNameToIndex["reward"] in statesThisTrial:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                    self.params["nRewarded1"].add(1)
                    self.params["nRewarded2"].add(1)
                    eventInd = np.flatnonzero(
                        statesThisTrial == self.sm.statesNameToIndex["reward"]
                    )[0]
                    self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                else:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["poke1only"]
                    self.results["timePoke2"][trialIndex] = np.nan
            elif self.sm.statesNameToIndex["waitForPoke1"] in statesThisTrial:
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["waitForPoke1"]
                )[0]
                self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                if self.sm.statesNameToIndex["reward"] in statesThisTrial:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                    self.params["nRewarded1"].add(1)
                    self.params["nRewarded2"].add(1)
                    eventInd = np.flatnonzero(
                        statesThisTrial == self.sm.statesNameToIndex["reward"]
                    )[0]
                    self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                else:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["poke2only"]
                    self.results["timePoke1"][trialIndex] = np.nan
            else:
                # -- This should never happen, since a trial requires a poke --
                self.results["outcome"][trialIndex] = self.results.labels["outcome"][
                    "none"
                ]
                self.results["timePoke1"][trialIndex] = np.nan
                self.results["timePoke2"][trialIndex] = np.nan
        elif taskMode in ["cooperate_lights", "cooperate"]:
            if self.sm.statesNameToIndex["waitForPoke2.0"] in statesThisTrial:
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["waitForPoke2.0"]
                )[0]
                self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                if self.sm.statesNameToIndex["reward0"] in statesThisTrial:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                    self.params["nRewarded1"].add(1)
                    self.params["nRewarded2"].add(1)
                    eventInd = np.flatnonzero(
                        statesThisTrial == self.sm.statesNameToIndex["reward0"]
                    )[0]
                    self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                else:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["poke1only"]
                    self.results["timePoke2"][trialIndex] = np.nan
            elif self.sm.statesNameToIndex["waitForPoke1.0"] in statesThisTrial:
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["waitForPoke1.0"]
                )[0]
                self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                if self.sm.statesNameToIndex["reward0"] in statesThisTrial:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                    self.params["nRewarded1"].add(1)
                    self.params["nRewarded2"].add(1)
                    eventInd = np.flatnonzero(
                        statesThisTrial == self.sm.statesNameToIndex["reward0"]
                    )[0]
                    self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                else:
                    self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["poke2only"]
                    self.results["timePoke1"][trialIndex] = np.nan
            else:
                # -- This should never happen, since a trial requires a poke --
                self.results["outcome"][trialIndex] = self.results.labels["outcome"][
                    "none"
                ]
                self.results["timePoke1"][trialIndex] = np.nan
                self.results["timePoke2"][trialIndex] = np.nan
        elif taskMode in ["one_track"]:
            if self.sm.statesNameToIndex["reward"] in statesThisTrial:
                self.params["nRewarded1"].add(1)
                self.params["nRewarded2"].add(1)
                self.results["outcome"][trialIndex] = self.results.labels[
                        "outcome"
                    ]["rewardedBoth"]
                eventInd = np.flatnonzero(
                    statesThisTrial == self.sm.statesNameToIndex["reward"]
                )[0]
                
                # given that only one poke is needed for trigger the water releasing the time is stored in both variables
                self.results["timePoke1"][trialIndex] = eventsThisTrial[eventInd, 0]
                self.results["timePoke2"][trialIndex] = eventsThisTrial[eventInd, 0]
                
            else:
                # -- This should never happen, since a trial requires a poke --
                self.results["outcome"][trialIndex] = self.results.labels["outcome"][
                    "none"
                ]
                self.results["timePoke1"][trialIndex] = np.nan
                self.results["timePoke2"][trialIndex] = np.nan
                
        
    def closeEvent(self, event):
        """
        Executed when closing the main window.
        This method is inherited from QtWidgets.QMainWindow, which explains
        its camelCase naming.
        """
        # self.soundClient.shutdown()
        self.dispatcher.die()
        event.accept()


if __name__ == "__main__":
    (app, paradigm) = paramgui.create_app(Paradigm)
