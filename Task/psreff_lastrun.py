#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.1),
    on Thu 06 Dec 2018 09:40:48 GMT
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'psreff'  # from the Builder filename that created this script
expInfo = {u'type': u'1', u'participant': u'9999'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/sebastijan/sebastijan.veselic@gmail.com/Work/Studies/2018/PrimarySecondaryReward/Notes/Experiment/psreff.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 764], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
import random

# we add + 1 just to make key type be either 1 or 2 
# If axcpt_key_type == 1 then:
# key 'f' denotes X did follow A
# key 'k' denotes A was not followed by X or 
#                 X was not preceeded by A

# if axcpt_key_type == 2 then, the opposite is true:
# key 'k' denotes X did follow A
# key 'f' denotes A was not followed by X or 
#                 X was not preceeded by A

axcpt_key_type = int(round(random.random())) + 1

# define colours used in the questions
opt_1, opt_2, opt_3, opt_4, opt_5 = [0.2, 0.2, 0.2], \
                                    [0.2, 0.2, 0.2], \
                                    [0.2, 0.2, 0.2], \
                                    [0.2, 0.2, 0.2], \
                                    [0.2, 0.2, 0.2]

# feedback color, may not be used in the future
feed_col = [-1, -1, -1]

# absolute trial counter; including practice trials
abs_trial = 1

# used to run either practice or real trials 
run_prac = 1
run_real = 0



# needs to be stored 
# - ev response and RT
# - stroop response and RT
# - 



