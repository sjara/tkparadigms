# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A flat collection of behavioral/stimulus-presentation paradigms from the Jaramillo lab, built on the
[taskontrol](https://github.com/sjara/taskontrol) framework. Each top-level `*.py` file is an independent,
directly runnable Qt GUI application; there is no package, build step, linter config, or test suite here.

The taskontrol source is checked out next to this repo at `../taskontrol` (installed in development mode).
Read it when you need to know what a framework call does: `taskontrol/{dispatcher,paramgui,statematrix,savedata}.py`
and `taskontrol/plugins/` (`templates.py`, `soundclient.py`, `speakercalibration.py`, plotting widgets).

## Running paradigms

Always use the `taskontrol` virtual environment (virtualenvwrapper, at `~/.virtualenvs/taskontrol`):

```bash
workon taskontrol                                   # or call ~/.virtualenvs/taskontrol/bin/python directly
python sound_tuning.py                              # GUI defaults only
python sound_tuning.py tuningFreq                   # load dict `tuningFreq` from rigsettings.DEFAULT_PARAMSFILE (./params.py)
python sound_tuning.py params.santiago.py tuningFreq  # load dict `tuningFreq` from the given params file
```

Argument handling lives in `paramgui.create_app()`. Run from the repository root, since the default params
file path is relative.

Running a paradigm opens a GUI window and blocks until it is closed, so it cannot be used as an unattended
check. To verify an edit without opening a window:

- `python -m py_compile <file>.py` for a syntax check.
- For behavior, run a short script with `QT_QPA_PLATFORM=offscreen SDL_AUDIODRIVER=dummy` that creates a
  `QApplication`, imports the paradigm, instantiates `Paradigm()`, replaces
  `paradigm.dispatcher.set_state_matrix` and `paradigm.dispatcher.ready_to_start_trial` with no-ops, and calls
  `paradigm.prepare_next_trial(trial)` by hand. Parameters can be set with `set_value()` / `set_string()` and
  read back after each call; `paradigm.grab().save(<png>)` gives an image of the layout. This needs
  `STATE_MACHINE_TYPE = 'emulator'` in the rig settings.
- Sound waveforms can be checked without any GUI through `soundclient.create_soundwave(sound_dict, samplingRate)`.

Rig-specific configuration (state machine type, sound server, inputs/outputs, data directory, speaker
calibration files) comes from `../taskontrol/settings/rigsettings.py`, not from this repository. With
`STATE_MACHINE_TYPE = 'emulator'` a paradigm runs without hardware and shows an emulator window.

## Anatomy of a paradigm

Every paradigm defines a `Paradigm` class (a `QMainWindow`) and ends with
`(app, paradigm) = paramgui.create_app(Paradigm)`. The constructor signature must be
`__init__(self, parent=None, paramfile=None, paramdictname=None)`. Inside it, in order:

1. Create a `dispatcher.Dispatcher` (trial loop + connection to the state machine).
2. Fill `self.params = paramgui.Container()` with `StringParam` / `NumericParam` / `MenuParam` objects, each
   assigned to a `group`; `self.params.layout_group(<group>)` returns the widget for that group.
3. Call `self.params.from_file(paramfile, paramdictname)` after all parameters are defined, to apply overrides.
4. Create the `statematrix.StateMatrix`, `savedata.SaveData`, and the `soundclient.SoundClient`.
5. Lay out the widgets and connect `self.dispatcher.prepareNextTrial` to `self.prepare_next_trial`.

`prepare_next_trial(next_trial)` is the core of each paradigm. It runs once per trial and must:
call `self.params.update_history(next_trial-1)` (skipped before the first trial), choose the next trial's
conditions, write them into GUI parameters, load sounds with `self.soundClient.set_sound(index, sound_dict)`,
rebuild the state matrix (`self.sm.reset_transitions()` then `self.sm.add_state(...)`), and finish with
`self.dispatcher.set_state_matrix(self.sm)` and `self.dispatcher.ready_to_start_trial()`.

Two families of paradigms exist:

- **Stimulus presentation** (`sound_tuning.py`, `am_tuning.py`, `tones_and_wn.py`, `oddball_sequence.py`, ...):
  subclass `QMainWindow` directly and build the whole layout themselves. The state matrix is a simple
  timed sequence (start → stimulus on → stimulus off). `sound_tuning.py` is the most recent and the best model
  for new ones.
- **Behavioral tasks** (`am_discrimination.py`, `headfixed_twochoice.py`, `sound_localization.py`, ...):
  subclass `templates.Paradigm2AFC` or `templates.ParadigmGoNoGo`, which provide the dispatcher, state matrix,
  save module, manual control, and plots. These add `set_state_matrix()` (transitions driven by port/lick
  events), `calculate_results(trialIndex)` to score the previous trial, and often `execute_automation()` for
  automatic changes to parameters across trials.

### Things that are easy to break

- **Parameter keys are the saved data schema.** Every key in `self.params` is saved per trial to the HDF5
  file, and `MenuParam` item strings are saved as labels. Downstream analysis code reads these names, so
  renaming a key or a menu item changes the data format for all future sessions. The same keys are used in
  the `params.*.py` dictionaries, which must be updated together with any rename.
- **Read-only "current value" parameters** (created with `enabled=False`) are how per-trial values that the
  code chooses get recorded. Anything that should be available per trial during analysis has to be written
  into such a parameter in `prepare_next_trial` before the history is updated on the next call.
- **Sound amplitudes come from speaker calibration**, not from raw numbers: intensities in dB SPL are
  converted with `speakercalibration.Calibration.find_amplitude(frequency, intensity)` (tones) or
  `NoiseCalibration.find_amplitude(intensity)` (noise), which return one amplitude per channel `[left, right]`.
- **Sync outputs are optional per rig.** Paradigms check `'outBit0' in rigsettings.OUTPUTS` (and similar)
  at module level and fall back to an empty list, so that the same file runs on rigs without those lines.
- `closeEvent` must call `self.soundClient.shutdown()` and `self.dispatcher.die()`.

### Adding a sound type to `sound_tuning.py`

`sound_tuning.py` is under active development and has one GUI group per sound type. A new type touches
these places, and often the taskontrol repository too:

1. If the waveform does not exist yet, add a branch to `create_soundwave()` in
   `../taskontrol/taskontrol/plugins/soundclient.py` and describe its parameters in that function's docstring.
   This is a separate git repository: it needs its own commit and push, and anyone pulling tkparadigms must
   pull taskontrol as well.
2. A parameter group with an `include_<type>` menu, the stimulus parameters (keys prefixed with the type
   name, such as `FMfixedrange_` or `bandnoise_`), and read-only `current_<type>_...` parameters.
3. The new label appended at the end of the `current_stim_type` menu.
4. A block in `populate_sound_params()` that appends one dictionary per condition, and a matching branch in
   `prepare_next_trial()` that builds the sound dictionary and sets the read-only parameters.
5. The group widget added to one of the layout columns.

While this paradigm is in development, renaming its keys or labels for a real improvement is acceptable when
asked; update the `params.*.py` dictionaries that use them in the same change.

## Parameter files

`params.<experimenter>.py` files contain plain dictionaries of `{parameter_key: value}`, usually named after
a subject (`test000`, `pred000`) or a stimulus set (`tuningFreq`, `tuningAM`). A dictionary only applies to
the paradigm whose parameter keys it uses; nothing records which paradigm a dictionary is meant for, so check
the keys against the paradigm. For `MenuParam` parameters the value is the item string. A key that the
paradigm does not have is skipped with a printed warning, not an error, so a stale dictionary fails silently.
`archive/` holds params files from past lab members.

Each params file belongs to the person it is named after, who may have unpushed edits. Keep changes to
someone else's file in a separate commit, and check with the user before committing them.

## Git workflow

Work generally happens on a branch, not directly on `master`. Before making large modifications, ask the
user whether to create a branch; this applies to taskontrol as well when the task changes it. Before starting
work, fetch both repositories and check that they are up to date with origin. The taskontrol checkout has
unrelated uncommitted changes in `examples/`; stage only the files that were changed for the task.

## State of the codebase

- About 20 older paradigms still import from `taskontrol.core` / `taskontrol.settings` (for example
  `tuning_curve.py`, `photostim.py`, `cued_discrim.py`, `light_discrim.py`). Those modules no longer exist in
  the installed taskontrol, so these files do not run as they are. Current imports are
  `from taskontrol import dispatcher, paramgui, savedata, statematrix, rigsettings, utils`.
- Naming style differs by age: older paradigms use camelCase for parameter keys and local variables
  (`targetDuration`, `nextTrial`), while newer ones (`sound_tuning.py`) use snake_case. Follow the style of
  the file being edited, and do not rename existing parameter keys just for consistency unless asked.
- Several files are copies or variants kept alongside the original (`temp_am_discrimination.py`,
  `am_tuning_new.py`, `headfixed_twochoice_SDTvars.py`, `cooperate_four_ports_v1_juan.py`,
  `more_sounds_copy20151120.py`). Confirm which one is meant before editing.
- `rig_test.py` and `water_calibration.py` are rig utilities, not experiments, and use their own class names.
