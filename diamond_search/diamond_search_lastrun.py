#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Sun Mar 26 20:33:01 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'diamond_search'  # from the Builder filename that created this script
expInfo = {
    'participant': f"sub_{randint(0, 9999):04.0f}",
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s' % (expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/strongway/LRZ Sync+Share/_git/discue_search/diamond_search/diamond_search_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1728, 1117], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "Instruction_display" ---
image_instr1 = visual.ImageStim(
    win=win,
    name='image_instr1', 
    image='display.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(10, 9.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_intro = visual.TextStim(win=win, name='text_intro',
    text='You will see a visual search display comprising six shapes on each trial. Sometimes, one shape may be a different color that you should ignore. \n\nYour task is to find if the diamond shape is on the right or left side.  \n',
    font='Arial',
    units='deg', pos=(0, 6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_key = keyboard.Keyboard()
text_cont2 = visual.TextStim(win=win, name='text_cont2',
    text='Press SPACE to continue ...',
    font='Arial',
    units='deg', pos=(0, -6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "fixation" ---
fixcross = visual.ShapeStim(
    win=win, name='fixcross', vertices='cross',units='deg', 
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "search" ---
# Run 'Begin Experiment' code from search_code
# genearte trial sequences, 
import pandas as pd

n_trials = 120
block_trials = 30
num_block = n_trials//block_trials

# there are 6 possible locations for the target and distractors, [0, 1,3,4] for target, [2,5] for distractors
# create an array of 120 rows with possible target locations
target_pos = np.array([randchoice([0,1,3,4], 1, replace=False) for i in range(n_trials)])
# create an array of 120 rows with possible distractor locations
distractor_pos = np.array([randchoice([2,5], 1, replace=False) for i in range(n_trials)])
# create any array of 120 rows, 5 columns with possible shapes for distractors, 3, 5, 6, 0 (triangle, pentagon, hexagon, circle)
distractor_shapes = np.array([randchoice([3,5,6,0], 5, replace=True) for i in range(n_trials)])
# create an array of 120 row with possible distractor presence (0,1)
singleton = np.array([randchoice([0,1], 1, replace=True) for i in range(n_trials)])
# create an array of 120 rows with possible target colors (0,1)
target_color = np.array([randchoice([0,1], 1, replace=True) for i in range(n_trials)])
# create correct answer 2D array of 120 rows, one column based on target_pos: > 2 is 0, < 2 is 1 (left, right) with one column
correct_answer = np.array([0 if i > 2 else 1 for i in target_pos])
# convert correct_answer to 2D array
correct_answer = correct_answer.reshape(n_trials, 1)

# concatenate all arrays into one array
sequences = np.concatenate((target_pos, distractor_pos, distractor_shapes, singleton, target_color, correct_answer), axis=1)
# convert sequences to pandas dataframe
sequences = pd.DataFrame(sequences, columns=['target_pos', 'distractor_pos', 'distractor_shape1', 'distractor_shape2', 
                                             'distractor_shape3', 'distractor_shape4', 'distractor_shape5', 
                                             'singleton', 'target_color', 'correct_answer'])
# change all columns to int
sequences = sequences.astype(int)
#save trials to csv file in subfolder sequences
seq_file = _thisDir + os.sep + u'data/%s_seq.csv' % (expInfo['participant'])
sequences.to_csv(seq_file, index=False)

circle_rad = 6 # radius of circle (degrees)  were centered from the fixation
lw = 1 # item border line width (pixels)
dw = 3 # diamond width (degrees)

col_Teal = [-0.7255,0.8902,0.8353]
col_orange = [1.000, 0.2491, -1.0000] 
col_black = [-1, -1, -1] 

# create a 6 circular coordinates from 0 to 300 degrees with radius of circle_rad
CoordsX = [circle_rad*cos(t*pi/180) for t in range(-30, 271, 60)]
CoordsY = [circle_rad*sin(t*pi/180) for t in range(-30, 271, 60)]

search_response = keyboard.Keyboard()

# --- Initialize components for Routine "block_break" ---
# Run 'Begin Experiment' code from break_code
corr_trials = 0
block_break = False
key_dur = 1.0 + random()/2.0
block_info = visual.TextStim(win=win, name='block_info',
    text='Take a rest',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_block = keyboard.Keyboard()

# --- Initialize components for Routine "finish" ---
end = visual.TextStim(win=win, name='end',
    text='The experiment is finished.\n\nThank you for your participation!\n',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instruction_display" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_key.keys = []
space_key.rt = []
_space_key_allKeys = []
# keep track of which components have finished
Instruction_displayComponents = [image_instr1, text_intro, space_key, text_cont2]
for thisComponent in Instruction_displayComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruction_display" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_instr1* updates
    if image_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_instr1.frameNStart = frameN  # exact frame index
        image_instr1.tStart = t  # local t and not account for scr refresh
        image_instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_instr1, 'tStartRefresh')  # time at next scr refresh
        image_instr1.setAutoDraw(True)
    
    # *text_intro* updates
    if text_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_intro.frameNStart = frameN  # exact frame index
        text_intro.tStart = t  # local t and not account for scr refresh
        text_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_intro, 'tStartRefresh')  # time at next scr refresh
        text_intro.setAutoDraw(True)
    
    # *space_key* updates
    waitOnFlip = False
    if space_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_key.frameNStart = frameN  # exact frame index
        space_key.tStart = t  # local t and not account for scr refresh
        space_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_key, 'tStartRefresh')  # time at next scr refresh
        space_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_key.status == STARTED and not waitOnFlip:
        theseKeys = space_key.getKeys(keyList=['space'], waitRelease=False)
        _space_key_allKeys.extend(theseKeys)
        if len(_space_key_allKeys):
            space_key.keys = _space_key_allKeys[-1].name  # just the last key pressed
            space_key.rt = _space_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_cont2* updates
    if text_cont2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_cont2.frameNStart = frameN  # exact frame index
        text_cont2.tStart = t  # local t and not account for scr refresh
        text_cont2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_cont2, 'tStartRefresh')  # time at next scr refresh
        text_cont2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_displayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction_display" ---
for thisComponent in Instruction_displayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction_display" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("data/"+expInfo['participant']+"_seq.csv"),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixcross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 0.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.800000)
    
    # --- Prepare to start Routine "search" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from search_code
    
    # draw six shapes in the six circular coordinates
    if target_color == 0:
        tar_col = col_Teal
        dis_col = col_orange
    else:
        tar_col = col_orange
        dis_col = col_Teal
    
    if correct_answer == 0:
        corr_ans = 'left'
    else:
        corr_ans = 'right'
        
    items = [None]*6
    
    dis_count = 0
    for i in range(6):
        # five distractor shapes
        shape = locals()[f'distractor_shape{dis_count+1}']
    
        if i == target_pos: #Target - Diamond
            items[i]= visual.Polygon(win = win, edges = 4, size = dw,lineWidth = lw)
            items[i].fillColor = tar_col
        else: # distractor
            if shape == 0:
                items[i]= visual.Circle(win=win,radius= dw/2,edges = 128, lineWidth=lw)
            else:
                items[i]= visual.Polygon(win = win, edges = shape, size = dw,lineWidth = lw)
            if shape == 3: #triangle, increase the area a bit
                items[i].size = dw * 1.02
            if singleton == 1 and i == distractor_pos: # distractor singleton
                items[i].fillColor = dis_col
            else:
                items[i].fillColor = tar_col
            # increase distractor count
            dis_count = dis_count + 1
        items[i].name='position_' + str(i+1)
        items[i].setPos((CoordsX[i], CoordsY[i]))
        items[i].setAutoDraw(True)
    
        
    
    search_response.keys = []
    search_response.rt = []
    _search_response_allKeys = []
    # keep track of which components have finished
    searchComponents = [search_response]
    for thisComponent in searchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "search" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *search_response* updates
        waitOnFlip = False
        if search_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_response.frameNStart = frameN  # exact frame index
            search_response.tStart = t  # local t and not account for scr refresh
            search_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'search_response.started')
            search_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(search_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(search_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if search_response.status == STARTED and not waitOnFlip:
            theseKeys = search_response.getKeys(keyList=['left','right'], waitRelease=False)
            _search_response_allKeys.extend(theseKeys)
            if len(_search_response_allKeys):
                search_response.keys = _search_response_allKeys[-1].name  # just the last key pressed
                search_response.rt = _search_response_allKeys[-1].rt
                # was this correct?
                if (search_response.keys == str(corr_ans)) or (search_response.keys == corr_ans):
                    search_response.corr = 1
                else:
                    search_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in searchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "search" ---
    for thisComponent in searchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from search_code
    for i in range(6):
        items[i].setAutoDraw(False)    
    win.flip()
    
    if search_response.corr == 1:
        corr_trials = corr_trials +1
        
    # check responses
    if search_response.keys in ['', [], None]:  # No response was made
        search_response.keys = None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           search_response.corr = 1;  # correct non-response
        else:
           search_response.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('search_response.keys',search_response.keys)
    trials.addData('search_response.corr', search_response.corr)
    if search_response.keys != None:  # we had a response
        trials.addData('search_response.rt', search_response.rt)
    # the Routine "search" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from break_code
    if ((trials.thisN+1) % block_trials == 0): 
        block_break = True
        key_dur = 1800.0 # maximum 30 minutes
        this_block=int((trials.thisN+1)/block_trials)
        corr_rate = round(corr_trials/block_trials*100)
        btext = 'Block No. ' + str(this_block) + ' was finished.\n\n'
        btext = btext + 'There are ' + str(num_block-this_block) + ' left. \n\n' 
        btext = btext + 'In the previous block, your correct rate was: \n\n' + str(corr_rate) + '%\n\n' 
        btext = btext + 'Please keep your correct rate as high as possible. \n'
        btext = btext + 'If you are ready, press the SPACEBAR to continue ...'
        block_info.text = btext
        corr_trials=0
    else:
        block_info.text = ''
    
    
    key_block.keys = []
    key_block.rt = []
    _key_block_allKeys = []
    # keep track of which components have finished
    block_breakComponents = [block_info, key_block]
    for thisComponent in block_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_break" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_info* updates
        if block_info.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            block_info.frameNStart = frameN  # exact frame index
            block_info.tStart = t  # local t and not account for scr refresh
            block_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_info, 'tStartRefresh')  # time at next scr refresh
            block_info.setAutoDraw(True)
        if block_info.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block_info.tStartRefresh + key_dur-frameTolerance:
                # keep track of stop time/frame for later
                block_info.tStop = t  # not accounting for scr refresh
                block_info.frameNStop = frameN  # exact frame index
                block_info.setAutoDraw(False)
        
        # *key_block* updates
        waitOnFlip = False
        if key_block.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_block.frameNStart = frameN  # exact frame index
            key_block.tStart = t  # local t and not account for scr refresh
            key_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_block, 'tStartRefresh')  # time at next scr refresh
            key_block.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_block.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_block.tStartRefresh + key_dur-frameTolerance:
                # keep track of stop time/frame for later
                key_block.tStop = t  # not accounting for scr refresh
                key_block.frameNStop = frameN  # exact frame index
                key_block.status = FINISHED
        if key_block.status == STARTED and not waitOnFlip:
            theseKeys = key_block.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
            _key_block_allKeys.extend(theseKeys)
            if len(_key_block_allKeys):
                key_block.keys = _key_block_allKeys[-1].name  # just the last key pressed
                key_block.rt = _key_block_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_break" ---
    for thisComponent in block_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from break_code
    block_break = False
    key_dur = 1.0 + random()/2.0
    
    
    # check responses
    if key_block.keys in ['', [], None]:  # No response was made
        key_block.keys = None
    trials.addData('key_block.keys',key_block.keys)
    if key_block.keys != None:  # we had a response
        trials.addData('key_block.rt', key_block.rt)
    # the Routine "block_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_key.keys = []
end_key.rt = []
_end_key_allKeys = []
# keep track of which components have finished
finishComponents = [end, end_key]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        end.setAutoDraw(True)
    
    # *end_key* updates
    waitOnFlip = False
    if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key.status == STARTED and not waitOnFlip:
        theseKeys = end_key.getKeys(keyList=['space'], waitRelease=False)
        _end_key_allKeys.extend(theseKeys)
        if len(_end_key_allKeys):
            end_key.keys = _end_key_allKeys[-1].name  # just the last key pressed
            end_key.rt = _end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_key.keys in ['', [], None]:  # No response was made
    end_key.keys = None
thisExp.addData('end_key.keys',end_key.keys)
if end_key.keys != None:  # we had a response
    thisExp.addData('end_key.rt', end_key.rt)
thisExp.nextEntry()
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
