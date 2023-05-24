import random
from expyriment import design, control, stimuli
import numpy as np

CONG_RESPONSE = 106 
INCONG_RESPONSE = 102
WAIT_TIME = 1000
MAX_RESPONSE_DELAY = 4000

A = (stimuli.Picture('shapeA.png'),"A")
B = (stimuli.Picture('shapeB.png'),"B")
C = (stimuli.Picture('shapeC.png'),"C")
D = (stimuli.Picture('shapeD.png'),"D")
E = (stimuli.Picture('shapeE.png'),"E")
F = (stimuli.Picture('shapeF.png'),"F")
G = (stimuli.Picture('shapeG.png'),"G")
H = (stimuli.Picture('shapeH.png'),"H")
I = (stimuli.Picture('shapeI.png'),"I")
J = (stimuli.Picture('shapeJ.png'),"J")
K = (stimuli.Picture('shapeK.png'),"K")
L = (stimuli.Picture('shapeL.png'),"L")

position1 = (-250,0)
position2 = (250,0)

shapes = [A, B, C, D, E, F, G, H, I, J, K, L]
N_trials = len(shapes)

exp = design.Experiment(name="Mental Rotation", text_size=40)
#control.set_develop_mode(on=True)
control.initialize(exp)

blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen("Instructions",
    f""" At each trial, you are gonna see to shapes presented next to each other. Your task is to indicate as fast as possible whether the two shapes are identical or not.

    Press {CONG_RESPONSE} when you think they are identical and press {INCONG_RESPONSE} when you think they are not.

    There will be {N_trials} trials in total.

    Press the spacebar to start.""")

exp.add_data_variable_names(['trial', 'shape', 'congruence', 'rotation', 'respkey', 'RT'])



congruence = ['cong']*(int(N_trials/2))+(['incong']*(int(N_trials/2)))
rotation_angles = [30,60,90,120,150,180]*2
c = list(zip(congruence, rotation_angles))
random.shuffle(c)
congruence, rotation_angles = zip(*c)

block = design.Block("The one and only block")
for i in range(N_trials):
    target1 = shapes[i][0]

    if congruence[i] == 'cong' :
        target2=target1.copy()
        
    elif congruence[i] == 'incong' :
        target2=target1.copy()
        target2.flip((True,False))
  
    target1.reposition(position1)
    target2.reposition(position2)
    target2.rotate(rotation_angles[i])

    trial = design.Trial()
    trial.add_stimulus(target1)
    trial.add_stimulus(target2)

    trial.set_factor("rotation_angle", rotation_angles[i])
    trial.set_factor("congruence", congruence[i])
    trial.set_factor("shape", shapes[i][1])
    block.add_trial(trial, copies=1)

block.shuffle_trials()

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

i=0
for T in block.trials:
    stim1, stim2 = T.stimuli
    stim1.present(clear=True, update=False)
    stim2.present(clear=False, update=True)
    key, rt = exp.keyboard.wait([CONG_RESPONSE, INCONG_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)
    exp.data.add([i, T.get_factor("shape"), T.get_factor("congruence"), T.get_factor("rotation_angle"), key, rt])
    blankscreen.present()
    exp.clock.wait(WAIT_TIME)
    i = i+1

control.end()
