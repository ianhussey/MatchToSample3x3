#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Fri Apr 22 20:45:28 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'MTS - OtM 3x3'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[800, 600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
inst_box = visual.TextStim(win=win, ori=0, name='inst_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instruct_training"
instruct_trainingClock = core.Clock()
inst_training_box = visual.TextStim(win=win, ori=0, name='inst_training_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Dependencies
import random

# Declare variable for pass/fail training
passed_training = False
passed_testing = False
total_correct = 0
max_testing_var = 0 # by default, don't do the testing block. This gets set to 1 if training is passed.
sample_box = visual.TextStim(win=win, ori=0, name='sample_box',
    text='default text',    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
target_left_box = visual.TextStim(win=win, ori=0, name='target_left_box',
    text='default text',    font='Arial',
    pos=[-.5, -.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
target_middle_box = visual.TextStim(win=win, ori=0, name='target_middle_box',
    text='default text',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
target_right_box = visual.TextStim(win=win, ori=0, name='target_right_box',
    text='default text',    font='Arial',
    pos=[.5, -.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_box = visual.TextStim(win=win, ori=0, name='feedback_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "post_training"
post_trainingClock = core.Clock()


# Initialize components for Routine "instruct_testing"
instruct_testingClock = core.Clock()
inst_testing_box = visual.TextStim(win=win, ori=0, name='inst_testing_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Dependencies
import random

# Declare variable for pass/fail training
passed_training = False
passed_testing = False
total_correct = 0
max_testing_var = 0 # by default, don't do the testing block. This gets set to 1 if training is passed.
sample_box = visual.TextStim(win=win, ori=0, name='sample_box',
    text='default text',    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
target_left_box = visual.TextStim(win=win, ori=0, name='target_left_box',
    text='default text',    font='Arial',
    pos=[-.5, -.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
target_middle_box = visual.TextStim(win=win, ori=0, name='target_middle_box',
    text='default text',    font='Arial',
    pos=[0, -.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
target_right_box = visual.TextStim(win=win, ori=0, name='target_right_box',
    text='default text',    font='Arial',
    pos=[.5, -.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "post_testing"
post_testingClock = core.Clock()


# Initialize components for Routine "end"
endClock = core.Clock()

end_box = visual.TextStim(win=win, ori=0, name='end_box',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
task = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('stimuli, instructions and parameters.xlsx'),
    seed=None, name='task')
thisExp.addLoop(task)  # add the loop to the experiment
thisTask = task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTask.rgb)
if thisTask != None:
    for paramName in thisTask.keys():
        exec(paramName + '= thisTask.' + paramName)

for thisTask in task:
    currentLoop = task
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask.keys():
            exec(paramName + '= thisTask.' + paramName)
    
    #------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    inst_box.setText(inst_intro
)
    inst_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    inst_resp.status = NOT_STARTED
    # keep track of which components have finished
    instructionsComponents = []
    instructionsComponents.append(inst_box)
    instructionsComponents.append(inst_resp)
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_box* updates
        if t >= 0.5 and inst_box.status == NOT_STARTED:
            # keep track of start time/frame for later
            inst_box.tStart = t  # underestimates by a little under one frame
            inst_box.frameNStart = frameN  # exact frame index
            inst_box.setAutoDraw(True)
        
        # *inst_resp* updates
        if t >= 0.5 and inst_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            inst_resp.tStart = t  # underestimates by a little under one frame
            inst_resp.frameNStart = frameN  # exact frame index
            inst_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if inst_resp.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    training_and_testing = data.TrialHandler(nReps=max_training_and_testing, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='training_and_testing')
    thisExp.addLoop(training_and_testing)  # add the loop to the experiment
    thisTraining_and_testing = training_and_testing.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTraining_and_testing.rgb)
    if thisTraining_and_testing != None:
        for paramName in thisTraining_and_testing.keys():
            exec(paramName + '= thisTraining_and_testing.' + paramName)
    
    for thisTraining_and_testing in training_and_testing:
        currentLoop = training_and_testing
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_and_testing.rgb)
        if thisTraining_and_testing != None:
            for paramName in thisTraining_and_testing.keys():
                exec(paramName + '= thisTraining_and_testing.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        training = data.TrialHandler(nReps=max_training, method='sequential', 
            extraInfo=expInfo, originPath=None,
            trialList=[None],
            seed=None, name='training')
        thisExp.addLoop(training)  # add the loop to the experiment
        thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTraining.rgb)
        if thisTraining != None:
            for paramName in thisTraining.keys():
                exec(paramName + '= thisTraining.' + paramName)
        
        for thisTraining in training:
            currentLoop = training
            # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
            if thisTraining != None:
                for paramName in thisTraining.keys():
                    exec(paramName + '= thisTraining.' + paramName)
            
            #------Prepare to start Routine "instruct_training"-------
            t = 0
            instruct_trainingClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            inst_training_box.setText(inst_training)
            inst_training_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            inst_training_resp.status = NOT_STARTED
            # keep track of which components have finished
            instruct_trainingComponents = []
            instruct_trainingComponents.append(inst_training_box)
            instruct_trainingComponents.append(inst_training_resp)
            for thisComponent in instruct_trainingComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "instruct_training"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = instruct_trainingClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inst_training_box* updates
                if t >= 0.5 and inst_training_box.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inst_training_box.tStart = t  # underestimates by a little under one frame
                    inst_training_box.frameNStart = frameN  # exact frame index
                    inst_training_box.setAutoDraw(True)
                
                # *inst_training_resp* updates
                if t >= 1 and inst_training_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inst_training_resp.tStart = t  # underestimates by a little under one frame
                    inst_training_resp.frameNStart = frameN  # exact frame index
                    inst_training_resp.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if inst_training_resp.status == STARTED:
                    theseKeys = event.getKeys()
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instruct_trainingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "instruct_training"-------
            for thisComponent in instruct_trainingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "instruct_training" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            training_trials = data.TrialHandler(nReps=training_block_length_multiplier, method='random', 
                extraInfo=expInfo, originPath=None,
                trialList=data.importConditions('training_block.xlsx'),
                seed=None, name='training_trials')
            thisExp.addLoop(training_trials)  # add the loop to the experiment
            thisTraining_trial = training_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb=thisTraining_trial.rgb)
            if thisTraining_trial != None:
                for paramName in thisTraining_trial.keys():
                    exec(paramName + '= thisTraining_trial.' + paramName)
            
            for thisTraining_trial in training_trials:
                currentLoop = training_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
                if thisTraining_trial != None:
                    for paramName in thisTraining_trial.keys():
                        exec(paramName + '= thisTraining_trial.' + paramName)
                
                #------Prepare to start Routine "trial"-------
                t = 0
                trialClock.reset()  # clock 
                frameN = -1
                # update component parameters for each repeat
                # Set target stimuli categories 
                # Location of the required category is set by the required response. 
                # Location of the two incorrect categories is randomised.
                if required_response == 'left':  # left from block_layout.xlsx
                    target_category_left = target_category_required  # latter from block_layout.xlsx
                    i = [target_category_wrong_1, target_category_wrong_2]
                    random.shuffle(i)
                    target_category_middle = i.pop()
                    target_category_right = i.pop()
                elif required_response == 'down':
                    target_category_middle = target_category_required
                    i = [target_category_wrong_1, target_category_wrong_2]
                    random.shuffle(i)
                    target_category_left = i.pop()
                    target_category_right = i.pop()
                elif required_response == 'right':
                    target_category_right = target_category_required
                    i = [target_category_wrong_1, target_category_wrong_2]
                    random.shuffle(i)
                    target_category_left = i.pop()
                    target_category_middle = i.pop()
                
                # Set specific stimuli based on categories
                # Translate a1 etc into actual exemplars from the stimuli.xlsx file
                #sample
                if sample_category == 'a1':
                    sample = a1_exemplar
                elif sample_category == 'a2':
                    sample = a2_exemplar
                elif sample_category == 'a3':
                    sample = a3_exemplar
                elif sample_category == 'b1':  # I include B and C classes for generalisation to an equivalence task
                    sample = b1_exemplar
                elif sample_category == 'b2':
                    sample = b2_exemplar
                elif sample_category == 'b3':
                    sample = b3_exemplar
                elif sample_category == 'c1':
                    sample = c1_exemplar
                elif sample_category == 'c2':
                    sample = c2_exemplar
                elif sample_category == 'c3':
                    sample = c3_exemplar
                
                #target left
                if target_category_left == 'b1':
                    target_left = b1_exemplar
                elif target_category_left == 'b2':
                    target_left = b2_exemplar
                elif target_category_left == 'b3':
                    target_left = b3_exemplar
                elif target_category_left == 'c1':
                    target_left = c1_exemplar
                elif target_category_left == 'c2':
                    target_left = c2_exemplar
                elif target_category_left == 'c3':
                    target_left = c3_exemplar
                
                #target middle
                if target_category_middle == 'b1':
                    target_middle = b1_exemplar
                elif target_category_middle == 'b2':
                    target_middle = b2_exemplar
                elif target_category_middle == 'b3':
                    target_middle = b3_exemplar
                elif target_category_middle == 'c1':
                    target_middle = c1_exemplar
                elif target_category_middle == 'c2':
                    target_middle = c2_exemplar
                elif target_category_middle == 'c3':
                    target_middle = c3_exemplar
                
                #target right
                if target_category_right == 'b1':
                    target_right = b1_exemplar
                elif target_category_right == 'b2':
                    target_right = b2_exemplar
                elif target_category_right == 'b3':
                    target_right = b3_exemplar
                elif target_category_right == 'c1':
                    target_right = c1_exemplar
                elif target_category_right == 'c2':
                    target_right = c2_exemplar
                elif target_category_right == 'c3':
                    target_right = c3_exemplar
                
                sample_box.setText(sample)
                target_left_box.setText(target_left)
                target_middle_box.setText(target_middle)
                target_right_box.setText(target_right)
                response = event.BuilderKeyResponse()  # create an object of type KeyResponse
                response.status = NOT_STARTED
                # keep track of which components have finished
                trialComponents = []
                trialComponents.append(sample_box)
                trialComponents.append(target_left_box)
                trialComponents.append(target_middle_box)
                trialComponents.append(target_right_box)
                trialComponents.append(response)
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "trial"-------
                continueRoutine = True
                while continueRoutine:
                    # get current time
                    t = trialClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *sample_box* updates
                    if t >= 0.5 and sample_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        sample_box.tStart = t  # underestimates by a little under one frame
                        sample_box.frameNStart = frameN  # exact frame index
                        sample_box.setAutoDraw(True)
                    
                    # *target_left_box* updates
                    if t >= 1 and target_left_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        target_left_box.tStart = t  # underestimates by a little under one frame
                        target_left_box.frameNStart = frameN  # exact frame index
                        target_left_box.setAutoDraw(True)
                    
                    # *target_middle_box* updates
                    if t >= 1 and target_middle_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        target_middle_box.tStart = t  # underestimates by a little under one frame
                        target_middle_box.frameNStart = frameN  # exact frame index
                        target_middle_box.setAutoDraw(True)
                    
                    # *target_right_box* updates
                    if t >= 1 and target_right_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        target_right_box.tStart = t  # underestimates by a little under one frame
                        target_right_box.frameNStart = frameN  # exact frame index
                        target_right_box.setAutoDraw(True)
                    
                    # *response* updates
                    if t >= 1 and response.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        response.tStart = t  # underestimates by a little under one frame
                        response.frameNStart = frameN  # exact frame index
                        response.status = STARTED
                        # keyboard checking is just starting
                        response.clock.reset()  # now t=0
                        event.clearEvents(eventType='keyboard')
                    if response.status == STARTED:
                        theseKeys = event.getKeys(keyList=['left', 'down', 'right'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if response.keys == []:  # then this was the first keypress
                                response.keys = theseKeys[0]  # just the first key pressed
                                response.rt = response.clock.getTime()
                                # was this 'correct'?
                                if (response.keys == str(required_response)) or (response.keys == required_response):
                                    response.corr = 1
                                else:
                                    response.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "trial"-------
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # Adjust feedback and counters based on response
                if response.corr == True:
                    total_correct += 1
                    message = correct_message
                    message_color = 'lime'
                elif response.corr == False:
                    message = wrong_message
                    message_color = 'red'
                
                # save variables to the experiment handler to be written to the data file
                thisExp.addData('sample', sample)
                thisExp.addData('target_left', target_left)
                thisExp.addData('target_middle', target_middle)
                thisExp.addData('target_right', target_right)
                # check responses
                if response.keys in ['', [], None]:  # No response was made
                   response.keys=None
                   # was no response the correct answer?!
                   if str(required_response).lower() == 'none': response.corr = 1  # correct non-response
                   else: response.corr = 0  # failed to respond (incorrectly)
                # store data for training_trials (TrialHandler)
                training_trials.addData('response.keys',response.keys)
                training_trials.addData('response.corr', response.corr)
                if response.keys != None:  # we had a response
                    training_trials.addData('response.rt', response.rt)
                # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                #------Prepare to start Routine "feedback"-------
                t = 0
                feedbackClock.reset()  # clock 
                frameN = -1
                routineTimer.add(1.500000)
                # update component parameters for each repeat
                feedback_box.setColor(message_color, colorSpace='rgb')
                feedback_box.setText(message)
                # keep track of which components have finished
                feedbackComponents = []
                feedbackComponents.append(feedback_box)
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "feedback"-------
                continueRoutine = True
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = feedbackClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *feedback_box* updates
                    if t >= 0.5 and feedback_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        feedback_box.tStart = t  # underestimates by a little under one frame
                        feedback_box.frameNStart = frameN  # exact frame index
                        feedback_box.setAutoDraw(True)
                    if feedback_box.status == STARTED and t >= (0.5 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                        feedback_box.setAutoDraw(False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "feedback"-------
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.nextEntry()
                
            # completed training_block_length_multiplier repeats of 'training_trials'
            
            
            # set up handler to look after randomisation of conditions etc
            post_training_loop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=None,
                trialList=[None],
                seed=None, name='post_training_loop')
            thisExp.addLoop(post_training_loop)  # add the loop to the experiment
            thisPost_training_loop = post_training_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb=thisPost_training_loop.rgb)
            if thisPost_training_loop != None:
                for paramName in thisPost_training_loop.keys():
                    exec(paramName + '= thisPost_training_loop.' + paramName)
            
            for thisPost_training_loop in post_training_loop:
                currentLoop = post_training_loop
                # abbreviate parameter names if possible (e.g. rgb = thisPost_training_loop.rgb)
                if thisPost_training_loop != None:
                    for paramName in thisPost_training_loop.keys():
                        exec(paramName + '= thisPost_training_loop.' + paramName)
                
                #------Prepare to start Routine "post_training"-------
                t = 0
                post_trainingClock.reset()  # clock 
                frameN = -1
                # update component parameters for each repeat
                
                
                
                
                # keep track of which components have finished
                post_trainingComponents = []
                for thisComponent in post_trainingComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "post_training"-------
                continueRoutine = True
                while continueRoutine:
                    # get current time
                    t = post_trainingClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in post_trainingComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "post_training"-------
                for thisComponent in post_trainingComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # End loops if mastery criterion was met
                thisExp.addData('total_correct', total_correct)
                
                if total_correct >= training_criterion:
                    passed_training = True
                    training.finished = True
                    max_testing_var = max_testing
                
                thisExp.addData('passed_training', passed_training)
                
                #reset counter for testing or more training
                total_correct = 0
                # the Routine "post_training" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'post_training_loop'
            
        # completed max_training repeats of 'training'
        
        
        # set up handler to look after randomisation of conditions etc
        testing = data.TrialHandler(nReps=max_testing_var, method='sequential', 
            extraInfo=expInfo, originPath=None,
            trialList=[None],
            seed=None, name='testing')
        thisExp.addLoop(testing)  # add the loop to the experiment
        thisTesting = testing.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTesting.rgb)
        if thisTesting != None:
            for paramName in thisTesting.keys():
                exec(paramName + '= thisTesting.' + paramName)
        
        for thisTesting in testing:
            currentLoop = testing
            # abbreviate parameter names if possible (e.g. rgb = thisTesting.rgb)
            if thisTesting != None:
                for paramName in thisTesting.keys():
                    exec(paramName + '= thisTesting.' + paramName)
            
            #------Prepare to start Routine "instruct_testing"-------
            t = 0
            instruct_testingClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            inst_testing_box.setText(inst_testing)
            inst_testing_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            inst_testing_resp.status = NOT_STARTED
            # keep track of which components have finished
            instruct_testingComponents = []
            instruct_testingComponents.append(inst_testing_box)
            instruct_testingComponents.append(inst_testing_resp)
            for thisComponent in instruct_testingComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "instruct_testing"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = instruct_testingClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inst_testing_box* updates
                if t >= 0.5 and inst_testing_box.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inst_testing_box.tStart = t  # underestimates by a little under one frame
                    inst_testing_box.frameNStart = frameN  # exact frame index
                    inst_testing_box.setAutoDraw(True)
                
                # *inst_testing_resp* updates
                if t >= 1 and inst_testing_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inst_testing_resp.tStart = t  # underestimates by a little under one frame
                    inst_testing_resp.frameNStart = frameN  # exact frame index
                    inst_testing_resp.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if inst_testing_resp.status == STARTED:
                    theseKeys = event.getKeys()
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instruct_testingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "instruct_testing"-------
            for thisComponent in instruct_testingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "instruct_testing" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            testing_trials = data.TrialHandler(nReps=testing_block_length_multiplier, method='sequential', 
                extraInfo=expInfo, originPath=None,
                trialList=data.importConditions('testing_block.xlsx'),
                seed=None, name='testing_trials')
            thisExp.addLoop(testing_trials)  # add the loop to the experiment
            thisTesting_trial = testing_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb=thisTesting_trial.rgb)
            if thisTesting_trial != None:
                for paramName in thisTesting_trial.keys():
                    exec(paramName + '= thisTesting_trial.' + paramName)
            
            for thisTesting_trial in testing_trials:
                currentLoop = testing_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTesting_trial.rgb)
                if thisTesting_trial != None:
                    for paramName in thisTesting_trial.keys():
                        exec(paramName + '= thisTesting_trial.' + paramName)
                
                #------Prepare to start Routine "trial"-------
                t = 0
                trialClock.reset()  # clock 
                frameN = -1
                # update component parameters for each repeat
                # Set target stimuli categories 
                # Location of the required category is set by the required response. 
                # Location of the two incorrect categories is randomised.
                if required_response == 'left':  # left from block_layout.xlsx
                    target_category_left = target_category_required  # latter from block_layout.xlsx
                    i = [target_category_wrong_1, target_category_wrong_2]
                    random.shuffle(i)
                    target_category_middle = i.pop()
                    target_category_right = i.pop()
                elif required_response == 'down':
                    target_category_middle = target_category_required
                    i = [target_category_wrong_1, target_category_wrong_2]
                    random.shuffle(i)
                    target_category_left = i.pop()
                    target_category_right = i.pop()
                elif required_response == 'right':
                    target_category_right = target_category_required
                    i = [target_category_wrong_1, target_category_wrong_2]
                    random.shuffle(i)
                    target_category_left = i.pop()
                    target_category_middle = i.pop()
                
                # Set specific stimuli based on categories
                # Translate a1 etc into actual exemplars from the stimuli.xlsx file
                #sample
                if sample_category == 'a1':
                    sample = a1_exemplar
                elif sample_category == 'a2':
                    sample = a2_exemplar
                elif sample_category == 'a3':
                    sample = a3_exemplar
                elif sample_category == 'b1':  # I include B and C classes for generalisation to an equivalence task
                    sample = b1_exemplar
                elif sample_category == 'b2':
                    sample = b2_exemplar
                elif sample_category == 'b3':
                    sample = b3_exemplar
                elif sample_category == 'c1':
                    sample = c1_exemplar
                elif sample_category == 'c2':
                    sample = c2_exemplar
                elif sample_category == 'c3':
                    sample = c3_exemplar
                
                #target left
                if target_category_left == 'b1':
                    target_left = b1_exemplar
                elif target_category_left == 'b2':
                    target_left = b2_exemplar
                elif target_category_left == 'b3':
                    target_left = b3_exemplar
                elif target_category_left == 'c1':
                    target_left = c1_exemplar
                elif target_category_left == 'c2':
                    target_left = c2_exemplar
                elif target_category_left == 'c3':
                    target_left = c3_exemplar
                
                #target middle
                if target_category_middle == 'b1':
                    target_middle = b1_exemplar
                elif target_category_middle == 'b2':
                    target_middle = b2_exemplar
                elif target_category_middle == 'b3':
                    target_middle = b3_exemplar
                elif target_category_middle == 'c1':
                    target_middle = c1_exemplar
                elif target_category_middle == 'c2':
                    target_middle = c2_exemplar
                elif target_category_middle == 'c3':
                    target_middle = c3_exemplar
                
                #target right
                if target_category_right == 'b1':
                    target_right = b1_exemplar
                elif target_category_right == 'b2':
                    target_right = b2_exemplar
                elif target_category_right == 'b3':
                    target_right = b3_exemplar
                elif target_category_right == 'c1':
                    target_right = c1_exemplar
                elif target_category_right == 'c2':
                    target_right = c2_exemplar
                elif target_category_right == 'c3':
                    target_right = c3_exemplar
                
                sample_box.setText(sample)
                target_left_box.setText(target_left)
                target_middle_box.setText(target_middle)
                target_right_box.setText(target_right)
                response = event.BuilderKeyResponse()  # create an object of type KeyResponse
                response.status = NOT_STARTED
                # keep track of which components have finished
                trialComponents = []
                trialComponents.append(sample_box)
                trialComponents.append(target_left_box)
                trialComponents.append(target_middle_box)
                trialComponents.append(target_right_box)
                trialComponents.append(response)
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "trial"-------
                continueRoutine = True
                while continueRoutine:
                    # get current time
                    t = trialClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *sample_box* updates
                    if t >= 0.5 and sample_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        sample_box.tStart = t  # underestimates by a little under one frame
                        sample_box.frameNStart = frameN  # exact frame index
                        sample_box.setAutoDraw(True)
                    
                    # *target_left_box* updates
                    if t >= 1 and target_left_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        target_left_box.tStart = t  # underestimates by a little under one frame
                        target_left_box.frameNStart = frameN  # exact frame index
                        target_left_box.setAutoDraw(True)
                    
                    # *target_middle_box* updates
                    if t >= 1 and target_middle_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        target_middle_box.tStart = t  # underestimates by a little under one frame
                        target_middle_box.frameNStart = frameN  # exact frame index
                        target_middle_box.setAutoDraw(True)
                    
                    # *target_right_box* updates
                    if t >= 1 and target_right_box.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        target_right_box.tStart = t  # underestimates by a little under one frame
                        target_right_box.frameNStart = frameN  # exact frame index
                        target_right_box.setAutoDraw(True)
                    
                    # *response* updates
                    if t >= 1 and response.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        response.tStart = t  # underestimates by a little under one frame
                        response.frameNStart = frameN  # exact frame index
                        response.status = STARTED
                        # keyboard checking is just starting
                        response.clock.reset()  # now t=0
                        event.clearEvents(eventType='keyboard')
                    if response.status == STARTED:
                        theseKeys = event.getKeys(keyList=['left', 'down', 'right'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if response.keys == []:  # then this was the first keypress
                                response.keys = theseKeys[0]  # just the first key pressed
                                response.rt = response.clock.getTime()
                                # was this 'correct'?
                                if (response.keys == str(required_response)) or (response.keys == required_response):
                                    response.corr = 1
                                else:
                                    response.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "trial"-------
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # Adjust feedback and counters based on response
                if response.corr == True:
                    total_correct += 1
                    message = correct_message
                    message_color = 'lime'
                elif response.corr == False:
                    message = wrong_message
                    message_color = 'red'
                
                # save variables to the experiment handler to be written to the data file
                thisExp.addData('sample', sample)
                thisExp.addData('target_left', target_left)
                thisExp.addData('target_middle', target_middle)
                thisExp.addData('target_right', target_right)
                # check responses
                if response.keys in ['', [], None]:  # No response was made
                   response.keys=None
                   # was no response the correct answer?!
                   if str(required_response).lower() == 'none': response.corr = 1  # correct non-response
                   else: response.corr = 0  # failed to respond (incorrectly)
                # store data for testing_trials (TrialHandler)
                testing_trials.addData('response.keys',response.keys)
                testing_trials.addData('response.corr', response.corr)
                if response.keys != None:  # we had a response
                    testing_trials.addData('response.rt', response.rt)
                # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed testing_block_length_multiplier repeats of 'testing_trials'
            
            
            # set up handler to look after randomisation of conditions etc
            post_testing_loop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=None,
                trialList=[None],
                seed=None, name='post_testing_loop')
            thisExp.addLoop(post_testing_loop)  # add the loop to the experiment
            thisPost_testing_loop = post_testing_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb=thisPost_testing_loop.rgb)
            if thisPost_testing_loop != None:
                for paramName in thisPost_testing_loop.keys():
                    exec(paramName + '= thisPost_testing_loop.' + paramName)
            
            for thisPost_testing_loop in post_testing_loop:
                currentLoop = post_testing_loop
                # abbreviate parameter names if possible (e.g. rgb = thisPost_testing_loop.rgb)
                if thisPost_testing_loop != None:
                    for paramName in thisPost_testing_loop.keys():
                        exec(paramName + '= thisPost_testing_loop.' + paramName)
                
                #------Prepare to start Routine "post_testing"-------
                t = 0
                post_testingClock.reset()  # clock 
                frameN = -1
                # update component parameters for each repeat
                
                
                
                
                # keep track of which components have finished
                post_testingComponents = []
                for thisComponent in post_testingComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                #-------Start Routine "post_testing"-------
                continueRoutine = True
                while continueRoutine:
                    # get current time
                    t = post_testingClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in post_testingComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #-------Ending Routine "post_testing"-------
                for thisComponent in post_testingComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # End loops if mastery criterion was met
                thisExp.addData('total_correct', total_correct)
                
                if total_correct >= testing_criterion:
                    passed_testing = True
                    training_and_testing.finished = True
                
                thisExp.addData('passed_testing', passed_testing)
                
                total_correct = 0  #reset counter for more training
                # the Routine "post_testing" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'post_testing_loop'
            
        # completed max_testing_var repeats of 'testing'
        
    # completed max_training_and_testing repeats of 'training_and_testing'
    
    
    #------Prepare to start Routine "end"-------
    t = 0
    endClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # adjust end message
    if passed_testing == True:
        end_message = 'PASSED \n\nEnd of task'
    elif passed_testing == False:
        end_message = 'FAILED \n\nEnd of task'
    end_box.setText(end_message)
    end_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    end_resp.status = NOT_STARTED
    # keep track of which components have finished
    endComponents = []
    endComponents.append(end_box)
    endComponents.append(end_resp)
    for thisComponent in endComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "end"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = endClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *end_box* updates
        if t >= 0.5 and end_box.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_box.tStart = t  # underestimates by a little under one frame
            end_box.frameNStart = frameN  # exact frame index
            end_box.setAutoDraw(True)
        
        # *end_resp* updates
        if t >= 0.5 and end_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_resp.tStart = t  # underestimates by a little under one frame
            end_resp.frameNStart = frameN  # exact frame index
            end_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if end_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "end"-------
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'task'






win.close()
core.quit()