text_7 = visual.TextStim(win=win, name='text_7',
    text='Instructions placeholder',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "prac_ann"
prac_annClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='First a series of practice trials \nwill follow to familiarise you with this game!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "real_ann"
real_annClock = core.Clock()

# Initialize components for Routine "cross_iti"
cross_itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rew_ann"
rew_annClock = core.Clock()

text_2 = visual.TextStim(win=win, name='text_2',
    text='On this trial you will play for:',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, -0.3), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "cross_iti"
cross_itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ev_prompt"
ev_promptClock = core.Clock()

text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
first = visual.Polygon(
    win=win, name='first',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[-0.6, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
second = visual.Polygon(
    win=win, name='second',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[-0.3, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
third = visual.Polygon(
    win=win, name='third',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[0, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
fourth = visual.Polygon(
    win=win, name='fourth',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[0.3, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
fifth = visual.Polygon(
    win=win, name='fifth',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[0.6, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='1',
    font='Arial',
    pos=[-0.6, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='2',
    font='Arial',
    pos=[-0.3, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='3',
    font='Arial',
    pos=[0.0, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='4',
    font='Arial',
    pos=[0.3, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='5',
    font='Arial',
    pos=[0.6, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);

# Initialize components for Routine "ev_feedback"
ev_feedbackClock = core.Clock()

first_feedback = visual.Polygon(
    win=win, name='first_feedback',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[-0.6, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
second_feedback = visual.Polygon(
    win=win, name='second_feedback',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[-0.3, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
third_feedback = visual.Polygon(
    win=win, name='third_feedback',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[0.0, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
fourth_feedback = visual.Polygon(
    win=win, name='fourth_feedback',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[0.3, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
fifth_feedback = visual.Polygon(
    win=win, name='fifth_feedback',
    edges=90, size=(0.25, 0.3),
    ori=0, pos=[0.6, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='1',
    font='Arial',
    pos=[-0.6, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='2',
    font='Arial',
    pos=[-0.3, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='3',
    font='Arial',
    pos=[0.0, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='4',
    font='Arial',
    pos=[0.3, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='5',
    font='Arial',
    pos=[0.6, -0.6], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);

# Initialize components for Routine "effort_ann"
effort_annClock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='Now comes the squeeze game!',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "cross_iti"
cross_itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "effort_task"
effort_taskClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Effort task placeholder',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "stroop_ann"
stroop_annClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='Now comes the concentration game!',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "cross_start"
cross_startClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "stroop_cue"
stroop_cueClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "var_time"
var_timeClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "stroop_target"
stroop_targetClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "stroop_feed"
stroop_feedClock = core.Clock()

image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "cross_iti"
cross_itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instr1_resp = event.BuilderKeyResponse()

# Depending on 'type' that's put in, we manually construct the 
# experimental design matrix that's used to determine
# the flow of tasks after each task. The ugliness of the 
# basic psychopy outcome that would have been obtained will
# be mitigated by a custom saving script. 
# it isn't necessary to have the complete matrix layout
# in all cases, but I am doing it here for sake of completeness

type = int(expInfo['type'])

run_ev, run_effort, run_stroop, run_rew = 1, 1, 1, 1

# run_ev, run_effort, run_stroop, run_rew
# here run_rew can be defined as 1 in all conditions
# because it will be changed during the task flow


if type == 1:
    run_ev, run_effort, run_stroop, run_rew = 1, 1, 1, 1
elif type == 2:
    run_ev, run_stroop, run_effort, run_rew = 1, 0, 1, 1
elif type == 3:
    run_effort, run_ev, run_stroop, run_rew  = 1, 0, 0, 1
elif type == 4:
    run_effort, run_stroop, run_ev, run_rew  = 1, 1, 0, 1
elif type == 5:
    run_stroop, run_ev, run_effort, run_rew  = 1, 0, 0, 1
elif type == 6:
    run_stroop, run_effort, run_ev, run_rew  = 1, 0, 0, 1
        
    
# keep track of which components have finished
instr1Components = [instr1_resp, text_7, text_9]
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1_resp* updates
    if t >= 0.0 and instr1_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1_resp.tStart = t
        instr1_resp.frameNStart = frameN  # exact frame index
        instr1_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr1_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr1_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr1_resp.keys = theseKeys[-1]  # just the last key pressed
            instr1_resp.rt = instr1_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *text_9* updates
    if t >= 1.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr1_resp.keys in ['', [], None]:  # No response was made
    instr1_resp.keys=None
thisExp.addData('instr1_resp.keys',instr1_resp.keys)
if instr1_resp.keys != None:  # we had a response
    thisExp.addData('instr1_resp.rt', instr1_resp.rt)
thisExp.nextEntry()

# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_trials.csv'),
    seed=None, name='main_loop')
thisExp.addLoop(main_loop)  # add the loop to the experiment
thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
if thisMain_loop != None:
    for paramName in thisMain_loop.keys():
        exec(paramName + '= thisMain_loop.' + paramName)

for thisMain_loop in main_loop:
    currentLoop = main_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop.keys():
            exec(paramName + '= thisMain_loop.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    prac_info = data.TrialHandler(nReps=run_prac, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='prac_info')
    thisExp.addLoop(prac_info)  # add the loop to the experiment
    thisPrac_info = prac_info.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_info.rgb)
    if thisPrac_info != None:
        for paramName in thisPrac_info.keys():
            exec(paramName + '= thisPrac_info.' + paramName)
    
    for thisPrac_info in prac_info:
        currentLoop = prac_info
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_info.rgb)
        if thisPrac_info != None:
            for paramName in thisPrac_info.keys():
                exec(paramName + '= thisPrac_info.' + paramName)
        
        # ------Prepare to start Routine "prac_ann"-------
        t = 0
        prac_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        prac_annComponents = [text_8, text_10, key_resp_2]
        for thisComponent in prac_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "prac_ann"-------
        while continueRoutine:
            # get current time
            t = prac_annClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_8* updates
            if t >= 0.0 and text_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_8.tStart = t
                text_8.frameNStart = frameN  # exact frame index
                text_8.setAutoDraw(True)
            
            # *text_10* updates
            if t >= 1 and text_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_10.tStart = t
                text_10.frameNStart = frameN  # exact frame index
                text_10.setAutoDraw(True)
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_ann"-------
        for thisComponent in prac_annComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
        prac_info.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            prac_info.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "prac_ann" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_prac repeats of 'prac_info'
    
    # get names of stimulus parameters
    if prac_info.trialList in ([], [None], None):
        params = []
    else:
        params = prac_info.trialList[0].keys()
    # save data for this loop
    prac_info.saveAsExcel(filename + '.xlsx', sheetName='prac_info',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    prac_info.saveAsText(filename + 'prac_info.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    real_info = data.TrialHandler(nReps=run_real, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='real_info')
    thisExp.addLoop(real_info)  # add the loop to the experiment
    thisReal_info = real_info.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisReal_info.rgb)
    if thisReal_info != None:
        for paramName in thisReal_info.keys():
            exec(paramName + '= thisReal_info.' + paramName)
    
    for thisReal_info in real_info:
        currentLoop = real_info
        # abbreviate parameter names if possible (e.g. rgb = thisReal_info.rgb)
        if thisReal_info != None:
            for paramName in thisReal_info.keys():
                exec(paramName + '= thisReal_info.' + paramName)
        
        # ------Prepare to start Routine "real_ann"-------
        t = 0
        real_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        real_annComponents = []
        for thisComponent in real_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "real_ann"-------
        while continueRoutine:
            # get current time
            t = real_annClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in real_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "real_ann"-------
        for thisComponent in real_annComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "real_ann" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_real repeats of 'real_info'
    
    # get names of stimulus parameters
    if real_info.trialList in ([], [None], None):
        params = []
    else:
        params = real_info.trialList[0].keys()
    # save data for this loop
    real_info.saveAsExcel(filename + '.xlsx', sheetName='real_info',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    real_info.saveAsText(filename + 'real_info.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    rew_role = data.TrialHandler(nReps=run_rew, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rew_role')
    thisExp.addLoop(rew_role)  # add the loop to the experiment
    thisRew_role = rew_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRew_role.rgb)
    if thisRew_role != None:
        for paramName in thisRew_role.keys():
            exec(paramName + '= thisRew_role.' + paramName)
    
    for thisRew_role in rew_role:
        currentLoop = rew_role
        # abbreviate parameter names if possible (e.g. rgb = thisRew_role.rgb)
        if thisRew_role != None:
            for paramName in thisRew_role.keys():
                exec(paramName + '= thisRew_role.' + paramName)
        
        # ------Prepare to start Routine "cross_iti"-------
        t = 0
        cross_itiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
        # keep track of which components have finished
        cross_itiComponents = [cross_sign]
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cross_iti"-------
        while continueRoutine:
            # get current time
            t = cross_itiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *cross_sign* updates
            if t >= 0.0 and cross_sign.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross_sign.tStart = t
                cross_sign.frameNStart = frameN  # exact frame index
                cross_sign.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cross_sign.status == STARTED and t >= frameRemains:
                cross_sign.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cross_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cross_iti"-------
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "cross_iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rew_ann"-------
        t = 0
        rew_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        if reward_type == 1:
            curr_reward = 'juice.png'
        else:
            curr_reward = 'pound.png'
        image.setImage(curr_reward)
        # keep track of which components have finished
        rew_annComponents = [text_2, image]
        for thisComponent in rew_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rew_ann"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rew_annClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rew_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rew_ann"-------
        for thisComponent in rew_annComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # run_ev, run_effort, run_stroop 
        if type == 2:
            run_ev, run_stroop, run_effort, run_rew = 1, 1, 0, 0
            abs_trial += 1
        elif type == 3:
            run_effort, run_ev, run_stroop, run_rew = 1, 0, 0, 0
        elif type == 4:
            run_effort, run_stroop, run_ev, run_rew = 1, 1, 0, 0
        elif type == 5:
            run_stroop, run_ev, run_effort, run_rew = 1, 0, 0, 0
            abs_trial += 1
        elif type == 6:
            run_stroop, run_effort, run_ev, run_rew = 1, 0, 0, 0
                
        thisExp.nextEntry()
        
    # completed run_rew repeats of 'rew_role'
    
    # get names of stimulus parameters
    if rew_role.trialList in ([], [None], None):
        params = []
    else:
        params = rew_role.trialList[0].keys()
    # save data for this loop
    rew_role.saveAsExcel(filename + '.xlsx', sheetName='rew_role',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    rew_role.saveAsText(filename + 'rew_role.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    ev_role = data.TrialHandler(nReps=run_ev, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ev_role')
    thisExp.addLoop(ev_role)  # add the loop to the experiment
    thisEv_role = ev_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEv_role.rgb)
    if thisEv_role != None:
        for paramName in thisEv_role.keys():
            exec(paramName + '= thisEv_role.' + paramName)
    
    for thisEv_role in ev_role:
        currentLoop = ev_role
        # abbreviate parameter names if possible (e.g. rgb = thisEv_role.rgb)
        if thisEv_role != None:
            for paramName in thisEv_role.keys():
                exec(paramName + '= thisEv_role.' + paramName)
        
        # ------Prepare to start Routine "cross_iti"-------
        t = 0
        cross_itiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
        # keep track of which components have finished
        cross_itiComponents = [cross_sign]
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cross_iti"-------
        while continueRoutine:
            # get current time
            t = cross_itiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *cross_sign* updates
            if t >= 0.0 and cross_sign.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross_sign.tStart = t
                cross_sign.frameNStart = frameN  # exact frame index
                cross_sign.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cross_sign.status == STARTED and t >= frameRemains:
                cross_sign.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cross_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cross_iti"-------
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "cross_iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        cb_loop2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ev.csv'),
            seed=None, name='cb_loop2')
        thisExp.addLoop(cb_loop2)  # add the loop to the experiment
        thisCb_loop2 = cb_loop2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCb_loop2.rgb)
        if thisCb_loop2 != None:
            for paramName in thisCb_loop2.keys():
                exec(paramName + '= thisCb_loop2.' + paramName)
        
        for thisCb_loop2 in cb_loop2:
            currentLoop = cb_loop2
            # abbreviate parameter names if possible (e.g. rgb = thisCb_loop2.rgb)
            if thisCb_loop2 != None:
                for paramName in thisCb_loop2.keys():
                    exec(paramName + '= thisCb_loop2.' + paramName)
            
            # ------Prepare to start Routine "ev_prompt"-------
            t = 0
            ev_promptClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            ev_resp = event.BuilderKeyResponse()
            curr_q = current_question
            text_5.setText(current_question)
            # keep track of which components have finished
            ev_promptComponents = [ev_resp, text_5, first, second, third, fourth, fifth, text_12, text_13, text_14, text_15, text_16]
            for thisComponent in ev_promptComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "ev_prompt"-------
            while continueRoutine:
                # get current time
                t = ev_promptClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ev_resp* updates
                if t >= 0.0 and ev_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ev_resp.tStart = t
                    ev_resp.frameNStart = frameN  # exact frame index
                    ev_resp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(ev_resp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if ev_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        ev_resp.keys = theseKeys[-1]  # just the last key pressed
                        ev_resp.rt = ev_resp.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                
                # *text_5* updates
                if t >= 0.0 and text_5.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_5.tStart = t
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.setAutoDraw(True)
                
                # *first* updates
                if t >= 0.0 and first.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    first.tStart = t
                    first.frameNStart = frameN  # exact frame index
                    first.setAutoDraw(True)
                
                # *second* updates
                if t >= 0.0 and second.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    second.tStart = t
                    second.frameNStart = frameN  # exact frame index
                    second.setAutoDraw(True)
                
                # *third* updates
                if t >= 0.0 and third.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    third.tStart = t
                    third.frameNStart = frameN  # exact frame index
                    third.setAutoDraw(True)
                
                # *fourth* updates
                if t >= 0.0 and fourth.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fourth.tStart = t
                    fourth.frameNStart = frameN  # exact frame index
                    fourth.setAutoDraw(True)
                
                # *fifth* updates
                if t >= 0.0 and fifth.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fifth.tStart = t
                    fifth.frameNStart = frameN  # exact frame index
                    fifth.setAutoDraw(True)
                
                # *text_12* updates
                if t >= 0.0 and text_12.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_12.tStart = t
                    text_12.frameNStart = frameN  # exact frame index
                    text_12.setAutoDraw(True)
                
                # *text_13* updates
                if t >= 0.0 and text_13.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_13.tStart = t
                    text_13.frameNStart = frameN  # exact frame index
                    text_13.setAutoDraw(True)
                
                # *text_14* updates
                if t >= 0.0 and text_14.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_14.tStart = t
                    text_14.frameNStart = frameN  # exact frame index
                    text_14.setAutoDraw(True)
                
                # *text_15* updates
                if t >= 0.0 and text_15.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_15.tStart = t
                    text_15.frameNStart = frameN  # exact frame index
                    text_15.setAutoDraw(True)
                
                # *text_16* updates
                if t >= 0.0 and text_16.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_16.tStart = t
                    text_16.frameNStart = frameN  # exact frame index
                    text_16.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ev_promptComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ev_prompt"-------
            for thisComponent in ev_promptComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if ev_resp.keys in ['', [], None]:  # No response was made
                ev_resp.keys=None
            cb_loop2.addData('ev_resp.keys',ev_resp.keys)
            if ev_resp.keys != None:  # we had a response
                cb_loop2.addData('ev_resp.rt', ev_resp.rt)
            
            # the Routine "ev_prompt" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ev_feedback"-------
            t = 0
            ev_feedbackClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            if ev_resp.keys == '1':
                opt_1 = [1, 0.84, 0.0]
                opt_2, opt_3, opt_4, opt_5 = [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2]
            elif ev_resp.keys == '2':
                opt_2 = [1, 0.84, 0.0]
                opt_1, opt_3, opt_4, opt_5 = [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2]
            elif ev_resp.keys == '3':
                opt_3 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_4, opt_5 = [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2]
            elif ev_resp.keys == '4':
                opt_4 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_3, opt_5 = [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2]
            elif ev_resp.keys == '5':
                opt_5 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_3, opt_4 = [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2], [0.2, 0.2, 0.2]
            
            
            
            
            
            
            
            
            first_feedback.setFillColor(opt_1)
            second_feedback.setFillColor(opt_2)
            third_feedback.setFillColor(opt_3)
            fourth_feedback.setFillColor(opt_4)
            fifth_feedback.setFillColor(opt_5)
            # keep track of which components have finished
            ev_feedbackComponents = [first_feedback, second_feedback, third_feedback, fourth_feedback, fifth_feedback, text_17, text_18, text_19, text_20, text_21]
            for thisComponent in ev_feedbackComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "ev_feedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ev_feedbackClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *first_feedback* updates
                if t >= 0.0 and first_feedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    first_feedback.tStart = t
                    first_feedback.frameNStart = frameN  # exact frame index
                    first_feedback.setAutoDraw(True)
                frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if first_feedback.status == STARTED and t >= frameRemains:
                    first_feedback.setAutoDraw(False)
                
                # *second_feedback* updates
                if t >= 0.0 and second_feedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    second_feedback.tStart = t
                    second_feedback.frameNStart = frameN  # exact frame index
                    second_feedback.setAutoDraw(True)
                frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if second_feedback.status == STARTED and t >= frameRemains:
                    second_feedback.setAutoDraw(False)
                
                # *third_feedback* updates
                if t >= 0.0 and third_feedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    third_feedback.tStart = t
                    third_feedback.frameNStart = frameN  # exact frame index
                    third_feedback.setAutoDraw(True)
                frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if third_feedback.status == STARTED and t >= frameRemains:
                    third_feedback.setAutoDraw(False)
                
                # *fourth_feedback* updates
                if t >= 0.0 and fourth_feedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fourth_feedback.tStart = t
                    fourth_feedback.frameNStart = frameN  # exact frame index
                    fourth_feedback.setAutoDraw(True)
                frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if fourth_feedback.status == STARTED and t >= frameRemains:
                    fourth_feedback.setAutoDraw(False)
                
                # *fifth_feedback* updates
                if t >= 0.0 and fifth_feedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fifth_feedback.tStart = t
                    fifth_feedback.frameNStart = frameN  # exact frame index
                    fifth_feedback.setAutoDraw(True)
                frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if fifth_feedback.status == STARTED and t >= frameRemains:
                    fifth_feedback.setAutoDraw(False)
                
                # *text_17* updates
                if t >= 0.0 and text_17.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_17.tStart = t
                    text_17.frameNStart = frameN  # exact frame index
                    text_17.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_17.status == STARTED and t >= frameRemains:
                    text_17.setAutoDraw(False)
                
                # *text_18* updates
                if t >= 0.0 and text_18.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_18.tStart = t
                    text_18.frameNStart = frameN  # exact frame index
                    text_18.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_18.status == STARTED and t >= frameRemains:
                    text_18.setAutoDraw(False)
                
                # *text_19* updates
                if t >= 0.0 and text_19.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_19.tStart = t
                    text_19.frameNStart = frameN  # exact frame index
                    text_19.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_19.status == STARTED and t >= frameRemains:
                    text_19.setAutoDraw(False)
                
                # *text_20* updates
                if t >= 0.0 and text_20.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_20.tStart = t
                    text_20.frameNStart = frameN  # exact frame index
                    text_20.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_20.status == STARTED and t >= frameRemains:
                    text_20.setAutoDraw(False)
                
                # *text_21* updates
                if t >= 0.0 and text_21.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_21.tStart = t
                    text_21.frameNStart = frameN  # exact frame index
                    text_21.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_21.status == STARTED and t >= frameRemains:
                    text_21.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ev_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ev_feedback"-------
            for thisComponent in ev_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # run_ev, run_effort, run_stroop 
            if type == 2:
                run_ev, run_stroop, run_effort, run_rew = 0, 1, 0, 1
            elif type == 3:
                run_effort, run_ev, run_stroop, run_rew = 0, 0, 1, 0
            elif type == 4:
                abs_trial += 1
                run_effort, run_stroop, run_ev, run_rew = 0, 0, 0, 1
            elif type == 5:
                run_stroop, run_ev, run_effort, run_rew = 0, 0, 1, 0
            elif type == 6:
                abs_trial += 1
                run_stroop, run_effort, run_ev, run_rew = 0, 0, 0, 1
                    
            thisExp.nextEntry()
            
        # completed 1 repeats of 'cb_loop2'
        
        # get names of stimulus parameters
        if cb_loop2.trialList in ([], [None], None):
            params = []
        else:
            params = cb_loop2.trialList[0].keys()
        # save data for this loop
        cb_loop2.saveAsExcel(filename + '.xlsx', sheetName='cb_loop2',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        cb_loop2.saveAsText(filename + 'cb_loop2.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed run_ev repeats of 'ev_role'
    
    # get names of stimulus parameters
    if ev_role.trialList in ([], [None], None):
        params = []
    else:
        params = ev_role.trialList[0].keys()
    # save data for this loop
    ev_role.saveAsExcel(filename + '.xlsx', sheetName='ev_role',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    ev_role.saveAsText(filename + 'ev_role.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    effort_role = data.TrialHandler(nReps=run_effort, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='effort_role')
    thisExp.addLoop(effort_role)  # add the loop to the experiment
    thisEffort_role = effort_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEffort_role.rgb)
    if thisEffort_role != None:
        for paramName in thisEffort_role.keys():
            exec(paramName + '= thisEffort_role.' + paramName)
    
    for thisEffort_role in effort_role:
        currentLoop = effort_role
        # abbreviate parameter names if possible (e.g. rgb = thisEffort_role.rgb)
        if thisEffort_role != None:
            for paramName in thisEffort_role.keys():
                exec(paramName + '= thisEffort_role.' + paramName)
        
        # ------Prepare to start Routine "effort_ann"-------
        t = 0
        effort_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        effort_annComponents = [text_23]
        for thisComponent in effort_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "effort_ann"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = effort_annClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_23* updates
            if t >= 0.0 and text_23.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_23.tStart = t
                text_23.frameNStart = frameN  # exact frame index
                text_23.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_23.status == STARTED and t >= frameRemains:
                text_23.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in effort_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "effort_ann"-------
        for thisComponent in effort_annComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "cross_iti"-------
        t = 0
        cross_itiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
        # keep track of which components have finished
        cross_itiComponents = [cross_sign]
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cross_iti"-------
        while continueRoutine:
            # get current time
            t = cross_itiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *cross_sign* updates
            if t >= 0.0 and cross_sign.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross_sign.tStart = t
                cross_sign.frameNStart = frameN  # exact frame index
                cross_sign.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cross_sign.status == STARTED and t >= frameRemains:
                cross_sign.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cross_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cross_iti"-------
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "cross_iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        cb_loop3 = data.TrialHandler(nReps=5, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='cb_loop3')
        thisExp.addLoop(cb_loop3)  # add the loop to the experiment
        thisCb_loop3 = cb_loop3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCb_loop3.rgb)
        if thisCb_loop3 != None:
            for paramName in thisCb_loop3.keys():
                exec(paramName + '= thisCb_loop3.' + paramName)
        
        for thisCb_loop3 in cb_loop3:
            currentLoop = cb_loop3
            # abbreviate parameter names if possible (e.g. rgb = thisCb_loop3.rgb)
            if thisCb_loop3 != None:
                for paramName in thisCb_loop3.keys():
                    exec(paramName + '= thisCb_loop3.' + paramName)
            
            # ------Prepare to start Routine "effort_task"-------
            t = 0
            effort_taskClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            
            # keep track of which components have finished
            effort_taskComponents = [text_11]
            for thisComponent in effort_taskComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "effort_task"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = effort_taskClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_11* updates
                if t >= 0.0 and text_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_11.tStart = t
                    text_11.frameNStart = frameN  # exact frame index
                    text_11.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_11.status == STARTED and t >= frameRemains:
                    text_11.setAutoDraw(False)
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in effort_taskComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "effort_task"-------
            for thisComponent in effort_taskComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # run_ev, run_effort, run_stroop 
            if type == 2:
                run_ev, run_stroop, run_effort, run_rew = 1, 0, 0, 1
                abs_trial += 1
            elif type == 3:
                run_prac = 0 # this needs to be here in order to prevent
                             # it from popping up unnecessarily 
                run_effort, run_ev, run_stroop, run_rew = 0, 1, 0, 0
            elif type == 4:
                run_effort, run_stroop, run_ev, run_rew = 0, 1, 1, 0
            elif type == 5:
                run_stroop, run_ev, run_effort, run_rew = 0, 0, 0, 1
                abs_trial += 1
            elif type == 6:
                run_stroop, run_effort, run_ev, run_rew = 0, 0, 1, 0
                    
            thisExp.nextEntry()
            
        # completed 5 repeats of 'cb_loop3'
        
        # get names of stimulus parameters
        if cb_loop3.trialList in ([], [None], None):
            params = []
        else:
            params = cb_loop3.trialList[0].keys()
        # save data for this loop
        cb_loop3.saveAsExcel(filename + '.xlsx', sheetName='cb_loop3',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        cb_loop3.saveAsText(filename + 'cb_loop3.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed run_effort repeats of 'effort_role'
    
    # get names of stimulus parameters
    if effort_role.trialList in ([], [None], None):
        params = []
    else:
        params = effort_role.trialList[0].keys()
    # save data for this loop
    effort_role.saveAsExcel(filename + '.xlsx', sheetName='effort_role',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    effort_role.saveAsText(filename + 'effort_role.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    stroop_role = data.TrialHandler(nReps=run_stroop, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='stroop_role')
    thisExp.addLoop(stroop_role)  # add the loop to the experiment
    thisStroop_role = stroop_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_role.rgb)
    if thisStroop_role != None:
        for paramName in thisStroop_role.keys():
            exec(paramName + '= thisStroop_role.' + paramName)
    
    for thisStroop_role in stroop_role:
        currentLoop = stroop_role
        # abbreviate parameter names if possible (e.g. rgb = thisStroop_role.rgb)
        if thisStroop_role != None:
            for paramName in thisStroop_role.keys():
                exec(paramName + '= thisStroop_role.' + paramName)
        
        # ------Prepare to start Routine "stroop_ann"-------
        t = 0
        stroop_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_annComponents = [text_22]
        for thisComponent in stroop_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "stroop_ann"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_annClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_22* updates
            if t >= 0.0 and text_22.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_22.tStart = t
                text_22.frameNStart = frameN  # exact frame index
                text_22.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_22.status == STARTED and t >= frameRemains:
                text_22.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_ann"-------
        for thisComponent in stroop_annComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "cross_start"-------
        t = 0
        cross_startClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        curr_t = min(2.1, max(0, random.gauss(520, 0.5)))
        axcpt_cue = cue
        axcpt_target = target
        # keep track of which components have finished
        cross_startComponents = [text]
        for thisComponent in cross_startComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cross_start"-------
        while continueRoutine:
            # get current time
            t = cross_startClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cross_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cross_start"-------
        for thisComponent in cross_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "cross_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "stroop_cue"-------
        t = 0
        stroop_cueClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        text_24.setText(axcpt_cue)
        # keep track of which components have finished
        stroop_cueComponents = [text_24]
        for thisComponent in stroop_cueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "stroop_cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_cueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_24* updates
            if t >= 0.0 and text_24.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_24.tStart = t
                text_24.frameNStart = frameN  # exact frame index
                text_24.setAutoDraw(True)
            frameRemains = 0.0 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_24.status == STARTED and t >= frameRemains:
                text_24.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_cue"-------
        for thisComponent in stroop_cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "var_time"-------
        t = 0
        var_timeClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        var_timeComponents = [text_6]
        for thisComponent in var_timeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "var_time"-------
        while continueRoutine:
            # get current time
            t = var_timeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if t >= 0.0 and text_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_6.tStart = t
                text_6.frameNStart = frameN  # exact frame index
                text_6.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_6.status == STARTED and t >= frameRemains:
                text_6.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in var_timeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "var_time"-------
        for thisComponent in var_timeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "var_time" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "stroop_target"-------
        t = 0
        stroop_targetClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_4.setText(axcpt_target)
        axcpt_resp = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        stroop_targetComponents = [text_4, axcpt_resp]
        for thisComponent in stroop_targetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "stroop_target"-------
        while continueRoutine:
            # get current time
            t = stroop_targetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            frameRemains = 0.0 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_4.status == STARTED and t >= frameRemains:
                text_4.setAutoDraw(False)
            
            # *axcpt_resp* updates
            if t >= 0.0 and axcpt_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                axcpt_resp.tStart = t
                axcpt_resp.frameNStart = frameN  # exact frame index
                axcpt_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(axcpt_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if axcpt_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'k'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    axcpt_resp.keys = theseKeys[-1]  # just the last key pressed
                    axcpt_resp.rt = axcpt_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
            
            if axcpt_resp.keys:
                feed_col = [1, 1, 1]
                responded = 0.5
                done = 2
            else:
                feed_col = [-1, -1, -1]
                
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_targetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_target"-------
        for thisComponent in stroop_targetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if axcpt_resp.keys in ['', [], None]:  # No response was made
            axcpt_resp.keys=None
        stroop_role.addData('axcpt_resp.keys',axcpt_resp.keys)
        if axcpt_resp.keys != None:  # we had a response
            stroop_role.addData('axcpt_resp.rt', axcpt_resp.rt)
        
        # the Routine "stroop_target" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "stroop_feed"-------
        t = 0
        stroop_feedClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        run_prac = 0
        
        if abs_trial == 20:
            run_real = 1
        
        if  axcpt_resp.keys == 'f' and axcpt_key_type == 1:
            part_resp = 1
        elif axcpt_resp.keys == 'k' and axcpt_key_type == 2:
            part_resp = 1
        else:
            part_resp = 2
        
        
        if correct_response == 1 and part_resp == 1 or \
            correct_response == 2 and part_resp == 2: 
        
            given_feedback = "correct.png" 
        else:
            given_feedback = "wrong.png"
        
            
        image_2.setImage(given_feedback)
        # keep track of which components have finished
        stroop_feedComponents = [image_2]
        for thisComponent in stroop_feedComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "stroop_feed"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_feedClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_feedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_feed"-------
        for thisComponent in stroop_feedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # run_ev, run_effort, run_stroop 
        
        if type == 1:
            abs_trial += 1
        
        if type == 2:
            run_ev, run_effort, run_stroop, run_rew = 0, 1, 0, 0
        elif type == 3:
            run_effort, run_ev, run_stroop, run_rew = 0, 0, 0, 1
            abs_trial += 1
        elif type == 4:
            run_effort, run_stroop, run_ev, run_rew = 1, 0, 1, 0
        elif type == 5:
            run_stroop, run_ev, run_effort, run_rew = 0, 1, 1, 0
        elif type == 6:
            run_stroop, run_effort, run_ev, run_rew = 0, 1, 0, 0
                
        
        # ------Prepare to start Routine "cross_iti"-------
        t = 0
        cross_itiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
        # keep track of which components have finished
        cross_itiComponents = [cross_sign]
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cross_iti"-------
        while continueRoutine:
            # get current time
            t = cross_itiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *cross_sign* updates
            if t >= 0.0 and cross_sign.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross_sign.tStart = t
                cross_sign.frameNStart = frameN  # exact frame index
                cross_sign.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cross_sign.status == STARTED and t >= frameRemains:
                cross_sign.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cross_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cross_iti"-------
        for thisComponent in cross_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "cross_iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_stroop repeats of 'stroop_role'
    
    # get names of stimulus parameters
    if stroop_role.trialList in ([], [None], None):
        params = []
    else:
        params = stroop_role.trialList[0].keys()
    # save data for this loop
    stroop_role.saveAsExcel(filename + '.xlsx', sheetName='stroop_role',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    stroop_role.saveAsText(filename + 'stroop_role.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_loop'

# get names of stimulus parameters
if main_loop.trialList in ([], [None], None):
    params = []
else:
    params = main_loop.trialList[0].keys()
# save data for this loop
main_loop.saveAsExcel(filename + '.xlsx', sheetName='main_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
main_loop.saveAsText(filename + 'main_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])












# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
