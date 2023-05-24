# mentalrotationtask

This repository stores scripts I wrote to create a 2D mental rotation task with expyriment, inspired by the famous 3D mental rotation task by Sheperd. 
For participants, each trial of this task consists in viewing two shapes rotated by distinct angles presented next to each other, and to decide whether the two shapes are identical or not. The hypothesis motivating this experiment is that, in order to identify whether two identical shapes that are presented with distinct rotation angles are indeed the same, participants have to perform mental rotation, which is reflected in their response times, that we expect to be proportional to the amplitude of the rotation performed. 

"shapesgenerationv1.py" is the script to execute in order to generate the 12 png files that will be used as stimuli during the experiment. The file generates those figures using pygame, by creating series of small white squares forming the shapes, which are each displayed inside of a black circle. The shapes were generated such that they are all chiral (not superimposable on their mirror image) and made of 6 small squares.

"mentalrotation.py" is the file that executes the experiment.
