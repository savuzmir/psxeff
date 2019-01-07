#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on January 07, 2019, at 18:35
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
expName = 'psreff3'  # from the Builder filename that created this script
expInfo = {u'participant': u'9999', u'num_pract': u'20', u'age': u'1992-11-12', u'pic_eval': u'1', u'sample': u'1', u'run_all': u'0', u'g_conn': u'1', u'type': u'1', u'run_debug': u'0'}
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
    originPath=u'E:\\Experiments\\UCL\\Sebastijan\\PrimarySecondaryReward\\N\\Experiment\\psreff.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
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
from datetime import datetime
from datetime import date
from dateutil import relativedelta 
from copy import deepcopy

################################################
########### defining basic variables ###########
################################################

# absolute trial counter; including practice trials
abs_trial = 1
# trial for values in evaluation
sub_trial = 1
# current trial within the matrix sequence
matrix_trial = 1


# used to run either practice or real trials 
run_prac = 1
run_real = 0
run_juice_reeval = 0
# run matrix reevaluation or not
run_correct = 0
#current row that is being pulled for the image in the matrix trial
run_matrix = 0

# helper variable used in the matrix evaluation procedure
already_switched = 0
# was the reverse correcetd (e.g. by 1 1)
reverse_corrected = 0
# initiate reverse sequence in WASI?
initiate_reverse = 0
# was the response correct or not in the matrix case
responded_correctly = 0
# indexing the item 
indx = 0
# diagnostics string
diagnostics_info = ''

################################################
######## generic helpre variables ##############
################################################

# generic helper variable
tmp = 0
# generic helper list
tmp_list = [] 
# generic helper dict
tmp_dict = {}
# generic helper variables
struct_1 = ''
struct_2 = ''
# tmp trial is used as a helper counter in various places
tmp_trial = 1

# key used for obtaining the final response from the participants
response = ''

# last matrix
last_matrix = 'stimuli/Item30-1.png'

# to not check for reverse correction every time
turn_off = 0

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
stor_matrix_ans = {}
stor_aux_ans = []
# list used for evaluating matrix reasoning correctness
tmp_evaluater = []

################################################
########### Matrix reasoning containers ########
################################################

# t score containers
t_1 = [20, 22, 23, 25, 27, 29, 31, 33, 34, 36, 38, 40, 42, 44, 46, 48, 51, 53, 55, 57, 59, 62, 65, 68, 72, 76, 79, 80, 80, 80, 80]
t_2 = [20, 21, 22, 24, 26, 28, 30, 32, 33, 35, 37, 39, 41, 43, 45, 47, 50, 52, 54, 56, 58, 61, 64, 67, 71, 75, 78, 80, 80, 80, 80]
t_3 = [20, 21, 22, 24, 26, 28, 30, 32, 33, 35, 37, 39, 40, 42, 45, 46, 49, 51, 53, 55, 57, 60, 63, 66, 70, 74, 78, 80, 80, 80, 80]
t_4 = [20, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36, 38, 40, 42, 44, 46, 49, 51, 53, 55, 57, 60, 63, 66, 70, 74, 77, 80, 80, 80, 80]
t_5 = [20, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 59, 62, 65, 69, 73, 77, 80, 80, 80, 80]
t_6 = [20, 20, 21, 23, 25, 27, 29, 30, 32, 33, 35, 37, 39, 41, 43, 45, 47, 49, 52, 54, 56, 58, 61, 65, 69, 73, 77, 80, 80, 80, 80]
t_7 = [20, 20, 21, 23, 24, 26, 28, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 58, 61, 64, 68, 72, 76, 79, 80, 80, 80]
t_8 = [20, 20, 21, 23, 24, 26, 28, 29, 31, 32, 34, 36, 38, 40, 42, 44, 46, 48, 51, 53, 55, 57, 60, 64, 68, 72, 76, 79, 80, 80, 80]
t_9 = [20, 20, 21, 23, 24, 26, 27, 29, 30, 32, 34, 36, 38, 40, 42, 43, 45, 47, 50, 52, 54, 56, 59, 63, 67, 71, 75, 78, 80, 80, 80]
t_10 = [20, 20, 20, 22, 23, 25, 27, 28, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 50, 52, 54, 56, 59, 63, 67, 71, 75, 78, 80, 80, 80]

t_11 = [20, 20, 20, 20, 20, 21, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 49, 51, 53, 55, 58, 62, 68, 73, 76, 79, 80]
t_12 = [20, 20, 20, 20, 20, 21, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 57, 61, 66, 71, 75, 78, 80]
t_13 = [20, 20, 20, 20, 20, 21, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 57, 60, 64, 69, 73, 77, 80]

age_adults = ['17-19', '20-24', '25-29']

age_children = ['9:0-9:3', '9:4-9:7', '9:8-9:11', '10:0-10:3', '10:4-10:7', \
                '10:8-10:11', '11:0-11:3', '11:4-11:7', '11:8-11:11', '12:0-12:3']


matrix_reason = {}
matrix_reason['adult'] = {}
matrix_reason['child'] = {}

matrix_reason['adult']['17-19'] = {}
matrix_reason['adult']['20-24'] = {}
matrix_reason['adult']['25-29'] = {}
matrix_reason['child']['9:0-9:3'] = {}
matrix_reason['child']['9:4-9:7'] = {}
matrix_reason['child']['9:8-9:11'] = {}
matrix_reason['child']['10:0-10:3'] = {}
matrix_reason['child']['10:4-10:7'] = {}
matrix_reason['child']['10:8-10:11'] = {}
matrix_reason['child']['11:0-11:3'] = {}
matrix_reason['child']['11:4-11:7'] = {}
matrix_reason['child']['11:8-11:11'] = {}
matrix_reason['child']['12:0-12:3'] = {}



for i in range(1, 31):
    str_i = str(i)
    matrix_reason['adult']['17-19'][str_i] = t_11[i]
    matrix_reason['adult']['20-24'][str_i]  = t_12[i]
    matrix_reason['adult']['25-29'][str_i]  = t_13[i]
    matrix_reason['child']['9:0-9:3'][str_i]  = t_1[i]
    matrix_reason['child']['9:4-9:7'][str_i]  = t_2[i]
    matrix_reason['child']['9:8-9:11'][str_i]  = t_3[i]
    matrix_reason['child']['10:0-10:3'][str_i]  = t_4[i]
    matrix_reason['child']['10:4-10:7'][str_i]  = t_5[i]
    matrix_reason['child']['10:8-10:11'][str_i]  = t_6[i]
    matrix_reason['child']['11:0-11:3'][str_i]  = t_7[i]
    matrix_reason['child']['11:4-11:7'][str_i]  = t_8[i]
    matrix_reason['child']['11:8-11:11'][str_i]  = t_9[i]
    matrix_reason['child']['12:0-12:3'][str_i]  = t_10[i]


stim_corr_ans = [2, 3, 2, 1, 3, 1, 5, 1, 3, 3, 4, 2, 3, 4, 1, 4, \
                 2, 5, 4, 2, 4, 2, 3, 3, 1, 4, 4, 2, 5, 5, 1, 2]

# generate a second stimuli list
stim_list = ['stimuli/Sample Item A-1.png', 'stimuli/Sample Item B-1.png']
for i in range(1, 31):
    if i < 10:
        stim_file = 'stimuli/Item0' + str(i) + '-1.png'
    else:
        stim_file = 'stimuli/Item' + str(i) + '-1.png'
    stim_list.append(stim_file)


# this is important for the saving portion 

# generate empty list with all responses
tmp_list = 30*[None]

# populate with 0s
for i in range(0, 30):
    if i < 5:
        tmp_list[i] = 1 # this is a very elegant assumption that saves a lot of loops
    else:
        tmp_list[i] = 0



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
# type of sequence failure in case an individual failed the first matrix reasoning trials 
failed_seq = 0


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


############################################################
################### helper functions #######################
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


def set_matrix(indx, stim_list, stim_corr_ans):
    return [stim_list[indx], stim_corr_ans[indx]]

options = [(1, [0.2, 0.2, 0.2]), \
           (2, [0.2, 0.2, 0.2]), \
           (3, [0.2, 0.2, 0.2]), \
           (4, [0.2, 0.2, 0.2]), \
           (5, [0.2, 0.2, 0.2]), \
           (6, [0.2, 0.2, 0.2])]


def color_change(picked_opt, options):
    copy_options = deepcopy(options) # this way we preserve the original
    ch_option = [1, 0.84, 0.0]
    unch_col = [0.2, 0.2, 0.2]

    for indx, option in enumerate(options):
        if str(option[0]) == picked_opt:
            tmp = list(options[indx]) # hack to remove issues with deleting
            del tmp[1]
            tmp.append(ch_option)
            copy_options[indx] = tuple(tmp)
    else:
        copy_options[indx] = tuple([indx+1, unch_col])
    return copy_options

