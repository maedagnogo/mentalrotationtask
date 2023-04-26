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

#position1 = (0,0)
position2 = (250,0)

trials = [A, B, C, D, E]
random.shuffle(trials)

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for i in range(len(trials)):
    blankscreen.present()
    exp.clock.wait(WAIT_TIME)
    target1 = trials[i][0]
    n = random.randint(0,1)
    rotation_angle = random.randint(0,180)
    if n == 0 :
        target2 = target1
        congruence = 'cong'
    elif n == 1 :
        target2 = target1
        target2.flip((True,False))
        congruence = 'incong'

    target2.rotate(rotation_angle)
    target2.reposition(position2)

    target1.present()
    target2.present(clear=False)

    key, rt = exp.keyboard.wait()
    exp.data.add([i, trials[i][1], congruence, rotation_angle, key, rt])

control.end()
