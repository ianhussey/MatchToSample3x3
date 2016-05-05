# One-to-Many Match to Sample Task for Three Three-Member Classes (MTS - OtM 3x3)

## License
Copyright (c) Ian Hussey 2016 (ian.hussey@ugent.be)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Version
0.7.4 (5/5/2016)

Written in PsychoPy 1.82.01

*NB This implementation is still in development and has not been used in a study yet.* 

## Notes
- Trains three three-member classes: A1-B1-C1, A2-B2-C2, and A3-B3-C3 via one-to-many match to sample training; then assesses for emergent C-B and B-C (equivalence) relations.
- Press return to end the task at the "end of task" screen.
- Includes R script in the "Analysis" folder which produces summaries of MTS performances, including demographic variables, pass/fail variables for both training and testing phases, and how many cycles of each were needed.
- All strings wihtin the task are set by the excel files. Easy to translate to other languages given there is full unicode support for non-english characters.
- The last row of a participant's .csv data file specifies whether they passed or failed the task under the "passed_training" and "passed_testing" columns record whether the mastery criterion was reached for each block. The R script extracts only the last repeat of each block in order to assess whether training and testing criteria were eventually passed or not.
- For demonstration and testing purposes the task present the stimuli as "A1", "C2" etc. To use word stimuli simply alter the stimuli.xlsx file (or replace it with the "stimuli ALT - ARBITRARY.xlsx" file which contains nonsense words.
- No support for image stimuli at present, but this would be trivial to add. For example, change TextComponents for ImageComponents and put image1.jpg etc in the stimulus file. All counterbalancing, block structure, etc is taken care of elsewhere.

## Task structure
*See the 'Explanation of task parameters' folder for illustrations of the task structure and the variables in the excel files that determine your parameters.*

- Training block contain X multiples of 18 trials, which each include a fully counterbalanced set of A1, A2 and A3 sample stimuli with the required target stimulus counterbalanced across all three stimuli locations. The location of the incorrect comparison stimuli is randomised for each trial.
- If the training crition of Y number of correct trials within a block is met, participants proceed to the testing block. 
- Otherwise, participants repeat the training block. This is done a max number of Z times.
- Testing block contains J multiples of 18 C-B and B-C (i.e. equivalence) trials. Symmetry relations could be added simply by modiying the task structure file.
-  If the testing crition of K number of correct trials within a block is met, the task ends with a "passed" message. 
-  Otherwise, participants repeat the testing block. This is done a max number of L times.
- If the max training or testing block repeats (Z or L) is reached, immediately after that block is finished the participant is recycled back to the start of the training blocks a maxiumum of Q number of times. 
- Note that the above means that if participant fail to meet the training criterion Z number of times they do not complete the testing blocks, but rather are given Q total opportunities to complete a max of Z number of training blocks, to meet the mastery criterion of Y trials out of X in each training block. This is somewhat abstract, but means that the task is trivial to adapt to the needs of your experimental design.
- NB By setting the training mastery criterion to 0 you can alter the structure of the task to that participants alwasys move from training to testing blocks, and therefore recieve loops of training and testing together rather than having to meet mastery criteria for each seperately. 

## Example task setups
In order to illustrate the flexibility of the current implimentation, three example setups are discussed below.

### Example setup 1
	training_criterion == 0
	testing_criterion == 17
	max_training == 1
	max_testing == 1
	max_training_and_testing == 10
	training_block_multiplier == 3
	testing_block_multiplier == 1
Participants will complete 1 block of 52 (i.e., 18\*3) training trials (A-B and A-C), and regardless of their performance on this block (because criterion = 0 and max = 1) it will be followed by 1 block of 18 (18\*1) testing trials (C-B and B-C). If they meet the testing criterion (>=17 correct) the task finishes, otherwise they will repeat this pair of training and testing blocks up to 9 additional times.

### Example setup 2
	training_criterion == 17
	testing_criterion == 17
	max_training == 18
	max_testing == 1
	max_training_and_testing == 2
	training_block_multiplier == 1
	testing_block_multiplier == 1
Participants will complete blocks of 18 (18\*1) training trials (A-B and A-C) until they meet the training mastery criterion (>=17 correct trials). They are provided with up to 18 opportunities to do so (i.e., up to 324 trials). If they meet the criterion, they will immediately complete a block of 18 (18\*1)  testing trials (C-B and B-C). If they meet the testing criterion (>=17) the task finishes, otherwise they will go back to the training phase. However, they will only be provided with a max of two total opportunities to pass the testing block.

### Example setup 3
	training_criterion == 47
	testing_criterion == 17
	max_training == 10
	max_testing == 10
	max_training_and_testing == 1
	training_block_multiplier == 3
	testing_block_multiplier == 1
Using these settings, participants will complete blocks of 52 (18\*3) training trials (A-B and A-C) until they meet the training mastery criterion (>=47). They are provided with up to 10 opportunities to do so (i.e., 520 max trials). If they meet the training criterion, they will immediately complete blocks of 18 (18\*1)  testing trials (C-B and B-C). Again, they will be provided with up to 10 opportunities to meet the criterion (>=17 correct), but will not be recycled back to the training phase after each failure or indeed at all. In this setup, participants must meet training and testing mastery criteria seperately to pass the task, but never recieve additional training once they have moved on to the testing phase.

## Known issues
None.

## To do
- None

## Changelog
### 0.7.4
- Testing by default includes B-C trials now as well as C-B trials, as bidirectionality here is likely to be important. 
- Updated explanation of task parameters appropriately.
- Updated default task parameters.

### 0.7.3
Trial sequence for testing was incorrectly set to sequential. Changed both training and testing to fullRandom.

### 0.7.2
Updated readme and included 'explanations of task parameters' folder to illustrate different parameters of the task.

### 0.7
Many changes. 
- Intigrated training and testing into one task. 
- All strings in stimuli file, as well as several task parameters.
- Several training and testing methods available based on the pairs of mastery criteria, block length multipliers, and max reps variables.
- Working R script

### 0.6
Moved loop.finished code to a new postblock routine so that the full block is completed. 

### 0.5
1. Extra variables saved to .csv files: pass/fail training, exemplars used on each trial, current N-in-a-row.
2. Full screen.
3. Saves log file.

### 0.4
1. Code solution to randomised location of incorrect target stimuli. block_layout file reorganised to refer to required, incorrect1 and incorrect2 stimuli and specify required response. Based on required response, the contents of this location is filled with the required answer. The contents of the other two targets are then shuffle-pop()'d. Block length is therefore more flexible now. 
2. N-in-a-row mastery criterion now in excel file.

### 0.3
Now has proper counterbalancing of location of incorrect taret stimuli, but this is done via full permutations in the stimulus file. If you want a block length smaller than 36 trials then a coder solution would be needed.

### 0.2
Seperate files for block structure and exemplars, plus code to populate the sample and target stimuli boxes on a trial by trial basis.

### 0.1
Stimuli pulled from single file however, therefore this file conflates block structure with stimulus exemplars.