def matrix_response(answer, correct_answer, container, curr_matrix):
    responded_correctly = answer.keys == str(correct_answer)
        
    curr_matrix = curr_matrix.split('-')[0][-2:] # fetches the string of the item

    if responded_correctly:
        container[curr_matrix] = 1
    else:
        container[curr_matrix] = 0

    return [responded_correctly, container]

def trial_evaluater(container):
    if sum(container[-3:]) == 0 and len(container) >= 6: # maybe change this but this assumes noone will have less
        return 1                                          # than the first 10 incorrect



def reverse_correction(matrix_trial, indx, aux_container, response, tmp):

    # these act as default values for the variables 
    reverse_corrected = 0
    turn_off = 0
    if (matrix_trial == 4 and indx == 4) or (matrix_trial == 5 and indx == 4):
        tmp = 1
    elif (matrix_trial == 5 and indx == 3) or (matrix_trial == 6 and indx == 3):
        tmp = 2
    if tmp == 1 or tmp == 2:
        aux_container.append(response)
        
    if tmp == 2:
        if sum(stor_aux_ans) == 2:
            reverse_corrected = 1
            turn_off = 1
    
    return [reverse_corrected, aux_container, turn_off]

# deprecated 

def matrix_resp_parser(container):
    tmp_it = [int(el) for el in container.keys()]
    tmp_it.sort()
    tmp_it = tmp_it[-1]

    if tmp_it < 10:
        tmp_it = '0' + str(tmp_it)
    else:
        tmp_it = str(tmp_it)

    return container[tmp_it]


def set_filename(part_char, addon):

    fname = part_char[0] + '_' + part_char[1] + '_' + part_char[2] + '_' + part_char[3] + '_' + addon + '.txt'

    ctr = 0 # recursively checks if the file already exists, if it doesn't it stops
    fname = check_file(fname, part_char[4], ctr)

    complete = part_char[4] + "\\data\\" + fname

    return complete

 





