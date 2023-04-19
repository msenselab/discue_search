#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on April 19, 2023, at 09:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
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
psychopyVersion = '2023.1.0'
expName = 'stress'  # from the Builder filename that created this script
expInfo = {
    'participant': f"sub_{randint(0, 9999):04.0f}",
    'session': '001',
    'distractor_prevalence': '0.5',
    'validity': '1.0',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\yunwa\\OneDrive\\Documents\\GSN-LMU MSC NEURO 2021\\Research Projects\\NEVIA Lab (LMU Klinikum)\\MAPC Project\\stress_MAPC_task_1\\stress_search_practice_Deutsch_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
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

# --- Initialize components for Routine "Instruction1" ---
image_inst_ = visual.ImageStim(
    win=win,
    name='image_inst_', 
    image='cue_display.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0), size=[10, 7.13],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_1 = visual.TextStim(win=win, name='text_1',
    text='Bei diesem Suchexperiment sehen Sie eine Hinweis- und eine Suchanzeige. Die Hinweisanzeige besteht aus einem Fixationskreuz und einer Linie, die in eine Richtung zeigt. Fokussieren Sie sich auf das Fixationskreuz und ignorieren Sie die Linie. Unten sehen Sie ein Beispiel für eine Hinweisanzeige.\n\n',
    font='Arial',
    units='deg', pos=(0, 6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space0 = keyboard.Keyboard()
text_cont = visual.TextStim(win=win, name='text_cont',
    text='Drücken Sie die LEERTASTE, um fortzufahren ...',
    font='Arial',
    units='deg', pos=(0, -6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Instruction2" ---
image_instr1 = visual.ImageStim(
    win=win,
    name='image_instr1', 
    image='display_Deutsch.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -1), size=(10, 7.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_intro = visual.TextStim(win=win, name='text_intro',
    text='Unmittelbar nach der Anzeige des Hinweises sehen Sie eine visuelle Suchanzeige mit sechs Elementen. Bei einigen Versuchen kann eines davon eine abweichende Farbe haben. Dies ist ein Ablenkungsfaktor, den Sie ignorieren sollten. \n\nIhre Aufgabe ist es, das Diamant-Objekt zu finden und die Ausrichtung der Linie darin zu erkennen.\n',
    font='Arial',
    units='deg', pos=(0, 6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_key = keyboard.Keyboard()
text_cont2 = visual.TextStim(win=win, name='text_cont2',
    text='Drücken Sie die LEERTASTE, um fortzufahren ...',
    font='Arial',
    units='deg', pos=(0, -6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "instruction3" ---
key_resp = keyboard.Keyboard()
diamond1 = visual.Rect(
    win=win, name='diamond1',
    width=(3, 3)[0], height=(3, 3)[1],
    ori=45.0, pos=(-4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7255,0.8902,0.8353], fillColor=[-0.7255,0.8902,0.8353],
    opacity=None, depth=-1.0, interpolate=True)
diamond2 = visual.Rect(
    win=win, name='diamond2',
    width=(3, 3)[0], height=(3, 3)[1],
    ori=45.0, pos=(4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.000, 0.2491, -1.0000], fillColor=[1.000, 0.2491, -1.0000],
    opacity=None, depth=-2.0, interpolate=True)
Task = visual.TextStim(win=win, name='Task',
    text='Ihre Aufgabe ist es, die Ausrichtung der Linie innerhalb das Diamant-Objektes zu erkennen und darauf zu reagieren, indem Sie die "linke Pfeiltaste" für horizontal und die "obere Pfeiltaste" für vertikal drücken. Ignorieren Sie bitte alle farblichen Ablenkungen, die auf dem Bildschirm erscheinen können. \n\nDrücken Sie die LEERTASTE zum Starten.\n',
    font='Arial',
    pos=(0, 6), height=1.0, wrapWidth=40.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
line1 = visual.Rect(
    win=win, name='line1',units='deg', 
    width=(1.5, 0.1)[0], height=(1.5, 0.1)[1],
    ori=0.0, pos=(-4.0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-4.0, interpolate=True)
line2 = visual.Rect(
    win=win, name='line2',units='deg', 
    width=(1.5, 0.1)[0], height=(1.5, 0.1)[1],
    ori=90.0, pos=(4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-5.0, interpolate=True)
key_f = visual.TextStim(win=win, name='key_f',
    text='linke Pfeiltaste',
    font='Arial',
    pos=(-4, -4), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
key_j = visual.TextStim(win=win, name='key_j',
    text='obere Pfeiltaste',
    font='Arial',
    pos=(4, -4), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "cue" ---
# Run 'Begin Experiment' code from cue_init
# genearte trial sequences, 
# first 6 cols: item positions (Target, Distractor, otherDist1-4)
# 6-11: shapes (3-6 polygon, 0 - circle)
# 12: singleton or not
# 13: target color 
# 14: target orientation
# 15: cue validity
import pandas as pd

n_trials = 25
block_trials=  25
num_block=n_trials//block_trials
# Create item locations, each row contains random shuffled numbers from 0 to 5 (first Target, second distractor)
itempos = np.array([randchoice(6, 6, replace=False) for i in range(n_trials)])
# create distractor shapes with 5 columns, each row contains random samples from [3,5,6,0,3,5,6,0] 
# 3,5,6,0(triangle, pentagon, hexagon, circle)
item_shapes = np.array([randchoice([3,5,6,0,3,5,6,0], 5, replace=False) for i in range(n_trials)])
# add a column of 4s to the first of the matrix
item_shapes = np.insert(item_shapes, 0, 4, axis=1)

# create target color, and target orietnation [0,1]
# initialize a matrix with half 0s and half 1s
item_specs = np.zeros((n_trials, 2))
# specify the second half of the matrix to be 1s
item_specs[n_trials//2:, :] = 1
# random shuffle rows, independent of each column
for i in range(2):
    np.random.shuffle(item_specs[:, i])

# singleton prevalence

nsingleton = np.int32(float(expInfo['distractor_prevalence'])*n_trials)

singleton_trials = np.concatenate((np.ones((nsingleton, 1)), 
    np.zeros((n_trials-nsingleton, 1))), axis=0)
np.random.shuffle(singleton_trials)
# add cue validitt as one column
cue_valid_trials = np.int16(float(expInfo['validity'])*n_trials)
item_valid = np.concatenate((np.ones((cue_valid_trials, 1)), np.zeros((n_trials-cue_valid_trials, 1))), axis=0)
# random shuffle rows
np.random.shuffle(item_valid)

# combine itempos, item_shapes, and item_specs into trials
sequences = np.concatenate((itempos, item_shapes, singleton_trials, item_specs, item_valid), axis=1)
# # convert trials to pandas dataframe
sequences = pd.DataFrame(sequences, columns=['pos1', 'pos2', 'pos3', 'pos4', 'pos5', 'pos6', 
                                       'shape1', 'shape2', 'shape3', 'shape4', 'shape5', 'shape6',
                                       'singleton', 'target_color', 'target_orientation', 'cue_validity'])
# change all columns to int
sequences = sequences.astype(int)
#save trials to csv file in subfolder sequences
seq_file = _thisDir + os.sep + u'data/seq_%s.csv' % (expInfo['participant'])
sequences.to_csv(seq_file, index=False)

circle_rad = 6 # radius of circle (degrees)  were centered from the fixation
lw = 1 # item border line width (pixels)
dw = 3 # diamond width (degrees)
#ill = 1.5 # internal line length (degrees)     1.5°
#ilw = 0.3 # internal line width  (degrees)     0.3°
#ilcol = 'black'
#color
col_Teal = [-0.7255,0.8902,0.8353]
col_orange = [1.000, 0.2491, -1.0000] 
col_black = [-1, -1, -1] 

# create a 6 circular coordinates from 0 to 300 degrees with radius of circle_rad
CoordsX = [circle_rad*cos(t*pi/180) for t in range(0, 301, 60)]
CoordsY = [circle_rad*sin(t*pi/180) for t in range(0, 301, 60)]

fix_disk = visual.ShapeStim(
    win=win, name='fix_disk',
    size=(0.5, 0.5), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[0.7000, 0.7000, 0.7000],
    opacity=None, depth=-1.0, interpolate=True)
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
fix_disk2 = visual.ShapeStim(
    win=win, name='fix_disk2',
    size=(0.1, 0.1), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7,0.7,0.7], fillColor=[0.7,0.7,0.7],
    opacity=None, depth=-3.0, interpolate=True)
line = visual.Line(
    win=win, name='line',
    start=(-(2, 0.5)[0]/2.0, 0), end=(+(2, 0.5)[0]/2.0, 0),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "search" ---
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
    text='Der Testdurchlauf ist fertig.',
    font='Open Sans',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instruction1" ---
continueRoutine = True
# update component parameters for each repeat
space0.keys = []
space0.rt = []
_space0_allKeys = []
# keep track of which components have finished
Instruction1Components = [image_inst_, text_1, space0, text_cont]
for thisComponent in Instruction1Components:
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

# --- Run Routine "Instruction1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_inst_* updates
    
    # if image_inst_ is starting this frame...
    if image_inst_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_inst_.frameNStart = frameN  # exact frame index
        image_inst_.tStart = t  # local t and not account for scr refresh
        image_inst_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_inst_, 'tStartRefresh')  # time at next scr refresh
        # update status
        image_inst_.status = STARTED
        image_inst_.setAutoDraw(True)
    
    # if image_inst_ is active this frame...
    if image_inst_.status == STARTED:
        # update params
        pass
    
    # *text_1* updates
    
    # if text_1 is starting this frame...
    if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_1.frameNStart = frameN  # exact frame index
        text_1.tStart = t  # local t and not account for scr refresh
        text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_1.status = STARTED
        text_1.setAutoDraw(True)
    
    # if text_1 is active this frame...
    if text_1.status == STARTED:
        # update params
        pass
    
    # *space0* updates
    waitOnFlip = False
    
    # if space0 is starting this frame...
    if space0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space0.frameNStart = frameN  # exact frame index
        space0.tStart = t  # local t and not account for scr refresh
        space0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space0, 'tStartRefresh')  # time at next scr refresh
        # update status
        space0.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space0.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space0.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space0.status == STARTED and not waitOnFlip:
        theseKeys = space0.getKeys(keyList=['space'], waitRelease=False)
        _space0_allKeys.extend(theseKeys)
        if len(_space0_allKeys):
            space0.keys = _space0_allKeys[-1].name  # just the last key pressed
            space0.rt = _space0_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_cont* updates
    
    # if text_cont is starting this frame...
    if text_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_cont.frameNStart = frameN  # exact frame index
        text_cont.tStart = t  # local t and not account for scr refresh
        text_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_cont, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_cont.status = STARTED
        text_cont.setAutoDraw(True)
    
    # if text_cont is active this frame...
    if text_cont.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction1" ---
for thisComponent in Instruction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruction2" ---
continueRoutine = True
# update component parameters for each repeat
space_key.keys = []
space_key.rt = []
_space_key_allKeys = []
# keep track of which components have finished
Instruction2Components = [image_instr1, text_intro, space_key, text_cont2]
for thisComponent in Instruction2Components:
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

# --- Run Routine "Instruction2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_instr1* updates
    
    # if image_instr1 is starting this frame...
    if image_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_instr1.frameNStart = frameN  # exact frame index
        image_instr1.tStart = t  # local t and not account for scr refresh
        image_instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_instr1, 'tStartRefresh')  # time at next scr refresh
        # update status
        image_instr1.status = STARTED
        image_instr1.setAutoDraw(True)
    
    # if image_instr1 is active this frame...
    if image_instr1.status == STARTED:
        # update params
        pass
    
    # *text_intro* updates
    
    # if text_intro is starting this frame...
    if text_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_intro.frameNStart = frameN  # exact frame index
        text_intro.tStart = t  # local t and not account for scr refresh
        text_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_intro, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_intro.status = STARTED
        text_intro.setAutoDraw(True)
    
    # if text_intro is active this frame...
    if text_intro.status == STARTED:
        # update params
        pass
    
    # *space_key* updates
    waitOnFlip = False
    
    # if space_key is starting this frame...
    if space_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_key.frameNStart = frameN  # exact frame index
        space_key.tStart = t  # local t and not account for scr refresh
        space_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_key, 'tStartRefresh')  # time at next scr refresh
        # update status
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
    
    # if text_cont2 is starting this frame...
    if text_cont2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_cont2.frameNStart = frameN  # exact frame index
        text_cont2.tStart = t  # local t and not account for scr refresh
        text_cont2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_cont2, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_cont2.status = STARTED
        text_cont2.setAutoDraw(True)
    
    # if text_cont2 is active this frame...
    if text_cont2.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction2" ---
for thisComponent in Instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instruction3Components = [key_resp, diamond1, diamond2, Task, line1, line2, key_f, key_j]
for thisComponent in instruction3Components:
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

# --- Run Routine "instruction3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *diamond1* updates
    
    # if diamond1 is starting this frame...
    if diamond1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diamond1.frameNStart = frameN  # exact frame index
        diamond1.tStart = t  # local t and not account for scr refresh
        diamond1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diamond1, 'tStartRefresh')  # time at next scr refresh
        # update status
        diamond1.status = STARTED
        diamond1.setAutoDraw(True)
    
    # if diamond1 is active this frame...
    if diamond1.status == STARTED:
        # update params
        pass
    
    # *diamond2* updates
    
    # if diamond2 is starting this frame...
    if diamond2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diamond2.frameNStart = frameN  # exact frame index
        diamond2.tStart = t  # local t and not account for scr refresh
        diamond2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diamond2, 'tStartRefresh')  # time at next scr refresh
        # update status
        diamond2.status = STARTED
        diamond2.setAutoDraw(True)
    
    # if diamond2 is active this frame...
    if diamond2.status == STARTED:
        # update params
        pass
    
    # *Task* updates
    
    # if Task is starting this frame...
    if Task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task.frameNStart = frameN  # exact frame index
        Task.tStart = t  # local t and not account for scr refresh
        Task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task, 'tStartRefresh')  # time at next scr refresh
        # update status
        Task.status = STARTED
        Task.setAutoDraw(True)
    
    # if Task is active this frame...
    if Task.status == STARTED:
        # update params
        pass
    
    # *line1* updates
    
    # if line1 is starting this frame...
    if line1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line1.frameNStart = frameN  # exact frame index
        line1.tStart = t  # local t and not account for scr refresh
        line1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line1, 'tStartRefresh')  # time at next scr refresh
        # update status
        line1.status = STARTED
        line1.setAutoDraw(True)
    
    # if line1 is active this frame...
    if line1.status == STARTED:
        # update params
        pass
    
    # *line2* updates
    
    # if line2 is starting this frame...
    if line2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        line2.frameNStart = frameN  # exact frame index
        line2.tStart = t  # local t and not account for scr refresh
        line2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(line2, 'tStartRefresh')  # time at next scr refresh
        # update status
        line2.status = STARTED
        line2.setAutoDraw(True)
    
    # if line2 is active this frame...
    if line2.status == STARTED:
        # update params
        pass
    
    # *key_f* updates
    
    # if key_f is starting this frame...
    if key_f.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_f.frameNStart = frameN  # exact frame index
        key_f.tStart = t  # local t and not account for scr refresh
        key_f.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_f, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_f.status = STARTED
        key_f.setAutoDraw(True)
    
    # if key_f is active this frame...
    if key_f.status == STARTED:
        # update params
        pass
    
    # *key_j* updates
    
    # if key_j is starting this frame...
    if key_j.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_j.frameNStart = frameN  # exact frame index
        key_j.tStart = t  # local t and not account for scr refresh
        key_j.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_j, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_j.status = STARTED
        key_j.setAutoDraw(True)
    
    # if key_j is active this frame...
    if key_j.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction3" ---
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("data/seq_"+expInfo['participant']+".csv"),
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
    
    # --- Prepare to start Routine "cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from cue_init
    # construct pointer
    ip = randchoice([pos1, pos3, pos4, pos5, pos6]) # except salient distractor
    # change line start, end
    line.start = [0,0]
    line.end = [CoordsX[ip]/3.0, CoordsY[ip]/3.0]
    if cue_validity == 1: 
        # point to distractor location
        line.end = [CoordsX[pos2]/3.0, CoordsY[pos2]/3.0]
    
    
    fixation_cross.setContrast(1.0)
    # keep track of which components have finished
    cueComponents = [fix_disk, fixation_cross, fix_disk2, line]
    for thisComponent in cueComponents:
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
    
    # --- Run Routine "cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_disk* updates
        
        # if fix_disk is starting this frame...
        if fix_disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_disk.frameNStart = frameN  # exact frame index
            fix_disk.tStart = t  # local t and not account for scr refresh
            fix_disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_disk, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix_disk.status = STARTED
            fix_disk.setAutoDraw(True)
        
        # if fix_disk is active this frame...
        if fix_disk.status == STARTED:
            # update params
            pass
        
        # if fix_disk is stopping this frame...
        if fix_disk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_disk.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fix_disk.tStop = t  # not accounting for scr refresh
                fix_disk.frameNStop = frameN  # exact frame index
                # update status
                fix_disk.status = FINISHED
                fix_disk.setAutoDraw(False)
        
        # *fixation_cross* updates
        
        # if fixation_cross is starting this frame...
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # update status
            fixation_cross.status = STARTED
            fixation_cross.setAutoDraw(True)
        
        # if fixation_cross is active this frame...
        if fixation_cross.status == STARTED:
            # update params
            pass
        
        # if fixation_cross is stopping this frame...
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                # update status
                fixation_cross.status = FINISHED
                fixation_cross.setAutoDraw(False)
        
        # *fix_disk2* updates
        
        # if fix_disk2 is starting this frame...
        if fix_disk2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_disk2.frameNStart = frameN  # exact frame index
            fix_disk2.tStart = t  # local t and not account for scr refresh
            fix_disk2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_disk2, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix_disk2.status = STARTED
            fix_disk2.setAutoDraw(True)
        
        # if fix_disk2 is active this frame...
        if fix_disk2.status == STARTED:
            # update params
            pass
        
        # if fix_disk2 is stopping this frame...
        if fix_disk2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_disk2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fix_disk2.tStop = t  # not accounting for scr refresh
                fix_disk2.frameNStop = frameN  # exact frame index
                # update status
                fix_disk2.status = FINISHED
                fix_disk2.setAutoDraw(False)
        
        # *line* updates
        
        # if line is starting this frame...
        if line.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            line.frameNStart = frameN  # exact frame index
            line.tStart = t  # local t and not account for scr refresh
            line.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
            # update status
            line.status = STARTED
            line.setAutoDraw(True)
        
        # if line is active this frame...
        if line.status == STARTED:
            # update params
            pass
        
        # if line is stopping this frame...
        if line.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > line.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                line.tStop = t  # not accounting for scr refresh
                line.frameNStop = frameN  # exact frame index
                # update status
                line.status = FINISHED
                line.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "cue" ---
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "search" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from search_code
    
    # draw six shapes in the six circular coordinates
    if target_color == 0:
        tar_col = col_Teal
        dis_col = col_orange
    else:
        tar_col = col_orange
        dis_col = col_Teal
    
    if target_orientation == 0:
        corr_ans = 'left'
    else:
        corr_ans = 'up'
    
    items = [None]*6
    
    for i in range(6):
        # pos1, pos2, pos3, pos4, pos5, pos6 are the six positions of the six shapes, let pos = pos$i
        position = locals()[f'pos{i+1}']
        shape = locals()[f'shape{i+1}']
        
        if shape == 0:
            items[i]= visual.Circle(win=win,radius= dw/2,edges = 128, lineWidth=lw)
        else:
            items[i]= visual.Polygon(win = win, edges = 4, size = dw,lineWidth = lw)
            items[i].edges = shape
        if shape == 3: #triangle, increase the area a bit
            items[i].size = dw * 1.02
        if singleton == 1 and i == 1: # distractor singleton
            items[i].fillColor = dis_col
        else:
            items[i].fillColor = tar_col
            
        items[i].name=f'pos{i+1}'
        items[i].setPos((CoordsX[position], CoordsY[position]))
        items[i].setAutoDraw(True)
    
    # Draw lines inside the shapes
    lines = [None]*6
    for i in range(6):
        lines[i]=visual.Rect(win=win,size = [dw/3.0,0.1], lineWidth=lw, fillColor = 'black', lineColor = 'black')
        lines[i].setPos((CoordsX[i], CoordsY[i]))
        if i==pos1:
            if target_orientation == 0:
                lines[i].ori = 0
            else:
                lines[i].ori = 90
    #    elif i==pos2 and cue_validity == 1: # distractor 
    #        if target_orientation == 0:
    #            lines[i].ori = 90
    #        else: 
    #            lines[i].ori = 0
        else:
            # random 0 or 90
            lines[i].ori = randchoice([0, 90])
        lines[i].setAutoDraw(True)
        
    
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *search_response* updates
        waitOnFlip = False
        
        # if search_response is starting this frame...
        if search_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            search_response.frameNStart = frameN  # exact frame index
            search_response.tStart = t  # local t and not account for scr refresh
            search_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(search_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            search_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(search_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(search_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if search_response.status == STARTED and not waitOnFlip:
            theseKeys = search_response.getKeys(keyList=['left','up'], waitRelease=False)
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
        lines[i].setAutoDraw(False)
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
    # update component parameters for each repeat
    # Run 'Begin Routine' code from break_code
    if ((trials.thisN+1) % block_trials == 0): 
        block_break = True
        key_dur = 1800.0 # maximum 30 minutes
        this_block=int((trials.thisN+1)/block_trials)
        corr_rate = round(corr_trials/block_trials*100)
        btext = 'Block Nr. ' + str(this_block) + ' ist fertig.\n\n'
        btext = btext + 'Es gibt noch ' + str(num_block-this_block) + '\n\n'
        btext = btext + 'Im vorigen Block war Ihre korrekte Rate: \n\n' + str(corr_rate) + '%\n\n' 
        btext = btext + 'Bitte halten Sie Ihre korrekte Rate so hoch wie möglich. \n\n'
        btext = btext + 'Bitte denken Sie daran, sich während der Anzeige des Hinweises auf das Fixationskreuz zu fokussieren. \n\n'
        btext = btext + 'Wenn Sie bereit sind, drücken Sie die LEERTASTE, um fortzufahren...'
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_info* updates
        
        # if block_info is starting this frame...
        if block_info.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            block_info.frameNStart = frameN  # exact frame index
            block_info.tStart = t  # local t and not account for scr refresh
            block_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_info, 'tStartRefresh')  # time at next scr refresh
            # update status
            block_info.status = STARTED
            block_info.setAutoDraw(True)
        
        # if block_info is active this frame...
        if block_info.status == STARTED:
            # update params
            pass
        
        # if block_info is stopping this frame...
        if block_info.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block_info.tStartRefresh + key_dur-frameTolerance:
                # keep track of stop time/frame for later
                block_info.tStop = t  # not accounting for scr refresh
                block_info.frameNStop = frameN  # exact frame index
                # update status
                block_info.status = FINISHED
                block_info.setAutoDraw(False)
        
        # *key_block* updates
        waitOnFlip = False
        
        # if key_block is starting this frame...
        if key_block.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_block.frameNStart = frameN  # exact frame index
            key_block.tStart = t  # local t and not account for scr refresh
            key_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_block, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_block.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_block.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_block.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_block is stopping this frame...
        if key_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_block.tStartRefresh + key_dur-frameTolerance:
                # keep track of stop time/frame for later
                key_block.tStop = t  # not accounting for scr refresh
                key_block.frameNStop = frameN  # exact frame index
                # update status
                key_block.status = FINISHED
                key_block.status = FINISHED
        if key_block.status == STARTED and not waitOnFlip:
            theseKeys = key_block.getKeys(keyList=['space'], waitRelease=False)
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


# --- Prepare to start Routine "finish" ---
continueRoutine = True
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
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    
    # if end is starting this frame...
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        # update status
        end.status = STARTED
        end.setAutoDraw(True)
    
    # if end is active this frame...
    if end.status == STARTED:
        # update params
        pass
    
    # *end_key* updates
    waitOnFlip = False
    
    # if end_key is starting this frame...
    if end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key.frameNStart = frameN  # exact frame index
        end_key.tStart = t  # local t and not account for scr refresh
        end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key, 'tStartRefresh')  # time at next scr refresh
        # update status
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
