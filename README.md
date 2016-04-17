# One-to-Many Match to Sample Task for Three Three-Member Classes (MTS - OtM 3x3)

## License
Copyright (c) Ian Hussey 2016 (ian.hussey@ugent.be)

Distributed under the MIT license.

## Version
0.6 (17/4/2016)

Written in PsychoPy 1.82.01

*NB This implimention is still in development and has not been used in a study yet.* 

## Block layout
- Trains three three-member classes: A1-B1-C1, A2-B2-C2, and A3-B3-C3 via one-to-many match to sample training.
- Blocks of 18 trials contain each contain a fully counterbalanced set of A1, A2 and A3 sample stimuli with the required target stimulus counterbalanced across all three stimuli locations. Location of 'incorrect' target stimuli is randomised. 
- Maximum of 12 blocks before task ends with a "Failed" message.
- Mastery criterion is N-in-a-row **within a given block**, and is set via a variable in the stimuli.xlsx file. Default is 15. If criterion is met, task immediately ends with a "Passed" message. 

## Notes
- The last row of a participant's .csv data file specifies whether they passed or failed the task under the "passed_training" column.
- For demonstration and testing purposes the task present the stimuli as "A1", "C2" etc. To use word stimuli simply alter the stimuli.xlsx file (or replace it with the "stimuli ALT - ARBITRARY.xlsx" file which contains nonsense words.
- Full unicode support, so one could use chinese characters etc as word stimuli. Font size might need to be increased however. 
- No support for image stimuli at present, but this would be trivial to add. For example, change TextComponents for ImageComponents and put image1.jpg etc in the stimulus file. All counterbalancing, block structure, etc is taken care of elsewhere.

## Known issues
None.

## To do
- Should the n-in-a-row be across blocks rather than within a given block? This could be done by simply moving "correct_in_a_row = 0" from instructions>inst_code>'Begin Routine' to instructions>inst_code>'Begin Experiment'.
- R script for data processing?
- Move instructions and accuracy feedback message to stimuli.xlsx file for translation to other languages?
- Fork a version for an equivalence task.

## Changelog
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