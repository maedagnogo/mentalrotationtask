import random
from expyriment import design, control, stimuli

WAIT_TIME = 2000

exp = design.Experiment(name="Mental Rotation", text_size=40)
#control.set_develop_mode(on=True)
control.initialize(exp)

blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen("Instructions",
    f"""
    There will be  trials in total.

    Press the spacebar to start.""")

exp.add_data_variable_names(['trial', 'shape', 'congruence', 'rotation', 'respkey', 'RT'])

A = [stimuli.Picture('shapeA1.png'),"A"]
B = [stimuli.Picture('shapeB1.png'),"B"]
C = [stimuli.Picture('shapeC1.png'),"C"]
D = [stimuli.Picture('shapeD1.png'),"D"]
E = [stimuli.Picture('shapeE1.png'),"E"]

position1 = (-20,0)
position2 = (250,0)

shapes = [A, B, C, D, E]
N_trials = len(shapes)
random.shuffle(shapes)

targets2 = []
targets1 = []
congruence = []
rotation_angles = []

for i in range(N_trials):
    target1 = shapes[i][0]
    n = random.randint(0,1)
    rotation_angle = random.randint(0,180)
    rotation_angles.append(rotation_angle)

    if n == 0 :
        target2=target1
        congruence.append('cong')
    elif n == 1 :
        target2 = target1
        target2.flip((True,False))
        congruence.append('incong')
  
    target1.reposition(position1)
    targets1.append(target1)
    target2.reposition(position2)
    target2.rotate(rotation_angle)
    targets2.append(target2)

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for j in range(N_trials):
    targets2[j].plot(blankscreen)
    targets1[j].plot(blankscreen)
    blankscreen.present()
    key, rt = exp.keyboard.wait()
    exp.data.add([j, shapes[j][1], congruence[j], rotation_angles[j], key, rt])


control.end()
