#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.1),
    on December 20, 2018, at 15:29
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
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
expName = u'psreff3'  # from the Builder filename that created this script
expInfo = {u'participant': u'9999', u'num_pract': u'20', u'ef_conn': u'1', u'run_debug': u'0', u'g_conn': u'1', u'type': u'1', u'pic_eval': u'1'}
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
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[1, 1, 1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
import random, os, serial, time, collections

################################################
########### defining basic variables ###########
################################################

# define colours used in the questions


opt_1, opt_2, opt_3, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                           [0.2, 0.2, 0.2], \
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

# variable that determines whether matrix reevaluation
# will be run or not
run_correct = 0

# current trial within the matrix sequence
matrix_trial = 1

#current row that is being pulled for the image in the matrix trial
curr_row = 0
# helper variable used in the matrix evaluation procedure
already_switched = 0

################################################
########### creating containers ################ 
################################################

# storage containers
stor_ev = {}
stor_eff = {}
stor_main = {}
pump_vol = {} # this gives us a clear mapping between volume and commands to send
stor_gust = {}
stor_init_q = []
stor_pic_q = []
stor_jui_eval = collections.defaultdict()
stor_matrix_ans = []

################################################
########### pump related information ########### 
################################################

# clear mapping to make sure we know how much to send 

pump_selecter = ['\13', '\14', '\15', '\16']
pumps = ['\1', '\2', '\3', '\4']

ctr = 1
pump_vol = {}
stringed_ctr = str(ctr)
for vol in range(100, 4100, 100):
    while stringed_ctr[-1] == '8' or stringed_ctr[-1] == '9':
        ctr += 1
        stringed_ctr = str(ctr)
    else:
        pump_vol[str(vol)] = ctr
        ctr += 1                       
        stringed_ctr = str(ctr)


# add nice background 
background_image = visual.ImageStim(win=win, image = 'background_f.png')

# response options
left_resp = 'f'
right_resp = 'k'

# this works but make it nicer so it adds up files together in a nicer way
def check_file(filename, cwd, ctr):
    for file in os.listdir(cwd):
        if file.endswith('.txt'):
            if file != filename: # if a file doesnt exist just return the fname
                return filename
            else:
                tmp = file.split('_')
                tmp[1] = tmp[1] + '_' + str(ctr) # our new sub_id is now id_ctr 
                ctr += 1 # increment for recursivity 
                filename = '_'.join(tmp) # rename the file
                check_file(filename, cwd, ctr) 


################################################
########### effort #############################
################################################

mvc = 95

curr_contr = 0
rew_multpl = 0

################################################
########### flanker ############################
################################################

obtained_rew = 0

base_rew = 0.10
# flanker difficulty
diff_lev = ['low', 'high']

# cue timing denotes how long the flanker cues are presented
cue_time = 0.3

# resp window denotes the length of the response window 
resp_wind = 0.5

vol = 1

juice_rew = 'juice.png'
pound_rew = 'pound.png'


###################################################
########## initial state determination ############
###################################################

# variable for initial questions that determine a participants state
initial_q = ''


################################################
################# juice evaluation #############
################################################

juice_trial = 1
run_dispenser = 1
pump = ''
tmp_val = 0
# we preconfigure our container to be a list for each pump
for el in pumps:
    jui = str(int(el.encode('hex'), 16))
    stor_jui_eval[jui] = []


# just for debugging purposes
run_debug = int(expInfo['run_debug'])




############################################################
################### file saving function ###################
############################################################

def save_to_file(dataset, curr_reward, stor_ev, abs_trial, stor_eff, stor_main, stor_gust, types):
    trial_l = sorted([int(el) for el in stor_ev.keys()])
    str_abs_t = str(abs_trial)
    
    # we make types a list that denotes which of the 6 potential conditions it will be
    if type == types[0] or type == types[1]:
        
        for t in trial_l:
            str_t = str(t)
            dataset.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{} \
                        {}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(str_abs_t,                # abs_trial
                                                             curr_reward,          # current reward type
                                                             stor_ev[str_t][0],    # question  
                                                             stor_ev[str_t][1],     # response
                                                             stor_ev[str_t][2],  # reaction time
                                                             stor_eff[str_abs_t][0],     # trial contraction
                                                             stor_eff[str_abs_t][1],     # reward multiplier | actual reward to be paid
                                                             stor_main[str_abs_t][0],  # first stim
                                                             stor_main[str_abs_t][1],  # go or no go
                                                             stor_main[str_abs_t][2],  # response
                                                             stor_main[str_abs_t][3],  # response rt 
                                                             stor_main[str_abs_t][4],  # reward
                                                             stor_gust[str_abs_t][0],  # pump
                                                             stor_gust[str_abs_t][1],  # times pumped
                                                             stor_gust[str_abs_t][2]))  # amount









text_7 = visual.TextStim(win=win, name='text_7',
    text=u'Instructions placeholder',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text=u'Press SPACE to continue!',
    font=u'Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "matrix_eval"
matrix_evalClock = core.Clock()

image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_55 = visual.TextStim(win=win, name='text_55',
    text=u'Answer by pressing keys from 1 to 5. If you do not know the answer, press 6.',
    font=u'Arial',
    pos=(0, 0.85), height=0.1, wrapWidth=1.4, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "matrix_answ"
matrix_answClock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.8, 1.6)[0], height=(0.8, 1.6)[1],
    ori=0, pos=(0, 0),
    lineWidth=10, lineColor=[0.2, 0.2, 0.2], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=0.9, depth=-1.0, interpolate=True)
