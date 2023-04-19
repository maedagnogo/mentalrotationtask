import random
from expyriment import design, control, stimuli

WAIT_TIME = 2000

exp = design.Experiment(name="Visual Detection", text_size=40)
#control.set_develop_mode(on=True)
control.initialize(exp)

blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen("Instructions",
    f"""
    There will be {N_TRIALS} trials in total.

    Press the spacebar to start.""")

exp.add_data_variable_names(['trial', 'shape', 'congruence', 'rotation', 'respkey', 'RT'])
#blabalabalaaapkeoidhzeouizio

#expyriment.stimuli.Picture