import random
from expyriment import design, control, stimuli


CONG_RESPONSE = 106 #key : "j"
INCONG_RESPONSE = 102 #key : "f"
WAIT_TIME = 1000
MAX_RESPONSE_DELAY = 4000

#lauching expyriment
exp = design.Experiment(name="Mental Rotation", text_size=40)
control.initialize(exp)

#loading the shapes generated with the shapesgeneration script, within a pair containing the shape object and its label
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

position1 = (-250,0) #position for the shape presented on the left
position2 = (250,0) #position for the shape presented on the right

shapes = [A, B, C, D, E, F, G, H, I, J, K, L] #storing the shapes in a list
N_trials = len(shapes) #there will be as many trials as shapes (1 trial per shape)

blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen("Instructions",
    f""" At each trial, you are gonna see to shapes presented next to each other. Your task is to indicate as fast as possible whether the two shapes are identical or not.

    Press J when you think they are identical and press F when you think they are not.

    There will be {N_trials} trials in total.

    Press the spacebar to start.""")

exp.add_data_variable_names(['trial', 'shape', 'congruence', 'rotation', 'respkey', 'RT'])


#Here, we create lists of trial conditions for congruence and rotation angles
congruence = ['cong']*(int(N_trials/2))+(['incong']*(int(N_trials/2))) #we create a list of 6 congruent trials and 6 incongruent trials
rotation_angles = [30,60,90,120,150,180]*2 #we create a list of 6 rotation angles, which is replicated once, so that all rotation angles are associated with both congruency conditions
tmp = list(zip(congruence, rotation_angles)) #we zip both lists together before shuffling, in order to make sure that all rotation angles are evenly spread across congruency conditions
random.shuffle(tmp) #shuffle the ziped lists so that when we create the trials, the shapes are not always in the same conditions across all participants
congruence, rotation_angles = zip(*tmp) #unshuffle to recover both of conditions separately

#let's now create a block
block = design.Block("The one and only block")

#we create trials for each of the 12 shapes
for i in range(N_trials):

    target1 = shapes[i][0] #we create the shape that will appear on the left, which will remain unchanged

    #we then create the shape that will appear on the right, which will be identical to target1 in the congruent condition, and which will be its chiral form in the incongruent condition
    if congruence[i] == 'cong' :
        target2=target1.copy()
        
    elif congruence[i] == 'incong' :
        target2=target1.copy()
        target2.flip((True,False))

    #we position both objects on the left and right positions on the screen defined before, and we rotate target 2 by the angle defined according to the list of angles created previously
  
    target1.reposition(position1)
    target2.reposition(position2)
    target2.rotate(rotation_angles[i])

    #create a trial and add the stimuli to it :
    trial = design.Trial()
    trial.add_stimulus(target1)
    trial.add_stimulus(target2)

    #create factors for the trial, so that we can later retrieve the conditions of the trial

    trial.set_factor("rotation_angle", rotation_angles[i])
    trial.set_factor("congruence", congruence[i])
    trial.set_factor("shape", shapes[i][1])
    block.add_trial(trial, copies=1)

#once trials have been created for all shapes, we shuffle the block to randomise the order of the trials
block.shuffle_trials()


#starting the experiment :
control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

i=0 #variable that will be used to update and store trial number
for T in block.trials: #for each trials in the block
    stim1, stim2 = T.stimuli #we define stim1 and 2 corresponding to the two targets created previously
    #present both stim at the same time:
    stim1.present(clear=True, update=False)
    stim2.present(clear=False, update=True)
    #retrieve key and RT:
    key, rt = exp.keyboard.wait([CONG_RESPONSE, INCONG_RESPONSE],
                                     duration=MAX_RESPONSE_DELAY)
    #store the data for each trial, by retrieving the conditions factor by using get_factor
    exp.data.add([i, T.get_factor("shape"), T.get_factor("congruence"), T.get_factor("rotation_angle"), key, rt])
    i = i+1
    blankscreen.present()
    exp.clock.wait(WAIT_TIME)
    

control.end()
