# mentalrotationtask

This repository stores scripts I wrote to create a 2D mental rotation task with expyriment (https://expyriment.org/), inspired by the famous 3D mental rotation task by Sheperd. 

For participants, each trial of this task consists in viewing two shapes rotated by distinct angles presented next to each other, and to decide whether the two shapes are identical or not. The hypothesis motivating this experiment is that, in order to identify whether two identical shapes that are presented with distinct rotation angles are indeed the same, participants have to perform a mental rotation which is reflected in their response times, that we expect to be proportional to the amplitude of the rotation performed. 

In this version of the experiment, I created twelve trials, including 6 trials in which the two shapes presented are identical (congruent trials) and 6 in which the two shapes are different (incongruent trials). Incongruent trials are designed such that the shape presented on the right is the chiral version of the shape presented on the left, so that participant cannot indentify that the shapes are different based on salient characteristic features differing between the two. 
In each trial, the shape presented on the right is rotated by a certain angle compared to the shape presented on the right. I implemented 6 conditions of rotation angles : rotation angles go from 30° to 180°, with 30° steps. 
The conditions are implemented such that each rotation angle is represented in both conditions of congruency. 


"shapesgenerationv1.py" is the script to execute in order to generate the 12 png files that will be used as stimuli during the experiment. The file generates those figures using pygame, by creating series of small white squares forming the shapes, which are each displayed inside of a black circle. The shapes were generated such that they are all chiral (not superimposable on their mirror image, so that chiral incongruent trials can be generated) and made of 6 small squares.

"mentalrotation.py" is the file that executes the experiment (it is commented with every information necessary to understand what was done).