text_7 = visual.TextStim(win=win, name='text_7',
    text='Instructions placeholder',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "mat_ev"
mat_evClock = core.Clock()

image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_55 = visual.TextStim(win=win, name='text_55',
    text='default text',
    font='Arial',
    pos=(0, 0.87), height=0.1, wrapWidth=1.4, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
diagnostics_3 = visual.TextStim(win=win, name='diagnostics_3',
    text='default text',
    font='Arial',
    pos=(0.4, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "mat_ans"
mat_ansClock = core.Clock()
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
    text='You have chosen:',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_53 = visual.TextStim(win=win, name='text_53',
    text='If this is true, press "y". \nIf you want to choose again, press "n".',
    font='Arial',
    pos=(0, 0.05), height=0.1, wrapWidth=0.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);

diagnostics = visual.TextStim(win=win, name='diagnostics',
    text='default text',
    font='Arial',
    pos=(0.4, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0);

# Initialize components for Routine "mat_re"
mat_reClock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

diagnostics_2 = visual.TextStim(win=win, name='diagnostics_2',
    text='default text',
    font='Arial',
    pos=(0.4, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "transition"
transitionClock = core.Clock()

text_54 = visual.TextStim(win=win, name='text_54',
    text='We would now like you to answer a number of questions!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_66 = visual.TextStim(win=win, name='text_66',
    text='default text',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_67 = visual.TextStim(win=win, name='text_67',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_68 = visual.TextStim(win=win, name='text_68',
    text='default text',
    font='Arial',
    pos=(0, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0);
text_69 = visual.TextStim(win=win, name='text_69',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "ev_iniq"
ev_iniqClock = core.Clock()

rating = visual.RatingScale(win=win, name='rating', size = 0.8,
lineColor = 'black',
stretch = 1.4,
textColor = "black",
labels = ["Not at all", "Extremely"])
text_44 = visual.TextStim(win=win, name='text_44',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "ev_pic"
ev_picClock = core.Clock()

rating_2 = visual.RatingScale(win=win, name='rating_2', size = 0.8,
lineColor = 'black',
stretch = 1.4,
textColor = "black",
labels = ["not at all", "extremely"])
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.8, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='How much do you like this picture?',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "est_sal"
est_salClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='You will now get to try a number of juices. After you obtain each juice, we would like you to rate them. We will take your answers into account so you will be playing for your favourite juice!\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "supl_jui"
supl_juiClock = core.Clock()

text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
jui_pic = visual.ImageStim(
    win=win, name='jui_pic',
    image='sin', mask=None,
    ori=0, pos=(0, -0.2), size=(0.2, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ev_jui"
ev_juiClock = core.Clock()

text_30 = visual.TextStim(win=win, name='text_30',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=0.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
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

# Initialize components for Routine "jui_fe"
jui_feClock = core.Clock()

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

# Initialize components for Routine "water_disp"
water_dispClock = core.Clock()

cross_sign = visual.TextStim(win=win, name='cross_sign',
    text='You are receiving water to cleanse your palate.',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "jui_out"
jui_outClock = core.Clock()

text_41 = visual.TextStim(win=win, name='text_41',
    text='Your favourite juice was:',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_70 = visual.TextStim(win=win, name='text_70',
    text='Please confirm by pressing "y" if this is correct or "n" if you want to choose another one.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
image_14 = visual.ImageStim(
    win=win, name='image_14',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "jui_re"
jui_reClock = core.Clock()

text_42 = visual.TextStim(win=win, name='text_42',
    text='Which if these juices was your favourite:',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_43 = visual.TextStim(win=win, name='text_43',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
image_11 = visual.ImageStim(
    win=win, name='image_11',
    image='sin', mask=None,
    ori=0, pos=(-0.4, -0.4), size=(0.2, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_12 = visual.ImageStim(
    win=win, name='image_12',
    image='sin', mask=None,
    ori=0, pos=(0, -0.4), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_13 = visual.ImageStim(
    win=win, name='image_13',
    image='sin', mask=None,
    ori=0, pos=(0.4, -0.4), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "test"
testClock = core.Clock()

text_50 = visual.TextStim(win=win, name='text_50',
    text='default text',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_64 = visual.TextStim(win=win, name='text_64',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_65 = visual.TextStim(win=win, name='text_65',
    text=stim_corr_ans,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_73 = visual.TextStim(win=win, name='text_73',
    text='Now we move to the next part of our experiment. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0);

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

# Initialize components for Routine "eff_press"
eff_pressClock = core.Clock()
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_9 = visual.ImageStim(
    win=win, name='image_9',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_10 = visual.ImageStim(
    win=win, name='image_10',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
text_28 = visual.TextStim(win=win, name='text_28',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
text_62 = visual.TextStim(win=win, name='text_62',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
text_63 = visual.TextStim(win=win, name='text_63',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "eff_feed"
eff_feedClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Effort task placeholder',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "beg_fix"
beg_fixClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='This round:',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
image_7 = visual.ImageStim(
    win=win, name='image_7',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

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
    edges=90, size=(0.8, 0.1),
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


# Initialize components for Routine "cog_eff_fin"
cog_eff_finClock = core.Clock()

# Initialize components for Routine "cog_eff_fin_answ"
cog_eff_fin_answClock = core.Clock()

# Initialize components for Routine "nasa_tlx"
nasa_tlxClock = core.Clock()

nasa_tlx_text = visual.TextStim(win=win, name='nasa_tlx_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
rating_3 = visual.RatingScale(win=win, name='rating_3', size = 0.8,
lineColor = 'black',
stretch = 1.4,
textColor = "black",
labels = ["Very Low", "Very High"])

# Initialize components for Routine "juice_eval"
juice_evalClock = core.Clock()
inputText = ""
quest_prompt = visual.TextStim(win=win, name='quest_prompt',
    text='How much do you think 100ml of juice is worth? (please write down the number in pence, e.g. for one pound, write down 100) ',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
resp_box = visual.TextStim(win=win, name='resp_box',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "ev_pic"
ev_picClock = core.Clock()

rating_2 = visual.RatingScale(win=win, name='rating_2', size = 0.8,
lineColor = 'black',
stretch = 1.4,
textColor = "black",
labels = ["not at all", "extremely"])
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.8, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='How much do you like this picture?',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "final_screen"
final_screenClock = core.Clock()
text_48 = visual.TextStim(win=win, name='text_48',
    text='That was all, you are done! Thank you for your participation :)',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

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


# type leads to 6 different potential variants of this task. 
type = int(expInfo['type'])

# just for debugging purposes
run_debug = int(expInfo['run_debug'])
run_all = int(expInfo['run_all'])
run_nasa = 1

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


# compute age to know which t-scores to look
part_age = str(expInfo['age'])
participant_type = int(expInfo['sample'])


part_age = [int(el) for el in part_age.split('-')]
part_age = datetime(part_age[0], part_age[1], part_age[2])

today = [int(el) for el in str(date.today()).split('-')]
today = datetime(today[0], today[1], today[2])

diff = relativedelta.relativedelta(today, part_age)
part_year = diff.years
part_month = diff.months

# function that finds the correct age bracket 
def find_age_bracket(part_year, part_month, age_list, part_type):
    corr_brack = ''
    for bracket in age_list:
        if part_type == 2:
            split_bracket = bracket.split('-')
            lb, ub = split_bracket[0].split(':'), split_bracket[1].split(':') # split into upper and lower 
            lyr, lmth, uyr, umth = int(lb[0]), int(lb[1]), int(ub[0]), int(ub[1]) # index years - 0, and months - 1
        else:
            bound = bracket.split('-')
            lyr, uyr = int(bound[0]), int(bound[1]) # split into upper and lower
        if part_type == 2:
            try:
                if (lyr <= part_year <= uyr) and (lmth <= part_month <= umth):
                    corr_brack = bracket # this means the participant falls into this bracket
                    break  
            except:
                pass 
        else:
            try:
                if (lyr <= part_year <= uyr):
                    corr_brack = bracket
                    break
            except:
                pass
    if corr_brack == '':
        print('The subject is either too old or too young')
    return corr_brack

if participant_type == 1:
    participant_age = find_age_bracket(part_year, part_month, age_adults, participant_type)
    participant_type = 'adult' # rename for dict purposes
else:
    participant_age = find_age_bracket(part_year, part_month, age_children, participant_type)
    participant_type = 'child'

# number of practice trials | default is 20
num_pract = int(expInfo['num_pract'])  


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

part_char = [exp_name, sub_id, out_type, dat, cwd]

# filename
complete = set_filename(part_char, 'main')

# open a text file 
dataset = open(complete, 'w')

# in the first row we save header columns | add the others later

dataset.write('trial\tcurr_rew\tquestion\tresponse\tresp_rt\ttrial_conc\trew_mult\tmain_st\tgng\tresp_m\tresp_m_rt\trew_m\tpump\tpump_tim\tpump_vol\n')

# connection is set at 1 as default, meaning we want to connect gustaf
gust_connected = int(expInfo['g_conn'])

gust_connected = 0

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
mat_tr = data.TrialHandler(nReps=run_matrix, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('m_reason.csv'),
    seed=None, name='mat_tr')
thisExp.addLoop(mat_tr)  # add the loop to the experiment
thisMat_tr = mat_tr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMat_tr.rgb)
if thisMat_tr != None:
    for paramName in thisMat_tr.keys():
        exec(paramName + '= thisMat_tr.' + paramName)

for thisMat_tr in mat_tr:
    currentLoop = mat_tr
    # abbreviate parameter names if possible (e.g. rgb = thisMat_tr.rgb)
    if thisMat_tr != None:
        for paramName in thisMat_tr.keys():
            exec(paramName + '= thisMat_tr.' + paramName)
    
    # ------Prepare to start Routine "mat_ev"-------
    t = 0
    mat_evClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    correct_answer = stim_corr_ans[matrix_trial-1]
    curr_matrix = stim_list[matrix_trial-1] # take -1 because
                                             # we init matrix_trial
                                             # as 1
    
    if matrix_trial <= 2:
        begin_blurb = 'Answer by pressing keys from 1 to 5. If you do not know the answer, press 6.'
    else:
        begin_blurb = ''
    
    if matrix_trial == 3: 
        indx = 5
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 4 and not initiate_reverse:
        indx = 6
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 4 and initiate_reverse:
        indx = 4
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 5 and not initiate_reverse:
        indx = 7
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 5 and initiate_reverse and indx == 4: # if we have already presented item 3
        indx = 3
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 5 and initiate_reverse and indx == 6:
        indx = 4
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 6 and not initiate_reverse:
        indx = 8
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 6 and reverse_corrected:
    # this assumes that initiate_reverse has been turned off 
        indx = 6
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        reverse_corrected = 0
        failed_seq = 2
    
    # the elif above will catch if its trial 6 and the sub had a correct response for 3 and 2
    # we would enter this only if the person would be incorrect in 3 2 and 1 
    
    elif matrix_trial == 6 and initiate_reverse and indx == 3: 
        indx = 2
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 6 and initiate_reverse and indx == 4:
        indx = 3
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 7 and failed_seq == 2:
        indx = 7
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        failed_seq = 2
    
    elif matrix_trial == 7 and not initiate_reverse:
        indx = 9
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 7 and initiate_reverse and indx == 3 and not reverse_corrected:
        indx = 2
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
    
    elif matrix_trial == 7 and initiate_reverse and indx == 2:
        indx = 6
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        failed_seq = 1
    
    elif matrix_trial == 7 and reverse_corrected and indx == 2:
        indx = 6
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        reverse_corrected = 0
        failed_seq = 1
    
    # for the last two, it should automatically go ahead with either 5 or 6 regardless of whether reverse was corrected or not
    # so it needs to be set appropriately
    elif matrix_trial == 7 and reverse_corrected and indx == 3:
        indx = 7
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        reverse_corrected = 0
        failed_seq = 2
    
    elif matrix_trial == 8 and indx == 2:
        failed_seq = 2
    
    # this will hold true for all subsequent ones. placing it before the one we actually have last is a cheap way of avoiding
    # additional thought
    elif matrix_trial >= 8:
        if failed_seq == 1:
            indx = matrix_trial - 1
        elif failed_seq == 2:
            indx = matrix_trial
        else:
            indx = matrix_trial + 2 # this is the correct difference between the matrix trial and the index acces element
        
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
    elif matrix_trial == 8 and reverse_corrected:
        indx = 7
        curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        reverse_corrected = 0
        failed_seq = 1
    
    
    if matrix_trial >= 4:
    
        diagnostics_info = "m_trial: " + str(matrix_trial) + ", indx: " + str(indx) + "\n" + \
                          "curr_resp: " + str(responded_correctly) + ", storage: " + str(stor_matrix_ans) +  "\n" + \
                          str(curr_matrix) + ", turn off: " + str(turn_off) + "\n" + \
                          "response storage: " + str(tmp_evaluater)
    else:
        diagnostics_info = "m_trial: " + str(matrix_trial) + ", indx: " + str(indx) + "\n" + \
                          "curr_resp: " + str(responded_correctly) + ", storage: " + str(stor_matrix_ans) +  "\n" + \
                          str(curr_matrix) + ", turn off: " + str(turn_off)
    image_3.setImage(curr_matrix)
    item_resp = event.BuilderKeyResponse()
    text_55.setText(begin_blurb)
    diagnostics_3.setText(diagnostics_info)
    # keep track of which components have finished
    mat_evComponents = [image_3, item_resp, text_55, diagnostics_3]
    for thisComponent in mat_evComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "mat_ev"-------
    while continueRoutine:
        # get current time
        t = mat_evClock.getTime()
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
        
        # *diagnostics_3* updates
        if t >= 0.0 and diagnostics_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            diagnostics_3.tStart = t
            diagnostics_3.frameNStart = frameN  # exact frame index
            diagnostics_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mat_evComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mat_ev"-------
    for thisComponent in mat_evComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    chosen_item = item_resp.keys
    # check responses
    if item_resp.keys in ['', [], None]:  # No response was made
        item_resp.keys=None
    mat_tr.addData('item_resp.keys',item_resp.keys)
    if item_resp.keys != None:  # we had a response
        mat_tr.addData('item_resp.rt', item_resp.rt)
    # the Routine "mat_ev" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "mat_ans"-------
    t = 0
    mat_ansClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(curr_matrix)
    text_52.setText(chosen_item)
    matrix_reeval = event.BuilderKeyResponse()
    
    diagnostics.setText(diagnostics_info)
    # keep track of which components have finished
    mat_ansComponents = [image_4, polygon_2, text_51, text_52, matrix_reeval, text_53, diagnostics]
    for thisComponent in mat_ansComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "mat_ans"-------
    while continueRoutine:
        # get current time
        t = mat_ansClock.getTime()
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
        
        
        # *diagnostics* updates
        if t >= 0.0 and diagnostics.status == NOT_STARTED:
            # keep track of start time/frame for later
            diagnostics.tStart = t
            diagnostics.frameNStart = frameN  # exact frame index
            diagnostics.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mat_ansComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mat_ans"-------
    for thisComponent in mat_ansComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if matrix_reeval.keys in ['', [], None]:  # No response was made
        matrix_reeval.keys=None
    mat_tr.addData('matrix_reeval.keys',matrix_reeval.keys)
    if matrix_reeval.keys != None:  # we had a response
        mat_tr.addData('matrix_reeval.rt', matrix_reeval.rt)
    if matrix_reeval.keys == 'n':
        run_correct = 1
    
    else:
        run_correct = 0 # dont need to run the second part
    
        if matrix_trial >= 3:
            responded_correctly, stor_matrix_ans = matrix_response(item_resp, correct_answer, stor_matrix_ans, curr_matrix)
            
           # we sort the keys which are the items according to order and take the last as this will be increasin
           # we transform the data structure in matrix_resp_parser and feed it into the trial evaluater
            tmp_evaluater.append(responded_correctly)
    
            # main stop rule 
            mat_tr.finished = trial_evaluater(tmp_evaluater)
    
            # item 4 
        if matrix_trial == 3 and not responded_correctly:
            already_switched = 1
            initiate_reverse = 1
    
            # item 5 
        elif matrix_trial == 4 and not already_switched and not responded_correctly:
            already_switched = 1
            initiate_reverse = 1
    
        # this code is a bit chunky but turning it into a function makes this just more problematic
    
        if not turn_off: # this prevents from this whole thing getting evaluated unnecessarily
            reverse_corrected, stor_aux_ans, turn_off = reverse_correction(matrix_trial, indx, stor_aux_ans, responded_correctly, tmp)
    
    
        if matrix_trial >= 3:
    
            diagnostics_info = "m_trial: " + str(matrix_trial) + ", indx: " + str(indx) + "\n" + \
                              "curr_resp: " + str(responded_correctly) + ", storage: " + str(stor_matrix_ans) +  "\n" + \
                              str(curr_matrix) + ", turn off: " + str(turn_off) + "\n" + \
                              "response storage: " + str(tmp_evaluater)
        else:
            diagnostics_info = "m_trial: " + str(matrix_trial) + ", indx: " + str(indx) + "\n" + \
                              "curr_resp: " + str(responded_correctly) + ", storage: " + str(stor_matrix_ans) +  "\n" + \
                              str(curr_matrix) + ", turn off: " + str(turn_off)
    
        matrix_trial += 1
    
        if curr_matrix == last_matrix:
            mat_tr.finished=True
    # the Routine "mat_ans" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    matrix_re = data.TrialHandler(nReps=run_correct, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='matrix_re')
    thisExp.addLoop(matrix_re)  # add the loop to the experiment
    thisMatrix_re = matrix_re.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMatrix_re.rgb)
    if thisMatrix_re != None:
        for paramName in thisMatrix_re.keys():
            exec(paramName + '= thisMatrix_re.' + paramName)
    
    for thisMatrix_re in matrix_re:
        currentLoop = matrix_re
        # abbreviate parameter names if possible (e.g. rgb = thisMatrix_re.rgb)
        if thisMatrix_re != None:
            for paramName in thisMatrix_re.keys():
                exec(paramName + '= thisMatrix_re.' + paramName)
        
        # ------Prepare to start Routine "mat_re"-------
        t = 0
        mat_reClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_5.setImage(curr_matrix)
        item_resp_again = event.BuilderKeyResponse()
        
        diagnostics_2.setText(diagnostics_info)
        # keep track of which components have finished
        mat_reComponents = [image_5, item_resp_again, diagnostics_2]
        for thisComponent in mat_reComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "mat_re"-------
        while continueRoutine:
            # get current time
            t = mat_reClock.getTime()
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
            
            
            # *diagnostics_2* updates
            if t >= 0.0 and diagnostics_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                diagnostics_2.tStart = t
                diagnostics_2.frameNStart = frameN  # exact frame index
                diagnostics_2.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mat_reComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mat_re"-------
        for thisComponent in mat_reComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if item_resp_again.keys in ['', [], None]:  # No response was made
            item_resp_again.keys=None
        matrix_re.addData('item_resp_again.keys',item_resp_again.keys)
        if item_resp_again.keys != None:  # we had a response
            matrix_re.addData('item_resp_again.rt', item_resp_again.rt)
        # check for response
        
        if matrix_trial >= 3:
            responded_correctly, stor_matrix_ans = matrix_response(item_resp_again, correct_answer, stor_matrix_ans, curr_matrix)
        
            tmp_evaluater.append(responded_correctly)
        
            mat_tr.finished = trial_evaluater(tmp_evaluater)
        
        if not turn_off: # this prevents from this whole thing getting evaluated unnecessarily
            reverse_corrected, stor_aux_ans, turn_off = reverse_correction(matrix_trial, indx, stor_aux_ans, responded_correctly, tmp)
        
        
            # item 4 
        if matrix_trial == 3 and not responded_correctly:
            already_switched = 1
            initiate_reverse = 1
        
        elif matrix_trial == 4 and not already_switched and not responded_correctly:
            already_switched = 1
            initiate_reverse = 1
        
        run_correct = 0
        
        if curr_matrix == last_matrix:
            mat_tr.finished=True
        
        if matrix_trial >= 3:
        
            diagnostics_info = "m_trial: " + str(matrix_trial) + ", indx: " + str(indx) + "\n" + \
                              "curr_resp: " + str(responded_correctly) + ", storage: " + str(stor_matrix_ans) +  "\n" + \
                              str(curr_matrix) + ", turn off: " + str(turn_off) + "\n" + \
                              "response storage: " + str(tmp_evaluater)
        else:
            diagnostics_info = "m_trial: " + str(matrix_trial) + ", indx: " + str(indx) + "\n" + \
                              "curr_resp: " + str(responded_correctly) + ", storage: " + str(stor_matrix_ans) +  "\n" + \
                              str(curr_matrix) + ", turn off: " + str(turn_off)
        
        matrix_trial += 1
        
        
        # the Routine "mat_re" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_correct repeats of 'matrix_re'
    
    # get names of stimulus parameters
    if matrix_re.trialList in ([], [None], None):
        params = []
    else:
        params = matrix_re.trialList[0].keys()
    # save data for this loop
    matrix_re.saveAsExcel(filename + '.xlsx', sheetName='matrix_re',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    matrix_re.saveAsText(filename + 'matrix_re.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed run_matrix repeats of 'mat_tr'

# get names of stimulus parameters
if mat_tr.trialList in ([], [None], None):
    params = []
else:
    params = mat_tr.trialList[0].keys()
# save data for this loop
mat_tr.saveAsExcel(filename + '.xlsx', sheetName='mat_tr',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
mat_tr.saveAsText(filename + 'mat_tr.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "transition"-------
t = 0
transitionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if run_matrix:
    # find appropriate t_values for our participant
    t_values = sorted(matrix_reason[participant_type][participant_age].values())

    # compute cumulative score from the matrix reasoning test
    
    f_r = '03'
    s_r = '02'
    
    if f_r in stor_matrix_ans and stor_matrix_ans[f_r] == 1:
        if stor_matrix_ans[s_r] == 1:
            ans_sum = str(sum(stor_matrix_ans.values()) + 1)
        # if s_r is 0, then it will automatically go to 1 as well so all will be accounted for
        else:
            ans_sum = str(sum(stor_matrix_ans.values()))
    
    elif f_r not in stor_matrix_ans:
        ans_sum = str(sum(stor_matrix_ans.values()) + 3) # this necessarily means 



    part_t = matrix_reason[participant_type][participant_age][ans_sum]

    # we arbitrarily pick a higher and lower t score value

    t_modifier = 15

    low = part_t - t_modifier
    medium = part_t + 2         # this will in most if not all cases yield the next or second next item of the three items
    high = part_t + t_modifier  # where the participant has failed. they therefore represent the medium difficulty

    # exception handling | 80 is the max t values and 20 is the min t value

    if high > 80:
        high = 80

    if low < 20:
        low = 20

    # now we find the t value that corresponds and/or is closest to the newly obtained modifier 

    low = min(enumerate(t_values), key=lambda i: abs(i[1]-low))[1]
    medium = min(enumerate(t_values), key=lambda i: abs(i[1]-medium))[1]
    high = min(enumerate(t_values), key=lambda i: abs(i[1]-high))[1]


    for key, value in matrix_reason[participant_type][participant_age].items():
        if value == high:
            high = key
        if value == low:
            low = key
        if value == medium:
            medium = key

    # they are now saved as the number of correct items which will correspond to the 
    # row they are being pulled from from the .csv. This is only approximate because
    # obviously someone can have 1 incorrect and two further ones correct. this is not
    # likely to happen often though.

    # we now convert them to rows. to all of them we need to add +2 due to sample item A and B being
    # in the first two rows 

    # these are now ready for the final examination

    # we can make this also such that if a participant has some incorrect responses in the middle 
    # then it will fetch those items closest to the t values of the participant that were incorrect
    # this will fetch either ones that had yet to be shown or were shown already but participants 
    # responded on them incorrectly 

    low = int(low) + 2 
    medium = int(medium) + 2
    high = int(high) + 2
    # these are the index values of items that we want to pick.
    t = [low, medium, high]

else:
    part_t = ''
    t = ''
    ans_sum = ''
    tmp_list = []
text_66.setText(part_t)
text_67.setText(t)
key_resp_7 = event.BuilderKeyResponse()
text_68.setText(ans_sum)
# keep track of which components have finished
transitionComponents = [text_54, text_66, text_67, key_resp_7, text_68, text_69]
for thisComponent in transitionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "transition"-------
while continueRoutine:
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
    
    # *text_66* updates
    if t >= 0.0 and text_66.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_66.tStart = t
        text_66.frameNStart = frameN  # exact frame index
        text_66.setAutoDraw(True)
    
    # *text_67* updates
    if t >= 0.0 and text_67.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_67.tStart = t
        text_67.frameNStart = frameN  # exact frame index
        text_67.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_68* updates
    if t >= 0.0 and text_68.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_68.tStart = t
        text_68.frameNStart = frameN  # exact frame index
        text_68.setAutoDraw(True)
    
    # *text_69* updates
    if t >= 1 and text_69.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_69.tStart = t
        text_69.frameNStart = frameN  # exact frame index
        text_69.setAutoDraw(True)
    
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

if run_matrix:
    # complete path 
    complete = set_filename(part_char, 'matrix_reasoning')

    # current file 
    matrix_data = open(complete, 'w')

    struct_1 = ''
    struct_2 = ''

    for i in range(1, 31):
        struct_1 +=  "item_" + str(i) + "\t" 
        struct_2 += "{}\t"

    struct_1 += "sub_id\n"
    struct_2 += "{}\n"

    matrix_data.write(struct_1)


    # take the length of the actual responses
    sma_len = len(stor_matrix_ans.keys())

    tmp_keys = sma_len*[None]

    # populate it with the index values of the tmp_list where 0s should be theoretically
    # substituted with the real responses
    for i in range(0, sma_len):
        tmp_keys[i] = (int(stor_matrix_ans.keys()[i]) - 1) # we reduce it by one and transform it 
                                                             # into an index 

    for el in tmp_keys:
        key_el = el + 1 # transform back into key 
        if key_el < 10:
            key_el = '0' + str(key_el)
        else:
            key_el = str(key_el)

        tmp_list[el] = stor_matrix_ans[key_el]

    tmp_list.append(part_char[1]) # sub_id

    matrix_data.write(struct_2.format(tmp_list[0], tmp_list[1],tmp_list[2], tmp_list[3],
                                          tmp_list[4], tmp_list[5],tmp_list[6], tmp_list[7],
                                          tmp_list[8], tmp_list[9],tmp_list[10], tmp_list[11],
                                          tmp_list[12], tmp_list[13],tmp_list[14], tmp_list[15],
                                          tmp_list[16], tmp_list[17],tmp_list[18], tmp_list[19],
                                          tmp_list[20], tmp_list[21],tmp_list[22], tmp_list[23],
                                          tmp_list[24], tmp_list[25],tmp_list[26], tmp_list[27],
                                          tmp_list[28], tmp_list[29],tmp_list[30]))
                


    matrix_data.close()

    # clear variables
    struct_1 = ''
    struct_2 = ''
    tmp_list = []



# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "transition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    
    # set up handler to look after randomisation of conditions etc
    init_qs = data.TrialHandler(nReps=0, method='random', 
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
        
        # ------Prepare to start Routine "ev_iniq"-------
        t = 0
        ev_iniqClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # this is the question it randomly pulls from the .csv file
        initial_q = current_question
        
        # this is added because by having an id of the question
        # where the questions are randomised, we can simply store it
        # later
        tmp_list.append(sav_mapping)
        rating.reset()
        text_44.setText(initial_q)
        # keep track of which components have finished
        ev_iniqComponents = [rating, text_44]
        for thisComponent in ev_iniqComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ev_iniq"-------
        while continueRoutine:
            # get current time
            t = ev_iniqClock.getTime()
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
            for thisComponent in ev_iniqComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ev_iniq"-------
        for thisComponent in ev_iniqComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        tmp_trial += 1
        
        stor_init_q.append(rating.getRating())
        
        if tmp_trial == 4:
        
            complete = set_filename(part_char, 'initial_q(initial_q.csv)')
            init_q_data = open(complete, 'w')
            
            for el in tmp_list:
                struct_1 += "quest" + str(el) + "\t"
            
            struct_1 += "sub_id\n"  #subid
            
            init_q_data.write(struct_1)
            
            for i in range(0, len(stor_init_q)):
                struct_2 += "{}\t"
        
            struct_2 += "{}\n"
        
            tmp_list = stor_init_q
            tmp_list.append(part_char[1])
        
            init_q_data.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3]))
            init_q_data.close()
        
            # clear variables
            struct_1 = ''
            struct_2 = ''
            tmp_list = []
            tmp_trial = 1
        # store data for init_qs (TrialHandler)
        init_qs.addData('rating.response', rating.getRating())
        # the Routine "ev_iniq" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 0 repeats of 'init_qs'
    
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
        
        # ------Prepare to start Routine "ev_pic"-------
        t = 0
        ev_picClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # this is the question it randomly pulls from the .csv file
        pic_q = current_question
        
        # this is added because by having an id of the question
        # where the questions are randomised, we can simply store it
        # later
        tmp_list.append(sav_mapping)
        rating_2.reset()
        image_2.setImage(pic_q)
        # keep track of which components have finished
        ev_picComponents = [rating_2, image_2, text_49]
        for thisComponent in ev_picComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ev_pic"-------
        while continueRoutine:
            # get current time
            t = ev_picClock.getTime()
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
            for thisComponent in ev_picComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ev_pic"-------
        for thisComponent in ev_picComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stor_pic_q.append(rating_2.getRating())
        
        tmp_trial += 1
        
        if tmp_trial == 7: # end of questions about pictures
        
            complete = set_filename(part_char, 'pic_q(pic_rating.csv)')
            pic_q_data = open(complete, 'w')
            
            for el in tmp_list:
                struct_1 += "pic" + str(el) + "\t"
            
            struct_1 += "sub_id\n"  #subid
        
            pic_q_data.write(struct_1)
            
            
            for i in range(0, len(stor_pic_q)):
                struct_2 += "{}\t"
        
            struct_2 += "{}\n"
        
            tmp_list = stor_pic_q
            tmp_list.append(part_char[1])
        
            pic_q_data.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3],
                                             tmp_list[4], tmp_list[5], tmp_list[6]))
            pic_q_data.close()
        
            struct_1 = ''
            struct_2 = ''
            tmp_list = []
        # store data for trial_pic_eval (TrialHandler)
        trial_pic_eval.addData('rating_2.response', rating_2.getRating())
        # the Routine "ev_pic" was not non-slip safe, so reset the non-slip timer
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
    jui_typ = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('juice_types.csv'),
        seed=None, name='jui_typ')
    thisExp.addLoop(jui_typ)  # add the loop to the experiment
    thisJui_typ = jui_typ.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisJui_typ.rgb)
    if thisJui_typ != None:
        for paramName in thisJui_typ.keys():
            exec(paramName + '= thisJui_typ.' + paramName)
    
    for thisJui_typ in jui_typ:
        currentLoop = jui_typ
        # abbreviate parameter names if possible (e.g. rgb = thisJui_typ.rgb)
        if thisJui_typ != None:
            for paramName in thisJui_typ.keys():
                exec(paramName + '= thisJui_typ.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        jui_sal = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('juice_salience.csv'),
            seed=None, name='jui_sal')
        thisExp.addLoop(jui_sal)  # add the loop to the experiment
        thisJui_sal = jui_sal.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisJui_sal.rgb)
        if thisJui_sal != None:
            for paramName in thisJui_sal.keys():
                exec(paramName + '= thisJui_sal.' + paramName)
        
        for thisJui_sal in jui_sal:
            currentLoop = jui_sal
            # abbreviate parameter names if possible (e.g. rgb = thisJui_sal.rgb)
            if thisJui_sal != None:
                for paramName in thisJui_sal.keys():
                    exec(paramName + '= thisJui_sal.' + paramName)
            
            # set up handler to look after randomisation of conditions etc
            disp = data.TrialHandler(nReps=run_dispenser, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='disp')
            thisExp.addLoop(disp)  # add the loop to the experiment
            thisDisp = disp.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDisp.rgb)
            if thisDisp != None:
                for paramName in thisDisp.keys():
                    exec(paramName + '= thisDisp.' + paramName)
            
            for thisDisp in disp:
                currentLoop = disp
                # abbreviate parameter names if possible (e.g. rgb = thisDisp.rgb)
                if thisDisp != None:
                    for paramName in thisDisp.keys():
                        exec(paramName + '= thisDisp.' + paramName)
                
                # ------Prepare to start Routine "supl_jui"-------
                t = 0
                supl_juiClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.500000)
                # update component parameters for each repeat
                pump_indx = current_pump
                # randomly takes one of the first three pumps
                # sends pump vol | the initial amount should be set at 1ml 
                
                # fetch correct one from initial definition of pumps
                pump = pumps[pump_indx]
                
                
                #dev.write(pump)
                # after it sends, it should wait a bit 
                
                text_4.setText(pump)
                jui_pic.setImage(curr_juice)
                # keep track of which components have finished
                supl_juiComponents = [text_4, jui_pic]
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
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_4.status == STARTED and t >= frameRemains:
                        text_4.setAutoDraw(False)
                    
                    # *jui_pic* updates
                    if t >= 0.0 and jui_pic.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        jui_pic.tStart = t
                        jui_pic.frameNStart = frameN  # exact frame index
                        jui_pic.setAutoDraw(True)
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if jui_pic.status == STARTED and t >= frameRemains:
                        jui_pic.setAutoDraw(False)
                    
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
                
            # completed run_dispenser repeats of 'disp'
            
            # get names of stimulus parameters
            if disp.trialList in ([], [None], None):
                params = []
            else:
                params = disp.trialList[0].keys()
            # save data for this loop
            disp.saveAsExcel(filename + '.xlsx', sheetName='disp',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            disp.saveAsText(filename + 'disp.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # ------Prepare to start Routine "ev_jui"-------
            t = 0
            ev_juiClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            juice_resp = event.BuilderKeyResponse()
            # this is the question it randomly pulls from the .csv file
            curr_q = current_question
            
            text_30.setText(current_question)
            # keep track of which components have finished
            ev_juiComponents = [juice_resp, text_30, first_2, second_2, third_2, fourth_2, fifth_2, sixth_2, text_31, text_32, text_33, text_34, text_35, text_22]
            for thisComponent in ev_juiComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "ev_jui"-------
            while continueRoutine:
                # get current time
                t = ev_juiClock.getTime()
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
                for thisComponent in ev_juiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ev_jui"-------
            for thisComponent in ev_juiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if juice_resp.keys in ['', [], None]:  # No response was made
                juice_resp.keys=None
            jui_sal.addData('juice_resp.keys',juice_resp.keys)
            if juice_resp.keys != None:  # we had a response
                jui_sal.addData('juice_resp.rt', juice_resp.rt)
            
            juice_type = curr_juice.split('.').split('//')[1]
            
            tmp_dict[juice] = [juice_resp.keys, sav_mapping]
            
            
            
            # the Routine "ev_jui" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "jui_fe"-------
            t = 0
            jui_feClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            # changes colors
            opt_1, opt_2, opt_3, opt_4, opt_5, opt_6 = color_change(juice_resp.keys, options)
            
            # selects correct part
            opt_1, opt_2, opt_3, opt_4, opt_5, opt_6 = opt_1[1], opt_2[1], opt_3[1], opt_4[1], opt_5[1], opt_6[1]
            
            # current pump
            #jui = str(int(pump.encode('hex'), 16))[-1]
            stor_jui_eval[juice].append(int(juice_resp.keys))
            
            if juice_trial == 1:
                run_dispenser = 0
                # water
            
            first_feedback_2.setFillColor(opt_1)
            second_feedback_2.setFillColor(opt_2)
            third_feedback_2.setFillColor(opt_3)
            fourth_feedback_2.setFillColor(opt_4)
            fifth_feedback_2.setFillColor(opt_5)
            sixth_feedback_2.setFillColor(opt_6)
            # keep track of which components have finished
            jui_feComponents = [first_feedback_2, second_feedback_2, third_feedback_2, fourth_feedback_2, fifth_feedback_2, sixth_feedback_2, text_36, text_37, text_38, text_39, text_40, text_25]
            for thisComponent in jui_feComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "jui_fe"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = jui_feClock.getTime()
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
                for thisComponent in jui_feComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "jui_fe"-------
            for thisComponent in jui_feComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            act_vol = int(pump.encode('hex'), 16)
            
            
            
            
            # set up handler to look after randomisation of conditions etc
            disp_c = data.TrialHandler(nReps=run_water, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='disp_c')
            thisExp.addLoop(disp_c)  # add the loop to the experiment
            thisDisp_c = disp_c.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDisp_c.rgb)
            if thisDisp_c != None:
                for paramName in thisDisp_c.keys():
                    exec(paramName + '= thisDisp_c.' + paramName)
            
            for thisDisp_c in disp_c:
                currentLoop = disp_c
                # abbreviate parameter names if possible (e.g. rgb = thisDisp_c.rgb)
                if thisDisp_c != None:
                    for paramName in thisDisp_c.keys():
                        exec(paramName + '= thisDisp_c.' + paramName)
                
                # ------Prepare to start Routine "water_disp"-------
                t = 0
                water_dispClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.500000)
                # update component parameters for each repeat
                if juice_trial == 3:
                #    dev.write('\4')
                    continue
                
                juice_trial += 1
                
                if juice_trial == 4:
                    run_dispenser = 1
                    juice_trial = 1
                
                # keep track of which components have finished
                water_dispComponents = [cross_sign]
                for thisComponent in water_dispComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "water_disp"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = water_dispClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *cross_sign* updates
                    if t >= 0.0 and cross_sign.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        cross_sign.tStart = t
                        cross_sign.frameNStart = frameN  # exact frame index
                        cross_sign.setAutoDraw(True)
                    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if cross_sign.status == STARTED and t >= frameRemains:
                        cross_sign.setAutoDraw(False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in water_dispComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "water_disp"-------
                for thisComponent in water_dispComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
                thisExp.nextEntry()
                
            # completed run_water repeats of 'disp_c'
            
            # get names of stimulus parameters
            if disp_c.trialList in ([], [None], None):
                params = []
            else:
                params = disp_c.trialList[0].keys()
            # save data for this loop
            disp_c.saveAsExcel(filename + '.xlsx', sheetName='disp_c',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            disp_c.saveAsText(filename + 'disp_c.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
        # completed 1 repeats of 'jui_sal'
        
        # get names of stimulus parameters
        if jui_sal.trialList in ([], [None], None):
            params = []
        else:
            params = jui_sal.trialList[0].keys()
        # save data for this loop
        jui_sal.saveAsExcel(filename + '.xlsx', sheetName='jui_sal',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        jui_sal.saveAsText(filename + 'jui_sal.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed 1 repeats of 'jui_typ'
    
    # get names of stimulus parameters
    if jui_typ.trialList in ([], [None], None):
        params = []
    else:
        params = jui_typ.trialList[0].keys()
    # save data for this loop
    jui_typ.saveAsExcel(filename + '.xlsx', sheetName='jui_typ',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    jui_typ.saveAsText(filename + 'jui_typ.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "jui_out"-------
    t = 0
    jui_outClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    summed = []
    for key, values in zip(stor_jui_eval.keys(), stor_jui_eval.values()):
        tmp_val = 0
        for value in values:
            tmp_val += value
        summed.append((key, tmp_val/3)) # we get the mean because we ask them 3 questions
    
    # picks the max and if there's more than one it picks one randomly
    # we then later ask to reconfirm their favourite juice 
    fav_juice = max(summed, key=lambda item:item[1])[0] # take the first element
    
    
    
    
    
    
    
    juice_conf = event.BuilderKeyResponse()
    image_14.setImage(fav_juice)
    # keep track of which components have finished
    jui_outComponents = [text_41, juice_conf, text_70, image_14]
    for thisComponent in jui_outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jui_out"-------
    while continueRoutine:
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
        
        # *juice_conf* updates
        if t >= 1 and juice_conf.status == NOT_STARTED:
            # keep track of start time/frame for later
            juice_conf.tStart = t
            juice_conf.frameNStart = frameN  # exact frame index
            juice_conf.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(juice_conf.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if juice_conf.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                juice_conf.keys = theseKeys[-1]  # just the last key pressed
                juice_conf.rt = juice_conf.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_70* updates
        if t >= 1 and text_70.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_70.tStart = t
            text_70.frameNStart = frameN  # exact frame index
            text_70.setAutoDraw(True)
        
        # *image_14* updates
        if t >= 0.0 and image_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_14.tStart = t
            image_14.frameNStart = frameN  # exact frame index
            image_14.setAutoDraw(True)
        
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
    if juice_conf.keys == 'y':
        run_juice_reeval = 0
    else:
        run_juice_reeval = 1
    
    # check responses
    if juice_conf.keys in ['', [], None]:  # No response was made
        juice_conf.keys=None
    trials.addData('juice_conf.keys',juice_conf.keys)
    if juice_conf.keys != None:  # we had a response
        trials.addData('juice_conf.rt', juice_conf.rt)
    # the Routine "jui_out" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    juice_re = data.TrialHandler(nReps=run_juice_reeval, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='juice_re')
    thisExp.addLoop(juice_re)  # add the loop to the experiment
    thisJuice_re = juice_re.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisJuice_re.rgb)
    if thisJuice_re != None:
        for paramName in thisJuice_re.keys():
            exec(paramName + '= thisJuice_re.' + paramName)
    
    for thisJuice_re in juice_re:
        currentLoop = juice_re
        # abbreviate parameter names if possible (e.g. rgb = thisJuice_re.rgb)
        if thisJuice_re != None:
            for paramName in thisJuice_re.keys():
                exec(paramName + '= thisJuice_re.' + paramName)
        
        # ------Prepare to start Routine "jui_re"-------
        t = 0
        jui_reClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        juice_pics = ['stimuli//applejuice.png', 'stimuli//orangejuice.png', 'stimuli//pineapplejuice.png']
        
        random.shuffle(juice_pics)
        
        juice_1, juice_2, juice_3 = juice_pics
        juice_reeval = event.BuilderKeyResponse()
        image_11.setImage(juice_1)
        image_12.setImage(juice_2)
        image_13.setImage(juice_3)
        key_resp_8 = event.BuilderKeyResponse()
        # keep track of which components have finished
        jui_reComponents = [juice_reeval, text_42, text_43, image_11, image_12, image_13, key_resp_8]
        for thisComponent in jui_reComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "jui_re"-------
        while continueRoutine:
            # get current time
            t = jui_reClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *juice_reeval* updates
            if t >= 0.0 and juice_reeval.status == NOT_STARTED:
                # keep track of start time/frame for later
                juice_reeval.tStart = t
                juice_reeval.frameNStart = frameN  # exact frame index
                juice_reeval.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(juice_reeval.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if juice_reeval.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    juice_reeval.keys = theseKeys[-1]  # just the last key pressed
                    juice_reeval.rt = juice_reeval.clock.getTime()
            
            # *text_42* updates
            if t >= 0.0 and text_42.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_42.tStart = t
                text_42.frameNStart = frameN  # exact frame index
                text_42.setAutoDraw(True)
            
            # *text_43* updates
            if t >= 3 and text_43.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_43.tStart = t
                text_43.frameNStart = frameN  # exact frame index
                text_43.setAutoDraw(True)
            
            # *image_11* updates
            if t >= 0.0 and image_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_11.tStart = t
                image_11.frameNStart = frameN  # exact frame index
                image_11.setAutoDraw(True)
            
            # *image_12* updates
            if t >= 0.0 and image_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_12.tStart = t
                image_12.frameNStart = frameN  # exact frame index
                image_12.setAutoDraw(True)
            
            # *image_13* updates
            if t >= 0.0 and image_13.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_13.tStart = t
                image_13.frameNStart = frameN  # exact frame index
                image_13.setAutoDraw(True)
            
            # *key_resp_8* updates
            if t >= 3 and key_resp_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_8.tStart = t
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_8.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_8.rt = key_resp_8.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in jui_reComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "jui_re"-------
        for thisComponent in jui_reComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fav_juice = juice_reeval.keys
        # check responses
        if juice_reeval.keys in ['', [], None]:  # No response was made
            juice_reeval.keys=None
        juice_re.addData('juice_reeval.keys',juice_reeval.keys)
        if juice_reeval.keys != None:  # we had a response
            juice_re.addData('juice_reeval.rt', juice_reeval.rt)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys=None
        juice_re.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            juice_re.addData('key_resp_8.rt', key_resp_8.rt)
        # the Routine "jui_re" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_juice_reeval repeats of 'juice_re'
    
    # get names of stimulus parameters
    if juice_re.trialList in ([], [None], None):
        params = []
    else:
        params = juice_re.trialList[0].keys()
    # save data for this loop
    juice_re.saveAsExcel(filename + '.xlsx', sheetName='juice_re',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    juice_re.saveAsText(filename + 'juice_re.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
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

# ------Prepare to start Routine "test"-------
t = 0
testClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
background_image.setAutoDraw(True)
text_50.setText(matrix_trial)
text_64.setText(stor_matrix_ans)
# keep track of which components have finished
testComponents = [text_50, text_64, text_65, text_73]
for thisComponent in testComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = testClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_50* updates
    if t >= 0.0 and text_50.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_50.tStart = t
        text_50.frameNStart = frameN  # exact frame index
        text_50.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_50.status == STARTED and t >= frameRemains:
        text_50.setAutoDraw(False)
    
    # *text_64* updates
    if t >= 0.0 and text_64.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_64.tStart = t
        text_64.frameNStart = frameN  # exact frame index
        text_64.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_64.status == STARTED and t >= frameRemains:
        text_64.setAutoDraw(False)
    
    # *text_65* updates
    if t >= 0.0 and text_65.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_65.tStart = t
        text_65.frameNStart = frameN  # exact frame index
        text_65.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_65.status == STARTED and t >= frameRemains:
        text_65.setAutoDraw(False)
    
    # *text_73* updates
    if t >= 0.0 and text_73.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_73.tStart = t
        text_73.frameNStart = frameN  # exact frame index
        text_73.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_73.status == STARTED and t >= frameRemains:
        text_73.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test"-------
for thisComponent in testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
main_loop = data.TrialHandler(nReps=run_all, method='random', 
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
                # changes colors
                opt_1, opt_2, opt_3, opt_4, opt_5, opt_6 = color_change(ev_resp.keys, options)
                
                # selects correct part
                opt_1, opt_2, opt_3, opt_4, opt_5, opt_6 = opt_1[1], opt_2[1], opt_3[1], opt_4[1], opt_5[1], opt_6[1]
                
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
            
            # ------Prepare to start Routine "eff_press"-------
            t = 0
            eff_pressClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_4 = event.BuilderKeyResponse()
            # keep track of which components have finished
            eff_pressComponents = [key_resp_4, image_8, image_9, image_10, text_28, text_62, text_63]
            for thisComponent in eff_pressComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_press"-------
            while continueRoutine:
                # get current time
                t = eff_pressClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
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
                
                # *image_8* updates
                if t >= 0.0 and image_8.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_8.tStart = t
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_8.status == STARTED and t >= frameRemains:
                    image_8.setAutoDraw(False)
                
                # *image_9* updates
                if t >= 0.0 and image_9.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_9.tStart = t
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_9.status == STARTED and t >= frameRemains:
                    image_9.setAutoDraw(False)
                
                # *image_10* updates
                if t >= 0.0 and image_10.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_10.tStart = t
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_10.status == STARTED and t >= frameRemains:
                    image_10.setAutoDraw(False)
                
                # *text_28* updates
                if t >= 0.0 and text_28.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_28.tStart = t
                    text_28.frameNStart = frameN  # exact frame index
                    text_28.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_28.status == STARTED and t >= frameRemains:
                    text_28.setAutoDraw(False)
                
                # *text_62* updates
                if t >= 0.0 and text_62.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_62.tStart = t
                    text_62.frameNStart = frameN  # exact frame index
                    text_62.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_62.status == STARTED and t >= frameRemains:
                    text_62.setAutoDraw(False)
                
                # *text_63* updates
                if t >= 0.0 and text_63.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_63.tStart = t
                    text_63.frameNStart = frameN  # exact frame index
                    text_63.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_63.status == STARTED and t >= frameRemains:
                    text_63.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in eff_pressComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_press"-------
            for thisComponent in eff_pressComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys=None
            effort_role.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                effort_role.addData('key_resp_4.rt', key_resp_4.rt)
            # the Routine "eff_press" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "eff_feed"-------
            t = 0
            eff_feedClock.reset()  # clock
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
            eff_feedComponents = [text_11]
            for thisComponent in eff_feedComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_feed"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = eff_feedClock.getTime()
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
                for thisComponent in eff_feedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_feed"-------
            for thisComponent in eff_feedComponents:
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
            beg_fixComponents = [text, image_7]
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
                
                # *image_7* updates
                if t >= 0.0 and image_7.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_7.tStart = t
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_7.status == STARTED and t >= frameRemains:
                    image_7.setAutoDraw(False)
                
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
    
# completed run_all repeats of 'main_loop'

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

# ------Prepare to start Routine "cog_eff_fin"-------
t = 0
cog_eff_finClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
cog_eff_finComponents = []
for thisComponent in cog_eff_finComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "cog_eff_fin"-------
while continueRoutine:
    # get current time
    t = cog_eff_finClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cog_eff_finComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cog_eff_fin"-------
for thisComponent in cog_eff_finComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "cog_eff_fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "cog_eff_fin_answ"-------
t = 0
cog_eff_fin_answClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
cog_eff_fin_answComponents = []
for thisComponent in cog_eff_fin_answComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "cog_eff_fin_answ"-------
while continueRoutine:
    # get current time
    t = cog_eff_fin_answClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cog_eff_fin_answComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cog_eff_fin_answ"-------
for thisComponent in cog_eff_fin_answComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "cog_eff_fin_answ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
nasa_trials = data.TrialHandler(nReps=run_nasa, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nasa_tlx.csv'),
    seed=None, name='nasa_trials')
thisExp.addLoop(nasa_trials)  # add the loop to the experiment
thisNasa_trial = nasa_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNasa_trial.rgb)
if thisNasa_trial != None:
    for paramName in thisNasa_trial.keys():
        exec(paramName + '= thisNasa_trial.' + paramName)

for thisNasa_trial in nasa_trials:
    currentLoop = nasa_trials
    # abbreviate parameter names if possible (e.g. rgb = thisNasa_trial.rgb)
    if thisNasa_trial != None:
        for paramName in thisNasa_trial.keys():
            exec(paramName + '= thisNasa_trial.' + paramName)
    
    # ------Prepare to start Routine "nasa_tlx"-------
    t = 0
    nasa_tlxClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    nasa_question = current_question
    nasa_tlx_text.setText(nasa_question)
    rating_3.reset()
    # keep track of which components have finished
    nasa_tlxComponents = [nasa_tlx_text, rating_3]
    for thisComponent in nasa_tlxComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "nasa_tlx"-------
    while continueRoutine:
        # get current time
        t = nasa_tlxClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *nasa_tlx_text* updates
        if t >= 0.0 and nasa_tlx_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            nasa_tlx_text.tStart = t
            nasa_tlx_text.frameNStart = frameN  # exact frame index
            nasa_tlx_text.setAutoDraw(True)
        # *rating_3* updates
        if t >= 0.0 and rating_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_3.tStart = t
            rating_3.frameNStart = frameN  # exact frame index
            rating_3.setAutoDraw(True)
        continueRoutine &= rating_3.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nasa_tlxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nasa_tlx"-------
    for thisComponent in nasa_tlxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # store data for nasa_trials (TrialHandler)
    nasa_trials.addData('rating_3.response', rating_3.getRating())
    nasa_trials.addData('rating_3.rt', rating_3.getRT())
    # the Routine "nasa_tlx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed run_nasa repeats of 'nasa_trials'

# get names of stimulus parameters
if nasa_trials.trialList in ([], [None], None):
    params = []
else:
    params = nasa_trials.trialList[0].keys()
# save data for this loop
nasa_trials.saveAsExcel(filename + '.xlsx', sheetName='nasa_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
nasa_trials.saveAsText(filename + 'nasa_trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "juice_eval"-------
t = 0
juice_evalClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
theseKeys="" 
shift_flag = False
continue_key = event.BuilderKeyResponse()
juice_valuation = event.BuilderKeyResponse()
# keep track of which components have finished
juice_evalComponents = [quest_prompt, continue_key, resp_box, juice_valuation]
for thisComponent in juice_evalComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "juice_eval"-------
while continueRoutine:
    # get current time
    t = juice_evalClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    n= len(theseKeys)
    i = 0
    while i < n:
    
        if theseKeys[i] == 'backspace':
            inputText = inputText[:-1]  # lose the final character
            i = i + 1
    
        elif theseKeys[i] == 'space':
            inputText += ' '
            i = i + 1
    
        elif theseKeys[i] in ['lshift', 'rshift']:
            shift_flag = True
            i = i + 1
    
        else:
            if len(theseKeys[i]) == 1:
                # we only have 1 char so should be a normal key, 
                # otherwise it might be 'ctrl' or similar so ignore it
                if shift_flag:
                    inputText += chr( ord(theseKeys[i]) - ord(' '))
                    shift_flag = False
                else:
                    inputText += theseKeys[i]
    
            i = i + 1
    
    
    
    
    
    
    # *quest_prompt* updates
    if t >= 0.0 and quest_prompt.status == NOT_STARTED:
        # keep track of start time/frame for later
        quest_prompt.tStart = t
        quest_prompt.frameNStart = frameN  # exact frame index
        quest_prompt.setAutoDraw(True)
    
    # *continue_key* updates
    if t >= 0.0 and continue_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        continue_key.tStart = t
        continue_key.frameNStart = frameN  # exact frame index
        continue_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(continue_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if continue_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            continue_key.keys = theseKeys[-1]  # just the last key pressed
            continue_key.rt = continue_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *resp_box* updates
    if t >= 0.0 and resp_box.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_box.tStart = t
        resp_box.frameNStart = frameN  # exact frame index
        resp_box.setAutoDraw(True)
    if resp_box.status == STARTED:  # only update if drawing
        resp_box.setText((inputText), log=False)
    
    # *juice_valuation* updates
    if t >= 0.0 and juice_valuation.status == NOT_STARTED:
        # keep track of start time/frame for later
        juice_valuation.tStart = t
        juice_valuation.frameNStart = frameN  # exact frame index
        juice_valuation.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(juice_valuation.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if juice_valuation.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            juice_valuation.keys.extend(theseKeys)  # storing all keys
            juice_valuation.rt.append(juice_valuation.clock.getTime())
    
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
inputText=""
# check responses
if continue_key.keys in ['', [], None]:  # No response was made
    continue_key.keys=None
thisExp.addData('continue_key.keys',continue_key.keys)
if continue_key.keys != None:  # we had a response
    thisExp.addData('continue_key.rt', continue_key.rt)
thisExp.nextEntry()
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
final_pic_eval_trials = data.TrialHandler(nReps=run_pic_eval_e, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pic_rating.csv'),
    seed=None, name='final_pic_eval_trials')
thisExp.addLoop(final_pic_eval_trials)  # add the loop to the experiment
thisFinal_pic_eval_trial = final_pic_eval_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFinal_pic_eval_trial.rgb)
if thisFinal_pic_eval_trial != None:
    for paramName in thisFinal_pic_eval_trial.keys():
        exec(paramName + '= thisFinal_pic_eval_trial.' + paramName)

for thisFinal_pic_eval_trial in final_pic_eval_trials:
    currentLoop = final_pic_eval_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFinal_pic_eval_trial.rgb)
    if thisFinal_pic_eval_trial != None:
        for paramName in thisFinal_pic_eval_trial.keys():
            exec(paramName + '= thisFinal_pic_eval_trial.' + paramName)
    
    # ------Prepare to start Routine "ev_pic"-------
    t = 0
    ev_picClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # this is the question it randomly pulls from the .csv file
    pic_q = current_question
    
    # this is added because by having an id of the question
    # where the questions are randomised, we can simply store it
    # later
    tmp_list.append(sav_mapping)
    rating_2.reset()
    image_2.setImage(pic_q)
    # keep track of which components have finished
    ev_picComponents = [rating_2, image_2, text_49]
    for thisComponent in ev_picComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ev_pic"-------
    while continueRoutine:
        # get current time
        t = ev_picClock.getTime()
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
        for thisComponent in ev_picComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ev_pic"-------
    for thisComponent in ev_picComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stor_pic_q.append(rating_2.getRating())
    
    tmp_trial += 1
    
    if tmp_trial == 7: # end of questions about pictures
    
        complete = set_filename(part_char, 'pic_q(pic_rating.csv)')
        pic_q_data = open(complete, 'w')
        
        for el in tmp_list:
            struct_1 += "pic" + str(el) + "\t"
        
        struct_1 += "sub_id\n"  #subid
    
        pic_q_data.write(struct_1)
        
        
        for i in range(0, len(stor_pic_q)):
            struct_2 += "{}\t"
    
        struct_2 += "{}\n"
    
        tmp_list = stor_pic_q
        tmp_list.append(part_char[1])
    
        pic_q_data.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3],
                                         tmp_list[4], tmp_list[5], tmp_list[6]))
        pic_q_data.close()
    
        struct_1 = ''
        struct_2 = ''
        tmp_list = []
    # store data for final_pic_eval_trials (TrialHandler)
    final_pic_eval_trials.addData('rating_2.response', rating_2.getRating())
    # the Routine "ev_pic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed run_pic_eval_e repeats of 'final_pic_eval_trials'

# get names of stimulus parameters
if final_pic_eval_trials.trialList in ([], [None], None):
    params = []
else:
    params = final_pic_eval_trials.trialList[0].keys()
# save data for this loop
final_pic_eval_trials.saveAsExcel(filename + '.xlsx', sheetName='final_pic_eval_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
final_pic_eval_trials.saveAsText(filename + 'final_pic_eval_trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "final_screen"-------
t = 0
final_screenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
final_screenComponents = [text_48]
for thisComponent in final_screenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "final_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = final_screenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_48* updates
    if t >= 0.0 and text_48.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_48.tStart = t
        text_48.frameNStart = frameN  # exact frame index
        text_48.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_48.status == STARTED and t >= frameRemains:
        text_48.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_screen"-------
for thisComponent in final_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

























# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