text_51 = visual.TextStim(win=win, name='text_51',
    text=u'You have chosen:',
    font=u'Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='default text',
    font=u'Arial',
    pos=(0, 0.4), height=0.3, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_53 = visual.TextStim(win=win, name='text_53',
    text=u'If this is true, press "y". \nIf you want to choose again, press "n".',
    font=u'Arial',
    pos=(0, 0.05), height=0.1, wrapWidth=0.6, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);


# Initialize components for Routine "matrix_correct"
matrix_correctClock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "transition"
transitionClock = core.Clock()
text_54 = visual.TextStim(win=win, name='text_54',
    text=u'We would now like you to answer a number of questions and pick your favourite juice!',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ini_q"
ini_qClock = core.Clock()
text_42 = visual.TextStim(win=win, name='text_42',
    text='We would first like to ask you a few questions. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_43 = visual.TextStim(win=win, name='text_43',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "eval_iniq"
eval_iniqClock = core.Clock()

rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.6, pos=[0.0, -0.4], low=0, high=1, precision=100, showValue=False, markerExpansion=0, scale='')
text_44 = visual.TextStim(win=win, name='text_44',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "eval_pic"
eval_picClock = core.Clock()


rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=['Very much', ' not at all'], scale='')
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='How much do you like this picture',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "est_sal"
est_salClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='You will now get to try a number of juices.\nAfter you obtain each juice, we would like you\nto rate them. We will take your answers into\naccount so you will be playing for your\nfavourite juice!\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "supl_jui"
supl_juiClock = core.Clock()

text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "eval_jui"
eval_juiClock = core.Clock()

text_30 = visual.TextStim(win=win, name='text_30',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=0.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
first_2 = visual.Rect(
    win=win, name='first_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.8, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
second_2 = visual.Rect(
    win=win, name='second_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.5, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
third_2 = visual.Rect(
    win=win, name='third_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.2, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
fourth_2 = visual.Rect(
    win=win, name='fourth_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.1, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
fifth_2 = visual.Rect(
    win=win, name='fifth_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.4, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
sixth_2 = visual.Rect(
    win=win, name='sixth_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=(0.7, -0.6),
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
text_31 = visual.TextStim(win=win, name='text_31',
    text='1',
    font='Arial',
    pos=[-0.8, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);
text_34 = visual.TextStim(win=win, name='text_34',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text='5',
    font='Arial',
    pos=[0.4, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='6',
    font='Arial',
    pos=[0.7, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-14.0);

# Initialize components for Routine "jui_feed"
jui_feedClock = core.Clock()

first_feedback_2 = visual.Rect(
    win=win, name='first_feedback_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.8, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
second_feedback_2 = visual.Rect(
    win=win, name='second_feedback_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.5, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
third_feedback_2 = visual.Rect(
    win=win, name='third_feedback_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.2, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
fourth_feedback_2 = visual.Rect(
    win=win, name='fourth_feedback_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.1, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
fifth_feedback_2 = visual.Rect(
    win=win, name='fifth_feedback_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.4, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
sixth_feedback_2 = visual.Rect(
    win=win, name='sixth_feedback_2',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=(0.7, -0.6),
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
text_36 = visual.TextStim(win=win, name='text_36',
    text='1',
    font='Arial',
    pos=[-0.8, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
text_39 = visual.TextStim(win=win, name='text_39',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
text_40 = visual.TextStim(win=win, name='text_40',
    text='5',
    font='Arial',
    pos=[0,0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='6',
    font='Arial',
    pos=(0.7, -0.58), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);

# Initialize components for Routine "jui_out"
jui_outClock = core.Clock()

text_41 = visual.TextStim(win=win, name='text_41',
    text='You choose:',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_45 = visual.TextStim(win=win, name='text_45',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "phy_mvc"
phy_mvcClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='We will now ask you to give your best and try to \nsqueeze the device in front of you as hard as possible.\n\nWe want to see how strong you are!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "prac_ann"
prac_annClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='First a series of practice trials \nwill follow to familiarise you with this game!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=0.8, ori=0, 
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
background_poly3 = visual.Rect(
    win=win, name='background_poly3',
    width=(0.8, 1.8)[0], height=(0.8, 1.8)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1, -1, -1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0.5, depth=0.0, interpolate=True)
text_26 = visual.TextStim(win=win, name='text_26',
    text='Now the game begins!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rew_ann"
rew_annClock = core.Clock()

text_2 = visual.TextStim(win=win, name='text_2',
    text='Now, you will play for:',
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

# Initialize components for Routine "iti"
itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ev_prom"
ev_promClock = core.Clock()

text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=0.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
first = visual.Rect(
    win=win, name='first',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.8, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
second = visual.Rect(
    win=win, name='second',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.5, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
third = visual.Rect(
    win=win, name='third',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.2, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
fourth = visual.Rect(
    win=win, name='fourth',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.1, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
fifth = visual.Rect(
    win=win, name='fifth',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.4, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
sixth = visual.Rect(
    win=win, name='sixth',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.7, -0.6],
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=[0.2, 0.2, 0.2], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='1',
    font='Arial',
    pos=[-0.8, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='5',
    font='Arial',
    pos=[0.4, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
text_47 = visual.TextStim(win=win, name='text_47',
    text='6',
    font='Arial',
    pos=[0.7, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-14.0);

# Initialize components for Routine "ev_feed"
ev_feedClock = core.Clock()

first_feedback = visual.Rect(
    win=win, name='first_feedback',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.8, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
second_feedback = visual.Rect(
    win=win, name='second_feedback',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.5, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
third_feedback = visual.Rect(
    win=win, name='third_feedback',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[-0.2, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
fourth_feedback = visual.Rect(
    win=win, name='fourth_feedback',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.1, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
fifth_feedback = visual.Rect(
    win=win, name='fifth_feedback',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=[0.4, -0.6],
    lineWidth=10, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
sixth_feedback = visual.Rect(
    win=win, name='sixth_feedback',
    width=(0.25, 0.3)[0], height=(0.25, 0.3)[1],
    ori=0, pos=(0.7, -0.6),
    lineWidth=10, lineColor=[0, 0, 0], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
text_17 = visual.TextStim(win=win, name='text_17',
    text='1',
    font='Arial',
    pos=[-0.8, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='5',
    font='Arial',
    pos=[0.4, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);
text_46 = visual.TextStim(win=win, name='text_46',
    text='6',
    font='Arial',
    pos=[0.7,  -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);

# Initialize components for Routine "ev_save"
ev_saveClock = core.Clock()


# Initialize components for Routine "eff_prom"
eff_promClock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='Now comes the squeeze game!',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "eff_tas"
eff_tasClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Effort task placeholder',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "beg_fix"
beg_fixClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "tar_ann"
tar_annClock = core.Clock()
main_image = visual.ImageStim(
    win=win, name='main_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "main_feed"
main_feedClock = core.Clock()
feed_info = visual.Polygon(
    win=win, name='feed_info',
    edges=90, size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "comp"
compClock = core.Clock()


# Initialize components for Routine "tar_feed"
tar_feedClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='You have obtained',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Initialize components for Routine "juice_eval"
juice_evalClock = core.Clock()

text_48 = visual.TextStim(win=win, name='text_48',
    text='How much do you think 100ml of juice is worth?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_50 = visual.TextStim(win=win, name='text_50',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "eval_pic"
eval_picClock = core.Clock()


rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=['Very much', ' not at all'], scale='')
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='How much do you like this picture',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

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
# experimental design matrix such that counterbalancing is achieved 
# the ugly psychopy output file that would be obtained through this
# will then be discarded and a custom saving script will be used 
# it isn't necessary to have the complete matrix layout written out
# in all cases, but I am doing it here for sake of completeness

type = int(expInfo['type'])

run_ev, run_effort, run_stroop, run_rew = 1, 1, 1, 1

# run_ev, run_effort, run_stroop, run_rew
# here run_rew can be defined as 1 in all conditions
# because it will be changed during the task flow


if type == 1:
    run_ev, run_effort, run_flanker, run_rew = 1, 1, 1, 1
elif type == 2:
    run_ev, run_flanker, run_effort, run_rew = 1, 0, 0, 1
elif type == 3:
    run_effort, run_ev, run_flanker, run_rew  = 1, 0, 0, 1
elif type == 4:
    run_effort, run_flanker, run_ev, run_rew  = 1, 0, 0, 1
elif type == 5:
    run_flanker, run_ev, run_effort, run_rew  = 1, 0, 0, 1
elif type == 6:
    run_flanker, run_effort, run_ev, run_rew  = 1, 0, 0, 1

# open datafile in the beginning
exp_name = str(expName)
sub_id = str(expInfo['participant']) 
dat = str(expInfo['date'])

# number of practice trials | default is 20
num_pract = int(expInfo['num_pract'])  

# connection is set at 1 as default, meaning we want to connect gustaf
gust_connected = str(expInfo['g_conn'])

# connection is set at 1 as default, meaning we want to connect the phys dev
eff_connected = str(expInfo['ef_conn'])

out_type = str(type) # we do this to avoid issues with reconverting type over and over 


pic_eval = int(expInfo['pic_eval'])

if pic_eval == 1:
    run_pic_eval_b = 1
    run_pic_eval_e = 0
else:
    run_pic_eval_b = 0
    run_pic_eval_e = 1



# get current working directory 
cwd = os.getcwd()

# filename
fname = exp_name + '_' + sub_id + '_' + out_type  + dat + '.txt'

complete = cwd + '\\data\\' + fname

# handling if a file with that sub_id already exists 

ctr = 0 # recursively checks if the file already exists, if it doesn't it stops
fname = check_file(fname, cwd, ctr)



# open a text file 
dataset = open(complete, 'w')

# in the first row we save header columns | add the others later

dataset.write('trial\tcurr_rew\tquestion\tresponse\tresp_rt\ttrial_conc\trew_mult\tmain_st\tgng\tresp_m\tresp_m_rt\trew_m\tpump\tpump_tim\tpump_vol\n')

# if we want to connect the gustatory device
if gust_connected == 1:

    # set up gustaf connection 

    timeout = 0
    params = {
        'timeout'  : timeout,
        'baudrate' : 19200,
        'bytesize' : serial.EIGHTBITS,
        'parity'   : serial.PARITY_NONE,
        'stopbits' : serial.STOPBITS_ONE,
    }

    dev = serial.Serial('COM3', **params)

    # Keep in mind there should be at least a 10ms difference
    # between changing amount of juice and the actual squirting
    # sequence itself. 

    # safety feature to make sure port is open 
    if(dev.isOpen() == False):
        dev.open()








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
matrix_trial = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'm_reason.csv', selection=curr_row),
    seed=None, name='matrix_trial')
thisExp.addLoop(matrix_trial)  # add the loop to the experiment
thisMatrix_trial = matrix_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMatrix_trial.rgb)
if thisMatrix_trial != None:
    for paramName in thisMatrix_trial.keys():
        exec(paramName + '= thisMatrix_trial.' + paramName)

for thisMatrix_trial in matrix_trial:
    currentLoop = matrix_trial
    # abbreviate parameter names if possible (e.g. rgb = thisMatrix_trial.rgb)
    if thisMatrix_trial != None:
        for paramName in thisMatrix_trial.keys():
            exec(paramName + '= thisMatrix_trial.' + paramName)
    
    # ------Prepare to start Routine "matrix_eval"-------
    t = 0
    matrix_evalClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    correct_answer = corr_answ
    curr_matrix = item
    image_3.setImage(item)
    item_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    matrix_evalComponents = [image_3, item_resp, text_55]
    for thisComponent in matrix_evalComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "matrix_eval"-------
    while continueRoutine:
        # get current time
        t = matrix_evalClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        
        # *item_resp* updates
        if t >= 0.0 and item_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            item_resp.tStart = t
            item_resp.frameNStart = frameN  # exact frame index
            item_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(item_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if item_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                item_resp.keys = theseKeys[-1]  # just the last key pressed
                item_resp.rt = item_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_55* updates
        if t >= 0.0 and text_55.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_55.tStart = t
            text_55.frameNStart = frameN  # exact frame index
            text_55.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in matrix_evalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "matrix_eval"-------
    for thisComponent in matrix_evalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    chosen_item = item_resp.keys
    # check responses
    if item_resp.keys in ['', [], None]:  # No response was made
        item_resp.keys=None
    matrix_trial.addData('item_resp.keys',item_resp.keys)
    if item_resp.keys != None:  # we had a response
        matrix_trial.addData('item_resp.rt', item_resp.rt)
    # the Routine "matrix_eval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "matrix_answ"-------
    t = 0
    matrix_answClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(current_matrx)
    text_52.setText(chosen_item)
    matrix_reeval = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    matrix_answComponents = [image_4, polygon_2, text_51, text_52, matrix_reeval, text_53]
    for thisComponent in matrix_answComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "matrix_answ"-------
    while continueRoutine:
        # get current time
        t = matrix_answClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        
        # *polygon_2* updates
        if t >= 0.0 and polygon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_2.tStart = t
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.setAutoDraw(True)
        
        # *text_51* updates
        if t >= 0.0 and text_51.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_51.tStart = t
            text_51.frameNStart = frameN  # exact frame index
            text_51.setAutoDraw(True)
        
        # *text_52* updates
        if t >= 0.0 and text_52.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_52.tStart = t
            text_52.frameNStart = frameN  # exact frame index
            text_52.setAutoDraw(True)
        
        # *matrix_reeval* updates
        if t >= 0.0 and matrix_reeval.status == NOT_STARTED:
            # keep track of start time/frame for later
            matrix_reeval.tStart = t
            matrix_reeval.frameNStart = frameN  # exact frame index
            matrix_reeval.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(matrix_reeval.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if matrix_reeval.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                matrix_reeval.keys = theseKeys[-1]  # just the last key pressed
                matrix_reeval.rt = matrix_reeval.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_53* updates
        if t >= 0.0 and text_53.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_53.tStart = t
            text_53.frameNStart = frameN  # exact frame index
            text_53.setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in matrix_answComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "matrix_answ"-------
    for thisComponent in matrix_answComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if matrix_reeval.keys in ['', [], None]:  # No response was made
        matrix_reeval.keys=None
    matrix_trial.addData('matrix_reeval.keys',matrix_reeval.keys)
    if matrix_reeval.keys != None:  # we had a response
        matrix_trial.addData('matrix_reeval.rt', matrix_reeval.rt)
    if matrix_reeval.keys == 'n':
        run_correct = 1
    else:
        run_correct = 0 
        
        # if the current matrix finished sample B, then we move to
        # item 4 
        if matrix_trial == 2:
            curr_row = 5
        else:
            curr_row += 1
    
    
    
    
    
        # we literally score them 1 or 0 depending on their performance
        responded_correctly = item_resp.keys == str(correct_answer)
        if responded_correctly:
            stor_matrix_ans.append(1)
        else:
            stor_matrix_ans.append(0) 
    
        # if the last three consecutive items are 0, it means
        # we need to stop the evaluation. 
        
        if trial == 3 and not responded_correctly:
            change_item = 1
    
        if sum(stor_matrix_ans[-3:]) == 0:
            matrix_trial.finished=True
        
        matrix_trial += 1
    # the Routine "matrix_answ" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    matrix_reevaluation = data.TrialHandler(nReps=run_correct, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='matrix_reevaluation')
    thisExp.addLoop(matrix_reevaluation)  # add the loop to the experiment
    thisMatrix_reevaluation = matrix_reevaluation.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMatrix_reevaluation.rgb)
    if thisMatrix_reevaluation != None:
        for paramName in thisMatrix_reevaluation.keys():
            exec(paramName + '= thisMatrix_reevaluation.' + paramName)
    
    for thisMatrix_reevaluation in matrix_reevaluation:
        currentLoop = matrix_reevaluation
        # abbreviate parameter names if possible (e.g. rgb = thisMatrix_reevaluation.rgb)
        if thisMatrix_reevaluation != None:
            for paramName in thisMatrix_reevaluation.keys():
                exec(paramName + '= thisMatrix_reevaluation.' + paramName)
        
        # ------Prepare to start Routine "matrix_correct"-------
        t = 0
        matrix_correctClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_5.setImage(current_matrix)
        item_resp_again = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        matrix_correctComponents = [image_5, item_resp_again]
        for thisComponent in matrix_correctComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "matrix_correct"-------
        while continueRoutine:
            # get current time
            t = matrix_correctClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_5* updates
            if t >= 0.0 and image_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_5.tStart = t
                image_5.frameNStart = frameN  # exact frame index
                image_5.setAutoDraw(True)
            
            # *item_resp_again* updates
            if t >= 0.0 and item_resp_again.status == NOT_STARTED:
                # keep track of start time/frame for later
                item_resp_again.tStart = t
                item_resp_again.frameNStart = frameN  # exact frame index
                item_resp_again.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(item_resp_again.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if item_resp_again.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    item_resp_again.keys = theseKeys[-1]  # just the last key pressed
                    item_resp_again.rt = item_resp_again.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in matrix_correctComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "matrix_correct"-------
        for thisComponent in matrix_correctComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if item_resp_again.keys in ['', [], None]:  # No response was made
            item_resp_again.keys=None
        matrix_reevaluation.addData('item_resp_again.keys',item_resp_again.keys)
        if item_resp_again.keys != None:  # we had a response
            matrix_reevaluation.addData('item_resp_again.rt', item_resp_again.rt)
        responded_correctly = item_resp_again.keys == str(correct_answer)
        
        if responded_correctly:
            stor_matrix_ans.append(1)
        else:
            stor_matrix_ans.append(0) 
        
        if sum(stor_matrix_ans[-3:]) == 0:
                matrix_trial.finished=True
        
        if matrix_trial == 3 and not responded_correctly:
            change_item = 1
            already_switched = 1
        elif matrix_trial  == 4 and not responded_correctly and already_switched == 0:
            change_item = 1
        
        # if the current matrix finished sample B, then we move to
        # item 4 
        
        if matrix_trial == 2:
            curr_row = 5
        else:
            curr_row += 1
        
        matrix_trial += 1
        # the Routine "matrix_correct" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_correct repeats of 'matrix_reevaluation'
    
    # get names of stimulus parameters
    if matrix_reevaluation.trialList in ([], [None], None):
        params = []
    else:
        params = matrix_reevaluation.trialList[0].keys()
    # save data for this loop
    matrix_reevaluation.saveAsExcel(filename + '.xlsx', sheetName='matrix_reevaluation',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    matrix_reevaluation.saveAsText(filename + 'matrix_reevaluation.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'matrix_trial'

# get names of stimulus parameters
if matrix_trial.trialList in ([], [None], None):
    params = []
else:
    params = matrix_trial.trialList[0].keys()
# save data for this loop
matrix_trial.saveAsExcel(filename + '.xlsx', sheetName='matrix_trial',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
matrix_trial.saveAsText(filename + 'matrix_trial.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "transition"-------
t = 0
transitionClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
transitionComponents = [text_54]
for thisComponent in transitionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "transition"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = transitionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_54* updates
    if t >= 0.0 and text_54.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_54.tStart = t
        text_54.frameNStart = frameN  # exact frame index
        text_54.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_54.status == STARTED and t >= frameRemains:
        text_54.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "transition"-------
for thisComponent in transitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=run_debug, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "ini_q"-------
    t = 0
    ini_qClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instr1_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    ini_qComponents = [instr1_resp_2, text_42, text_43]
    for thisComponent in ini_qComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ini_q"-------
    while continueRoutine:
        # get current time
        t = ini_qClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr1_resp_2* updates
        if t >= 0.0 and instr1_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr1_resp_2.tStart = t
            instr1_resp_2.frameNStart = frameN  # exact frame index
            instr1_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instr1_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if instr1_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                instr1_resp_2.keys = theseKeys[-1]  # just the last key pressed
                instr1_resp_2.rt = instr1_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_42* updates
        if t >= 0.0 and text_42.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_42.tStart = t
            text_42.frameNStart = frameN  # exact frame index
            text_42.setAutoDraw(True)
        
        # *text_43* updates
        if t >= 1.0 and text_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_43.tStart = t
            text_43.frameNStart = frameN  # exact frame index
            text_43.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ini_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ini_q"-------
    for thisComponent in ini_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instr1_resp_2.keys in ['', [], None]:  # No response was made
        instr1_resp_2.keys=None
    trials.addData('instr1_resp_2.keys',instr1_resp_2.keys)
    if instr1_resp_2.keys != None:  # we had a response
        trials.addData('instr1_resp_2.rt', instr1_resp_2.rt)
    # the Routine "ini_q" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    init_qs = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('initial_q.csv'),
        seed=None, name='init_qs')
    thisExp.addLoop(init_qs)  # add the loop to the experiment
    thisInit_q = init_qs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInit_q.rgb)
    if thisInit_q != None:
        for paramName in thisInit_q.keys():
            exec(paramName + '= thisInit_q.' + paramName)
    
    for thisInit_q in init_qs:
        currentLoop = init_qs
        # abbreviate parameter names if possible (e.g. rgb = thisInit_q.rgb)
        if thisInit_q != None:
            for paramName in thisInit_q.keys():
                exec(paramName + '= thisInit_q.' + paramName)
        
        # ------Prepare to start Routine "eval_iniq"-------
        t = 0
        eval_iniqClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # this is the question it randomly pulls from the .csv file
        initial_q = current_question
        
        # this is added because by having an id of the question
        # where the questions are randomised, we can simply store it
        # later
        q_id = sav_mapping
        rating.reset()
        text_44.setText(initial_q)
        # keep track of which components have finished
        eval_iniqComponents = [rating, text_44]
        for thisComponent in eval_iniqComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "eval_iniq"-------
        while continueRoutine:
            # get current time
            t = eval_iniqClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rating* updates
            if t >= 0.0 and rating.status == NOT_STARTED:
                # keep track of start time/frame for later
                rating.tStart = t
                rating.frameNStart = frameN  # exact frame index
                rating.setAutoDraw(True)
            continueRoutine &= rating.noResponse  # a response ends the trial
            
            # *text_44* updates
            if t >= 0.0 and text_44.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_44.tStart = t
                text_44.frameNStart = frameN  # exact frame index
                text_44.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eval_iniqComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "eval_iniq"-------
        for thisComponent in eval_iniqComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stor_init_q.append(rating.getRating())
        # store data for init_qs (TrialHandler)
        init_qs.addData('rating.response', rating.getRating())
        # the Routine "eval_iniq" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'init_qs'
    
    # get names of stimulus parameters
    if init_qs.trialList in ([], [None], None):
        params = []
    else:
        params = init_qs.trialList[0].keys()
    # save data for this loop
    init_qs.saveAsExcel(filename + '.xlsx', sheetName='init_qs',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    init_qs.saveAsText(filename + 'init_qs.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trial_pic_eval = data.TrialHandler(nReps=run_pic_eval_b, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pic_rating.csv'),
        seed=None, name='trial_pic_eval')
    thisExp.addLoop(trial_pic_eval)  # add the loop to the experiment
    thisTrial_pic_eval = trial_pic_eval.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_pic_eval.rgb)
    if thisTrial_pic_eval != None:
        for paramName in thisTrial_pic_eval.keys():
            exec(paramName + '= thisTrial_pic_eval.' + paramName)
    
    for thisTrial_pic_eval in trial_pic_eval:
        currentLoop = trial_pic_eval
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_pic_eval.rgb)
        if thisTrial_pic_eval != None:
            for paramName in thisTrial_pic_eval.keys():
                exec(paramName + '= thisTrial_pic_eval.' + paramName)
        
        # ------Prepare to start Routine "eval_pic"-------
        t = 0
        eval_picClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # this is the question it randomly pulls from the .csv file
        pic_q = current_question
        
        # this is added because by having an id of the question
        # where the questions are randomised, we can simply store it
        # later
        q_id = sav_mapping
        rating_2.reset()
        image_2.setImage(pic_q)
        # keep track of which components have finished
        eval_picComponents = [rating_2, image_2, text_49]
        for thisComponent in eval_picComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "eval_pic"-------
        while continueRoutine:
            # get current time
            t = eval_picClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rating_2* updates
            if t >= 0.0 and rating_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                rating_2.tStart = t
                rating_2.frameNStart = frameN  # exact frame index
                rating_2.setAutoDraw(True)
            continueRoutine &= rating_2.noResponse  # a response ends the trial
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            
            # *text_49* updates
            if t >= 0.0 and text_49.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_49.tStart = t
                text_49.frameNStart = frameN  # exact frame index
                text_49.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eval_picComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "eval_pic"-------
        for thisComponent in eval_picComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stor_pic_q.append(rating.getRating())
        # store data for trial_pic_eval (TrialHandler)
        trial_pic_eval.addData('rating_2.response', rating_2.getRating())
        trial_pic_eval.addData('rating_2.rt', rating_2.getRT())
        # the Routine "eval_pic" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_pic_eval_b repeats of 'trial_pic_eval'
    
    # get names of stimulus parameters
    if trial_pic_eval.trialList in ([], [None], None):
        params = []
    else:
        params = trial_pic_eval.trialList[0].keys()
    # save data for this loop
    trial_pic_eval.saveAsExcel(filename + '.xlsx', sheetName='trial_pic_eval',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trial_pic_eval.saveAsText(filename + 'trial_pic_eval.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "est_sal"-------
    t = 0
    est_salClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    est_salComponents = [text_24, key_resp_5, text_29]
    for thisComponent in est_salComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "est_sal"-------
    while continueRoutine:
        # get current time
        t = est_salClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_24* updates
        if t >= 0.0 and text_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_24.tStart = t
            text_24.frameNStart = frameN  # exact frame index
            text_24.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_29* updates
        if t >= 1 and text_29.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_29.tStart = t
            text_29.frameNStart = frameN  # exact frame index
            text_29.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in est_salComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "est_sal"-------
    for thisComponent in est_salComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "est_sal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    juice_types = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('juice_types.csv'),
        seed=None, name='juice_types')
    thisExp.addLoop(juice_types)  # add the loop to the experiment
    thisJuice_type = juice_types.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisJuice_type.rgb)
    if thisJuice_type != None:
        for paramName in thisJuice_type.keys():
            exec(paramName + '= thisJuice_type.' + paramName)
    
    for thisJuice_type in juice_types:
        currentLoop = juice_types
        # abbreviate parameter names if possible (e.g. rgb = thisJuice_type.rgb)
        if thisJuice_type != None:
            for paramName in thisJuice_type.keys():
                exec(paramName + '= thisJuice_type.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        juice_salience = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('juice_salience.csv'),
            seed=None, name='juice_salience')
        thisExp.addLoop(juice_salience)  # add the loop to the experiment
        thisJuice_salience = juice_salience.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisJuice_salience.rgb)
        if thisJuice_salience != None:
            for paramName in thisJuice_salience.keys():
                exec(paramName + '= thisJuice_salience.' + paramName)
        
        for thisJuice_salience in juice_salience:
            currentLoop = juice_salience
            # abbreviate parameter names if possible (e.g. rgb = thisJuice_salience.rgb)
            if thisJuice_salience != None:
                for paramName in thisJuice_salience.keys():
                    exec(paramName + '= thisJuice_salience.' + paramName)
            
            # set up handler to look after randomisation of conditions etc
            dispenser = data.TrialHandler(nReps=run_dispenser, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='dispenser')
            thisExp.addLoop(dispenser)  # add the loop to the experiment
            thisDispenser = dispenser.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDispenser.rgb)
            if thisDispenser != None:
                for paramName in thisDispenser.keys():
                    exec(paramName + '= thisDispenser.' + paramName)
            
            for thisDispenser in dispenser:
                currentLoop = dispenser
                # abbreviate parameter names if possible (e.g. rgb = thisDispenser.rgb)
                if thisDispenser != None:
                    for paramName in thisDispenser.keys():
                        exec(paramName + '= thisDispenser.' + paramName)
                
                # ------Prepare to start Routine "supl_jui"-------
                t = 0
                supl_juiClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                pump = current_pump # fetches information on a random pump it will take 
                                    # randomly takes one of the first three pumps
                # sends pump vol | the initial amount should be set at 1ml
                
                
                #dev.write(pump)
                # after it sends, it should wait a bit 
                #time.sleep(1)
                text_4.setText(pump)
                # keep track of which components have finished
                supl_juiComponents = [text_4]
                for thisComponent in supl_juiComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "supl_jui"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = supl_juiClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *text_4* updates
                    if t >= 0.0 and text_4.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_4.tStart = t
                        text_4.frameNStart = frameN  # exact frame index
                        text_4.setAutoDraw(True)
                    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_4.status == STARTED and t >= frameRemains:
                        text_4.setAutoDraw(False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in supl_juiComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "supl_jui"-------
                for thisComponent in supl_juiComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
                thisExp.nextEntry()
                
            # completed run_dispenser repeats of 'dispenser'
            
            # get names of stimulus parameters
            if dispenser.trialList in ([], [None], None):
                params = []
            else:
                params = dispenser.trialList[0].keys()
            # save data for this loop
            dispenser.saveAsExcel(filename + '.xlsx', sheetName='dispenser',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            dispenser.saveAsText(filename + 'dispenser.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # ------Prepare to start Routine "eval_jui"-------
            t = 0
            eval_juiClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            juice_resp = event.BuilderKeyResponse()
            # this is the question it randomly pulls from the .csv file
            curr_q = current_question
            
            # this is added because by having an id of the question
            # where the questions are randomised, we can simply store it
            # later
            q_id = sav_mapping
            text_30.setText(current_question)
            # keep track of which components have finished
            eval_juiComponents = [juice_resp, text_30, first_2, second_2, third_2, fourth_2, fifth_2, sixth_2, text_31, text_32, text_33, text_34, text_35, text_22]
            for thisComponent in eval_juiComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eval_jui"-------
            while continueRoutine:
                # get current time
                t = eval_juiClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *juice_resp* updates
                if t >= 0.0 and juice_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    juice_resp.tStart = t
                    juice_resp.frameNStart = frameN  # exact frame index
                    juice_resp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(juice_resp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if juice_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        juice_resp.keys = theseKeys[-1]  # just the last key pressed
                        juice_resp.rt = juice_resp.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                
                # *text_30* updates
                if t >= 0.0 and text_30.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_30.tStart = t
                    text_30.frameNStart = frameN  # exact frame index
                    text_30.setAutoDraw(True)
                
                # *first_2* updates
                if t >= 0.0 and first_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    first_2.tStart = t
                    first_2.frameNStart = frameN  # exact frame index
                    first_2.setAutoDraw(True)
                
                # *second_2* updates
                if t >= 0.0 and second_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    second_2.tStart = t
                    second_2.frameNStart = frameN  # exact frame index
                    second_2.setAutoDraw(True)
                
                # *third_2* updates
                if t >= 0.0 and third_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    third_2.tStart = t
                    third_2.frameNStart = frameN  # exact frame index
                    third_2.setAutoDraw(True)
                
                # *fourth_2* updates
                if t >= 0.0 and fourth_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fourth_2.tStart = t
                    fourth_2.frameNStart = frameN  # exact frame index
                    fourth_2.setAutoDraw(True)
                
                # *fifth_2* updates
                if t >= 0.0 and fifth_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fifth_2.tStart = t
                    fifth_2.frameNStart = frameN  # exact frame index
                    fifth_2.setAutoDraw(True)
                
                # *sixth_2* updates
                if t >= 0.0 and sixth_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    sixth_2.tStart = t
                    sixth_2.frameNStart = frameN  # exact frame index
                    sixth_2.setAutoDraw(True)
                
                # *text_31* updates
                if t >= 0.0 and text_31.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_31.tStart = t
                    text_31.frameNStart = frameN  # exact frame index
                    text_31.setAutoDraw(True)
                
                # *text_32* updates
                if t >= 0.0 and text_32.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_32.tStart = t
                    text_32.frameNStart = frameN  # exact frame index
                    text_32.setAutoDraw(True)
                
                # *text_33* updates
                if t >= 0.0 and text_33.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_33.tStart = t
                    text_33.frameNStart = frameN  # exact frame index
                    text_33.setAutoDraw(True)
                
                # *text_34* updates
                if t >= 0.0 and text_34.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_34.tStart = t
                    text_34.frameNStart = frameN  # exact frame index
                    text_34.setAutoDraw(True)
                
                # *text_35* updates
                if t >= 0.0 and text_35.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_35.tStart = t
                    text_35.frameNStart = frameN  # exact frame index
                    text_35.setAutoDraw(True)
                
                # *text_22* updates
                if t >= 0.0 and text_22.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_22.tStart = t
                    text_22.frameNStart = frameN  # exact frame index
                    text_22.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in eval_juiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eval_jui"-------
            for thisComponent in eval_juiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if juice_resp.keys in ['', [], None]:  # No response was made
                juice_resp.keys=None
            juice_salience.addData('juice_resp.keys',juice_resp.keys)
            if juice_resp.keys != None:  # we had a response
                juice_salience.addData('juice_resp.rt', juice_resp.rt)
            
            # the Routine "eval_jui" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "jui_feed"-------
            t = 0
            jui_feedClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            if juice_resp.keys == '1':
                opt_1 = [1, 0.84, 0.0]
                opt_2, opt_3, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2]
            
            elif juice_resp.keys == '2':
                opt_2 = [1, 0.84, 0.0]
                opt_1, opt_3, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2]
            
            elif juice_resp.keys == '3':
                opt_3 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2]
            
            elif juice_resp.keys == '4':
                opt_4 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_3, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2]
            
            elif juice_resp.keys == '5':
                opt_5 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_3, opt_4, opt_6 = [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2]
            
            elif juice_resp.keys == '6':
                opt_6 = [1, 0.84, 0.0]
                opt_1, opt_2, opt_3, opt_4, opt_5 = [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2], \
                                              [0.2, 0.2, 0.2]
            
            # current pump
            jui = str(int(pump.encode('hex'), 16))[-1]
            stor_jui_eval[jui].append(int(juice_resp.keys))
            
            if juice_trial == 1:
                run_dispenser = 0
            
            juice_trial += 1
            
            if juice_trial == 4:
                run_dispenser = 1
                juice_trial = 1
            first_feedback_2.setFillColor(opt_1)
            second_feedback_2.setFillColor(opt_2)
            third_feedback_2.setFillColor(opt_3)
            fourth_feedback_2.setFillColor(opt_4)
            fifth_feedback_2.setFillColor(opt_5)
            sixth_feedback_2.setFillColor(opt_6)
            # keep track of which components have finished
            jui_feedComponents = [first_feedback_2, second_feedback_2, third_feedback_2, fourth_feedback_2, fifth_feedback_2, sixth_feedback_2, text_36, text_37, text_38, text_39, text_40, text_25]
            for thisComponent in jui_feedComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "jui_feed"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = jui_feedClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *first_feedback_2* updates
                if t >= 0.0 and first_feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    first_feedback_2.tStart = t
                    first_feedback_2.frameNStart = frameN  # exact frame index
                    first_feedback_2.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if first_feedback_2.status == STARTED and t >= frameRemains:
                    first_feedback_2.setAutoDraw(False)
                
                # *second_feedback_2* updates
                if t >= 0.0 and second_feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    second_feedback_2.tStart = t
                    second_feedback_2.frameNStart = frameN  # exact frame index
                    second_feedback_2.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if second_feedback_2.status == STARTED and t >= frameRemains:
                    second_feedback_2.setAutoDraw(False)
                
                # *third_feedback_2* updates
                if t >= 0.0 and third_feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    third_feedback_2.tStart = t
                    third_feedback_2.frameNStart = frameN  # exact frame index
                    third_feedback_2.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if third_feedback_2.status == STARTED and t >= frameRemains:
                    third_feedback_2.setAutoDraw(False)
                
                # *fourth_feedback_2* updates
                if t >= 0.0 and fourth_feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fourth_feedback_2.tStart = t
                    fourth_feedback_2.frameNStart = frameN  # exact frame index
                    fourth_feedback_2.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if fourth_feedback_2.status == STARTED and t >= frameRemains:
                    fourth_feedback_2.setAutoDraw(False)
                
                # *fifth_feedback_2* updates
                if t >= 0.0 and fifth_feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fifth_feedback_2.tStart = t
                    fifth_feedback_2.frameNStart = frameN  # exact frame index
                    fifth_feedback_2.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if fifth_feedback_2.status == STARTED and t >= frameRemains:
                    fifth_feedback_2.setAutoDraw(False)
                
                # *sixth_feedback_2* updates
                if t >= 0.0 and sixth_feedback_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    sixth_feedback_2.tStart = t
                    sixth_feedback_2.frameNStart = frameN  # exact frame index
                    sixth_feedback_2.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if sixth_feedback_2.status == STARTED and t >= frameRemains:
                    sixth_feedback_2.setAutoDraw(False)
                
                # *text_36* updates
                if t >= 0.0 and text_36.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_36.tStart = t
                    text_36.frameNStart = frameN  # exact frame index
                    text_36.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_36.status == STARTED and t >= frameRemains:
                    text_36.setAutoDraw(False)
                
                # *text_37* updates
                if t >= 0.0 and text_37.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_37.tStart = t
                    text_37.frameNStart = frameN  # exact frame index
                    text_37.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_37.status == STARTED and t >= frameRemains:
                    text_37.setAutoDraw(False)
                
                # *text_38* updates
                if t >= 0.0 and text_38.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_38.tStart = t
                    text_38.frameNStart = frameN  # exact frame index
                    text_38.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_38.status == STARTED and t >= frameRemains:
                    text_38.setAutoDraw(False)
                
                # *text_39* updates
                if t >= 0.0 and text_39.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_39.tStart = t
                    text_39.frameNStart = frameN  # exact frame index
                    text_39.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_39.status == STARTED and t >= frameRemains:
                    text_39.setAutoDraw(False)
                
                # *text_40* updates
                if t >= 0.0 and text_40.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_40.tStart = t
                    text_40.frameNStart = frameN  # exact frame index
                    text_40.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_40.status == STARTED and t >= frameRemains:
                    text_40.setAutoDraw(False)
                if text_40.status == STARTED:  # only update if drawing
                    text_40.setPos([0.4, -0.58], log=False)
                
                # *text_25* updates
                if t >= 0.0 and text_25.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_25.tStart = t
                    text_25.frameNStart = frameN  # exact frame index
                    text_25.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_25.status == STARTED and t >= frameRemains:
                    text_25.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jui_feedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "jui_feed"-------
            for thisComponent in jui_feedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #act_vol = int(pump.encode('hex'), 16)
            
            # water
            #dev.write()
            
            thisExp.nextEntry()
            
        # completed 1 repeats of 'juice_salience'
        
        # get names of stimulus parameters
        if juice_salience.trialList in ([], [None], None):
            params = []
        else:
            params = juice_salience.trialList[0].keys()
        # save data for this loop
        juice_salience.saveAsExcel(filename + '.xlsx', sheetName='juice_salience',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        juice_salience.saveAsText(filename + 'juice_salience.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'juice_types'
    
    # get names of stimulus parameters
    if juice_types.trialList in ([], [None], None):
        params = []
    else:
        params = juice_types.trialList[0].keys()
    # save data for this loop
    juice_types.saveAsExcel(filename + '.xlsx', sheetName='juice_types',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    juice_types.saveAsText(filename + 'juice_types.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "jui_out"-------
    t = 0
    jui_outClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    summed = []
    for key, values in zip(stor_jui_eval.keys(), stor_jui_eval.values()):
        tmp_val = 0
        for value in values:
            tmp_val += value
        summed.append((key, tmp_val/3)) # because we ask them 3 questions 
    
    # should automatically pick a random element
    fav_juice = max(summed, key=lambda item:item[1])[0] # take the first element
    
    
    
    
    
    
    
    text_45.setText(fav_juice)
    # keep track of which components have finished
    jui_outComponents = [text_41, text_45]
    for thisComponent in jui_outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jui_out"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = jui_outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_41* updates
        if t >= 0.0 and text_41.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_41.tStart = t
            text_41.frameNStart = frameN  # exact frame index
            text_41.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_41.status == STARTED and t >= frameRemains:
            text_41.setAutoDraw(False)
        
        # *text_45* updates
        if t >= 0.0 and text_45.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_45.tStart = t
            text_45.frameNStart = frameN  # exact frame index
            text_45.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_45.status == STARTED and t >= frameRemains:
            text_45.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jui_outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jui_out"-------
    for thisComponent in jui_outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "phy_mvc"-------
    t = 0
    phy_mvcClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    phy_mvcComponents = [text_28, key_resp_4]
    for thisComponent in phy_mvcComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "phy_mvc"-------
    while continueRoutine:
        # get current time
        t = phy_mvcClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_28* updates
        if t >= 0.0 and text_28.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_28.tStart = t
            text_28.frameNStart = frameN  # exact frame index
            text_28.setAutoDraw(True)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phy_mvcComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phy_mvc"-------
    for thisComponent in phy_mvcComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "phy_mvc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed run_debug repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
        background_image.setAutoDraw(True)
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
        key_resp_3 = event.BuilderKeyResponse()
        # keep track of which components have finished
        real_annComponents = [background_poly3, text_26, text_27, key_resp_3]
        for thisComponent in real_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "real_ann"-------
        while continueRoutine:
            # get current time
            t = real_annClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_poly3* updates
            if t >= 0.0 and background_poly3.status == NOT_STARTED:
                # keep track of start time/frame for later
                background_poly3.tStart = t
                background_poly3.frameNStart = frameN  # exact frame index
                background_poly3.setAutoDraw(True)
            
            # *text_26* updates
            if t >= 0.0 and text_26.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_26.tStart = t
                text_26.frameNStart = frameN  # exact frame index
                text_26.setAutoDraw(True)
            
            # *text_27* updates
            if t >= 1 and text_27.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_27.tStart = t
                text_27.frameNStart = frameN  # exact frame index
                text_27.setAutoDraw(True)
            
            # *key_resp_3* updates
            if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
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
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys=None
        real_info.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            real_info.addData('key_resp_3.rt', key_resp_3.rt)
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
        
        # ------Prepare to start Routine "iti"-------
        t = 0
        itiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
        
        # denotes current first trial num of a new vector of questions
        # following each trial
        sub_trial = 1
        
        
        # keep track of which components have finished
        itiComponents = [cross_sign]
        for thisComponent in itiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "iti"-------
        while continueRoutine:
            # get current time
            t = itiClock.getTime()
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
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti"-------
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rew_ann"-------
        t = 0
        rew_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        if reward_type == 1:
            curr_reward = juice_rew
        else:
            curr_reward = pound_rew
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
        # run_ev, run_effort, run_flanker 
        if type == 2:
            run_ev, run_flanker, run_effort, run_rew = 1, 0, 0, 0
        elif type == 3:
            run_effort, run_ev, run_flanker, run_rew = 1, 0, 0, 0
            abs_trial += 1
        elif type == 4:
            abs_trial += 1
            run_effort, run_flanker, run_ev, run_rew = 1, 1, 0, 0
        elif type == 5:
            run_flanker, run_ev, run_effort, run_rew = 1, 0, 0, 0
            abs_trial += 1
        elif type == 6:
            run_flanker, run_effort, run_ev, run_rew = 1, 0, 0, 0
            abs_trial += 1
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
    exp_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('flanker_trials.csv'),
        seed=None, name='exp_loop')
    thisExp.addLoop(exp_loop)  # add the loop to the experiment
    thisExp_loop = exp_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
    if thisExp_loop != None:
        for paramName in thisExp_loop.keys():
            exec(paramName + '= thisExp_loop.' + paramName)
    
    for thisExp_loop in exp_loop:
        currentLoop = exp_loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
        if thisExp_loop != None:
            for paramName in thisExp_loop.keys():
                exec(paramName + '= thisExp_loop.' + paramName)
        
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
            
            # ------Prepare to start Routine "iti"-------
            t = 0
            itiClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
            
            # denotes current first trial num of a new vector of questions
            # following each trial
            sub_trial = 1
            
            
            # keep track of which components have finished
            itiComponents = [cross_sign]
            for thisComponent in itiComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "iti"-------
            while continueRoutine:
                # get current time
                t = itiClock.getTime()
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
                for thisComponent in itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "iti"-------
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            ev_loop = data.TrialHandler(nReps=1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('ev.csv'),
                seed=None, name='ev_loop')
            thisExp.addLoop(ev_loop)  # add the loop to the experiment
            thisEv_loop = ev_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisEv_loop.rgb)
            if thisEv_loop != None:
                for paramName in thisEv_loop.keys():
                    exec(paramName + '= thisEv_loop.' + paramName)
            
            for thisEv_loop in ev_loop:
                currentLoop = ev_loop
                # abbreviate parameter names if possible (e.g. rgb = thisEv_loop.rgb)
                if thisEv_loop != None:
                    for paramName in thisEv_loop.keys():
                        exec(paramName + '= thisEv_loop.' + paramName)
                
                # ------Prepare to start Routine "ev_prom"-------
                t = 0
                ev_promClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                ev_resp = event.BuilderKeyResponse()
                # this is the question it randomly pulls from the .csv file
                curr_q = current_question
                
                # this is added because by having an id of the question
                # where the questions are randomised, we can simply store it
                # later
                q_id = sav_mapping
                text_5.setText(current_question)
                # keep track of which components have finished
                ev_promComponents = [ev_resp, text_5, first, second, third, fourth, fifth, sixth, text_12, text_13, text_14, text_15, text_16, text_47]
                for thisComponent in ev_promComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "ev_prom"-------
                while continueRoutine:
                    # get current time
                    t = ev_promClock.getTime()
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
                        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6'])
                        
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
                    
                    # *sixth* updates
                    if t >= 0.0 and sixth.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        sixth.tStart = t
                        sixth.frameNStart = frameN  # exact frame index
                        sixth.setAutoDraw(True)
                    
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
                    
                    # *text_47* updates
                    if t >= 0.0 and text_47.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_47.tStart = t
                        text_47.frameNStart = frameN  # exact frame index
                        text_47.setAutoDraw(True)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in ev_promComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "ev_prom"-------
                for thisComponent in ev_promComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if ev_resp.keys in ['', [], None]:  # No response was made
                    ev_resp.keys=None
                ev_loop.addData('ev_resp.keys',ev_resp.keys)
                if ev_resp.keys != None:  # we had a response
                    ev_loop.addData('ev_resp.rt', ev_resp.rt)
                
                # the Routine "ev_prom" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "ev_feed"-------
                t = 0
                ev_feedClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(0.500000)
                # update component parameters for each repeat
                if ev_resp.keys == '1':
                    opt_1 = [1, 0.84, 0.0]
                    opt_2, opt_3, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2]
                
                elif ev_resp.keys == '2':
                    opt_2 = [1, 0.84, 0.0]
                    opt_1, opt_3, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2]
                
                elif ev_resp.keys == '3':
                    opt_3 = [1, 0.84, 0.0]
                    opt_1, opt_2, opt_4, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2]
                
                elif ev_resp.keys == '4':
                    opt_4 = [1, 0.84, 0.0]
                    opt_1, opt_2, opt_3, opt_5, opt_6 = [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2]
                
                elif ev_resp.keys == '5':
                    opt_5 = [1, 0.84, 0.0]
                    opt_1, opt_2, opt_3, opt_4, opt_6 = [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2]
                
                elif ev_resp.keys == '6':
                    opt_6 = [1, 0.84, 0.0]
                    opt_1, opt_2, opt_3, opt_4, opt_5 = [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2], \
                                                  [0.2, 0.2, 0.2]
                
                stor_ev[str(sub_trial)] = [q_id, int(ev_resp.keys), ev_resp.rt]
                
                
                
                
                first_feedback.setFillColor(opt_1)
                second_feedback.setFillColor(opt_2)
                third_feedback.setFillColor(opt_3)
                fourth_feedback.setFillColor(opt_4)
                fifth_feedback.setFillColor(opt_5)
                sixth_feedback.setFillColor(opt_6)
                # keep track of which components have finished
                ev_feedComponents = [first_feedback, second_feedback, third_feedback, fourth_feedback, fifth_feedback, sixth_feedback, text_17, text_18, text_19, text_20, text_21, text_46]
                for thisComponent in ev_feedComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "ev_feed"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = ev_feedClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *first_feedback* updates
                    if t >= 0.0 and first_feedback.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        first_feedback.tStart = t
                        first_feedback.frameNStart = frameN  # exact frame index
                        first_feedback.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if first_feedback.status == STARTED and t >= frameRemains:
                        first_feedback.setAutoDraw(False)
                    
                    # *second_feedback* updates
                    if t >= 0.0 and second_feedback.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        second_feedback.tStart = t
                        second_feedback.frameNStart = frameN  # exact frame index
                        second_feedback.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if second_feedback.status == STARTED and t >= frameRemains:
                        second_feedback.setAutoDraw(False)
                    
                    # *third_feedback* updates
                    if t >= 0.0 and third_feedback.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        third_feedback.tStart = t
                        third_feedback.frameNStart = frameN  # exact frame index
                        third_feedback.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if third_feedback.status == STARTED and t >= frameRemains:
                        third_feedback.setAutoDraw(False)
                    
                    # *fourth_feedback* updates
                    if t >= 0.0 and fourth_feedback.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        fourth_feedback.tStart = t
                        fourth_feedback.frameNStart = frameN  # exact frame index
                        fourth_feedback.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if fourth_feedback.status == STARTED and t >= frameRemains:
                        fourth_feedback.setAutoDraw(False)
                    
                    # *fifth_feedback* updates
                    if t >= 0.0 and fifth_feedback.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        fifth_feedback.tStart = t
                        fifth_feedback.frameNStart = frameN  # exact frame index
                        fifth_feedback.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if fifth_feedback.status == STARTED and t >= frameRemains:
                        fifth_feedback.setAutoDraw(False)
                    
                    # *sixth_feedback* updates
                    if t >= 0.0 and sixth_feedback.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        sixth_feedback.tStart = t
                        sixth_feedback.frameNStart = frameN  # exact frame index
                        sixth_feedback.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if sixth_feedback.status == STARTED and t >= frameRemains:
                        sixth_feedback.setAutoDraw(False)
                    
                    # *text_17* updates
                    if t >= 0.0 and text_17.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_17.tStart = t
                        text_17.frameNStart = frameN  # exact frame index
                        text_17.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_17.status == STARTED and t >= frameRemains:
                        text_17.setAutoDraw(False)
                    
                    # *text_18* updates
                    if t >= 0.0 and text_18.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_18.tStart = t
                        text_18.frameNStart = frameN  # exact frame index
                        text_18.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_18.status == STARTED and t >= frameRemains:
                        text_18.setAutoDraw(False)
                    
                    # *text_19* updates
                    if t >= 0.0 and text_19.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_19.tStart = t
                        text_19.frameNStart = frameN  # exact frame index
                        text_19.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_19.status == STARTED and t >= frameRemains:
                        text_19.setAutoDraw(False)
                    
                    # *text_20* updates
                    if t >= 0.0 and text_20.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_20.tStart = t
                        text_20.frameNStart = frameN  # exact frame index
                        text_20.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_20.status == STARTED and t >= frameRemains:
                        text_20.setAutoDraw(False)
                    
                    # *text_21* updates
                    if t >= 0.0 and text_21.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_21.tStart = t
                        text_21.frameNStart = frameN  # exact frame index
                        text_21.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_21.status == STARTED and t >= frameRemains:
                        text_21.setAutoDraw(False)
                    
                    # *text_46* updates
                    if t >= 0.0 and text_46.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_46.tStart = t
                        text_46.frameNStart = frameN  # exact frame index
                        text_46.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_46.status == STARTED and t >= frameRemains:
                        text_46.setAutoDraw(False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in ev_feedComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "ev_feed"-------
                for thisComponent in ev_feedComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # run_ev, run_effort, run_stroop 
                #if type == 1:
                #    abs_trial += 1
                if type == 2:
                    run_ev, run_flanker, run_effort, run_rew = 0, 1, 0, 0
                elif type == 3:
                    run_effort, run_ev, run_flanker, run_rew = 0, 0, 1, 0
                elif type == 4:
                    run_effort, run_flanker, run_ev, run_rew = 0, 0, 0, 1
                
                    abs_trial += 1
                    run_prac = 0
                    if abs_trial == num_pract:
                        run_real = 1
                
                
                elif type == 5:
                    run_flanker, run_ev, run_effort, run_rew = 0, 0, 1, 0
                elif type == 6:
                    run_flanker, run_effort, run_ev, run_rew = 0, 0, 0, 1
                
                    abs_trial += 1
                    run_prac = 0
                    if abs_trial == num_pract:
                        run_real = 1
                
                
                
                
                # for EV our data structure looks like this:
                # 'trial':[question_id, response, rt]
                
                
                sub_trial += 1
                thisExp.nextEntry()
                
            # completed 1 repeats of 'ev_loop'
            
            # get names of stimulus parameters
            if ev_loop.trialList in ([], [None], None):
                params = []
            else:
                params = ev_loop.trialList[0].keys()
            # save data for this loop
            ev_loop.saveAsExcel(filename + '.xlsx', sheetName='ev_loop',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            ev_loop.saveAsText(filename + 'ev_loop.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # ------Prepare to start Routine "ev_save"-------
            t = 0
            ev_saveClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # we sort and order the keys because they correspond to the trials 
            
            # saves to participant file
            save_to_file(dataset, curr_reward, stor_ev, abs_trial, stor_eff, stor_main, stor_gust, [4, 6])
            
            # keep track of which components have finished
            ev_saveComponents = []
            for thisComponent in ev_saveComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "ev_save"-------
            while continueRoutine:
                # get current time
                t = ev_saveClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ev_saveComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ev_save"-------
            for thisComponent in ev_saveComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "ev_save" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
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
            
            # ------Prepare to start Routine "eff_prom"-------
            t = 0
            eff_promClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            eff_promComponents = [text_23]
            for thisComponent in eff_promComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_prom"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = eff_promClock.getTime()
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
                for thisComponent in eff_promComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_prom"-------
            for thisComponent in eff_promComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # ------Prepare to start Routine "iti"-------
            t = 0
            itiClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            curr_t = min(3.8, max(0.6, random.gauss(1, 0.5)))
            
            # denotes current first trial num of a new vector of questions
            # following each trial
            sub_trial = 1
            
            
            # keep track of which components have finished
            itiComponents = [cross_sign]
            for thisComponent in itiComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "iti"-------
            while continueRoutine:
                # get current time
                t = itiClock.getTime()
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
                for thisComponent in itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "iti"-------
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "iti" was not non-slip safe, so reset the non-slip timer
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
                
                # ------Prepare to start Routine "eff_tas"-------
                t = 0
                eff_tasClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                
                
                # let's say we store participant data here. 
                # cur_contr - we would get this information back from the dynamometer
                # mvc - denotes the maximal values we would get back from the dynamometer
                
                curr_contr_perc = int((curr_contr - mvc)/100)*100
                
                if curr_contr_perc >= 80:
                    rew_multpl = 1.2
                elif 50 <= curr_contr_perc <= 79:
                    rew_multpl = 1
                elif 25 <= curr_contr_perc <= 50:
                    rew_multpl = 0.8
                
                
                # keep track of which components have finished
                eff_tasComponents = [text_11]
                for thisComponent in eff_tasComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "eff_tas"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = eff_tasClock.getTime()
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
                    for thisComponent in eff_tasComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "eff_tas"-------
                for thisComponent in eff_tasComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
                # save data on a per trial basis
                stor_eff[str(abs_trial)] = [curr_contr, rew_multpl]
                
                
                # run_ev, run_effort, run_stroop 
                if type == 2:
                    run_ev, run_flanker, run_effort, run_rew = 0, 0, 0, 1
                    
                    abs_trial += 1
                    run_prac = 0
                    if abs_trial == num_pract:
                        run_real = 1
                
                elif type == 3:
                    run_prac = 0 # this needs to be here in order to prevent
                                 # it from popping up unnecessarily 
                    run_effort, run_ev, run_flanker, run_rew = 0, 1, 0, 0
                elif type == 4:
                    run_effort, run_flanker, run_ev, run_rew = 0, 1, 0, 0
                elif type == 5:
                    run_flanker, run_ev, run_effort, run_rew = 0, 0, 0, 1
                    
                    abs_trial += 1
                    run_prac = 0
                    if abs_trial == num_pract:
                        run_real = 1
                
                elif type == 6:
                    run_flanker, run_effort, run_ev, run_rew = 0, 0, 1, 0
                
                # here we would get the response from an individual in terms of 
                # the exerted effort. the question is now if this will be 
                # dynamic or just a static value in the end 
                
                # we will make it such that the data on the ev will be automatically repeated
                # the good thing about that is that it will be very easy to analyse in both python and r
                
                save_to_file(dataset, curr_reward, stor_ev, abs_trial, stor_eff, stor_main, stor_gust, [2, 5])
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
        flanker_role = data.TrialHandler(nReps=run_flanker, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='flanker_role')
        thisExp.addLoop(flanker_role)  # add the loop to the experiment
        thisFlanker_role = flanker_role.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFlanker_role.rgb)
        if thisFlanker_role != None:
            for paramName in thisFlanker_role.keys():
                exec(paramName + '= thisFlanker_role.' + paramName)
        
        for thisFlanker_role in flanker_role:
            currentLoop = flanker_role
            # abbreviate parameter names if possible (e.g. rgb = thisFlanker_role.rgb)
            if thisFlanker_role != None:
                for paramName in thisFlanker_role.keys():
                    exec(paramName + '= thisFlanker_role.' + paramName)
            
            # ------Prepare to start Routine "beg_fix"-------
            t = 0
            beg_fixClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            curr_t = min(2.5, max(0.5, random.gauss(2, 0.1)))
            main_cue = cue
            curr_diff_lev = diff_lev[0]
            
            if curr_diff_lev == 'low':
                cue_timing = 0.4
                resp_wind = 0.6
                feed_sound = 'lowest.wav'
            elif curr_diff_lev == 'high':
                cue_timing = 0.2
                resp_wind =  0.4
                feed_sound = 'highest.wav'
            else:
                cue_timing = 0.3
                resp_wind = 0.5
                feed_sound = 'medium.wav'
            
            resp_fin = 5
            # keep track of which components have finished
            beg_fixComponents = [text]
            for thisComponent in beg_fixComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "beg_fix"-------
            while continueRoutine:
                # get current time
                t = beg_fixClock.getTime()
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
                for thisComponent in beg_fixComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "beg_fix"-------
            for thisComponent in beg_fixComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "beg_fix" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "tar_ann"-------
            t = 0
            tar_annClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            main_image.setImage(main_cue)
            main_resp = event.BuilderKeyResponse()
            # keep track of which components have finished
            tar_annComponents = [main_image, main_resp]
            for thisComponent in tar_annComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "tar_ann"-------
            while continueRoutine:
                # get current time
                t = tar_annClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *main_image* updates
                if t >= 0.0 and main_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    main_image.tStart = t
                    main_image.frameNStart = frameN  # exact frame index
                    main_image.setAutoDraw(True)
                frameRemains = 0.0 + resp_wind- win.monitorFramePeriod * 0.75  # most of one frame period left
                if main_image.status == STARTED and t >= frameRemains:
                    main_image.setAutoDraw(False)
                
                # *main_resp* updates
                if t >= resp_wind and main_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    main_resp.tStart = t
                    main_resp.frameNStart = frameN  # exact frame index
                    main_resp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(main_resp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                frameRemains = resp_wind + resp_wind+resp_fin- win.monitorFramePeriod * 0.75  # most of one frame period left
                if main_resp.status == STARTED and t >= frameRemains:
                    main_resp.status = STOPPED
                if main_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['f', 'k'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        main_resp.keys = theseKeys[-1]  # just the last key pressed
                        main_resp.rt = main_resp.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in tar_annComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "tar_ann"-------
            for thisComponent in tar_annComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if main_resp.keys in ['', [], None]:  # No response was made
                main_resp.keys=None
            flanker_role.addData('main_resp.keys',main_resp.keys)
            if main_resp.keys != None:  # we had a response
                flanker_role.addData('main_resp.rt', main_resp.rt)
            # the Routine "tar_ann" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "main_feed"-------
            t = 0
            main_feedClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.100000)
            # update component parameters for each repeat
            # keep track of which components have finished
            main_feedComponents = [feed_info]
            for thisComponent in main_feedComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "main_feed"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = main_feedClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feed_info* updates
                if t >= 0.0 and feed_info.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    feed_info.tStart = t
                    feed_info.frameNStart = frameN  # exact frame index
                    feed_info.setAutoDraw(True)
                frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if feed_info.status == STARTED and t >= frameRemains:
                    feed_info.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in main_feedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "main_feed"-------
            for thisComponent in main_feedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # ------Prepare to start Routine "comp"-------
            t = 0
            compClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            if  main_resp.keys == left_resp:
                part_resp = 1 # left
            elif main_resp.keys == right_resp:
                part_resp = 2 # right
            else: # no go trial
                part_resp = 3
            
            # make sure this is correct
            # if participant does respond and was suppose to respond and responds correctly
            if part_resp == 1 and correct_response == 1 or \
                part_resp == 2 and correct_response == 2:
                computed_resp = 1 # hit
            
            # if participant does respond and was supposed to respond and responds incorrectly
            elif part_resp == 1 and correct_response == 2 or \
                part_resp == 2 and correct_response == 1:
                computed_resp = 2 # incorrect response due to pressing incorrect key 
            
            # if participant does respond and was not supposed to respond
            elif (part_resp == 1 or part_resp == 2) and correct_response == 3:
                computed_resp = 3 # false alarm
            
            # if participant does not respond and was not supposed to respond
            elif part_resp == 3 and correct_response == 3:
                computed_resp = 0 # correct rejection 
            
            # if participant does not respond and was supposed to respond 
            elif part_resp == 3 and correct_response != 3:
                computed_resp = 4 # miss
            
            # remove this later
            act_pump, act_pump_nr, act_vol = 0, 0, 0
            # keep track of which components have finished
            compComponents = []
            for thisComponent in compComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "comp"-------
            while continueRoutine:
                # get current time
                t = compClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in compComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "comp"-------
            for thisComponent in compComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if gust_connected == 1:
                if current_rew == juice_rew and \
                   computed_resp == 1 or computed_resp == 0:
            
                    dev.write('\13')
                    amount = str(int(pump_vol['2500']) * rew_multpl) # this needs to be changed obvs.
                    dev.write(amount)
            
                    dev.write('\1') # send juice squirt
                    gus_fed = dev.readlines()
            
                    obtained_rew = str(amount) + 'units of juice'
            
                elif current_rew == pound_rew and \
                    computed_resp == 1 or computed_resp == 0:
                        obtained_rew = str(base_rew*rew_multpl) + 'pence'
                elif computed_resp == 2 or \
                     computed_resp == 3 or \
                     computed_resp == 4:
                        vol = 0
                        obtained_rew = 'nothing'
                    
                if current_rew == juice_rew:
                    # we parse the feedback - we can convert from hexadecimal here 
                    gus_fed = gus_fed[0]
                    if len(gus_fed) == 3: # we know that if the length is 3 then it sent extra information
                        act_pump = gus_fed[0] # because the default setting is to send information on 1ml
                        act_pump_nr = gus_fed[1]
                        act_vol = int(gustaf_feedback[2].encode('hex'), 16)*1000  
                    else:
                        act_pump = gus_fed[0]
                        act_pump_nr = gus_fed[1]
                        act_vol = 1000
                else:
                    act_pump, act_pump_nr, act_vol = 0, 0, 0
            
            
            # save data on a per trial basis
            str_abs_t = str(abs_trial)
            
            stor_main[str_abs_t] = [cue, cond, computed_resp, main_resp.rt, obtained_rew]
            stor_gust[str_abs_t] = [act_pump, act_pump_nr, act_vol]
            
            
            save_to_file(dataset, curr_reward, stor_ev, abs_trial, stor_eff, stor_main, stor_gust, [1, 3])
            
            # run_ev, run_effort, run_flanker 
            if type == 1:
                abs_trial += 1
                run_prac = 0
                if abs_trial == num_pract:
                    run_real = 1
            
            if type == 2:
                run_ev, run_effort, run_flanker, run_rew = 0, 1, 0, 0
            elif type == 3:
                run_effort, run_ev, run_flanker, run_rew = 0, 0, 0, 1
                
                abs_trial += 1
                run_prac = 0
                if abs_trial == num_pract:
                    run_real = 1
            
            elif type == 4:
                run_effort, run_flanker, run_ev, run_rew = 0, 0, 1, 0
            elif type == 5:
                run_flanker, run_ev, run_effort, run_rew = 0, 1, 0, 0
            elif type == 6:
                run_flanker, run_effort, run_ev, run_rew = 0, 1, 0, 0
            
            
            # the Routine "comp" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "tar_feed"-------
            t = 0
            tar_feedClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            text_6.setText(obtained_rew)
            
            # keep track of which components have finished
            tar_feedComponents = [text_3, text_6]
            for thisComponent in tar_feedComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "tar_feed"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = tar_feedClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_3* updates
                if t >= 0.0 and text_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_3.tStart = t
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_3.status == STARTED and t >= frameRemains:
                    text_3.setAutoDraw(False)
                
                # *text_6* updates
                if t >= 0.0 and text_6.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_6.tStart = t
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_6.status == STARTED and t >= frameRemains:
                    text_6.setAutoDraw(False)
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in tar_feedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "tar_feed"-------
            for thisComponent in tar_feedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            thisExp.nextEntry()
            
        # completed run_flanker repeats of 'flanker_role'
        
        # get names of stimulus parameters
        if flanker_role.trialList in ([], [None], None):
            params = []
        else:
            params = flanker_role.trialList[0].keys()
        # save data for this loop
        flanker_role.saveAsExcel(filename + '.xlsx', sheetName='flanker_role',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        flanker_role.saveAsText(filename + 'flanker_role.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'exp_loop'
    
    # get names of stimulus parameters
    if exp_loop.trialList in ([], [None], None):
        params = []
    else:
        params = exp_loop.trialList[0].keys()
    # save data for this loop
    exp_loop.saveAsExcel(filename + '.xlsx', sheetName='exp_loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    exp_loop.saveAsText(filename + 'exp_loop.csv', delim=',',
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

# ------Prepare to start Routine "juice_eval"-------
t = 0
juice_evalClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

juice_valuation = event.BuilderKeyResponse()
# keep track of which components have finished
juice_evalComponents = [text_48, juice_valuation, text_50]
for thisComponent in juice_evalComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "juice_eval"-------
while continueRoutine:
    # get current time
    t = juice_evalClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    tmp_key = juice_valuation.keys
    
    
    response += tmp_key
    
    # *text_48* updates
    if t >= 0.0 and text_48.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_48.tStart = t
        text_48.frameNStart = frameN  # exact frame index
        text_48.setAutoDraw(True)
    
    # *juice_valuation* updates
    if t >= 0.0 and juice_valuation.status == NOT_STARTED:
        # keep track of start time/frame for later
        juice_valuation.tStart = t
        juice_valuation.frameNStart = frameN  # exact frame index
        juice_valuation.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(juice_valuation.clock.reset)  # t=0 on next screen flip
    if juice_valuation.status == STARTED:
        theseKeys = event.getKeys(keyList=['all'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            juice_valuation.keys = theseKeys[-1]  # just the last key pressed
            juice_valuation.rt = juice_valuation.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_50* updates
    if t >= 0.0 and text_50.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_50.tStart = t
        text_50.frameNStart = frameN  # exact frame index
        text_50.setAutoDraw(True)
    if text_50.status == STARTED:  # only update if drawing
        text_50.setText(response, log=False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in juice_evalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "juice_eval"-------
for thisComponent in juice_evalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if juice_valuation.keys in ['', [], None]:  # No response was made
    juice_valuation.keys=None
thisExp.addData('juice_valuation.keys',juice_valuation.keys)
if juice_valuation.keys != None:  # we had a response
    thisExp.addData('juice_valuation.rt', juice_valuation.rt)
thisExp.nextEntry()
# the Routine "juice_eval" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_pic_eval_2 = data.TrialHandler(nReps=run_pic_eval_e, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic_rating.csv'),
    seed=None, name='trial_pic_eval_2')
thisExp.addLoop(trial_pic_eval_2)  # add the loop to the experiment
thisTrial_pic_eval_2 = trial_pic_eval_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_pic_eval_2.rgb)
if thisTrial_pic_eval_2 != None:
    for paramName in thisTrial_pic_eval_2.keys():
        exec(paramName + '= thisTrial_pic_eval_2.' + paramName)

for thisTrial_pic_eval_2 in trial_pic_eval_2:
    currentLoop = trial_pic_eval_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_pic_eval_2.rgb)
    if thisTrial_pic_eval_2 != None:
        for paramName in thisTrial_pic_eval_2.keys():
            exec(paramName + '= thisTrial_pic_eval_2.' + paramName)
    
    # ------Prepare to start Routine "eval_pic"-------
    t = 0
    eval_picClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # this is the question it randomly pulls from the .csv file
    pic_q = current_question
    
    # this is added because by having an id of the question
    # where the questions are randomised, we can simply store it
    # later
    q_id = sav_mapping
    rating_2.reset()
    image_2.setImage(pic_q)
    # keep track of which components have finished
    eval_picComponents = [rating_2, image_2, text_49]
    for thisComponent in eval_picComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "eval_pic"-------
    while continueRoutine:
        # get current time
        t = eval_picClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating_2* updates
        if t >= 0.0 and rating_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_2.tStart = t
            rating_2.frameNStart = frameN  # exact frame index
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        
        # *text_49* updates
        if t >= 0.0 and text_49.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_49.tStart = t
            text_49.frameNStart = frameN  # exact frame index
            text_49.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eval_picComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eval_pic"-------
    for thisComponent in eval_picComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stor_pic_q.append(rating.getRating())
    # store data for trial_pic_eval_2 (TrialHandler)
    trial_pic_eval_2.addData('rating_2.response', rating_2.getRating())
    trial_pic_eval_2.addData('rating_2.rt', rating_2.getRT())
    # the Routine "eval_pic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed run_pic_eval_e repeats of 'trial_pic_eval_2'

# get names of stimulus parameters
if trial_pic_eval_2.trialList in ([], [None], None):
    params = []
else:
    params = trial_pic_eval_2.trialList[0].keys()
# save data for this loop
trial_pic_eval_2.saveAsExcel(filename + '.xlsx', sheetName='trial_pic_eval_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trial_pic_eval_2.saveAsText(filename + 'trial_pic_eval_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
























# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
