#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.2),
    on January 21, 2019, at 13:42
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('3')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.0.2'
expName = 'psreff3'  # from the Builder filename that created this script
expInfo = {u'participant': u'9999', u'go_pract': u'5', u'eff_pract': u'4', u'age': u'1992-11-12', u'run_first': u'1', u'sample': u'1', u'run_second': u'1', u're_o': u'1', u'g_conn': u'1', u'type': u'1', u'pic_eval': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\Experiments\\UCL\\Sebastijan\\PrimarySecondaryReward\\Experiment\\psreff_t.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='default', color=[1, 1, 1], colorSpace='rgb',
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
import glob
import math as m
import itertools


################################################################################################
############################## set up eye tracker ##############################################
################################################################################################
from psychopy_tobii_controller import tobii_controller

try:
    controller = tobii_controller(win)
    et_connected = 1
except:
    et_connected = 0


################################################################################################
########### listing all the functions in the experiment ########################################
################################################################################################

def mean(inp):
    return float(sum(inp))/len(inp)

def std(inp):
    tmp = 0
    avg = mean(inp)
    for el in inp:
        tmp += (el - avg)**2
    if len(inp) == 1:
        return m.sqrt(tmp/len(inp)) # computes pop std, happens only on first trial
    else:
        return m.sqrt(tmp/(len(inp) - 1)) # computes sample std
    
def transform_information(diffs, t_scores):
    diff_levels = ['easiest', 'easy', 'medium', 'hard'] # we run this just once so I can initialise it inside the function
    diffs_copy = deepcopy(diffs)
    for idx, diff in enumerate(diffs_copy):
    
        for idx2, t in enumerate(t_scores):
            if diff == diff_levels[idx2]:
                diffs_copy[idx] = t_scores[idx2]

    return diffs_copy

def get_current_text(texts, trial):
    return texts[trial]

def stop_sequence(trial, limit, runner):
    if trial == len(limit):
        runner = 0
        trial = 1
    return [trial, runner]


def get_input_box(dict_inp, key, type):
    tmp = dict_inp[key]
    if type == 1: # int
        return int(tmp)
    else:
        return str(tmp)


def save_ev(ev_dataset, ev_f):
    
    ev_f.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \n".format(
                                                                                          ev_dataset[0], \
                                                                                          ev_dataset[1], \
                                                                                          ev_dataset[2], \
                                                                                          ev_dataset[3], \
                                                                                          ev_dataset[4], \
                                                                                          ev_dataset[5], \
                                                                                          ev_dataset[6], \
                                                                                          ev_dataset[7], \
                                                                                          ev_dataset[8], \
                                                                                          ev_dataset[9], \
                                                                                          ev_dataset[10], \
                                                                                          ev_dataset[11]))

def save_eff(eff_dataset, eff_f):
    
    
    eff_f.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \n".format(
                                                                  eff_dataset[0], \
                                                                  eff_dataset[1], \
                                                                  eff_dataset[2], \
                                                                  eff_dataset[3], \
                                                                  eff_dataset[4], \
                                                                  eff_dataset[5], \
                                                                  eff_dataset[6]))

def save_go(go_dataset, go_f):

    go_f.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \n".format(
                                                                                                    go_dataset[0], \
                                                                                                    go_dataset[1], \
                                                                                                    go_dataset[2], \
                                                                                                    go_dataset[3], \
                                                                                                    go_dataset[4], \
                                                                                                    go_dataset[5], \
                                                                                                    go_dataset[6], \
                                                                                                    go_dataset[7], \
                                                                                                    go_dataset[8], \
                                                                                                    go_dataset[9], \
                                                                                                    go_dataset[10], \
                                                                                                    go_dataset[11], \
                                                                                                    go_dataset[12]))




def fill_keys(dict, keys):
    for k in keys:
        dict.setdefault(k, [])
    return dict

def gen_stim_path(inp):
    return 'stimuli/' + inp + '.png'
    #return 'stimuli//' + inp + '.png'

def set_matrix(indx, stim_list, stim_corr_ans):
    return [stim_list[indx], stim_corr_ans[indx]]

options = [(1, [0.2, 0.2, 0.2]), \
           (2, [0.2, 0.2, 0.2]), \
           (3, [0.2, 0.2, 0.2]), \
           (4, [0.2, 0.2, 0.2]), \
           (5, [0.2, 0.2, 0.2]), \
           (6, [0.2, 0.2, 0.2])]


def color_change(picked_opt, options):
    copy_options = deepcopy(options)                                           # this way we preserve the original

    ch_option = [1, 0.84, 0.0]
    unch_col = [0.2, 0.2, 0.2]

    for indx, option in enumerate(options):
        if str(option[0]) == picked_opt:
            tmp = list(options[indx])                                          # hack to remove issues with deleting
            del tmp[1]
            tmp.append(ch_option)
            copy_options[indx] = tuple(tmp)
        else:
            copy_options[indx] = tuple([indx+1, unch_col])
    return copy_options



def matrix_response(answer, correct_answer, container, curr_matrix):
    responded_correctly = answer.keys == str(correct_answer)
        
    curr_matrix = curr_matrix.split('-')[0][-2:]                              # fetches the string of the item

    if responded_correctly:
        container[curr_matrix] = 1
    else:
        container[curr_matrix] = 0

    return [responded_correctly, container]

def trial_evaluater(container):
    if sum(container[-3:]) == 0 and len(container) >= 6:                    # maybe change this but this assumes noone will have less
        return 1                                                              # than the first 10 incorrect



def reverse_correction(matrix_trial, indx, aux_container, response, tmp):

    reverse_corrected = 0                                                      # these act as default values for the variables 
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

def matrix_resp_parser(container):                          # deprecated 
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

#    ctr = 0                                               # recursively checks if the file already exists, if it doesn't it stops
#    fname = check_file(fname, part_char[4], ctr)          # TODO: Fix. It should work anyway because the date stamp is in the filename 
                                                           # so it's basically impossible there will be an overlap. 
    complete = part_char[4] + "/data/" + fname
    #complete = part_char[4] + "\\data\\" + fname

    return complete


 
def check_file(filename, cwd, ctr):                     # this works but make it nicer so it adds up files together in a nicer way
    for file in os.listdir(cwd):
        if file.endswith('.txt'):
            if file != filename:                                                       # if a file doesnt exist just return the fname
                return filename
            else:
                tmp = file.split('_')
                tmp[1] = tmp[1] + '_' + str(ctr)                                      # our new sub_id is now id_ctr 
                ctr += 1                                                               # increment for recursivity 
                filename = '_'.join(tmp)                                               # rename the file
                check_file(filename, cwd, ctr) 


# function that finds the correct age bracket 
def find_age_bracket(part_year, part_month, age_list, part_type):
    corr_brack = ''
    for bracket in age_list:
        if part_type == 2:
            split_bracket = bracket.split('-')
            lb, ub = split_bracket[0].split(':'), split_bracket[1].split(':')         # split into upper and lower 
            lyr, lmth, uyr, umth = int(lb[0]), int(lb[1]), int(ub[0]), int(ub[1])    # index years - 0, and months - 1
        else:
            bound = bracket.split('-')
            lyr, uyr = int(bound[0]), int(bound[1])                                   # split into upper and lower
        if part_type == 2:
            try:
                if (lyr <= part_year <= uyr) and (lmth <= part_month <= umth):
                    corr_brack = bracket                                                # this means the participant falls into this bracket
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

def get_juice_name(info):
    if info == 0:
        juice_type = "apple"
    elif info == 1:
        juice_type = "orange"
    elif info == 2:
        juice_type = "pineapple"

    return juice_type 


def get_juice_pump(info):
    juice_id = ''
    juice_vol = ''
    if info == 'apple':
        juice_id = '\1'
        juice_vol = '\13'
    elif info == 'orange':
        juice_id = '\2'
        juice_vol = '\14'
    elif info == 'pineapple':
        juice_id = '\3'
        juice_vol = '\15'
    print(juice_id, juice_vol)
    return [juice_id, juice_vol]


def decode_gustaf(dev_name):
    tmp = dev_name.readlines()[0]                                                        # takes the string out
    
    try:
        pump_nr, pump_times, vol = int(tmp[0].encode('hex'), 16), int(tmp[1].encode('hex'), 16), int(tmp[2].encode('hex'), 16)*100
    except:
        print("Something went wrong {}".format(tmp))
        pump_nr, pump_times, vol = -1, -1, -1
        pass
    
    return [pump_nr, pump_times, vol]


def save_juice_eval(part_char, container):

    struct_1 = ''
    struct_2 = ''

    complete = set_filename(part_char, 'ev_juice(juice_salience.csv)')
    ev_juice_data = open(complete, 'w')

    tmp_len = len(container['apple']) + 1                        # for 3 questions. we want nice naming not indexing
                                                                  # the key indexed doesnt matter because its the same for all
    for i in range(1, tmp_len): 
        struct_1 += "question" + str(i) + "\t"

    struct_1 += "act_pump\tact_pump_nr\tact_vol\tsub_id\n"

    ev_juice_data.write(struct_1)

    for i in range(0, tmp_len - 1):                              # we can just take the length of one of the keys because
        struct_2 += "{}\t"                                        # all of them have the same length

    struct_2 += "{}\t{}\t{}\t{}\n"                                # for pump, volume, and subid


    for el  in container.keys():
        
        tmp_list = container[el]
        tmp_list.sort(key=lambda x: x[1])
        tmp = [tmp_list[0][2], tmp_list[0][3], tmp_list[0][4]]  # this is equivalent to pump_nr, pump_times and vol 
        tmp_list = [tl[0] for tl in tmp_list]                    # take just the responses
        for el in tmp:
            tmp_list.append(el)
        tmp_list.append(part_char[1])                             # add sub_id 

                                                                  # we want to store the responses as an integers
        ev_juice_data.write(struct_2.format(int(tmp_list[0]), int(tmp_list[1]), int(tmp_list[2]), tmp_list[3],
                                     tmp_list[4], tmp_list[5], tmp_list[6]))

    ev_juice_data.close()
    print("Successfully saved the juice evaluation dataset.")



def determine_sequence(type, case, ender):

    if type == 1:
        if case == 'beg':
            run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'rew':
            run_rew, run_ev, run_effort, run_go = 0, 1, 0, 0
        elif case == 'ev':
            run_rew, run_ev, run_effort, run_go = 0, 0, 76, 0           # effort should be at 76 repetitions to account for 
        elif case == 'eff':                                             # 72 real trials + 4 practice trials 
            run_rew, run_ev, run_effort, run_go = 0, 0, 0, 1
        elif case == 'go':
            if ender:
                run_rew, run_ev, run_effort, run_go = 0, 0, 0, 0
            else:
                run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0

    if type == 2:
        if case == 'beg':
            run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'rew':
            run_rew, run_ev, run_effort, run_go = 0, 1, 0, 0
        elif case == 'ev':
            run_rew, run_ev, run_effort, run_go = 0, 0, 0, 1
        elif case == 'eff':
            if ender:
                run_rew, run_ev, run_effort, run_go = 0, 0, 0, 0
            else:
                run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0

        elif case == 'go':
            run_rew, run_ev, run_effort, run_go = 0, 0, 76, 0

    if type == 3:
        if case == 'beg':
            run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'rew':
            run_rew, run_ev, run_effort, run_go = 0, 0, 76, 0
        elif case == 'ev':
            run_rew, run_ev, run_effort, run_go = 0, 0, 0, 1
        elif case == 'eff':
            run_rew, run_ev, run_effort, run_go = 0, 1, 0, 0
        elif case == 'go':
            if ender:
                run_rew, run_ev, run_effort, run_go = 0, 0, 0, 0
            else:
                run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0

    if type == 4:
        if case == 'beg':
            run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'rew':
            run_rew, run_ev, run_effort, run_go = 0, 0, 76, 0
        elif case == 'ev':
            if ender:
                run_rew, run_ev, run_effort, run_go = 0, 0, 0, 0
            else:
                run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0

        elif case == 'eff':
            run_rew, run_ev, run_effort, run_go = 0, 0, 0, 1
        elif case == 'go':
            run_rew, run_ev, run_effort, run_go = 0, 1, 0, 0

    if type == 5:
        if case == 'beg':
            run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'rew':
            run_rew, run_ev, run_effort, run_go = 0, 0, 0, 1
        elif case == 'ev':
            run_rew, run_ev, run_effort, run_go = 0, 0, 76, 0
        elif case == 'eff':
            if ender:
                run_rew, run_ev, run_effort, run_go = 0, 0, 0, 0
            else:
                run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'go':
            run_rew, run_ev, run_effort, run_go = 0, 1, 0, 0

    if type == 6:
        if case == 'beg':
            run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0
        elif case == 'rew':
            run_rew, run_ev, run_effort, run_go = 0, 0, 0, 1
        elif case == 'ev':
            if ender:
                run_rew, run_ev, run_effort, run_go = 0, 0, 0, 0
            else:
                run_rew, run_ev, run_effort, run_go = 1, 0, 0, 0

        elif case == 'eff':
            run_rew, run_ev, run_effort, run_go = 0, 1, 0, 0
        elif case == 'go':
            run_rew, run_ev, run_effort, run_go = 0, 0, 76, 0


    return [run_rew, run_ev, run_effort, run_go]


def get_mouse_coord(inp):
    x, y = inp.getPos()[0], inp.getPos()[1] 
    return [x, y]


def evaluate_coordinates(fromx, tox, fromy, toy, actx, acty):
    return (fromx < actx <= tox and fromy < acty <= toy)


def get_mouse_choice_complex(act_x, act_y, list_inp1, list_inp2, type, door1, chest1):
    chosen_option = [gen_stim_path('empty'), gen_stim_path('empty'), 0]            # empty is the name of the image we are going to present by default

    from_x1, to_x1, from_y1, to_y1 = list_inp1
    from_x2, to_x2, from_y2, to_y2 = list_inp2

    if evaluate_coordinates(from_x1, to_x1, from_y1, to_y1, act_x, act_y) and type == 1:
        chosen_option = [door1, chest1, 1]                     # option will be selected with an additional bit of information that the right thing was selected
   
    elif evaluate_coordinates(-to_x1, -from_x1, from_y1, to_y1, act_x, act_y) and type == 2:
        chosen_option = [door1, chest1, 1]

    if evaluate_coordinates(from_x2, to_x2, from_y2, to_y2, act_x, act_y)  and type == 1:
        chosen_option[2] = 1

    elif evaluate_coordinates(-to_x2, -from_x2, from_y2, to_y2, act_x, act_y) and type == 2:
        chosen_option[2] = 1

    return chosen_option


def get_mouse_choice_simple(x, y, from_X, to_x, from_y, to_y, inp):
        if evaluate_coordinates(from_X, to_x, from_y, to_y, x, y):
            return inp
        else:
            return 9

def remove_stim_path(inp):
    return inp.split('/')[1].split('.')[0]

def get_stim_paths(list_inp):

    tmp_list = []

    for inp in list_inp:
        tmp_list.append(gen_stim_path(inp))
    
    return tmp_list

def juice_out(part_char, stor_jui_eval, fav_juice):

    save_juice_eval(part_char, stor_jui_eval)
    out_pump, out_pumpid = get_juice_pump(fav_juice)
    out_path = gen_stim_path(fav_juice)

    tmp_list = [out_pump, out_pumpid, out_path]
    
    return tmp_list


def turn_on_tutorial():
    lh = 0.1
    opac = 1
    return [lh, opac]

def turn_off_tutorial():
    lh = 0.000001
    opac = 0
    return [lh, opac]

def stop_instructions(trial, limit, run_instructions):
    runner = 1

    trial, runner = stop_sequence(trial, limit, runner)

    if not runner:
        run_instructions = 0
        trial  = 0

    trial += 1
    
    tmp_list = [trial, run_instructions]

    return tmp_list

def is_trial(trial, trial_list):
    return any([1 for el in trial_list if el == trial])


################################################################################################
################################# defining basic variables #####################################
################################################################################################

matrix_trial = 1                                  # current trial within the matrix sequence
ev_trial = 1                                      # explicit evaluation trial
eff_trial = 1                                     # hypothetical effort trial
go_trial = 1
juice_trial = 1                                   # runner within the initial juice determination
close_ev = 0
cog_eff_trial = 1
nfc_trial = 0

go_switch = 0                                     # number of switches for the real announcement
eff_switch = 0                                      
ev_switch = 0                                       
num_trials = 38                                  # will decide on the absolute number of trials / this subsumes eff and ev and is akin to abs_trial
num_eff_trials = 144                               # 6 (rew) * 4 (diff) * 3 (repeated)

halfway_go = int(round(num_trials/2))
halfway_eff = int(round(num_eff_trials/2))


run_rew = 1
run_ev = 1
run_effort = 1
run_go = 1


run_nasa = 1                                            # runs the nasa questions
run_fin_eff = 2                                         # run the final cog eff sequence at all
run_prac = 1                                            # used to run either practice or real trials 
run_matrix = 1                                          # current row that is being pulled for the image in the matrix trial
run_dispenser = 1                                       # run juice dispenser in init_q
run_water = 0                                           # run the water dispenser
run_correct = 0                                         # run matrix reevaluation or not
run_pr = 0                                              # run practice | delete?
run_transition = 1                                      # run transition from one task to other
run_real = 0                                            # used to run either practice or real trials 
run_juice_reeval = 0                                    # used to run juice reevaluation
run_est_sal = 100
run_effort_midway = 0 
run_pause = 0
run_fin_eff_tr = 1

tutorial_opac = 0

# instruction runners
run_begin_instr = 100
run_est_sal_instr = 100
run_rew_instr = 100
run_ev_instr = 100
run_eff_instr_mini = 100
run_eff_instr = 100
run_go_instr = 100
run_cog_eff_instr = 100

begin_instr_trial = 1
est_sal_trial = 1
rew_instr_trial = 1
ev_instr_trial = 1
eff_instr_trial = 1
go_instr_trial = 1
cog_eff_instr_trial = 1

num_pauses = 1                                     # defines number of breaks
block_length = num_trials/num_pauses               # defines block length for gng task

already_switched = 0                              # helper variable used in the matrix evaluation procedure
reverse_corrected = 0                             # was the reverse correcetd (e.g. by 1 1)
initiate_reverse = 0                              # initiate reverse sequence in WASI?

responded_correctly = 0                           # was the response correct or not in the matrix case

indx = 0                                          # indexing the item 
diagnostics_info = ''                             # diagnostics string
ctr = 1                                           # used in the pump volume evaluation

pump = ''

cum_amount = 0
turn_off = 0                                        # to not check for reverse correction every time
initial_q = ''                                      # variable for initial questions that determine a participants state
failed_seq = 0                                      # type of sequence failure in case an individual failed the first matrix reasoning trials

juices = ['apple', 'orange', 'pineapple']

# always remember to clean after use 
################################################################################################
################################# generic helper variables #####################################
################################################################################################

tmp_val = 0
tmp = 0                                                # generic helper variable
tmp_list = []                                          # generic helper list
tmp_dict = collections.defaultdict()                   # generic helper dict
tmp_design_matrix = []                                 # this is a special case that doesn't need to be deleted
tmp_evaluater = []                                     # list used for evaluating
                                                       # matrix reasoning correctness
tmp_str = ''
tmp_rt = [0.6] # we initialize with a sensible value that will get removed afterwards
tmp_runner = 100
struct_1 = ''                                          # generic helper variables
struct_2 = ''
tmp_trial = 1                                          # tmp trial is used as a helper counter in various places

response = ''                                          # key used for obtaining the final response from the participants

################################################################################################
################################# creating containers ##########################################
################################################################################################

primary, secondary = [], []
pump_vol = {}
stor_ev = collections.defaultdict()
stor_eff = []
stor_go = []
pump_vol = {}                                          # this gives us a clear mapping between volume and commands to send
stor_init_q = []
stor_pic_q = []
stor_nasa_q = []
stor_jui_eval = collections.defaultdict()
stor_jui_eval = fill_keys(stor_jui_eval, juices)
stor_matrix_ans = {}
stor_aux_ans = []
stor_nfc_q = []

################################################################################################
################################# MR containers ################################################
################################################################################################

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

stim_list = ['stimuli/Sample Item A-1.png', 'stimuli/Sample Item B-1.png']     # generate a second stimuli list

last_matrix = 'stimuli/Item30-1.png'                   # last matrix

for i in range(1, 31):
    if i < 10:
        stim_file = 'stimuli/Item0' + str(i) + '-1.png'
    else:
        stim_file = 'stimuli/Item' + str(i) + '-1.png'
    stim_list.append(stim_file)

                                                                                # this is important for the saving portion 
tmp_list = 30*[None]                                                            # generate empty list with all responses

for i in range(0, 30):                                                         # populate with 0s
    if i < 5:
        tmp_list[i] = 1                                                         # populating with 1s saves trouble later
    else:                                                                       # because we assume people won't be incorrect there
        tmp_list[i] = 0


################################################################################################
################################ pump related information ######################################
################################################################################################


pump_selecter = ['\13', '\14', '\15', '\16']                                   # clear mapping to make sure we know how much to send 
pumps = ['\1', '\2', '\3']

stringed_ctr = str(ctr)
for vol in range(100, 5100, 100):
    while stringed_ctr[-1] == '8' or stringed_ctr[-1] == '9':                # this might not be needed if we have fixed 
        ctr += 1                                                               # quantities of juice being squirted
        stringed_ctr = str(ctr)
    else:
        pump_vol[str(vol)] = ctr
        ctr += 1                       
        stringed_ctr = str(ctr)

for el in pumps:                                    # we preconfigure our container to be a list for each pump
    jui = str(int(el.encode('hex'), 16))
    stor_jui_eval[jui] = []

background_image = visual.ImageStim(win=win, image = 'stimuli/background_f.png')      # add nice background 


act_pump = 0
act_pump_nr = 0
act_vol = 0
################################################################################################
################################# go no go #####################################################
################################################################################################

obtained_rew = 0
base_rew = 0.10
cue_time = 0.3                                                  # cue timing denotes how long the flanker go are presented
resp_wind = 0.5                                                 # resp window denotes the length of the response window 

vol = 1

left_resp = 'f'                                                 # response options 
right_resp = 'k'

juice_rew = 'primary'
pound_rew = 'secondary'


text_7 = visual.TextStim(win=win, name='text_7',
    text='Welcome to the experiment! We kindly ask you to turn off your phone and put it in your bag/on the chair behind you. If your phone is turned on, it will interfere with the signal and cause data loss for us. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "calibration"
calibrationClock = core.Clock()


# Initialize components for Routine "instr2"
instr2Clock = core.Clock()

text_79 = visual.TextStim(win=win, name='text_79',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_80 = visual.TextStim(win=win, name='text_80',
    text='default text',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_19 = visual.ImageStim(
    win=win, name='image_19',
    image='sin', mask=None,
    ori=0, pos=(0, -0.2), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "part1"
part1Clock = core.Clock()

text_84 = visual.TextStim(win=win, name='text_84',
    text='Part I: Tell us about yourself!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_87 = visual.TextStim(win=win, name='text_87',
    text='Press SPACE to continue!    ',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
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
    languageStyle='LTR',
    depth=-3.0);
diagnostics_3 = visual.TextStim(win=win, name='diagnostics_3',
    text='default text',
    font='Arial',
    pos=(0.4, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "mat_ans"
mat_ansClock = core.Clock()

image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.7, 0.9)[0], height=(0.7, 0.9)[1],
    ori=0, pos=(0, 0.3),
    lineWidth=10, lineColor=[0.2, 0.2, 0.2], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=0.9, depth=-2.0, interpolate=True)
text_51 = visual.TextStim(win=win, name='text_51',
    text='You have chosen:',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='default text',
    font='Arial',
    pos=(0, 0.4), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_53 = visual.TextStim(win=win, name='text_53',
    text='If this is true, press "y". \nIf you want to choose again, press "n".',
    font='Arial',
    pos=(0, 0.05), height=0.1, wrapWidth=0.6, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
diagnostics = visual.TextStim(win=win, name='diagnostics',
    text='default text',
    font='Arial',
    pos=(0.4, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-7.0);
polygon_5 = visual.Polygon(
    win=win, name='polygon_5',
    edges=90, size=(0.2, 0.3),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1, 0.84, 0.2], lineColorSpace='rgb',
    fillColor=[1, 0.84, 0.2], fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)

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
    color='black', colorSpace='rgb', opacity=0, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "transition"
transitionClock = core.Clock()

text_54 = visual.TextStim(win=win, name='text_54',
    text='Great job! We would now like you to answer a number of questions!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_66 = visual.TextStim(win=win, name='text_66',
    text='default text',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_67 = visual.TextStim(win=win, name='text_67',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_68 = visual.TextStim(win=win, name='text_68',
    text='default text',
    font='Arial',
    pos=(0, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_69 = visual.TextStim(win=win, name='text_69',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
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
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ev_pic"
ev_picClock = core.Clock()

rating_2 = visual.RatingScale(win=win, name='rating_2', size = 0.8,
lineColor = 'black',
stretch = 1.4,
textColor = "black",
labels = ["not at all", "extremely"])
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(207, 23),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='How much do you like this picture?',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "est_sal"
est_salClock = core.Clock()

text_24 = visual.TextStim(win=win, name='text_24',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "jui_warn"
jui_warnClock = core.Clock()
text_88 = visual.TextStim(win=win, name='text_88',
    text='You will now receive juice!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "supl_jui"
supl_juiClock = core.Clock()

text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
jui_pic = visual.ImageStim(
    win=win, name='jui_pic',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.15, 0.6),
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
    languageStyle='LTR',
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
    languageStyle='LTR',
    depth=-9.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_34 = visual.TextStim(win=win, name='text_34',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text='5',
    font='Arial',
    pos=[0.4, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='6',
    font='Arial',
    pos=[0.7, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
image_23 = visual.ImageStim(
    win=win, name='image_23',
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.15, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)

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
    languageStyle='LTR',
    depth=-7.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_39 = visual.TextStim(win=win, name='text_39',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_40 = visual.TextStim(win=win, name='text_40',
    text='5',
    font='Arial',
    pos=[0,0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='6',
    font='Arial',
    pos=(0.7, -0.58), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
image_25 = visual.ImageStim(
    win=win, name='image_25',
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.15, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)

# Initialize components for Routine "wat_warn"
wat_warnClock = core.Clock()
palate_cleanse = visual.TextStim(win=win, name='palate_cleanse',
    text='You will now receive water to wash out the juice!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "water_disp"
water_dispClock = core.Clock()

prompt_next = visual.TextStim(win=win, name='prompt_next',
    text='Get ready for the next one!',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "jui_out"
jui_outClock = core.Clock()

fav_juice_t = visual.TextStim(win=win, name='fav_juice_t',
    text='Your favourite juice was:',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
conf_prompt = visual.TextStim(win=win, name='conf_prompt',
    text='Please confirm by pressing "y" if this is correct or "n" if you want to choose another one.',
    font='Arial',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
fav_juice_pic = visual.ImageStim(
    win=win, name='fav_juice_pic',
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.2, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "jui_re"
jui_reClock = core.Clock()

mouse_prompt = visual.TextStim(win=win, name='mouse_prompt',
    text='Select your favourite by pressing:\n1 (left), 2 (middle), 3 (right)',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
jui_pic_1 = visual.ImageStim(
    win=win, name='jui_pic_1',
    image='sin', mask=None,
    ori=0, pos=(-0.4, -0.4), size=(0.15, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
jui_pic_2 = visual.ImageStim(
    win=win, name='jui_pic_2',
    image='sin', mask=None,
    ori=0, pos=(0, -0.4), size=(0.15, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
jui_pic_3 = visual.ImageStim(
    win=win, name='jui_pic_3',
    image='sin', mask=None,
    ori=0, pos=(0.4, -0.4), size=(0.15, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "jui_inf"
jui_infClock = core.Clock()
image_21 = visual.ImageStim(
    win=win, name='image_21',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.15, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "transition2"
transition2Clock = core.Clock()

text_73 = visual.TextStim(win=win, name='text_73',
    text='Part II: Get ready for the games!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rew_expl"
rew_explClock = core.Clock()
lh = 0.000001
text_41 = visual.TextStim(win=win, name='text_41',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_82 = visual.TextStim(win=win, name='text_82',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-4.0);
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1, -1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)

# Initialize components for Routine "rew_ann"
rew_annClock = core.Clock()

text_2 = visual.TextStim(win=win, name='text_2',
    text='You are playing for:',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.35, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_125 = visual.TextStim(win=win, name='text_125',
    text='Get ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ev_expl"
ev_explClock = core.Clock()

text_45 = visual.TextStim(win=win, name='text_45',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_64 = visual.TextStim(win=win, name='text_64',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_89 = visual.TextStim(win=win, name='text_89',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
polygon_7 = visual.Rect(
    win=win, name='polygon_7',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)

# Initialize components for Routine "ev_prom"
ev_promClock = core.Clock()

text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=0.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
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
    languageStyle='LTR',
    depth=-9.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='5',
    font='Arial',
    pos=[0.4, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
text_47 = visual.TextStim(win=win, name='text_47',
    text='6',
    font='Arial',
    pos=[0.7, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
image_17 = visual.ImageStim(
    win=win, name='image_17',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.35, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)

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
    languageStyle='LTR',
    depth=-7.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='2',
    font='Arial',
    pos=[-0.5, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='3',
    font='Arial',
    pos=[-0.2, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='4',
    font='Arial',
    pos=[0.1, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='5',
    font='Arial',
    pos=[0.4, -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_46 = visual.TextStim(win=win, name='text_46',
    text='6',
    font='Arial',
    pos=[0.7,  -0.58], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
text_91 = visual.TextStim(win=win, name='text_91',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "ev_save"
ev_saveClock = core.Clock()


# Initialize components for Routine "eff_expl"
eff_explClock = core.Clock()

text_50 = visual.TextStim(win=win, name='text_50',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_65 = visual.TextStim(win=win, name='text_65',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
polygon_10 = visual.Rect(
    win=win, name='polygon_10',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
text_92 = visual.TextStim(win=win, name='text_92',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image_29 = visual.ImageStim(
    win=win, name='image_29',
    image='stimuli/Item01-1.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image_35 = visual.ImageStim(
    win=win, name='image_35',
    image='stimuli/easiest.png', mask=None,
    ori=0, pos=(-0.6, -0.2), size=(0.25, 0.3),
    color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image_36 = visual.ImageStim(
    win=win, name='image_36',
    image='stimuli/easy.png', mask=None,
    ori=0, pos=(-0.2, -0.2), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image_37 = visual.ImageStim(
    win=win, name='image_37',
    image='stimuli/medium.png', mask=None,
    ori=0, pos=(0.2, -0.2), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
image_38 = visual.ImageStim(
    win=win, name='image_38',
    image='stimuli/hard.png', mask=None,
    ori=0, pos=(0.6, -0.2), size=(0.25, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
text_122 = visual.TextStim(win=win, name='text_122',
    text='default text',
    font='Arial',
    pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "eff_expl2"
eff_expl2Clock = core.Clock()

text_70 = visual.TextStim(win=win, name='text_70',
    text='The size of the reward will change:',
    font='Arial',
    pos=(0, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=(-0.6, 0.65), size=(0.25, 0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_9 = visual.ImageStim(
    win=win, name='image_9',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0.45), size=(0.25, 0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_10 = visual.ImageStim(
    win=win, name='image_10',
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0.25), size=(0.25, 0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
text_71 = visual.TextStim(win=win, name='text_71',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_93 = visual.TextStim(win=win, name='text_93',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
polygon_11 = visual.Rect(
    win=win, name='polygon_11',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)
image_26 = visual.ImageStim(
    win=win, name='image_26',
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.25, 0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
image_33 = visual.ImageStim(
    win=win, name='image_33',
    image='sin', mask=None,
    ori=0, pos=(0.2, -0.25), size=(0.25, 0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
image_34 = visual.ImageStim(
    win=win, name='image_34',
    image='sin', mask=None,
    ori=0, pos=(0.5, -0.45), size=(0.25, 0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "eff_expl4"
eff_expl4Clock = core.Clock()

text_77 = visual.TextStim(win=win, name='text_77',
    text='You will see both the picture type and reward:',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_16 = visual.ImageStim(
    win=win, name='image_16',
    image='sin', mask=None,
    ori=0, pos=(0.0, 0.0), size=(0.2,0.35),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_83 = visual.TextStim(win=win, name='text_83',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_95 = visual.TextStim(win=win, name='text_95',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
polygon_13 = visual.Rect(
    win=win, name='polygon_13',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1, -1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
image_18 = visual.ImageStim(
    win=win, name='image_18',
    image='sin', mask=None,
    ori=0, pos=(0, 0.4), size=(0.4, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
text_28 = visual.TextStim(win=win, name='text_28',
    text='And will choose between playing it out or not:',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_62 = visual.TextStim(win=win, name='text_62',
    text='Yes',
    font='Arial',
    pos=(0.2, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_63 = visual.TextStim(win=win, name='text_63',
    text='No',
    font='Arial',
    pos=(-0.2, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "eff_practice"
eff_practiceClock = core.Clock()
text_104 = visual.TextStim(win=win, name='text_104',
    text="Let's practice!",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "eff_midway"
eff_midwayClock = core.Clock()

text_99 = visual.TextStim(win=win, name='text_99',
    text='Now you will be choosing for:',
    font='Arial',
    pos=(0, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_27 = visual.ImageStim(
    win=win, name='image_27',
    image='sin', mask=None,
    ori=0, pos=(-0.6, 0.65), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_28 = visual.ImageStim(
    win=win, name='image_28',
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0.45), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_29r = visual.ImageStim(
    win=win, name='image_29r',
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0.25), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
text_105 = visual.TextStim(win=win, name='text_105',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
image_39 = visual.ImageStim(
    win=win, name='image_39',
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image_40 = visual.ImageStim(
    win=win, name='image_40',
    image='sin', mask=None,
    ori=0, pos=(0.2, -0.25), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image_41 = visual.ImageStim(
    win=win, name='image_41',
    image='sin', mask=None,
    ori=0, pos=(0.5, -0.45), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)

# Initialize components for Routine "real_ann"
real_annClock = core.Clock()

text_26 = visual.TextStim(win=win, name='text_26',
    text='Now the main game begins!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "eff_press"
eff_pressClock = core.Clock()

dr1 = visual.ImageStim(
    win=win, name='dr1',
    image='sin', mask=None,
    ori=0, pos=(0,0), size=(0.3, 0.5),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
chst1 = visual.ImageStim(
    win=win, name='chst1',
    image='sin', mask=None,
    ori=0, pos=(0,0.55), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
polygon_14 = visual.Rect(
    win=win, name='polygon_14',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1, -1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
text_96 = visual.TextStim(win=win, name='text_96',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_114 = visual.TextStim(win=win, name='text_114',
    text='Please try to respond faster',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_78 = visual.TextStim(win=win, name='text_78',
    text='Yes',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_118 = visual.TextStim(win=win, name='text_118',
    text='No',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_123 = visual.TextStim(win=win, name='text_123',
    text='default text',
    font='Arial',
    pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_124 = visual.TextStim(win=win, name='text_124',
    text='default text',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "eff_feed"
eff_feedClock = core.Clock()

image_11 = visual.ImageStim(
    win=win, name='image_11',
    image='sin', mask=None,
    ori=0, pos=(0, 0.0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_12 = visual.ImageStim(
    win=win, name='image_12',
    image='sin', mask=None,
    ori=0, pos=(0.0,  0.55), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_97 = visual.TextStim(win=win, name='text_97',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
polygon_15 = visual.Rect(
    win=win, name='polygon_15',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
text_119 = visual.TextStim(win=win, name='text_119',
    text='Yes',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_120 = visual.TextStim(win=win, name='text_120',
    text='No',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "transition3"
transition3Clock = core.Clock()

text_43 = visual.TextStim(win=win, name='text_43',
    text="Let's continue with the next game!",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_121 = visual.TextStim(win=win, name='text_121',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "go_expl"
go_explClock = core.Clock()

text_low = visual.TextStim(win=win, name='text_low',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_85 = visual.TextStim(win=win, name='text_85',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_upp = visual.TextStim(win=win, name='text_upp',
    text='default text',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
image_upp = visual.ImageStim(
    win=win, name='image_upp',
    image='sin', mask=None,
    ori=0, pos=(0, 0.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_low = visual.ImageStim(
    win=win, name='image_low',
    image='sin', mask=None,
    ori=0, pos=(0, -0.5), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
text_100 = visual.TextStim(win=win, name='text_100',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)

# Initialize components for Routine "go_expl3"
go_expl3Clock = core.Clock()
text_106 = visual.TextStim(win=win, name='text_106',
    text="Let's practice!",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "real_go_ann"
real_go_annClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='Now the main game begins!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_81 = visual.TextStim(win=win, name='text_81',
    text='Press SPACE to continue!',
    font='Arial',
    pos=(0, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_90 = visual.TextStim(win=win, name='text_90',
    text='Take a little break!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

text_111 = visual.TextStim(win=win, name='text_111',
    text='We start in 3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_112 = visual.TextStim(win=win, name='text_112',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_113 = visual.TextStim(win=win, name='text_113',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "beg_fix"
beg_fixClock = core.Clock()

image_7 = visual.ImageStim(
    win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.35, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_101 = visual.TextStim(win=win, name='text_101',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
polygon_17 = visual.Rect(
    win=win, name='polygon_17',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
image_30 = visual.ImageStim(
    win=win, name='image_30',
    image='sin', mask=None,
    ori=0, pos=(0, 0.35), size=(0.2, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "isi"
isiClock = core.Clock()
text_108 = visual.TextStim(win=win, name='text_108',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "tar_ann"
tar_annClock = core.Clock()
main_image = visual.ImageStim(
    win=win, name='main_image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(207, 23),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_18 = visual.Rect(
    win=win, name='polygon_18',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1, -1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
text_102 = visual.TextStim(win=win, name='text_102',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "comp"
compClock = core.Clock()

text_86 = visual.TextStim(win=win, name='text_86',
    text='default text',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_22 = visual.ImageStim(
    win=win, name='image_22',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.35, 0.5),
    color=[90, 0, 1], colorSpace='dkl', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_103 = visual.TextStim(win=win, name='text_103',
    text='Tutorial',
    font='Arial',
    pos=(-0.8, 0.8), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
polygon_19 = visual.Rect(
    win=win, name='polygon_19',
    width=(0.25, 0.15)[0], height=(0.25, 0.15)[1],
    ori=0, pos=(-0.8, 0.8),
    lineWidth=10, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
text_116 = visual.TextStim(win=win, name='text_116',
    text='default text',
    font='Arial',
    pos=(-0.4, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_117 = visual.TextStim(win=win, name='text_117',
    text='default text',
    font='Arial',
    pos=(0.3, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "cog_eff_instr"
cog_eff_instrClock = core.Clock()

text_109 = visual.TextStim(win=win, name='text_109',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_110 = visual.TextStim(win=win, name='text_110',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "cog_eff_fin_select"
cog_eff_fin_selectClock = core.Clock()

text_115 = visual.TextStim(win=win, name='text_115',
    text='The computer selected:',
    font='Arial',
    pos=(0, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_31 = visual.ImageStim(
    win=win, name='image_31',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_32 = visual.ImageStim(
    win=win, name='image_32',
    image='sin', mask=None,
    ori=0, pos=(0.0, 0.55), size=(0.35, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "cog_eff_fin"
cog_eff_finClock = core.Clock()
image_24 = visual.ImageStim(
    win=win, name='image_24',
    image='sin', mask=None,
    ori=0, pos=(0, 0.0), size=(1.5, 1.5),
    color=[0,45,1], colorSpace='dkl', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "cog_eff_fin_answ"
cog_eff_fin_answClock = core.Clock()

text_98 = visual.TextStim(win=win, name='text_98',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "nasa_tlx"
nasa_tlxClock = core.Clock()

nasa_tlx_text = visual.TextStim(win=win, name='nasa_tlx_text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
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
    languageStyle='LTR',
    depth=-1.0);
resp_box = visual.TextStim(win=win, name='resp_box',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ev_pic"
ev_picClock = core.Clock()

rating_2 = visual.RatingScale(win=win, name='rating_2', size = 0.8,
lineColor = 'black',
stretch = 1.4,
textColor = "black",
labels = ["not at all", "extremely"])
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(207, 23),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='How much do you like this picture?',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "nfc_scale"
nfc_scaleClock = core.Clock()

nfc_scale_text = visual.TextStim(win=win, name='nfc_scale_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_4 = visual.RatingScale(win=win, name='rating_4', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=['extremely uncharacteristic of me', ' somewhat uncharacteristic of me', ' uncertain', ' somewhat characteristic of me', ' extremely characteristic of me'], scale='')

# Initialize components for Routine "final_screen"
final_screenClock = core.Clock()
text_48 = visual.TextStim(win=win, name='text_48',
    text='That was all, you are done! Thank you for your participation :)',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
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
win.mouseVisible = False


exp_name = str(expName)                                 # open datafile in the beginning
sub_id = get_input_box(expInfo, 'participant', 2)       # participant id
dat = get_input_box(expInfo, 'date', 2)                 # date
part_age = get_input_box(expInfo, 'age', 2)             # computes age to know which t-scores to look (yyyy-mm-dd)
participant_type = get_input_box(expInfo, 'sample', 1)  # sample 1 - adult, 2 - child
type = get_input_box(expInfo, 'type', 1)                # type leads to the 6 variants of this task. 
run_debug = get_input_box(expInfo, 'run_first', 1)      # just for debugging purposes
run_all = get_input_box(expInfo, 'run_second', 1)          # runs main part
reinforcer_type = get_input_box(expInfo, 're_o', 1)     # tells us if we start with primary or secondary (1 - primary, 2- secondary)
                                                        # 1 - we start with primary and go to secondary, 2 - we start with secondary
chance_level = 0.5

cwd = os.getcwd()                                       # get current working directory

participant_file = get_input_box(expInfo, 'participant', 2)
participant_file = cwd + '/trial_gen/part_' + participant_file + '.csv'


if random.random () > chance_level:                      # key mapping for cog eff (1 - left yes right no, 2 - right yes, left no)
    yes = (-0.2, -0.4)
    no = (0.2, -0.4)
    key_position = 1
else:
    yes = (0.2, -0.4)
    no = (-0.2, -0.4)
    key_position = 2

part_age = [int(el) for el in part_age.split('-')]
part_age = datetime(part_age[0], part_age[1], part_age[2])

today = [int(el) for el in str(date.today()).split('-')]
today = datetime(today[0], today[1], today[2])

diff = relativedelta.relativedelta(today, part_age)
part_year = diff.years
part_month = diff.months

if participant_type == 1:
    participant_age = find_age_bracket(part_year, part_month, age_adults, participant_type)
    participant_type = 'adult'                          # rename for dict purposes
else:
    participant_age = find_age_bracket(part_year, part_month, age_children, participant_type)
    participant_type = 'child'

go_pract = get_input_box(expInfo, 'go_pract', 1)     # number of practice trials | default is 20
eff_pract = get_input_box(expInfo, 'eff_pract', 1)

halfway_go = halfway_go - go_pract

out_type = str(type)                                   # we do this to avoid issues with reconverting type over and over 


pic_eval = get_input_box(expInfo, 'pic_eval', 1) 

if pic_eval == 1:
    run_pic_eval_b = 1
    run_pic_eval_e = 0
else:
    run_pic_eval_b = 0
    run_pic_eval_e = 1


part_char = [exp_name, sub_id, out_type, dat, cwd]


compl_go = set_filename(part_char, 'go')              # filename
compl_eff = set_filename(part_char, 'eff')              # filename
compl_ev = set_filename(part_char, 'ev')              # filename


go_f = open(compl_go, 'w')                           # open a text file 
eff_f = open(compl_eff, 'w')                           
ev_f= open(compl_ev, 'w')                           

                                                        # in the first row we save header columns | add the others later

go_f.write('trial \t reinforcer \t reward_size \t difficulty \t direction \t condition \t response \t rt \t sub_id \t cum_amount \t pump \t pump_vol \t pump_times\n') 
eff_f.write('trial \t reinforcer \t reward_size \t difficulty \t choice \t rt \t sub_id \n')

ev_f.write('trial \t quest1 \t quest1rt \t quest2 \t quest2rt \t quest3 \t quest3rt \t reinforcer \t sub_id \n')



gust_connected = get_input_box(expInfo, 'g_conn', 1)    # connection is set at 1 as default, meaning the below if evaluates
                                                        # this is mostly a debugging aspect

if gust_connected:                                      # if we want to connect the gustatory device 

    timeout = 0                                         # set up gustaf connection parameters
    params = {
        'timeout'  : timeout,
        'baudrate' : 19200,
        'bytesize' : serial.EIGHTBITS,
        'parity'   : serial.PARITY_NONE,
        'stopbits' : serial.STOPBITS_ONE,
    }

    dev = serial.Serial('COM3', **params)   # if the gusto does not work you might need to change the COM number. The fastest way to check this is 
                                            # to go into PresentationTM -> settings -> ports -> inputs and check which are offered. Most often it should
                                            # be between COM1 to COM6 or something similar. 

                                             # Keep in mind there should be at least a 10ms difference
                                             # between changing amount of juice and the actual squirting
                                             # sequence itself. 
    dev.write('\13') # write to pump 1 
    dev.write('\62') # set 5ml for tasting 
    core.wait(0.2)
    dev.write('\14') # write to pump 2
    dev.write('\62') # set 5ml for tasting 
    core.wait(0.2)
    dev.write('\15') # write to pump 3
    dev.write('\62') # set 5ml for tasting 
    core.wait(0.2)
    dev.write('\16') # write to water 
    dev.write('106') # give them 7ml of water to rinse 
    core.wait(0.2)


    if(dev.isOpen() == False):              # safety feature to make sure port is open 
        dev.open()


if et_connected:
    eyetracker_file = 'data/eyetracker/eyetracker_' + sub_id + '_' + dat + '.tsv'
    controller.open_datafile(eyetracker_file, embed_events=False)



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
    if instr1_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
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
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calibration"-------
t = 0
calibrationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
win.setColor('gray')
controller.subscribe()

if et_connected:
    ret = controller.run_calibration(
        [(-0.4,0.4), (0.4,0.4) , (0.0,0.0), (-0.4,-0.4), (0.4,-0.4)],
        )

# keep track of which components have finished
calibrationComponents = []
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "calibration"-------
while continueRoutine:
    # get current time
    t = calibrationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calibration"-------
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=run_begin_instr, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr2"-------
    t = 0
    instr2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    
    win.setColor('white')
    
    imgs_main = ["empty", \
                  "empty", \
                  "empty", \
                  "empty", \
                  "empty", \
                  "empty", \
                  "empty", \
                  "empty", \
                  "Sample_Upper", \
                  "Sample_Highlight", \
                  "Sample Item A-1_modif", \
                  "empty", \
                  "empty", \
                  "empty"]
    
    
    texts_main = ["This experiment is composed of two parts!", \
                   "In the first part, we want to find out a few things about you.", \
                   "In the second part, you will get to play a couple of games for different rewards!", \
                   "All the games in the second part will be explained to you and will have a tutorial.", \
                   "The experimenter will also stay inside the room to ensure you understood all the objectives.", \
                   "The games you will play are easy to understand and we will let you familiarise yourself with them first.", \
                   "However, if you will have any questions during the explanations, please do ask.", \
                   "In the first part you will see picture sequences!", \
                   "You will see a picture sequence: ", \
                   "Your goal will be to always select from five options underneath the sequence the one that logically follows in the sequence: ", \
                  "For the first two sequences, the experimenter will guide you and explain how this is done.", \
                  "You will answer the remaining ones by yourself.", \
                  "This game is not timed. However, the experimenter will let you know if you should be faster.", \
                  "Let's start!"]
    
    text_instr = get_current_text(texts_main, begin_instr_trial - 1)
    
    img_main = gen_stim_path(imgs_main[begin_instr_trial - 1])
    
    
    
     
    text_79.setText(text_instr)
    instr_resp_2 = event.BuilderKeyResponse()
    text_80.setText('Press SPACE  to continue!')
    image_19.setImage(img_main)
    # keep track of which components have finished
    instr2Components = [text_79, instr_resp_2, text_80, image_19]
    for thisComponent in instr2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr2"-------
    while continueRoutine:
        # get current time
        t = instr2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_79* updates
        if t >= 0.0 and text_79.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_79.tStart = t
            text_79.frameNStart = frameN  # exact frame index
            text_79.setAutoDraw(True)
        
        # *instr_resp_2* updates
        if t >= 0.0 and instr_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr_resp_2.tStart = t
            instr_resp_2.frameNStart = frameN  # exact frame index
            instr_resp_2.status = STARTED
            # keyboard checking is just starting
            instr_resp_2.clock.reset()  # now t=0
        if instr_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                instr_resp_2.keys = theseKeys[-1]  # just the last key pressed
                instr_resp_2.rt = instr_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_80* updates
        if t >= 1 and text_80.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_80.tStart = t
            text_80.frameNStart = frameN  # exact frame index
            text_80.setAutoDraw(True)
        
        # *image_19* updates
        if t >= 0.0 and image_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_19.tStart = t
            image_19.frameNStart = frameN  # exact frame index
            image_19.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr2"-------
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    begin_instr_trial, run_begin_instr = stop_instructions(begin_instr_trial, texts_main, run_begin_instr)
    
    if not run_begin_instr:
        continueRoutine = False
        trials_6.finished = True
    
    
    # check responses
    if instr_resp_2.keys in ['', [], None]:  # No response was made
        instr_resp_2.keys=None
    trials_6.addData('instr_resp_2.keys',instr_resp_2.keys)
    if instr_resp_2.keys != None:  # we had a response
        trials_6.addData('instr_resp_2.rt', instr_resp_2.rt)
    # the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed run_begin_instr repeats of 'trials_6'


# set up handler to look after randomisation of conditions etc
first_loop = data.TrialHandler(nReps=run_debug, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='first_loop')
thisExp.addLoop(first_loop)  # add the loop to the experiment
thisFirst_loop = first_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFirst_loop.rgb)
if thisFirst_loop != None:
    for paramName in thisFirst_loop:
        exec('{} = thisFirst_loop[paramName]'.format(paramName))

for thisFirst_loop in first_loop:
    currentLoop = first_loop
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_loop.rgb)
    if thisFirst_loop != None:
        for paramName in thisFirst_loop:
            exec('{} = thisFirst_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "part1"-------
    t = 0
    part1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    tmp_runner = 100
    
    key_resp_12 = event.BuilderKeyResponse()
    # keep track of which components have finished
    part1Components = [text_84, key_resp_12, text_87]
    for thisComponent in part1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "part1"-------
    while continueRoutine:
        # get current time
        t = part1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_84* updates
        if t >= 0.0 and text_84.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_84.tStart = t
            text_84.frameNStart = frameN  # exact frame index
            text_84.setAutoDraw(True)
        
        # *key_resp_12* updates
        if t >= 0.0 and key_resp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_12.tStart = t
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_12.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_12.keys = theseKeys[-1]  # just the last key pressed
                key_resp_12.rt = key_resp_12.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_87* updates
        if t >= 1 and text_87.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_87.tStart = t
            text_87.frameNStart = frameN  # exact frame index
            text_87.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in part1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "part1"-------
    for thisComponent in part1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys=None
    first_loop.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        first_loop.addData('key_resp_12.rt', key_resp_12.rt)
    # the Routine "part1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    mat_tr = data.TrialHandler(nReps=run_matrix, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('m_reason.csv'),
        seed=None, name='mat_tr')
    thisExp.addLoop(mat_tr)  # add the loop to the experiment
    thisMat_tr = mat_tr.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMat_tr.rgb)
    if thisMat_tr != None:
        for paramName in thisMat_tr:
            exec('{} = thisMat_tr[paramName]'.format(paramName))
    
    for thisMat_tr in mat_tr:
        currentLoop = mat_tr
        # abbreviate parameter names if possible (e.g. rgb = thisMat_tr.rgb)
        if thisMat_tr != None:
            for paramName in thisMat_tr:
                exec('{} = thisMat_tr[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "mat_ev"-------
        t = 0
        mat_evClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        correct_answer = stim_corr_ans[matrix_trial-1]          # index with -1 because matrix trial initialised at 1
        curr_matrix = stim_list[matrix_trial-1] 
        
        if matrix_trial <= 2:                                   # sample items in the beginning
            begin_blurb = 'Answer by pressing keys from 1 to 5. If you do not know the answer, press 6.'
        else:
            begin_blurb = ''
        
        if matrix_trial == 3: 
            indx = 5                                            # present item 4 | first item for age > 9
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 4 and not initiate_reverse:        # if item 4 was correct, continue with 5
            indx = 6
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 4 and initiate_reverse:            # if item 4 was incorrect, go to item 3 
            indx = 4
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 5 and not initiate_reverse:        # if item 5 was correct, go to item 6
            indx = 7
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 5 and initiate_reverse and indx == 4: # if item 3 was presented, go to item 2 
            indx = 3
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 5 and initiate_reverse and indx == 6: # if item 5 was incorrect, go to item 4
            indx = 4
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 6 and not initiate_reverse:           # if item 6 was correct, go to item 7
            indx = 8
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 6 and reverse_corrected:              # if item 3 was presented and correct, reverse correct and go to item 5
            indx = 6                                               # this assumes that initiate_reverse has been turned off 
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
            reverse_corrected = 0
            failed_seq = 2
        
        elif matrix_trial == 6 and initiate_reverse and indx == 3: # if item 2 was presented and incorrect, go to item 1
            indx = 2
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 6 and initiate_reverse and indx == 4: # if item 3 was presented and incorrect, go to item 2 
            indx = 3
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 7 and failed_seq == 2:                # if the reverse was corrected on trial 5 (by being incorrect on item 4 in the beginning and correct on 3, 2)
            indx = 7                                               # go to item 6
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
            failed_seq = 2
        
        elif matrix_trial == 7 and not initiate_reverse:           # if item 6 was correct, go to item 7
            indx = 9
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 7 and initiate_reverse and indx == 3 and not reverse_corrected:    # if item 2 was incorrect, go to item 1 
            indx = 2
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
        
        elif matrix_trial == 7 and initiate_reverse and indx == 2:                              # if item 1 was presented go to item 5
            indx = 6
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
            failed_seq = 1
        
        elif matrix_trial == 7 and reverse_corrected and indx == 2:                             # if item 1 was presented and they have reversed, go to item 5
            indx = 6
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
            reverse_corrected = 0
            failed_seq = 1
        
        elif matrix_trial == 7 and reverse_corrected and indx == 3:                             # if item 2 was presented and the reverse was corrected, go to item 6
            indx = 7
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
            reverse_corrected = 0
            failed_seq = 2
        
        elif matrix_trial == 8 and indx == 2:                                                   # if item 1 was presented, we just set the failed sequence at this stage 
            failed_seq = 2
        
        elif matrix_trial >= 8:  
            if failed_seq == 1:
                indx = matrix_trial - 1
            elif failed_seq == 2:
                indx = matrix_trial
            else:
                indx = matrix_trial + 2 # this is the correct difference between the matrix trial and the index acces element if thez were completly correct
            
            curr_matrix, correct_answer = set_matrix(indx, stim_list, stim_corr_ans)
            
        elif matrix_trial == 8 and reverse_corrected:                                          # this runs just for one possible scenario where we want to continue
            indx = 7                                                                           # with item 6 when we started the reverse after item 5 was incorrect
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mat_evComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mat_ev"-------
        for thisComponent in mat_evComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        chosen_item = item_resp.keys
        
        if item_resp.keys == '1':
            pos = (-0.488, -0.49)
        elif item_resp.keys == '2':
            pos = (-0.246, -0.49)
        elif item_resp.keys == '3':
            pos = (-0.01,  -0.49)
        elif item_resp.keys == '4':
            pos = (0.225, -0.49)
        elif item_resp.keys == '5':
            pos = (0.475, -0.49)
        elif item_resp.keys == '6':
            pos = (0, -0.49)
        
        if item_resp.keys == '6':
            opac = 0
        else:
            opac = 0.7
        
        
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
        polygon_5.setPos(pos)
        polygon_5.setOpacity(opac)
        # keep track of which components have finished
        mat_ansComponents = [image_4, polygon_2, text_51, text_52, matrix_reeval, text_53, diagnostics, polygon_5]
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
            
            # *polygon_5* updates
            if t >= 0.0 and polygon_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_5.tStart = t
                polygon_5.frameNStart = frameN  # exact frame index
                polygon_5.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mat_ansComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "mat_ans"-------
        for thisComponent in mat_ansComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if matrix_reeval.keys == 'n':
            run_correct = 1
        
        else:
            run_correct = 0 # dont need to run the second part
        
            if matrix_trial >= 3:
                responded_correctly, stor_matrix_ans = matrix_response(item_resp, correct_answer, stor_matrix_ans, curr_matrix)
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
        # check responses
        if matrix_reeval.keys in ['', [], None]:  # No response was made
            matrix_reeval.keys=None
        mat_tr.addData('matrix_reeval.keys',matrix_reeval.keys)
        if matrix_reeval.keys != None:  # we had a response
            mat_tr.addData('matrix_reeval.rt', matrix_reeval.rt)
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
            for paramName in thisMatrix_re:
                exec('{} = thisMatrix_re[paramName]'.format(paramName))
        
        for thisMatrix_re in matrix_re:
            currentLoop = matrix_re
            # abbreviate parameter names if possible (e.g. rgb = thisMatrix_re.rgb)
            if thisMatrix_re != None:
                for paramName in thisMatrix_re:
                    exec('{} = thisMatrix_re[paramName]'.format(paramName))
            
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
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mat_reComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
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
        # completed run_correct repeats of 'matrix_re'
        
    # completed run_matrix repeats of 'mat_tr'
    
    
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
        t_r = '01'
        
        if f_r in stor_matrix_ans and stor_matrix_ans[f_r] == 1:        # means that it was a failure on item 4 already
            if s_r in stor_matrix_ans:
                if stor_matrix_ans[s_r] == 1:                           # if this isn't true then '01' is already accounted for 
                    ans_sum = str(sum(stor_matrix_ans.values()) + 1) 
                else:
                    ans_sum = str(sum(stor_matrix_ans.values()))
    
            else:                                                       # the only way item 3 is inside and item 2 isn't, is if the person
                ans_sum = str(sum(stor_matrix_ans.values())) + 2        # reversed already on item 3, hence +2 for item 2 and 1
    
        elif f_r in stor_matrix_ans and stor_matrix_ans[f_r] != 1:      # here it necessarily goes to item 1 and thus you can
            ans_sum = str(sum(stor_matrix_ans.values()))                # just sum normally because all of them are inside
        
        elif f_r not in stor_matrix_ans:
            ans_sum = str(sum(stor_matrix_ans.values()) + 3)            # this necessarily means reverse wasnt entered so this is ok
    
        print("This is ans sum {} and this is stor matrix ans {}".format(ans_sum, stor_matrix_ans))
    
    
        part_t = matrix_reason[participant_type][participant_age][ans_sum]
    
        t_modifier = 18                                                 # we arbitrarily pick a higher and lower t score value
        half_t = int(round(t_modifier/3))
    
        easiest = part_t - t_modifier
        easy = part_t - half_t                                          # the middle ones will be slightly below or above their performance
        medium = part_t + half_t         
        high = part_t + t_modifier  
    
        # exception handling | 80 is the max t values and 20 is the min t value
        if high > 80:
            high = 80
        
        if medium > 80:
            medium = 80
    
        if easy > 80:                   # if someone were to score all of them correct
            easy = 80
    
        if easiest > 80:                # if someone were to score all of them correct
            easiest = 80
    
        # not very probable that someone would score so low 
        if easiest < 20:
            easiest = 20
    
        if easy < 20:
            easy = 20
    
        if medium < 20:
            medium = 20
    
        if high < 20:
            high = 20
    
        # we also want to make sure that none have the same t value
        # though this doesn't necessarily matter because they will only be exposed to 2 trials. 
    
        all_t = [easiest, easy, medium, high]
    
        combos = list(itertools.combinations(all_t, 2))
    
        tmp_ctr = 0
    
    #    for t1, t2 in combos:
        
    #        if t1 == t2:
                
        
    #    tmp_ctr += 1
        
    
        # now we find the t value that corresponds and/or is closest to the newly obtained modifier 
    
        easiest = min(enumerate(t_values), key=lambda i: abs(i[1]-easiest))[1]
        easy = min(enumerate(t_values), key=lambda i: abs(i[1]-easy))[1]
        medium = min(enumerate(t_values), key=lambda i: abs(i[1]-medium))[1]
        high = min(enumerate(t_values), key=lambda i: abs(i[1]-high))[1]
    
        
        elems = [easiest, easy, medium, high]
        
    
        for key, value in matrix_reason[participant_type][participant_age].items():
            for indx, el in enumerate(elems):
                if value == el:
                    elems[indx] = key
                    
    #        if value == high:
    #            high = key
    #        if value == easy:
    #            easy = key
    #        if value == easiest:
    #            easiest == key
    #        if value == medium:
    #            medium = key
    
        # they are now saved as the number of correct items which will correspond to the 
        # row they are being pulled for presentation This is only approximate because
        # obviously someone can have 1 incorrect and two further ones correct. 
    
        # we now convert them to index numbers, to all of them we need to add +1 because we are using the generated stim list 
        # to actually present the pictures. So it goes from 0 to 31, with 0 and 1 being sample items A and B 
    
        for indx, el in enumerate(elems):
            elems[indx] = int(el) + 1
    
        # these are the index values of items that we want to pick.
    
    else:
        part_t = ''
        t = ''
        ans_sum = ''
        tmp_list = []
        elems = [15, 21, 24, 30]
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in transitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
        print("Successfully saved the matrix reasoning dataset.")
        # clear variables
        struct_1 = ''
        struct_2 = ''
        tmp_list = []
    
        tmp_runner = 1
    
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys=None
    first_loop.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        first_loop.addData('key_resp_7.rt', key_resp_7.rt)
    # the Routine "transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    init_qs = data.TrialHandler(nReps=0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('initial_q.csv'),
        seed=None, name='init_qs')
    thisExp.addLoop(init_qs)  # add the loop to the experiment
    thisInit_q = init_qs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInit_q.rgb)
    if thisInit_q != None:
        for paramName in thisInit_q:
            exec('{} = thisInit_q[paramName]'.format(paramName))
    
    for thisInit_q in init_qs:
        currentLoop = init_qs
        # abbreviate parameter names if possible (e.g. rgb = thisInit_q.rgb)
        if thisInit_q != None:
            for paramName in thisInit_q:
                exec('{} = thisInit_q[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ev_iniq"-------
        t = 0
        ev_iniqClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # this is the question it randomly pulls from the .csv file
        initial_q = current_question
        
        win.mouseVisible = True
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ev_iniqComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ev_iniq"-------
        for thisComponent in ev_iniqComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        tmp_trial += 1
        row_len = 5
        stor_init_q.append([sav_mapping, rating.getRating()])
        
        if tmp_trial == row_len:
        
            complete = set_filename(part_char, 'initial_q(initial_q.csv)')
            init_q_data = open(complete, 'w')
        
            # order according to the first element. 
            
            stor_init_q = sorted(stor_init_q, key=lambda x: x[0])
        
            for id, q in stor_init_q:
                struct_1 += "init_quest_" + str(id) + "\t"
            
            struct_1 += "sub_id\n"  #subid
            
            init_q_data.write(struct_1)
            
            for i in range(0, len(stor_init_q)):     # needs to be + 1 for the amount of questions we always want 
                struct_2 += "{}\t"
        
            struct_2 += "{}\n"
        
            tmp_list = [el2 for el1, el2 in stor_init_q] # extract question answers
            tmp_list.append(sub_id)
        
            print(tmp_list)
            print(struct_1)
            print(struct_2)
            print(stor_init_q)
        
            init_q_data.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3], tmp_list[4]))
            init_q_data.close()
            print("Successfully saved the initial evaluation dataset.")
        
            # clear variables
            struct_1 = ''
            struct_2 = ''
            tmp_list = []
            tmp_trial = 0
        # store data for init_qs (TrialHandler)
        init_qs.addData('rating.response', rating.getRating())
        # the Routine "ev_iniq" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 0 repeats of 'init_qs'
    
    
    # set up handler to look after randomisation of conditions etc
    trial_pic_eval = data.TrialHandler(nReps=run_pic_eval_b, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('pic_rating.csv'),
        seed=None, name='trial_pic_eval')
    thisExp.addLoop(trial_pic_eval)  # add the loop to the experiment
    thisTrial_pic_eval = trial_pic_eval.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_pic_eval.rgb)
    if thisTrial_pic_eval != None:
        for paramName in thisTrial_pic_eval:
            exec('{} = thisTrial_pic_eval[paramName]'.format(paramName))
    
    for thisTrial_pic_eval in trial_pic_eval:
        currentLoop = trial_pic_eval
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_pic_eval.rgb)
        if thisTrial_pic_eval != None:
            for paramName in thisTrial_pic_eval:
                exec('{} = thisTrial_pic_eval[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ev_pic"-------
        t = 0
        ev_picClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # this is the question it randomly pulls from the .csv file
        pic_q = current_question
        
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ev_picComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ev_pic"-------
        for thisComponent in ev_picComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stor_pic_q.append([sav_mapping, rating_2.getRating()])
        tmp_trial += 1
        row_len = 7
        
        if tmp_trial == row_len: # end of questions about pictures
        
            stor_pic_q = sorted(stor_pic_q, key=lambda x: x[0])
        
            complete = set_filename(part_char, 'pic_q(pic_rating.csv)')
            pic_q_data = open(complete, 'w')
            
            for el1, el2 in stor_pic_q:
                struct_1 += "pic" + str(el1) + "\t"
            
            struct_1 += "sub_id\n"  #subid
        
            pic_q_data.write(struct_1)
            
            for i in range(0, len(stor_pic_q)):
                struct_2 += "{}\t"
        
            struct_2 += "{}\n"
        
            tmp_list = [el2 for el1, el2 in stor_pic_q] 
            tmp_list.append(sub_id)
        
            pic_q_data.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3],
                                             tmp_list[4], tmp_list[5], tmp_list[6]))
            pic_q_data.close()
            print("Successfully saved the picture evaluation dataset.")
        
            struct_1 = ''
            struct_2 = ''
            tmp_list = []
            tmp_trial = 0
            print("this is tmp trial after ev pic {}".format(tmp_trial))
        
        # store data for trial_pic_eval (TrialHandler)
        trial_pic_eval.addData('rating_2.response', rating_2.getRating())
        # the Routine "ev_pic" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed run_pic_eval_b repeats of 'trial_pic_eval'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_9 = data.TrialHandler(nReps=run_est_sal, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_9')
    thisExp.addLoop(trials_9)  # add the loop to the experiment
    thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    for thisTrial_9 in trials_9:
        currentLoop = trials_9
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
        if thisTrial_9 != None:
            for paramName in thisTrial_9:
                exec('{} = thisTrial_9[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "est_sal"-------
        t = 0
        est_salClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        
        
        
        texts_main = ["We mentioned that you will be playing for rewards in the second part.", \
                      "If you will do well, you will be rewarded for your score.", \
                      "There will be two types of rewards - juice and money.", \
                      "We will always tell you what reward you will be playing for.", \
                      "We now want to make sure, that you will be playing for a juice you like!", \
                      "That is why you will now get to taste several juices.", \
                      "After you obtain each juice, we would like you to rate it.", \
                      "By telling us which one you like the most...", \
                      "We will be able to give you that one as a reward later!"]
        
        
        text_instr = get_current_text(texts_main, est_sal_trial - 1)
        
        text_24.setText(text_instr)
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in est_salComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "est_sal"-------
        for thisComponent in est_salComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        est_sal_trial, run_est_sal = stop_instructions(est_sal_trial, texts_main, run_est_sal)
        
        if not run_est_sal:
            continueRoutine = False
            trials_9.finished = True
        
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys=None
        trials_9.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials_9.addData('key_resp_5.rt', key_resp_5.rt)
        # the Routine "est_sal" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed run_est_sal repeats of 'trials_9'
    
    
    # set up handler to look after randomisation of conditions etc
    jui_typ = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('juice_types.csv'),
        seed=None, name='jui_typ')
    thisExp.addLoop(jui_typ)  # add the loop to the experiment
    thisJui_typ = jui_typ.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisJui_typ.rgb)
    if thisJui_typ != None:
        for paramName in thisJui_typ:
            exec('{} = thisJui_typ[paramName]'.format(paramName))
    
    for thisJui_typ in jui_typ:
        currentLoop = jui_typ
        # abbreviate parameter names if possible (e.g. rgb = thisJui_typ.rgb)
        if thisJui_typ != None:
            for paramName in thisJui_typ:
                exec('{} = thisJui_typ[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        jui_sal = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('juice_salience.csv'),
            seed=None, name='jui_sal')
        thisExp.addLoop(jui_sal)  # add the loop to the experiment
        thisJui_sal = jui_sal.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisJui_sal.rgb)
        if thisJui_sal != None:
            for paramName in thisJui_sal:
                exec('{} = thisJui_sal[paramName]'.format(paramName))
        
        for thisJui_sal in jui_sal:
            currentLoop = jui_sal
            # abbreviate parameter names if possible (e.g. rgb = thisJui_sal.rgb)
            if thisJui_sal != None:
                for paramName in thisJui_sal:
                    exec('{} = thisJui_sal[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            disp = data.TrialHandler(nReps=run_dispenser, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='disp')
            thisExp.addLoop(disp)  # add the loop to the experiment
            thisDisp = disp.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDisp.rgb)
            if thisDisp != None:
                for paramName in thisDisp:
                    exec('{} = thisDisp[paramName]'.format(paramName))
            
            for thisDisp in disp:
                currentLoop = disp
                # abbreviate parameter names if possible (e.g. rgb = thisDisp.rgb)
                if thisDisp != None:
                    for paramName in thisDisp:
                        exec('{} = thisDisp[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "jui_warn"-------
                t = 0
                jui_warnClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(0.500000)
                # update component parameters for each repeat
                # keep track of which components have finished
                jui_warnComponents = [text_88]
                for thisComponent in jui_warnComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "jui_warn"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = jui_warnClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_88* updates
                    if t >= 0.0 and text_88.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_88.tStart = t
                        text_88.frameNStart = frameN  # exact frame index
                        text_88.setAutoDraw(True)
                    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_88.status == STARTED and t >= frameRemains:
                        text_88.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in jui_warnComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "jui_warn"-------
                for thisComponent in jui_warnComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
                # ------Prepare to start Routine "supl_jui"-------
                t = 0
                supl_juiClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                pump_indx = current_pump # information is in the csv
                                         # randomly takes one of the first three pumps
                                         # sends pump vol 
                
                # fetch correct one from initial definition of pumps
                pump = pumps[pump_indx]
                
                if gust_connected:
                    dev.write(pump)
                # after it sends, it should wait a bit
                win.mouseVisible = False
                
                #duration set to 10s
                jui_t = 1
                text_4.setText(pump)
                jui_pic.setImage(curr_juice)
                # keep track of which components have finished
                supl_juiComponents = [text_4, jui_pic]
                for thisComponent in supl_juiComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "supl_jui"-------
                while continueRoutine:
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
                    frameRemains = 0.0 + jui_t- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_4.status == STARTED and t >= frameRemains:
                        text_4.setAutoDraw(False)
                    
                    # *jui_pic* updates
                    if t >= 0.0 and jui_pic.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        jui_pic.tStart = t
                        jui_pic.frameNStart = frameN  # exact frame index
                        jui_pic.setAutoDraw(True)
                    frameRemains = 0.0 + jui_t- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if jui_pic.status == STARTED and t >= frameRemains:
                        jui_pic.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in supl_juiComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "supl_jui"-------
                for thisComponent in supl_juiComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
                # the Routine "supl_jui" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed run_dispenser repeats of 'disp'
            
            
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
            image_23.setImage(curr_juice)
            # keep track of which components have finished
            ev_juiComponents = [juice_resp, text_30, first_2, second_2, third_2, fourth_2, fifth_2, sixth_2, text_31, text_32, text_33, text_34, text_35, text_22, image_23]
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
                
                # *image_23* updates
                if t >= 0.0 and image_23.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_23.tStart = t
                    image_23.frameNStart = frameN  # exact frame index
                    image_23.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ev_juiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
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
            
            if juice_trial == 1:
                run_dispenser = 0
                run_water = 0
                if gust_connected:
                    act_pump, act_pump_nr, act_vol = decode_gustaf(dev)
                # water
            
            if juice_trial == 3:
                run_water = 1
            
            
            
            first_feedback_2.setFillColor(opt_1)
            second_feedback_2.setFillColor(opt_2)
            third_feedback_2.setFillColor(opt_3)
            fourth_feedback_2.setFillColor(opt_4)
            fifth_feedback_2.setFillColor(opt_5)
            sixth_feedback_2.setFillColor(opt_6)
            image_25.setImage(curr_juice)
            # keep track of which components have finished
            jui_feComponents = [first_feedback_2, second_feedback_2, third_feedback_2, fourth_feedback_2, fifth_feedback_2, sixth_feedback_2, text_36, text_37, text_38, text_39, text_40, text_25, image_25]
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
                
                # *image_25* updates
                if t >= 0.0 and image_25.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_25.tStart = t
                    image_25.frameNStart = frameN  # exact frame index
                    image_25.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_25.status == STARTED and t >= frameRemains:
                    image_25.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jui_feComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "jui_fe"-------
            for thisComponent in jui_feComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #if juice_trial == 1:
            #    print(act_pump, act_pump_nr, act_vol)
            #    print("On trial {} and juice type {} with responses given {}".format(juice_trial, juice_type, len(tmp_list))) 
            
            juice_type = get_juice_name(pump_indx)
            
            stor_jui_eval[juice_type].append([juice_resp.keys, sav_mapping, act_pump, act_pump_nr, act_vol])
            
            tmp_list.append(juice_resp.keys)
            
            
            juice_trial += 1
            
            # set up handler to look after randomisation of conditions etc
            disp_c = data.TrialHandler(nReps=run_water, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='disp_c')
            thisExp.addLoop(disp_c)  # add the loop to the experiment
            thisDisp_c = disp_c.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDisp_c.rgb)
            if thisDisp_c != None:
                for paramName in thisDisp_c:
                    exec('{} = thisDisp_c[paramName]'.format(paramName))
            
            for thisDisp_c in disp_c:
                currentLoop = disp_c
                # abbreviate parameter names if possible (e.g. rgb = thisDisp_c.rgb)
                if thisDisp_c != None:
                    for paramName in thisDisp_c:
                        exec('{} = thisDisp_c[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "wat_warn"-------
                t = 0
                wat_warnClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(2.000000)
                # update component parameters for each repeat
                # keep track of which components have finished
                wat_warnComponents = [palate_cleanse]
                for thisComponent in wat_warnComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "wat_warn"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = wat_warnClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *palate_cleanse* updates
                    if t >= 0.0 and palate_cleanse.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        palate_cleanse.tStart = t
                        palate_cleanse.frameNStart = frameN  # exact frame index
                        palate_cleanse.setAutoDraw(True)
                    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if palate_cleanse.status == STARTED and t >= frameRemains:
                        palate_cleanse.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in wat_warnComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "wat_warn"-------
                for thisComponent in wat_warnComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
                # ------Prepare to start Routine "water_disp"-------
                t = 0
                water_dispClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                if juice_trial == 4:
                    if gust_connected:
                        dev.write('\4')
                    run_dispenser = 1
                    juice_trial = 1
                    t1 = 1
                    t2 = 2 #should be 10
                    col = 'black'
                
                if len(tmp_list) == 9:
                    t1 = 0
                    t2 = 0.01
                    col = 'white'
                    tmp_list = []
                prompt_next.setColor(col, colorSpace='rgb')
                # keep track of which components have finished
                water_dispComponents = [prompt_next]
                for thisComponent in water_dispComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "water_disp"-------
                while continueRoutine:
                    # get current time
                    t = water_dispClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *prompt_next* updates
                    if t >= t1 and prompt_next.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        prompt_next.tStart = t
                        prompt_next.frameNStart = frameN  # exact frame index
                        prompt_next.setAutoDraw(True)
                    frameRemains = t2 - win.monitorFramePeriod * 0.75  # most of one frame period left
                    if prompt_next.status == STARTED and t >= frameRemains:
                        prompt_next.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in water_dispComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "water_disp"-------
                for thisComponent in water_dispComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                if gust_connected:
                    dev.readlines() # needs to be cleared
                # the Routine "water_disp" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed run_water repeats of 'disp_c'
            
        # completed 1 repeats of 'jui_sal'
        
    # completed 1 repeats of 'jui_typ'
    
    
    # ------Prepare to start Routine "jui_out"-------
    t = 0
    jui_outClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    tmp_list = []
    
    # maybe worthwhile checking out where those numbers come from 
    stor_jui_eval = dd = {k:v for k, v in zip(stor_jui_eval.keys(), stor_jui_eval.values()) if len(v)}
    
    for key, values in zip(stor_jui_eval.keys(), stor_jui_eval.values()):
        tmp_val = 0
        for value in values: 
            tmp_val += int(value[0]) # we take the first value because that denotes the response
        tmp_len = len(stor_jui_eval[key])
        tmp_list.append((key, tmp_val/tmp_len)) # we get the mean (we ask them 3 questions)
    
    # picks the max and if there's more than one it picks one randomly
    # we then later ask to reconfirm their favourite juice 
    print("these are the juice mean values {}".format(tmp_list))
    
    fav_juice = max(tmp_list, key=lambda item:item[1])[0] # take the max
    
    fav_juice_path = gen_stim_path(fav_juice)
    
    tmp_val = 0
    tmp_len = 0
    tmp_list = []
    juice_conf = event.BuilderKeyResponse()
    fav_juice_pic.setImage(fav_juice_path)
    # keep track of which components have finished
    jui_outComponents = [fav_juice_t, juice_conf, conf_prompt, fav_juice_pic]
    for thisComponent in jui_outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jui_out"-------
    while continueRoutine:
        # get current time
        t = jui_outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *fav_juice_t* updates
        if t >= 0.0 and fav_juice_t.status == NOT_STARTED:
            # keep track of start time/frame for later
            fav_juice_t.tStart = t
            fav_juice_t.frameNStart = frameN  # exact frame index
            fav_juice_t.setAutoDraw(True)
        
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
        
        # *conf_prompt* updates
        if t >= 1 and conf_prompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            conf_prompt.tStart = t
            conf_prompt.frameNStart = frameN  # exact frame index
            conf_prompt.setAutoDraw(True)
        
        # *fav_juice_pic* updates
        if t >= 0.0 and fav_juice_pic.status == NOT_STARTED:
            # keep track of start time/frame for later
            fav_juice_pic.tStart = t
            fav_juice_pic.frameNStart = frameN  # exact frame index
            fav_juice_pic.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jui_outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jui_out"-------
    for thisComponent in jui_outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if juice_conf.keys == 'y':
        run_juice_reeval = 0
    
        fav_juice_pump, fav_juice_pumpid, fav_juice_path = juice_out(part_char, stor_jui_eval, fav_juice)
    
    else:
        run_juice_reeval = 1
        win.mouseVisible = True
    
    # check responses
    if juice_conf.keys in ['', [], None]:  # No response was made
        juice_conf.keys=None
    first_loop.addData('juice_conf.keys',juice_conf.keys)
    if juice_conf.keys != None:  # we had a response
        first_loop.addData('juice_conf.rt', juice_conf.rt)
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
        for paramName in thisJuice_re:
            exec('{} = thisJuice_re[paramName]'.format(paramName))
    
    for thisJuice_re in juice_re:
        currentLoop = juice_re
        # abbreviate parameter names if possible (e.g. rgb = thisJuice_re.rgb)
        if thisJuice_re != None:
            for paramName in thisJuice_re:
                exec('{} = thisJuice_re[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "jui_re"-------
        t = 0
        jui_reClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        random.shuffle(juices) # by shuffling this we always randomise presen
                               # tation sequence. simultaneously we can still
                               # extract information in the end routine without
                               # further modification because in that case the 
                               # positioning remains the same 
        
        for el in juices:
            tmp_list.append(gen_stim_path(el))
        
        
        juice_1, juice_2, juice_3 = tmp_list
        
        jui_pic_1.setImage(juice_1)
        jui_pic_2.setImage(juice_2)
        jui_pic_3.setImage(juice_3)
        jui_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        jui_reComponents = [mouse_prompt, jui_pic_1, jui_pic_2, jui_pic_3, jui_resp]
        for thisComponent in jui_reComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "jui_re"-------
        while continueRoutine:
            # get current time
            t = jui_reClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #l, _, r = mouse.getPressed()
            
            #if l or r:
            #    x, y = get_mouse_coord(mouse)
                
            #    j1 = get_mouse_choice_simple(x, y, -0.55, -0.25, 0.1, 0.7, 0)
            #    j2= get_mouse_choice_simple(x, y, -0.15, 0.15, 0.1, 0.7, 1)
            #    j3 = get_mouse_choice_simple(x, y, 0.25, 0.55, 0.1, 0.7, 2)
                
            #    mx = max([j1, j2, j3])
                
            #    if mx < 5: # means one of them evaluated to true 
            #        print("this is mx {}".format(mx))
            #        print("This is tmp list {}".format(tmp_list))
            #        fav_juice = tmp_list[mx].split('/')[1].split('.')[0] # and we can index that one
            #        print(fav_juice)
            #        continueRoutine = False
            #        run_juice_reeval = 0
            #        juice_re.finished = True
            #        mouse_rt = time.time() - begin
            #    else:
            #        mouse.clickReset()
            #        core.wait(.01)
            
            
            
            
            # *mouse_prompt* updates
            if t >= 0.0 and mouse_prompt.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouse_prompt.tStart = t
                mouse_prompt.frameNStart = frameN  # exact frame index
                mouse_prompt.setAutoDraw(True)
            
            # *jui_pic_1* updates
            if t >= 0.0 and jui_pic_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                jui_pic_1.tStart = t
                jui_pic_1.frameNStart = frameN  # exact frame index
                jui_pic_1.setAutoDraw(True)
            
            # *jui_pic_2* updates
            if t >= 0.0 and jui_pic_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                jui_pic_2.tStart = t
                jui_pic_2.frameNStart = frameN  # exact frame index
                jui_pic_2.setAutoDraw(True)
            
            # *jui_pic_3* updates
            if t >= 0.0 and jui_pic_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                jui_pic_3.tStart = t
                jui_pic_3.frameNStart = frameN  # exact frame index
                jui_pic_3.setAutoDraw(True)
            
            # *jui_resp* updates
            if t >= 0.0 and jui_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                jui_resp.tStart = t
                jui_resp.frameNStart = frameN  # exact frame index
                jui_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(jui_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if jui_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    jui_resp.keys = theseKeys[-1]  # just the last key pressed
                    jui_resp.rt = jui_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in jui_reComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "jui_re"-------
        for thisComponent in jui_reComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        run_juice_reeval = 0
        
        fav_juice = tmp_list[int(jui_resp.keys)-1]
        
        fav_juice = remove_stim_path(fav_juice)
        
        fav_juice_pump, fav_juice_pumpid, fav_juice_path = juice_out(part_char, stor_jui_eval, fav_juice)
        
        tmp_list = []
        
        
        # check responses
        if jui_resp.keys in ['', [], None]:  # No response was made
            jui_resp.keys=None
        juice_re.addData('jui_resp.keys',jui_resp.keys)
        if jui_resp.keys != None:  # we had a response
            juice_re.addData('jui_resp.rt', jui_resp.rt)
        # the Routine "jui_re" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "jui_inf"-------
        t = 0
        jui_infClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        image_21.setImage(fav_juice_path)
        # keep track of which components have finished
        jui_infComponents = [image_21]
        for thisComponent in jui_infComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "jui_inf"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = jui_infClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_21* updates
            if t >= 0.0 and image_21.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_21.tStart = t
                image_21.frameNStart = frameN  # exact frame index
                image_21.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_21.status == STARTED and t >= frameRemains:
                image_21.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in jui_infComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "jui_inf"-------
        for thisComponent in jui_infComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed run_juice_reeval repeats of 'juice_re'
    
    thisExp.nextEntry()
    
# completed run_debug repeats of 'first_loop'

# get names of stimulus parameters
if first_loop.trialList in ([], [None], None):
    params = []
else:
    params = first_loop.trialList[0].keys()
# save data for this loop
first_loop.saveAsExcel(filename + '.xlsx', sheetName='first_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
first_loop.saveAsText(filename + 'first_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "transition2"-------
t = 0
transition2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
time.sleep(0.5)
background_image.setAutoDraw(True)
# keep track of which components have finished
transition2Components = [text_73]
for thisComponent in transition2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "transition2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = transition2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_73* updates
    if t >= 0.5 and text_73.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_73.tStart = t
        text_73.frameNStart = frameN  # exact frame index
        text_73.setAutoDraw(True)
    frameRemains = 0.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_73.status == STARTED and t >= frameRemains:
        text_73.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transition2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "transition2"-------
for thisComponent in transition2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
main_loop = data.TrialHandler(nReps=run_all, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('part_1_small.csv'),
    seed=None, name='main_loop')
thisExp.addLoop(main_loop)  # add the loop to the experiment
thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
if thisMain_loop != None:
    for paramName in thisMain_loop:
        exec('{} = thisMain_loop[paramName]'.format(paramName))

for thisMain_loop in main_loop:
    currentLoop = main_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            exec('{} = thisMain_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    rew_role = data.TrialHandler(nReps=run_rew, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rew_role')
    thisExp.addLoop(rew_role)  # add the loop to the experiment
    thisRew_role = rew_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRew_role.rgb)
    if thisRew_role != None:
        for paramName in thisRew_role:
            exec('{} = thisRew_role[paramName]'.format(paramName))
    
    for thisRew_role in rew_role:
        currentLoop = rew_role
        # abbreviate parameter names if possible (e.g. rgb = thisRew_role.rgb)
        if thisRew_role != None:
            for paramName in thisRew_role:
                exec('{} = thisRew_role[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=run_rew_instr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "rew_expl"-------
            t = 0
            rew_explClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            
            
            texts_main_1_1 = ["If you remember, in the first part we said you will be rewarded for your score!", \
                          "That's why we wanted to know what your favourite juice is.", \
                          "Now, you will be rewarded with that juice if you do well!", \
                          "To make it really clear, you will see an image of a juice carton.", \
                          "This means your reward will be juice. An example will be shown soon.", \
                          "Every time you see the word 'tutorial' in a red frame like in the upper left corner...", \
                          "You know that the screen you are seeing is part of the tutorial.", \
                          "If you do not see that screen it means, it is the real game!", \
                          "We will also let you know to make sure you understand the real game has started!"]
            
            # second half
            texts_main_1_2 = ["Great, you are now halfway through the games!", \
                              "In the beginning we said you would be rewarded for your score.", \
                              "But juice is not the only type of reward we have in store for you.", \
                              "To make it more fun, you can also earn money if your score will be good.", \
                              "In the second half you will therefore earn money if you do well!", \
                              "On the next screen you will be shown a symbol of a pound.", \
                              "That is the reward you will get for the rest of the games!"]
            
            
            texts_main_2_1 = ["If you remember, in the first part we said you will be rewarded for your score!", \
                            "Now, you will be able to earn money if your score will be good!", \
                            "To make it really clear, you will see a symbol of a pound.", \
                            "This means your reward will be money. An example will be shown soon.", \
                            "Every time you see the word 'tutorial' in a red frame like in the upper left corner...", \
                            "You know that the screen you are seeing is part of the tutorial.", \
                            "If you do not see that screen it means, you are playing the real game!", \
                            "We will also let you know to make sure you understand the real game has started!"]
            
            # second half 
            texts_main_2_2 = ["Great, you are now halfway through the games!", \
                          "In the beginning we said you would be rewarded for your score.", \
                          "But money is not the only type of reward we have in store for you.", \
                          "That's why we wanted to know what your favourite juice is.", \
                          "To make it more fun, in this part your reward will be your favourite juice!." \
                          "In the second half you will therefore earn juice if you do well!", \
                          "On the next screen you will be shown an image of a juice carton.", \
                          "That is the reward you will get for the rest of the games!"]
            
            present_tutorial = 6 
            if rew_instr_trial == present_tutorial:                # this is the trial where we want to start presenting the tutorial sign
                lh, tutorial_opac = turn_on_tutorial()
            
            if reinforcer == 'primary':
                texts_main = texts_main_1_1
                curr_reward = gen_stim_path('juice')
            else:
                texts_main = texts_main_2_1
                curr_reward = gen_stim_path('pound')
            
            if (trial + go_pract) >= halfway_go:                          # when this evaluated, we are halfway through 
                if reinforcer == 'primary': 
                    texts_main = texts_main_1_2
                    curr_reward = gen_stim_path('pound')
                else:
                    texts_main = texts_main_2_2
                    curr_reward = gen_stim_path('juice')
            
            
            
            text_rew = texts_main[rew_instr_trial - 1]
            text_41.setText(text_rew)
            instr_resp = event.BuilderKeyResponse()
            text_82.setOpacity(tutorial_opac)
            text_82.setHeight(lh)
            polygon_6.setOpacity(tutorial_opac)
            # keep track of which components have finished
            rew_explComponents = [text_41, instr_resp, text_42, text_82, polygon_6]
            for thisComponent in rew_explComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "rew_expl"-------
            while continueRoutine:
                # get current time
                t = rew_explClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_41* updates
                if t >= 0.0 and text_41.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_41.tStart = t
                    text_41.frameNStart = frameN  # exact frame index
                    text_41.setAutoDraw(True)
                
                # *instr_resp* updates
                if t >= 0.0 and instr_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    instr_resp.tStart = t
                    instr_resp.frameNStart = frameN  # exact frame index
                    instr_resp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if instr_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        instr_resp.keys = theseKeys[-1]  # just the last key pressed
                        instr_resp.rt = instr_resp.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_42* updates
                if t >= 2 and text_42.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_42.tStart = t
                    text_42.frameNStart = frameN  # exact frame index
                    text_42.setAutoDraw(True)
                
                # *text_82* updates
                if t >= 0.0 and text_82.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_82.tStart = t
                    text_82.frameNStart = frameN  # exact frame index
                    text_82.setAutoDraw(True)
                
                # *polygon_6* updates
                if t >= 0.0 and polygon_6.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_6.tStart = t
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in rew_explComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rew_expl"-------
            for thisComponent in rew_explComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            rew_instr_trial, run_rew_instr = stop_instructions(rew_instr_trial, texts_main, run_rew_instr)
            
            if not run_rew_instr:
                continueRoutine = False
                trials_2.finished = True
                
            
            
            # check responses
            if instr_resp.keys in ['', [], None]:  # No response was made
                instr_resp.keys=None
            trials_2.addData('instr_resp.keys',instr_resp.keys)
            if instr_resp.keys != None:  # we had a response
                trials_2.addData('instr_resp.rt', instr_resp.rt)
            # the Routine "rew_expl" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed run_rew_instr repeats of 'trials_2'
        
        
        # ------Prepare to start Routine "rew_ann"-------
        t = 0
        rew_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        rew_t = 5
        
        if trial >= halfway_go: # this only happens if the participant is halfway through
            lh, tutorial_opac = turn_off_tutorial()
        
        if not run_rew_instr:
            run_rew_instr = 100         # we set back to initial values
            rew_instr_trial = 1
        image.setImage(curr_reward)
        # keep track of which components have finished
        rew_annComponents = [text_2, image, text_125]
        for thisComponent in rew_annComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rew_ann"-------
        while continueRoutine:
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
            frameRemains = 0.0 + rew_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + rew_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # *text_125* updates
            if t >= 5 and text_125.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_125.tStart = t
                text_125.frameNStart = frameN  # exact frame index
                text_125.setAutoDraw(True)
            frameRemains = 5 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_125.status == STARTED and t >= frameRemains:
                text_125.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rew_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rew_ann"-------
        for thisComponent in rew_annComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'rew', 0)
        
        # the Routine "rew_ann" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed run_rew repeats of 'rew_role'
    
    
    # set up handler to look after randomisation of conditions etc
    ev_role = data.TrialHandler(nReps=run_ev, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ev_role')
    thisExp.addLoop(ev_role)  # add the loop to the experiment
    thisEv_role = ev_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEv_role.rgb)
    if thisEv_role != None:
        for paramName in thisEv_role:
            exec('{} = thisEv_role[paramName]'.format(paramName))
    
    for thisEv_role in ev_role:
        currentLoop = ev_role
        # abbreviate parameter names if possible (e.g. rgb = thisEv_role.rgb)
        if thisEv_role != None:
            for paramName in thisEv_role:
                exec('{} = thisEv_role[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        ev_loop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('ev.csv'),
            seed=None, name='ev_loop')
        thisExp.addLoop(ev_loop)  # add the loop to the experiment
        thisEv_loop = ev_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisEv_loop.rgb)
        if thisEv_loop != None:
            for paramName in thisEv_loop:
                exec('{} = thisEv_loop[paramName]'.format(paramName))
        
        for thisEv_loop in ev_loop:
            currentLoop = ev_loop
            # abbreviate parameter names if possible (e.g. rgb = thisEv_loop.rgb)
            if thisEv_loop != None:
                for paramName in thisEv_loop:
                    exec('{} = thisEv_loop[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            trials_3 = data.TrialHandler(nReps=run_ev_instr, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_3')
            thisExp.addLoop(trials_3)  # add the loop to the experiment
            thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    exec('{} = thisTrial_3[paramName]'.format(paramName))
            
            for thisTrial_3 in trials_3:
                currentLoop = trials_3
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
                if thisTrial_3 != None:
                    for paramName in thisTrial_3:
                        exec('{} = thisTrial_3[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "ev_expl"-------
                t = 0
                ev_explClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                
                
                
                texts_main = ["In this game, we simply want you to tell us how much you like this reward", \
                                  "You will do this by answering a few questions on the next screen!"]
                
                
                
                text_rew = texts_main[ev_instr_trial - 1]
                text_45.setText(text_rew)
                key_resp_6 = event.BuilderKeyResponse()
                text_89.setHeight(lh)
                polygon_7.setOpacity(tutorial_opac)
                # keep track of which components have finished
                ev_explComponents = [text_45, key_resp_6, text_64, text_89, polygon_7]
                for thisComponent in ev_explComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "ev_expl"-------
                while continueRoutine:
                    # get current time
                    t = ev_explClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *text_45* updates
                    if t >= 0.0 and text_45.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_45.tStart = t
                        text_45.frameNStart = frameN  # exact frame index
                        text_45.setAutoDraw(True)
                    
                    # *key_resp_6* updates
                    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        key_resp_6.tStart = t
                        key_resp_6.frameNStart = frameN  # exact frame index
                        key_resp_6.status = STARTED
                        # keyboard checking is just starting
                    if key_resp_6.status == STARTED:
                        theseKeys = event.getKeys(keyList=['space'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_64* updates
                    if t >= 1 and text_64.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_64.tStart = t
                        text_64.frameNStart = frameN  # exact frame index
                        text_64.setAutoDraw(True)
                    
                    # *text_89* updates
                    if t >= 0.0 and text_89.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_89.tStart = t
                        text_89.frameNStart = frameN  # exact frame index
                        text_89.setAutoDraw(True)
                    
                    # *polygon_7* updates
                    if t >= 0.0 and polygon_7.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        polygon_7.tStart = t
                        polygon_7.frameNStart = frameN  # exact frame index
                        polygon_7.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in ev_explComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "ev_expl"-------
                for thisComponent in ev_explComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                ev_instr_trial, run_ev_instr = stop_instructions(ev_instr_trial, texts_main, run_ev_instr)
                
                if not run_ev_instr:
                    continueRoutine = False
                    trials_3.finished = True
                
                
                # the Routine "ev_expl" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed run_ev_instr repeats of 'trials_3'
            
            
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
            
            lh, tutorial_opac = turn_off_tutorial()
            
            text_5.setText(current_question)
            image_17.setImage(curr_reward)
            # keep track of which components have finished
            ev_promComponents = [ev_resp, text_5, first, second, third, fourth, fifth, sixth, text_12, text_13, text_14, text_15, text_16, text_47, image_17]
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
                
                # *image_17* updates
                if t >= 0.0 and image_17.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_17.tStart = t
                    image_17.frameNStart = frameN  # exact frame index
                    image_17.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ev_promComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
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
            
            stor_ev[str(ev_trial)] = [q_id, int(ev_resp.keys), ev_resp.rt]
            
            
            
            
            first_feedback.setFillColor(opt_1)
            second_feedback.setFillColor(opt_2)
            third_feedback.setFillColor(opt_3)
            fourth_feedback.setFillColor(opt_4)
            fifth_feedback.setFillColor(opt_5)
            sixth_feedback.setFillColor(opt_6)
            text_91.setHeight(lh)
            # keep track of which components have finished
            ev_feedComponents = [first_feedback, second_feedback, third_feedback, fourth_feedback, fifth_feedback, sixth_feedback, text_17, text_18, text_19, text_20, text_21, text_46, text_91]
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
                
                # *text_91* updates
                if t >= 0.0 and text_91.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_91.tStart = t
                    text_91.frameNStart = frameN  # exact frame index
                    text_91.setAutoDraw(True)
                frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_91.status == STARTED and t >= frameRemains:
                    text_91.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ev_feedComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ev_feed"-------
            for thisComponent in ev_feedComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ev_trial += 1
            
        # completed 1 repeats of 'ev_loop'
        
        
        # ------Prepare to start Routine "ev_save"-------
        t = 0
        ev_saveClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        
        
        long_stor = [trial, stor_ev['1'][0], stor_ev['1'][1], stor_ev['1'][2], \
                                   stor_ev['2'][0], stor_ev['2'][1], stor_ev['2'][2], \
                                   stor_ev['3'][0], stor_ev['3'][1], stor_ev['3'][2], reinforcer, sub_id]
        
        # saves to participant file
        save_ev(long_stor, ev_f)
        
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
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ev_saveComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ev_save"-------
        for thisComponent in ev_saveComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        if go_trial >= num_trials and eff_trial >= num_eff_trials:
            run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'ev', 1)
        else:
            run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'ev', 0)
        
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
    effort_role = data.TrialHandler(nReps=run_effort, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='effort_role')
    thisExp.addLoop(effort_role)  # add the loop to the experiment
    thisEffort_role = effort_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEffort_role.rgb)
    if thisEffort_role != None:
        for paramName in thisEffort_role:
            exec('{} = thisEffort_role[paramName]'.format(paramName))
    
    for thisEffort_role in effort_role:
        currentLoop = effort_role
        # abbreviate parameter names if possible (e.g. rgb = thisEffort_role.rgb)
        if thisEffort_role != None:
            for paramName in thisEffort_role:
                exec('{} = thisEffort_role[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler(nReps=run_eff_instr, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_4')
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    exec('{} = thisTrial_4[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            trials_7 = data.TrialHandler(nReps=run_eff_instr, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_7')
            thisExp.addLoop(trials_7)  # add the loop to the experiment
            thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
            if thisTrial_7 != None:
                for paramName in thisTrial_7:
                    exec('{} = thisTrial_7[paramName]'.format(paramName))
            
            for thisTrial_7 in trials_7:
                currentLoop = trials_7
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
                if thisTrial_7 != None:
                    for paramName in thisTrial_7:
                        exec('{} = thisTrial_7[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "eff_expl"-------
                t = 0
                eff_explClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                texts_main = ['In the next game we want you to make a number of choices.', \
                              'If you remember from early on in the experiment, we asked you to complete picture sequences: ', \
                              'You probably found some easy...', \
                              'For some you had to think a bit to get them right...', \
                              "For some you had to think but you weren't sure if you were correct...", \
                              'And for some you did not know the answer at all.', \
                              'The choices you will be making will be about having to play out similar picture sequences.', \
                              'You will be presented with a certain difficulty level denoted by the number of filled out quarters.', \
                              'So, the left shows, a picture sequence that you found very easy.', \
                              'On the right, you see one that you found very hard.', \
                              'You will now be given several choices between either playing a shown picture sequence or not playing.', \
                              'Remember that the picture sequences will vary in difficulty level and that this is indicated by the filled out quarters.', \
                              'The computer will save all of your choices and then randomly select a few of them.', \
                              "Those that will be selected will be played out at the end of today's experiment!", \
                              "That means, if it will select a round where you decided to play it out...", \
                              "You will see a picture sequence towards the end of the experiment and will have to give us an answer.", \
                              "If it will select a round where you decided not to do it, you will not have to play and will not do anything.", \
                              "To make it more interesting, by opening a door and providing an answer...", \
                              "You will get a reward!"]
                
                curr_text = texts_main[eff_instr_trial - 1]
                
                if is_trial(eff_instr_trial, [2]):
                    _, img_opac = turn_on_tutorial()
                else:
                    _, img_opac = turn_off_tutorial()
                    
                
                if is_trial(eff_instr_trial, [8, 9, 10]):
                    _, diff_lev_opac = turn_on_tutorial()
                else:
                    _, diff_lev_opac = turn_off_tutorial()
                
                
                lh, tutorial_opac = turn_on_tutorial() 
                
                text_50.setText(curr_text)
                key_resp_8 = event.BuilderKeyResponse()
                polygon_10.setOpacity(tutorial_opac)
                text_92.setHeight(lh)
                image_29.setOpacity(img_opac)
                image_35.setOpacity(diff_lev_opac)
                image_36.setOpacity(diff_lev_opac)
                image_37.setOpacity(diff_lev_opac)
                image_38.setOpacity(diff_lev_opac)
                text_122.setText(str(run_eff_instr))
                # keep track of which components have finished
                eff_explComponents = [text_50, key_resp_8, text_65, polygon_10, text_92, image_29, image_35, image_36, image_37, image_38, text_122]
                for thisComponent in eff_explComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "eff_expl"-------
                while continueRoutine:
                    # get current time
                    t = eff_explClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    
                    # *text_50* updates
                    if t >= 0.0 and text_50.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_50.tStart = t
                        text_50.frameNStart = frameN  # exact frame index
                        text_50.setAutoDraw(True)
                    
                    # *key_resp_8* updates
                    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        key_resp_8.tStart = t
                        key_resp_8.frameNStart = frameN  # exact frame index
                        key_resp_8.status = STARTED
                        # keyboard checking is just starting
                    if key_resp_8.status == STARTED:
                        theseKeys = event.getKeys(keyList=['space'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *text_65* updates
                    if t >= 1 and text_65.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_65.tStart = t
                        text_65.frameNStart = frameN  # exact frame index
                        text_65.setAutoDraw(True)
                    
                    # *polygon_10* updates
                    if t >= 0.0 and polygon_10.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        polygon_10.tStart = t
                        polygon_10.frameNStart = frameN  # exact frame index
                        polygon_10.setAutoDraw(True)
                    
                    # *text_92* updates
                    if t >= 0.0 and text_92.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_92.tStart = t
                        text_92.frameNStart = frameN  # exact frame index
                        text_92.setAutoDraw(True)
                    
                    # *image_29* updates
                    if t >= 0.0 and image_29.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_29.tStart = t
                        image_29.frameNStart = frameN  # exact frame index
                        image_29.setAutoDraw(True)
                    
                    # *image_35* updates
                    if t >= 0.0 and image_35.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_35.tStart = t
                        image_35.frameNStart = frameN  # exact frame index
                        image_35.setAutoDraw(True)
                    
                    # *image_36* updates
                    if t >= 0.0 and image_36.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_36.tStart = t
                        image_36.frameNStart = frameN  # exact frame index
                        image_36.setAutoDraw(True)
                    
                    # *image_37* updates
                    if t >= 0.0 and image_37.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_37.tStart = t
                        image_37.frameNStart = frameN  # exact frame index
                        image_37.setAutoDraw(True)
                    
                    # *image_38* updates
                    if t >= 0.0 and image_38.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_38.tStart = t
                        image_38.frameNStart = frameN  # exact frame index
                        image_38.setAutoDraw(True)
                    
                    # *text_122* updates
                    if t >= 0.0 and text_122.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_122.tStart = t
                        text_122.frameNStart = frameN  # exact frame index
                        text_122.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in eff_explComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "eff_expl"-------
                for thisComponent in eff_explComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                eff_instr_trial, run_eff_instr = stop_instructions(eff_instr_trial, texts_main, run_eff_instr)
                
                if not run_eff_instr:
                    continueRoutine = False
                    trials_7.finished = True
                    trials_4.finished = True
                
                
                # the Routine "eff_expl" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed run_eff_instr repeats of 'trials_7'
            
            
            # ------Prepare to start Routine "eff_expl2"-------
            t = 0
            eff_expl2Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            ################################################################################################
            ################################# effort (design matrix) #######################################
            ################################################################################################
            fav_juice = 'apple'            # comment out when doin git for real
            
            drops = ["1_drops_", "2_drops_", "3_drops_", "4_drops_", "5_drops_", "6_drops_"]
            pounds = ["1_pounds", "2_pounds", "3_pounds", "4_pounds", "5_pounds", "6_pounds"]
            
            diff_levels = ['easiest', 'easy', 'medium', 'hard']
            
            for id, el in enumerate(diff_levels):
                diff_levels[id] = gen_stim_path(el)
                
            design_matrix = []
            
            design_matrix_2 = []
            
            if reinforcer_type == 1:
                
                for id, el in enumerate(drops):
                    drops[id] = gen_stim_path(el + fav_juice)
                minr, smallr, mediumr, larger, largerr, largestr = drops
                rewards = drops
            
                for i in range(0, 3): # we want 3x the same trials 
                    for rew in rewards:
                        for diff in diff_levels:
                            design_matrix.append([diff, rew])
            
                opt = design_matrix[0]
            
                rew_pic = opt[1]
                diff_pic = opt[0]
            
                for id, el in enumerate(pounds):
                    pounds[id] = gen_stim_path(el)
                rewards = pounds
            
                for i in range(0, 3): # we want 3x the same trials 
                    for rew in rewards:
                        for diff in diff_levels:
                            design_matrix_2.append([diff, rew])
            
            else:
                for id, el in enumerate(pounds):
                    pounds[id] = gen_stim_path(el)
                minr, smallr, mediumr, larger, largerr, largestr = pounds
                rewards = pounds
            
                for i in range(0, 3): # we want 3x the same trials 
                    for rew in rewards:
                        for diff in diff_levels:
                            design_matrix.append([diff, rew])
            
                opt = design_matrix[0]
            
                rew_pic = opt[1]
                diff_pic = opt[0]
            
                for id, el in enumerate(drops):
                    drops[id] = gen_stim_path(el + fav_juice)
                rewards = drops
            
                for i in range(0, 3): # we want 3x the same trials 
                    for rew in rewards:
                        for diff in diff_levels:
                            design_matrix_2.append([diff, rew])
            
            
            tmp_design_matrix = deepcopy(design_matrix)
            random.shuffle(tmp_design_matrix) 
            image_8.setImage(minr)
            image_9.setImage(smallr)
            image_10.setImage(mediumr)
            key_resp_4 = event.BuilderKeyResponse()
            text_93.setHeight(lh)
            polygon_11.setOpacity(tutorial_opac)
            image_26.setImage(larger)
            image_33.setImage(largerr)
            image_34.setImage(largestr)
            # keep track of which components have finished
            eff_expl2Components = [text_70, image_8, image_9, image_10, key_resp_4, text_71, text_93, polygon_11, image_26, image_33, image_34]
            for thisComponent in eff_expl2Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_expl2"-------
            while continueRoutine:
                # get current time
                t = eff_expl2Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_70* updates
                if t >= 0.0 and text_70.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_70.tStart = t
                    text_70.frameNStart = frameN  # exact frame index
                    text_70.setAutoDraw(True)
                
                # *image_8* updates
                if t >= 0.0 and image_8.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_8.tStart = t
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.setAutoDraw(True)
                
                # *image_9* updates
                if t >= 0.0 and image_9.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_9.tStart = t
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.setAutoDraw(True)
                
                # *image_10* updates
                if t >= 0.0 and image_10.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_10.tStart = t
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.setAutoDraw(True)
                
                # *key_resp_4* updates
                if t >= 0.0 and key_resp_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_4.tStart = t
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                if key_resp_4.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_71* updates
                if t >= 1 and text_71.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_71.tStart = t
                    text_71.frameNStart = frameN  # exact frame index
                    text_71.setAutoDraw(True)
                
                # *text_93* updates
                if t >= 0.0 and text_93.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_93.tStart = t
                    text_93.frameNStart = frameN  # exact frame index
                    text_93.setAutoDraw(True)
                
                # *polygon_11* updates
                if t >= 0.0 and polygon_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_11.tStart = t
                    polygon_11.frameNStart = frameN  # exact frame index
                    polygon_11.setAutoDraw(True)
                
                # *image_26* updates
                if t >= 0.0 and image_26.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_26.tStart = t
                    image_26.frameNStart = frameN  # exact frame index
                    image_26.setAutoDraw(True)
                
                # *image_33* updates
                if t >= 0.0 and image_33.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_33.tStart = t
                    image_33.frameNStart = frameN  # exact frame index
                    image_33.setAutoDraw(True)
                
                # *image_34* updates
                if t >= 0.0 and image_34.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_34.tStart = t
                    image_34.frameNStart = frameN  # exact frame index
                    image_34.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in eff_expl2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_expl2"-------
            for thisComponent in eff_expl2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "eff_expl2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "eff_expl4"-------
            t = 0
            eff_expl4Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            image_16.setImage(diff_pic)
            key_resp_10 = event.BuilderKeyResponse()
            text_95.setHeight(lh)
            polygon_13.setOpacity(tutorial_opac)
            image_18.setImage(rew_pic)
            # keep track of which components have finished
            eff_expl4Components = [text_77, image_16, key_resp_10, text_83, text_95, polygon_13, image_18, text_28, text_62, text_63]
            for thisComponent in eff_expl4Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_expl4"-------
            while continueRoutine:
                # get current time
                t = eff_expl4Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_77* updates
                if t >= 0.0 and text_77.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_77.tStart = t
                    text_77.frameNStart = frameN  # exact frame index
                    text_77.setAutoDraw(True)
                frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_77.status == STARTED and t >= frameRemains:
                    text_77.setAutoDraw(False)
                
                # *image_16* updates
                if t >= 0.0 and image_16.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_16.tStart = t
                    image_16.frameNStart = frameN  # exact frame index
                    image_16.setAutoDraw(True)
                
                # *key_resp_10* updates
                if t >= 0.0 and key_resp_10.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_10.tStart = t
                    key_resp_10.frameNStart = frameN  # exact frame index
                    key_resp_10.status = STARTED
                    # keyboard checking is just starting
                if key_resp_10.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_83* updates
                if t >= 6 and text_83.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_83.tStart = t
                    text_83.frameNStart = frameN  # exact frame index
                    text_83.setAutoDraw(True)
                
                # *text_95* updates
                if t >= 0.0 and text_95.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_95.tStart = t
                    text_95.frameNStart = frameN  # exact frame index
                    text_95.setAutoDraw(True)
                
                # *polygon_13* updates
                if t >= 0.0 and polygon_13.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_13.tStart = t
                    polygon_13.frameNStart = frameN  # exact frame index
                    polygon_13.setAutoDraw(True)
                
                # *image_18* updates
                if t >= 0.0 and image_18.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_18.tStart = t
                    image_18.frameNStart = frameN  # exact frame index
                    image_18.setAutoDraw(True)
                
                # *text_28* updates
                if t >= 5 and text_28.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_28.tStart = t
                    text_28.frameNStart = frameN  # exact frame index
                    text_28.setAutoDraw(True)
                
                # *text_62* updates
                if t >= 5 and text_62.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_62.tStart = t
                    text_62.frameNStart = frameN  # exact frame index
                    text_62.setAutoDraw(True)
                
                # *text_63* updates
                if t >= 5 and text_63.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_63.tStart = t
                    text_63.frameNStart = frameN  # exact frame index
                    text_63.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in eff_expl4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_expl4"-------
            for thisComponent in eff_expl4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            run_eff_instr = 0
            trials_4.finished = True
            
            win.mouseVisible = False
            # the Routine "eff_expl4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "eff_practice"-------
            t = 0
            eff_practiceClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            eff_practiceComponents = [text_104]
            for thisComponent in eff_practiceComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_practice"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = eff_practiceClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_104* updates
                if t >= 0.0 and text_104.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_104.tStart = t
                    text_104.frameNStart = frameN  # exact frame index
                    text_104.setAutoDraw(True)
                frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_104.status == STARTED and t >= frameRemains:
                    text_104.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in eff_practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_practice"-------
            for thisComponent in eff_practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
        # completed run_eff_instr repeats of 'trials_4'
        
        
        # set up handler to look after randomisation of conditions etc
        effort_midway = data.TrialHandler(nReps=run_effort_midway, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='effort_midway')
        thisExp.addLoop(effort_midway)  # add the loop to the experiment
        thisEffort_midway = effort_midway.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisEffort_midway.rgb)
        if thisEffort_midway != None:
            for paramName in thisEffort_midway:
                exec('{} = thisEffort_midway[paramName]'.format(paramName))
        
        for thisEffort_midway in effort_midway:
            currentLoop = effort_midway
            # abbreviate parameter names if possible (e.g. rgb = thisEffort_midway.rgb)
            if thisEffort_midway != None:
                for paramName in thisEffort_midway:
                    exec('{} = thisEffort_midway[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "eff_midway"-------
            t = 0
            eff_midwayClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            if reinforcer_type == 1:
                minr, smallr, mediumr, larger, largerr, largestr = pounds
            
            else: 
                minr, smallr, mediumr, larger, largerr, largestr = drops
            image_27.setImage(minr)
            image_28.setImage(smallr)
            image_29r.setImage(mediumr)
            key_resp_13 = event.BuilderKeyResponse()
            image_39.setImage(larger)
            image_40.setImage(largerr)
            image_41.setImage(largestr)
            # keep track of which components have finished
            eff_midwayComponents = [text_99, image_27, image_28, image_29r, key_resp_13, text_105, image_39, image_40, image_41]
            for thisComponent in eff_midwayComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "eff_midway"-------
            while continueRoutine:
                # get current time
                t = eff_midwayClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_99* updates
                if t >= 0.0 and text_99.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_99.tStart = t
                    text_99.frameNStart = frameN  # exact frame index
                    text_99.setAutoDraw(True)
                
                # *image_27* updates
                if t >= 0.0 and image_27.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_27.tStart = t
                    image_27.frameNStart = frameN  # exact frame index
                    image_27.setAutoDraw(True)
                
                # *image_28* updates
                if t >= 0.0 and image_28.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_28.tStart = t
                    image_28.frameNStart = frameN  # exact frame index
                    image_28.setAutoDraw(True)
                
                # *image_29r* updates
                if t >= 0.0 and image_29r.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_29r.tStart = t
                    image_29r.frameNStart = frameN  # exact frame index
                    image_29r.setAutoDraw(True)
                
                # *key_resp_13* updates
                if t >= 0.0 and key_resp_13.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_13.tStart = t
                    key_resp_13.frameNStart = frameN  # exact frame index
                    key_resp_13.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if key_resp_13.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_105* updates
                if t >= 1 and text_105.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_105.tStart = t
                    text_105.frameNStart = frameN  # exact frame index
                    text_105.setAutoDraw(True)
                
                # *image_39* updates
                if t >= 0.0 and image_39.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_39.tStart = t
                    image_39.frameNStart = frameN  # exact frame index
                    image_39.setAutoDraw(True)
                
                # *image_40* updates
                if t >= 0.0 and image_40.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_40.tStart = t
                    image_40.frameNStart = frameN  # exact frame index
                    image_40.setAutoDraw(True)
                
                # *image_41* updates
                if t >= 0.0 and image_41.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_41.tStart = t
                    image_41.frameNStart = frameN  # exact frame index
                    image_41.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in eff_midwayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "eff_midway"-------
            for thisComponent in eff_midwayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "eff_midway" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed run_effort_midway repeats of 'effort_midway'
        
        
        # set up handler to look after randomisation of conditions etc
        real_info = data.TrialHandler(nReps=run_real, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='real_info')
        thisExp.addLoop(real_info)  # add the loop to the experiment
        thisReal_info = real_info.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisReal_info.rgb)
        if thisReal_info != None:
            for paramName in thisReal_info:
                exec('{} = thisReal_info[paramName]'.format(paramName))
        
        for thisReal_info in real_info:
            currentLoop = real_info
            # abbreviate parameter names if possible (e.g. rgb = thisReal_info.rgb)
            if thisReal_info != None:
                for paramName in thisReal_info:
                    exec('{} = thisReal_info[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "real_ann"-------
            t = 0
            real_annClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            if run_real == 1:
            
                eff_trial = 1
                run_real = 0
            
                lh, tutorial_opac = turn_off_tutorial()
            
                eff_switch = 1
            
                tmp_design_matrix = [] # cleans out and starts with a new matrix after the real trials 
                tmp_design_matrix = deepcopy(design_matrix)      # start the real experiment
                random.shuffle(tmp_design_matrix) 
                tmp_str = ''
                run_real = 0
            key_resp_3 = event.BuilderKeyResponse()
            # keep track of which components have finished
            real_annComponents = [text_26, text_27, key_resp_3]
            for thisComponent in real_annComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "real_ann"-------
            while continueRoutine:
                # get current time
                t = real_annClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
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
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in real_annComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
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
        # completed run_real repeats of 'real_info'
        
        
        # ------Prepare to start Routine "eff_press"-------
        t = 0
        eff_pressClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        win.mouseVisible = False
        
        diagnostics = str(["eff tr: ", eff_trial, "design matrx: ", len(tmp_design_matrix), "haflway eff: ", halfway_eff, "run_effort: {}", run_effort, "run_go {}".format(run_go)])
        
        if not len(tmp_design_matrix):                      # we do this only once
            tmp_design_matrix = deepcopy(design_matrix_2)
            random.shuffle(tmp_design_matrix)
        #    continueRoutine = False
            run_effort = 0
        
        #print(tmp_design_matrix)
        el = 0                                               # take the first element
        
        opt = tmp_design_matrix[el]                          # first one is always the door
        tmp_design_matrix.pop(el)                            # remove so it doesn't repeat 
        
        
        door1 = opt[0]
        chest1 = opt[1]
        
        
        
        
        dr1.setImage(door1)
        chst1.setImage(chest1)
        polygon_14.setOpacity(tutorial_opac)
        text_96.setHeight(lh)
        eff_choice_box = event.BuilderKeyResponse()
        text_78.setPos(yes)
        text_118.setPos(no)
        text_123.setText(diagnostics)
        text_124.setText(run_eff_instr)
        # keep track of which components have finished
        eff_pressComponents = [dr1, chst1, polygon_14, text_96, text_114, eff_choice_box, text_78, text_118, text_123, text_124]
        for thisComponent in eff_pressComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "eff_press"-------
        while continueRoutine:
            # get current time
            t = eff_pressClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *dr1* updates
            if t >= 0.0 and dr1.status == NOT_STARTED:
                # keep track of start time/frame for later
                dr1.tStart = t
                dr1.frameNStart = frameN  # exact frame index
                dr1.setAutoDraw(True)
            
            # *chst1* updates
            if t >= 0.0 and chst1.status == NOT_STARTED:
                # keep track of start time/frame for later
                chst1.tStart = t
                chst1.frameNStart = frameN  # exact frame index
                chst1.setAutoDraw(True)
            
            # *polygon_14* updates
            if t >= 0.0 and polygon_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_14.tStart = t
                polygon_14.frameNStart = frameN  # exact frame index
                polygon_14.setAutoDraw(True)
            
            # *text_96* updates
            if t >= 0.0 and text_96.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_96.tStart = t
                text_96.frameNStart = frameN  # exact frame index
                text_96.setAutoDraw(True)
            
            # *text_114* updates
            if t >= 3 and text_114.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_114.tStart = t
                text_114.frameNStart = frameN  # exact frame index
                text_114.setAutoDraw(True)
            
            # *eff_choice_box* updates
            if t >= 0.0 and eff_choice_box.status == NOT_STARTED:
                # keep track of start time/frame for later
                eff_choice_box.tStart = t
                eff_choice_box.frameNStart = frameN  # exact frame index
                eff_choice_box.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(eff_choice_box.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if eff_choice_box.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    eff_choice_box.keys = theseKeys[-1]  # just the last key pressed
                    eff_choice_box.rt = eff_choice_box.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_78* updates
            if t >= 0.0 and text_78.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_78.tStart = t
                text_78.frameNStart = frameN  # exact frame index
                text_78.setAutoDraw(True)
            
            # *text_118* updates
            if t >= 0.0 and text_118.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_118.tStart = t
                text_118.frameNStart = frameN  # exact frame index
                text_118.setAutoDraw(True)
            
            # *text_123* updates
            if t >= 0.0 and text_123.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_123.tStart = t
                text_123.frameNStart = frameN  # exact frame index
                text_123.setAutoDraw(True)
            
            # *text_124* updates
            if t >= 0.0 and text_124.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_124.tStart = t
                text_124.frameNStart = frameN  # exact frame index
                text_124.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eff_pressComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "eff_press"-------
        for thisComponent in eff_pressComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        if eff_choice_box.keys == 'left' and key_position == 1:
            eff_choice = 1
            picked_yes = 'green'
            picked_no = 'white'
            tr_dr = door1
            tr_ch = chest1
        
        elif eff_choice_box.keys == 'left' and key_position == 2:
            eff_choice = 0
            picked_yes = 'white'
            picked_no = 'green'
            tr_dr = door1
            tr_ch = chest1
            door1 = gen_stim_path('empty')
            chest1 = gen_stim_path('empty')
        
        if eff_choice_box.keys == 'right' and key_position == 1:
            eff_choice = 0
            picked_yes = 'white'
            picked_no = 'green'
            tr_dr = door1
            tr_ch = chest1
            door1 = gen_stim_path('empty')
            chest1 = gen_stim_path('empty')
        
        elif eff_choice_box.keys == 'right' and key_position == 2:
            eff_choice = 1
            picked_yes = 'green'
            picked_no = 'white'
            tr_dr = door1
            tr_ch = chest1
        
        # check responses
        if eff_choice_box.keys in ['', [], None]:  # No response was made
            eff_choice_box.keys=None
        effort_role.addData('eff_choice_box.keys',eff_choice_box.keys)
        if eff_choice_box.keys != None:  # we had a response
            effort_role.addData('eff_choice_box.rt', eff_choice_box.rt)
        # the Routine "eff_press" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "eff_feed"-------
        t = 0
        eff_feedClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        win.mouseVisible = False
        image_11.setImage(door1)
        image_12.setImage(chest1)
        text_97.setHeight(lh)
        polygon_15.setOpacity(tutorial_opac)
        text_119.setColor(picked_yes, colorSpace='rgb')
        text_119.setPos(yes)
        text_120.setColor(picked_no, colorSpace='rgb')
        text_120.setPos(no)
        # keep track of which components have finished
        eff_feedComponents = [image_11, image_12, text_97, polygon_15, text_119, text_120]
        for thisComponent in eff_feedComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "eff_feed"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = eff_feedClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *image_11* updates
            if t >= 0.0 and image_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_11.tStart = t
                image_11.frameNStart = frameN  # exact frame index
                image_11.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_11.status == STARTED and t >= frameRemains:
                image_11.setAutoDraw(False)
            
            # *image_12* updates
            if t >= 0.0 and image_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_12.tStart = t
                image_12.frameNStart = frameN  # exact frame index
                image_12.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_12.status == STARTED and t >= frameRemains:
                image_12.setAutoDraw(False)
            
            # *text_97* updates
            if t >= 0.0 and text_97.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_97.tStart = t
                text_97.frameNStart = frameN  # exact frame index
                text_97.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_97.status == STARTED and t >= frameRemains:
                text_97.setAutoDraw(False)
            
            # *polygon_15* updates
            if t >= 0.0 and polygon_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_15.tStart = t
                polygon_15.frameNStart = frameN  # exact frame index
                polygon_15.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_15.status == STARTED and t >= frameRemains:
                polygon_15.setAutoDraw(False)
            
            # *text_119* updates
            if t >= 0.0 and text_119.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_119.tStart = t
                text_119.frameNStart = frameN  # exact frame index
                text_119.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_119.status == STARTED and t >= frameRemains:
                text_119.setAutoDraw(False)
            
            # *text_120* updates
            if t >= 0.0 and text_120.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_120.tStart = t
                text_120.frameNStart = frameN  # exact frame index
                text_120.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_120.status == STARTED and t >= frameRemains:
                text_120.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in eff_feedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "eff_feed"-------
        for thisComponent in eff_feedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        run_effort_midway = 0                                        # should be always turned off 
        
        
        tmp = remove_stim_path(tr_ch).split('_') # takes only the main information. works for drops and pounds
        
        if len(tmp) == 3:
            eff_rew, eff_reinf, _ = tmp
        else:
            eff_rew, eff_reinf = tmp
        
        eff_rew = eff_rew.strip()
        eff_reinf = eff_reinf.strip()
        
        if eff_reinf == 'drops':
            eff_reinf = 'primary'
        else:
            eff_reinf = 'secondary' 
        
        eff_diff = remove_stim_path(tr_dr).strip()
        
        
        stor_eff = [eff_trial, eff_reinf, eff_rew, eff_diff,  eff_choice, eff_choice_box.rt, part_char[1]]
        save_eff(stor_eff, eff_f)
        
        
        if eff_trial == eff_pract and not eff_switch:               # eff switch is used because we revert eff trial 
            run_real = 1                                            # to 1 after finishing the practice trial
            lh, tutorial_opac = turn_off_tutorial()                 # so when the switch is turned on
                                                                    # the tutorial goes off
        
        if eff_trial == halfway_eff:                                 # if we reached the middle 
            run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'eff', 0)
            run_eff_instr = 0
            run_effort_midway = 1                                    # so next time we see it, it will change
        
        elif eff_trial == num_eff_trials + eff_pract:                     # if they are done with the task 
            run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'eff', 1)
            run_eff_instr = 0                                        # 
        
        if not len(tmp_design_matrix):                           # this should only run
            run_transition = 1                                   # when we have emptied out
                                                                 # all the trials
        #if eff_trial >= 144:
        #    run_effort = 0
        #    effort_role.finished = True
        
        eff_trial += 1
        
        
        
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
    trials_12 = data.TrialHandler(nReps=run_transition, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_12')
    thisExp.addLoop(trials_12)  # add the loop to the experiment
    thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            exec('{} = thisTrial_12[paramName]'.format(paramName))
    
    for thisTrial_12 in trials_12:
        currentLoop = trials_12
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
        if thisTrial_12 != None:
            for paramName in thisTrial_12:
                exec('{} = thisTrial_12[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "transition3"-------
        t = 0
        transition3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        key_resp_16 = event.BuilderKeyResponse()
        # keep track of which components have finished
        transition3Components = [text_43, key_resp_16, text_121]
        for thisComponent in transition3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "transition3"-------
        while continueRoutine:
            # get current time
            t = transition3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_43* updates
            if t >= 0.0 and text_43.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_43.tStart = t
                text_43.frameNStart = frameN  # exact frame index
                text_43.setAutoDraw(True)
            
            # *key_resp_16* updates
            if t >= 0.0 and key_resp_16.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_16.tStart = t
                key_resp_16.frameNStart = frameN  # exact frame index
                key_resp_16.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if key_resp_16.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_121* updates
            if t >= 1 and text_121.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_121.tStart = t
                text_121.frameNStart = frameN  # exact frame index
                text_121.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in transition3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "transition3"-------
        for thisComponent in transition3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        run_transition = 0
        # the Routine "transition3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed run_transition repeats of 'trials_12'
    
    # get names of stimulus parameters
    if trials_12.trialList in ([], [None], None):
        params = []
    else:
        params = trials_12.trialList[0].keys()
    # save data for this loop
    trials_12.saveAsExcel(filename + '.xlsx', sheetName='trials_12',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_12.saveAsText(filename + 'trials_12.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    go_role = data.TrialHandler(nReps=run_go, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='go_role')
    thisExp.addLoop(go_role)  # add the loop to the experiment
    thisGo_role = go_role.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGo_role.rgb)
    if thisGo_role != None:
        for paramName in thisGo_role:
            exec('{} = thisGo_role[paramName]'.format(paramName))
    
    for thisGo_role in go_role:
        currentLoop = go_role
        # abbreviate parameter names if possible (e.g. rgb = thisGo_role.rgb)
        if thisGo_role != None:
            for paramName in thisGo_role:
                exec('{} = thisGo_role[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler(nReps=run_go_instr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_5')
        thisExp.addLoop(trials_5)  # add the loop to the experiment
        thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        for thisTrial_5 in trials_5:
            currentLoop = trials_5
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
            if thisTrial_5 != None:
                for paramName in thisTrial_5:
                    exec('{} = thisTrial_5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "go_expl"-------
            t = 0
            go_explClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            imgs_upper = ["steven", \
                          "steven", \
                          "empty", \
                          "empty", \
                          "steven_l", \
                          "steven_l", \
                          "steven_con", \
                          "steven_con", \
                          "steven_inc", \
                          "steven_inc", \
                           "empty", \
                           "empty", \
                           "juice", \
                           "juice", \
                           "hard_diff", \
                           "hard_diff", \
                           "empty", \
                           "5_drops", \
                           "5_drops", \
                            "empty"]
            
            
            imgs_lower = ["empty", \
                          "empty", \
                          "empty", \
                          "steven_r", \
                          "empty", \
                          "steven_r", \
                          "empty", \
                          "steven_con", \
                          "empty", \
                          "steven_no", \
                          "empty", \
                          "empty", \
                          "empty", \
                          "empty", \
                          "empty", \
                          "easy_diff", \
                          "empty",  \
                          "empty", \
                          "1_drops", \
                          "empty",]
            
            size_u = [(0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.1, 0.035), \
                    (0.1, 0.035), \
                    (0.1, 0.035), \
                    (0.1, 0.035), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.35, 0.5), \
                    (0.35, 0.5), \
                    (0.2, 0.3), \
                    (0.2, 0.3), \
                    (0.3, 0.5), \
                    (0.3, 0.5), \
                    (0.3, 0.5), \
                    (0.2, 0.2), \
                    (0.2, 0.2)]
            
            size_l = [(0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.1, 0.035), \
                    (0.1, 0.035), \
                    (0.1, 0.035), \
                    (0.1, 0.035), \
                    (0.2, 0.2), \
                    (0.35, 0.5), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.2, 0.3), \
                    (0.2, 0.2), \
                    (0.2, 0.2), \
                    (0.3, 0.5), \
                    (0.2, 0.2)]
            
            fav_juice = 'apple'         # comment out when done 
            
            if reinforcer == 'primary':
                imgs_upper[12] = 'juice'
                imgs_upper[13] = 'juice'
                imgs_upper[17] = '5_drops_' + fav_juice
                imgs_upper[18] = '5_drops_' + fav_juice
                imgs_lower[18] = '1_drops_' + fav_juice
            
            else:
                imgs_upper[12] = 'pound'
                imgs_upper[13] = 'pound'
                imgs_upper[17] = '5_pounds'
                imgs_upper[18] = '5_pounds'
                imgs_lower[18] = '1_pounds'
            
            
            texts_upper = ["Meet Steven!", \
                           "Meet Steven!", \
            
                           "You will have to help Steven find the direction of the food.", \
                           "You will have to help Steven find the direction of the food.", \
            
                          "If you see Steven with the arrow in this direction, then you need to press 'f' on the keyboard as quickly as possible.", \
                          "If you see Steven with the arrow in this direction, then you need to press 'f' on the keyboard as quickly as possible.", \
            
                          "Steven will always be accompanied by friends: ", \
                          "Steven will always be accompanied by friends: ", \
            
                          "In other cases, Steven's friends will be facing another direction, because they think the food is there.", \
                          "In other cases, Steven's friends will be facing another direction, because they think the food is there.", \
                    
                          "It is important that you always pay attention only to Steven and not to his friends. So, you have to focus on Steven!", \
                          "It is important that you always pay attention only to Steven and not to his friends. So, you have to focus on Steven!", \
            
                          "You will receive the reward you were told about before: ", \
                          "You will receive the reward you were told about before: ", \
            
                          "One last thing is that sometimes you will see Steven only briefly. If that happens, you will see the red clock: ", \
                          "One last thing is that sometimes you will see Steven only briefly. If that happens, you will see the red clock: ", \
            
                          "When you will see him briefly, you will need to be extra quick with your response!", \
            
                          "Sometimes, Steven will be able to give you a lot of reward if you will be correct: ", \
                          "Sometimes, Steven will be able to give you a lot of reward if you will be correct: ", \
            
                          "Let's do some practice now!"]
            
            
            texts_lower = ["", \
                           "Steven is hungry and wants to eat.", \
                           "", \
                          "To make it easier for you, Steven has been equipped with an arrow that will show you where the food is.", 
                          "", \
                          "If you see him going in this direction, you need to press 'k', again as quickly as possible.", \
                          "", \
                          "Sometimes, his friends will be facing the same direction: ", \
                          "", \
                          "Sometimes, it will happen that there is no food, so you should not press anything!", \
                          "", \
                          "If you do the correct thing (pressing 'f' or 'k' when we know where the food is and not pressing anything when we do not...)", \
                          "", \
                          "This means, the more often you will be correct, the more rewards you will get!", \
                          "", \
                          "If you will see him for a longer time, you will see the green clock: ", \
                          "", \
                          "", \
                          "Sometimes, he will only be able to give you a little reward, if you are correct.", \
                          ""]
            
            curr_upp = texts_upper[go_instr_trial - 1]
            curr_low = texts_lower[go_instr_trial - 1]
            curr_upp_img = gen_stim_path(imgs_upper[go_instr_trial - 1])
            curr_low_img = gen_stim_path(imgs_lower[go_instr_trial - 1])
            
            curr_size_l = size_l[go_instr_trial - 1]
            curr_size_u = size_u[go_instr_trial - 1]
            
            lh, tutorial_opac = turn_on_tutorial()
            
             
            text_low.setText(curr_low)
            key_resp_11 = event.BuilderKeyResponse()
            text_upp.setText(curr_upp)
            image_upp.setImage(curr_upp_img)
            image_upp.setSize(curr_size_u)
            image_low.setImage(curr_low_img)
            image_low.setSize(curr_size_l)
            text_100.setHeight(lh)
            polygon_16.setOpacity(tutorial_opac)
            # keep track of which components have finished
            go_explComponents = [text_low, key_resp_11, text_85, text_upp, image_upp, image_low, text_100, polygon_16]
            for thisComponent in go_explComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "go_expl"-------
            while continueRoutine:
                # get current time
                t = go_explClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text_low* updates
                if t >= 0.0 and text_low.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_low.tStart = t
                    text_low.frameNStart = frameN  # exact frame index
                    text_low.setAutoDraw(True)
                
                # *key_resp_11* updates
                if t >= 0.0 and key_resp_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_11.tStart = t
                    key_resp_11.frameNStart = frameN  # exact frame index
                    key_resp_11.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if key_resp_11.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_85* updates
                if t >= 1 and text_85.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_85.tStart = t
                    text_85.frameNStart = frameN  # exact frame index
                    text_85.setAutoDraw(True)
                
                # *text_upp* updates
                if t >= 0.0 and text_upp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_upp.tStart = t
                    text_upp.frameNStart = frameN  # exact frame index
                    text_upp.setAutoDraw(True)
                
                # *image_upp* updates
                if t >= 0.0 and image_upp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_upp.tStart = t
                    image_upp.frameNStart = frameN  # exact frame index
                    image_upp.setAutoDraw(True)
                
                # *image_low* updates
                if t >= 0.0 and image_low.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_low.tStart = t
                    image_low.frameNStart = frameN  # exact frame index
                    image_low.setAutoDraw(True)
                
                # *text_100* updates
                if t >= 0.0 and text_100.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_100.tStart = t
                    text_100.frameNStart = frameN  # exact frame index
                    text_100.setAutoDraw(True)
                
                # *polygon_16* updates
                if t >= 0.0 and polygon_16.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    polygon_16.tStart = t
                    polygon_16.frameNStart = frameN  # exact frame index
                    polygon_16.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in go_explComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "go_expl"-------
            for thisComponent in go_explComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            go_instr_trial, run_go_instr = stop_instructions(go_instr_trial, texts_upper, run_go_instr)
            
            if not run_go_instr:
                continueRoutine = False
                trials_5.finished = True
                run_pr = 1
            
            # the Routine "go_expl" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_8 = data.TrialHandler(nReps=run_pr, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_8')
            thisExp.addLoop(trials_8)  # add the loop to the experiment
            thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
            if thisTrial_8 != None:
                for paramName in thisTrial_8:
                    exec('{} = thisTrial_8[paramName]'.format(paramName))
            
            for thisTrial_8 in trials_8:
                currentLoop = trials_8
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
                if thisTrial_8 != None:
                    for paramName in thisTrial_8:
                        exec('{} = thisTrial_8[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "go_expl3"-------
                t = 0
                go_expl3Clock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                # keep track of which components have finished
                go_expl3Components = [text_106]
                for thisComponent in go_expl3Components:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "go_expl3"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = go_expl3Clock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_106* updates
                    if t >= 0.0 and text_106.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        text_106.tStart = t
                        text_106.frameNStart = frameN  # exact frame index
                        text_106.setAutoDraw(True)
                    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if text_106.status == STARTED and t >= frameRemains:
                        text_106.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in go_expl3Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "go_expl3"-------
                for thisComponent in go_expl3Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
            # completed run_pr repeats of 'trials_8'
            
        # completed run_go_instr repeats of 'trials_5'
        
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=run_real, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
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
            
            # ------Prepare to start Routine "real_go_ann"-------
            t = 0
            real_go_annClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            if run_real == 1:
            
                go_trial = 1
                run_real = 0
            
                tmp_rt = [mean(tmp_rt)] # on the first real trial, we let the beginning
                                         # mean be their practice mean 
                
                lh, tutorial_opac = turn_off_tutorial()
            
                go_switch = 1
            key_resp_15 = event.BuilderKeyResponse()
            # keep track of which components have finished
            real_go_annComponents = [text, text_81, key_resp_15]
            for thisComponent in real_go_annComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "real_go_ann"-------
            while continueRoutine:
                # get current time
                t = real_go_annClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *text* updates
                if t >= 0.0 and text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text.tStart = t
                    text.frameNStart = frameN  # exact frame index
                    text.setAutoDraw(True)
                
                # *text_81* updates
                if t >= 1 and text_81.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_81.tStart = t
                    text_81.frameNStart = frameN  # exact frame index
                    text_81.setAutoDraw(True)
                
                # *key_resp_15* updates
                if t >= 0.0 and key_resp_15.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_15.tStart = t
                    key_resp_15.frameNStart = frameN  # exact frame index
                    key_resp_15.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if key_resp_15.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in real_go_annComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "real_go_ann"-------
            for thisComponent in real_go_annComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "real_go_ann" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed run_real repeats of 'trials'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_11 = data.TrialHandler(nReps=run_pause, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_11')
        thisExp.addLoop(trials_11)  # add the loop to the experiment
        thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
        if thisTrial_11 != None:
            for paramName in thisTrial_11:
                exec('{} = thisTrial_11[paramName]'.format(paramName))
        
        for thisTrial_11 in trials_11:
            currentLoop = trials_11
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
            if thisTrial_11 != None:
                for paramName in thisTrial_11:
                    exec('{} = thisTrial_11[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "pause"-------
            t = 0
            pauseClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(18.000000)
            # update component parameters for each repeat
            run_pause = 0
            # keep track of which components have finished
            pauseComponents = [text_90, text_111, text_112, text_113]
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "pause"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = pauseClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_90* updates
                if t >= 0.0 and text_90.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_90.tStart = t
                    text_90.frameNStart = frameN  # exact frame index
                    text_90.setAutoDraw(True)
                frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_90.status == STARTED and t >= frameRemains:
                    text_90.setAutoDraw(False)
                
                
                # *text_111* updates
                if t >= 15 and text_111.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_111.tStart = t
                    text_111.frameNStart = frameN  # exact frame index
                    text_111.setAutoDraw(True)
                frameRemains = 15 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_111.status == STARTED and t >= frameRemains:
                    text_111.setAutoDraw(False)
                
                # *text_112* updates
                if t >= 16 and text_112.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_112.tStart = t
                    text_112.frameNStart = frameN  # exact frame index
                    text_112.setAutoDraw(True)
                frameRemains = 16 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_112.status == STARTED and t >= frameRemains:
                    text_112.setAutoDraw(False)
                
                # *text_113* updates
                if t >= 17 and text_113.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_113.tStart = t
                    text_113.frameNStart = frameN  # exact frame index
                    text_113.setAutoDraw(True)
                frameRemains = 17 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_113.status == STARTED and t >= frameRemains:
                    text_113.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pauseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "pause"-------
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            if et_connected:
                controller.subscribe()
            
        # completed run_pause repeats of 'trials_11'
        
        
        # ------Prepare to start Routine "beg_fix"-------
        t = 0
        beg_fixClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # deprecated
        #block_types = ['easy_low_pound', 'easy_high_pound', 'hard_low_pound', 'hard_high_pound', \
        #               'easy_low_juice', 'easy_high_juice', 'hard_low_juice', 'hard_high_juice']
        
        curr_t = random.uniform(0.1, 0.5)
        #fav_juice = 'apple'                 # comment out when done
        
        if reinforcer == 'primary':
            reward_type = fav_juice 
            rew_pic = reward_size + "_" + fav_juice
        else:
            reward_type = 'pound'
            rew_pic = reward_size + "_" + reward_type
        
        
        diff_pic = gen_stim_path(difficulty + "_diff")
        block_type = reward_size + '_' + reward_type
        block_type = gen_stim_path(block_type)
        
        if difficulty == 'easy':
            cue_timing = 0.4
            resp_wind = mean(tmp_rt) + std(tmp_rt)*2
        
        elif difficulty == 'hard':
            cue_timing = 0.2
            resp_wind = mean(tmp_rt) + std(tmp_rt)*0.5
        
        if reward_size == 'high':
            if reinforcer == 'primary':
                amount = '\6'
            else:
                amount = 0.06
                
        else:
            if reinforcer == 'primary':
                amount = '\2'
            else:
                amount = 0.02
        
        feed_pic = gen_stim_path('empty')
        
        
        image_7.setImage(block_type)
        text_101.setHeight(lh)
        polygon_17.setOpacity(tutorial_opac)
        image_30.setImage(diff_pic)
        # keep track of which components have finished
        beg_fixComponents = [image_7, text_101, polygon_17, image_30]
        for thisComponent in beg_fixComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "beg_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = beg_fixClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *image_7* updates
            if t >= 0.0 and image_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_7.tStart = t
                image_7.frameNStart = frameN  # exact frame index
                image_7.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_7.status == STARTED and t >= frameRemains:
                image_7.setAutoDraw(False)
            
            # *text_101* updates
            if t >= 0.0 and text_101.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_101.tStart = t
                text_101.frameNStart = frameN  # exact frame index
                text_101.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_101.status == STARTED and t >= frameRemains:
                text_101.setAutoDraw(False)
            
            # *polygon_17* updates
            if t >= 0.0 and polygon_17.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_17.tStart = t
                polygon_17.frameNStart = frameN  # exact frame index
                polygon_17.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_17.status == STARTED and t >= frameRemains:
                polygon_17.setAutoDraw(False)
            
            # *image_30* updates
            if t >= 0.0 and image_30.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_30.tStart = t
                image_30.frameNStart = frameN  # exact frame index
                image_30.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_30.status == STARTED and t >= frameRemains:
                image_30.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in beg_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "beg_fix"-------
        for thisComponent in beg_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        main_cue = gen_stim_path(stimulus)
        
        # ------Prepare to start Routine "isi"-------
        t = 0
        isiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        isiComponents = [text_108]
        for thisComponent in isiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "isi"-------
        while continueRoutine:
            # get current time
            t = isiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_108* updates
            if t >= 0.0 and text_108.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_108.tStart = t
                text_108.frameNStart = frameN  # exact frame index
                text_108.setAutoDraw(True)
            frameRemains = 0.0 + curr_t- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_108.status == STARTED and t >= frameRemains:
                text_108.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isi"-------
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "isi" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "tar_ann"-------
        t = 0
        tar_annClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        main_image.setImage(main_cue)
        main_resp = event.BuilderKeyResponse()
        polygon_18.setOpacity(tutorial_opac)
        text_102.setHeight(lh)
        # keep track of which components have finished
        tar_annComponents = [main_image, main_resp, polygon_18, text_102]
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
            frameRemains = 0.0 + cue_timing- win.monitorFramePeriod * 0.75  # most of one frame period left
            if main_image.status == STARTED and t >= frameRemains:
                main_image.setAutoDraw(False)
            
            # *main_resp* updates
            if t >= 0 and main_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                main_resp.tStart = t
                main_resp.frameNStart = frameN  # exact frame index
                main_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(main_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if main_resp.status == STARTED and t >= frameRemains:
                main_resp.status = FINISHED
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
            
            # *polygon_18* updates
            if t >= 0.0 and polygon_18.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_18.tStart = t
                polygon_18.frameNStart = frameN  # exact frame index
                polygon_18.setAutoDraw(True)
            frameRemains = 0.0 + resp_wind- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_18.status == STARTED and t >= frameRemains:
                polygon_18.setAutoDraw(False)
            
            # *text_102* updates
            if t >= 0.0 and text_102.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_102.tStart = t
                text_102.frameNStart = frameN  # exact frame index
                text_102.setAutoDraw(True)
            frameRemains = 0.0 + resp_wind- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_102.status == STARTED and t >= frameRemains:
                text_102.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tar_annComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
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
        go_role.addData('main_resp.keys',main_resp.keys)
        if main_resp.keys != None:  # we had a response
            go_role.addData('main_resp.rt', main_resp.rt)
        # the Routine "tar_ann" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "comp"-------
        t = 0
        compClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if  main_resp.keys == left_resp:
            part_resp = 1 # left
        elif main_resp.keys == right_resp:
            part_resp = 2 # right
        else: # no go trial
            part_resp = 3
        
        if correct_resp == 'f':
            correct_response = 1
        elif correct_resp == 'k':
            correct_response = 2
        else:
            correct_response = 3
        
        allowed_length = resp_wind
        
        # make sure this is correct
        # if participant does respond and was suppose to respond and responds correctly
        if ((part_resp == 1) and (correct_response == 1) and (main_resp.rt < allowed_length)) or \
            ((part_resp == 2) and (correct_response == 2) and (main_resp.rt < allowed_length)):
            computed_resp = 1 # hit
        
        # if participant does respond and was supposed to respond and responds incorrectly
        elif ((part_resp == 1) and (correct_response == 2)) or \
            ((part_resp == 2) and (correct_response == 1)):
            computed_resp = 2 # incorrect response due to pressing incorrect key 
        
        # if participant does respond and was not supposed to respond
        elif (part_resp == 1 or part_resp == 2) and (correct_response == 3):
            computed_resp = 3 # false alarm
        
        # if participant does not respond and was not supposed to respond
        elif (part_resp == 3) and (correct_response == 3) and not main_resp.rt: # this makes it sure that participants
            computed_resp = 0 # correct rejection                               # who press in a nogo dont get accounted as 0
        
        # if participant does not respond and was supposed to respond 
        elif (part_resp == 3) and (correct_response != 3):
            computed_resp = 4 # miss
        
        elif ((part_resp == 1) and (correct_response == 1) and (main_resp.rt > allowed_length)) or \
            ((part_resp == 2) and (correct_response == 2) and (main_resp.rt > allowed_length)):
                computed_resp = 5
        
        if main_resp.rt and (computed_resp != 3):
        
            tmp_rt.append(main_resp.rt)
        
        if reinforcer == 'primary' and (computed_resp == 1 or computed_resp == 0):
        
            if gust_connected:
                dev.write(fav_juice_pumpid)
                core.wait(0.1)
                dev.write(amount)
                core.wait(0.1)
                dev.write(fav_juice_pump) # send juice squirt
                core.wait(0.1)
        
            feed_pic = gen_stim_path(rew_pic)
        #        obtained_rew = "Won: " + str(int(amount.encode('hex'), 16)/10) + ' mL of juice'
            obtained_rew = ''
        
        elif reinforcer == 'secondary' and (computed_resp == 1 or computed_resp == 0):
            cum_amount += amount
            obtained_rew = "Total: " + str(cum_amount) + ' pounds'
            feed_pic = gen_stim_path(rew_pic)
        
        
        elif computed_resp == 2 or \
             computed_resp == 3 or \
             computed_resp == 4 or \
             computed_resp == 5:
        
                vol = 0
        #            obtained_rew = 'Won: 0'
                feed_pic = gen_stim_path('empty')
        
        
        
        
        text_86.setText(obtained_rew)
        image_22.setImage(feed_pic)
        text_103.setHeight(lh)
        polygon_19.setOpacity(tutorial_opac)
        text_116.setText(str(num_trials))
        text_117.setText(str(go_trial))
        # keep track of which components have finished
        compComponents = [text_86, image_22, text_103, polygon_19, text_116, text_117]
        for thisComponent in compComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "comp"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = compClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_86* updates
            if t >= 0.0 and text_86.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_86.tStart = t
                text_86.frameNStart = frameN  # exact frame index
                text_86.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_86.status == STARTED and t >= frameRemains:
                text_86.setAutoDraw(False)
            
            # *image_22* updates
            if t >= 0.0 and image_22.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_22.tStart = t
                image_22.frameNStart = frameN  # exact frame index
                image_22.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_22.status == STARTED and t >= frameRemains:
                image_22.setAutoDraw(False)
            
            # *text_103* updates
            if t >= 0.0 and text_103.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_103.tStart = t
                text_103.frameNStart = frameN  # exact frame index
                text_103.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_103.status == STARTED and t >= frameRemains:
                text_103.setAutoDraw(False)
            
            # *polygon_19* updates
            if t >= 0.0 and polygon_19.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_19.tStart = t
                polygon_19.frameNStart = frameN  # exact frame index
                polygon_19.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_19.status == STARTED and t >= frameRemains:
                polygon_19.setAutoDraw(False)
            
            # *text_116* updates
            if t >= 0.0 and text_116.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_116.tStart = t
                text_116.frameNStart = frameN  # exact frame index
                text_116.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_116.status == STARTED and t >= frameRemains:
                text_116.setAutoDraw(False)
            
            # *text_117* updates
            if t >= 0.0 and text_117.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_117.tStart = t
                text_117.frameNStart = frameN  # exact frame index
                text_117.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_117.status == STARTED and t >= frameRemains:
                text_117.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in compComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "comp"-------
        for thisComponent in compComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if go_trial == go_pract and not go_switch:              # start running the main trials 
            run_real = 1
        
        if reinforcer == 'primary':                             # get gustaf information
            if (computed_resp == 1) or (not computed_resp):
                core.wait(0.2)
                if gust_connected:
                    act_pump, act_pump_nr, act_vol = decode_gustaf(dev)
            else:
                act_pump, act_pump_nr, act_vol = 0, 0, 0
        
        # saving the data every trial 
        stor_go = [go_trial, reinforcer, reward_size, difficulty, position, trial_type, computed_resp, main_resp.rt, cum_amount, sub_id, act_pump, act_vol, act_pump_nr]
        save_go(stor_go, go_f)
        
        if go_trial == halfway_go - 2:                          # if we are done with the first half of the go
            run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'go', 0)
        
            if et_connected:
                controller.unsubscribe()
        
        elif go_trial == num_trials:
            run_rew, run_ev, run_effort, run_go = determine_sequence(type, 'go', 1)
            if et_connected:
                controller.unsubscribe()
            
        if go_trial == block_length:
            run_pause = 1
            block_length += block_length
            if et_connected:
                controller.unsubscribe()
        
        
        go_trial += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        thisExp.nextEntry()
        
    # completed run_go repeats of 'go_role'
    
    # get names of stimulus parameters
    if go_role.trialList in ([], [None], None):
        params = []
    else:
        params = go_role.trialList[0].keys()
    # save data for this loop
    go_role.saveAsExcel(filename + '.xlsx', sheetName='go_role',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    go_role.saveAsText(filename + 'go_role.csv', delim=',',
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

# set up handler to look after randomisation of conditions etc
trials_10 = data.TrialHandler(nReps=run_cog_eff_instr, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_10')
thisExp.addLoop(trials_10)  # add the loop to the experiment
thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
if thisTrial_10 != None:
    for paramName in thisTrial_10:
        exec('{} = thisTrial_10[paramName]'.format(paramName))

for thisTrial_10 in trials_10:
    currentLoop = trials_10
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            exec('{} = thisTrial_10[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cog_eff_instr"-------
    t = 0
    cog_eff_instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    background_image.setAutoDraw(False)
    
    elems = [15, 21, 24, 30]
    
    texts_main = ["Great job so far.", \
                  "If you remember, we told you before that you would play out a few picture sequences in the end.", \
                  "The computer selected one of your choices when you were deciding for juice and one for money.", \
                  "If you decided to play in the choices that were selected, you will do so in the next game.", \
                  "This time you will not get to reconfirm your choice so make sure you answer correctly on the first try!", \
                  "If you decided to not play, you will not have to play out the picture sequence.", \
                  "Please look at the screen until you are sure you have made your choice.", \
                  "We would also ask to try and blink as little as possible while you are making your choice.", \
                  "However, you can blink when we tell you if you were correct or not!", \
                  "This is important because we will be recording with the eye tracker!", \
                  "Good luck!"]
    
    
    text_instr = get_current_text(texts_main, cog_eff_instr_trial - 1)
    
    if cog_eff_instr_trial == 1:
        all_go = glob.glob('data/*eff.txt')
        for el in all_go:
            parsed = el.split('.')[0].split('_')[1] # take the id
            if parsed == part_char[1]: # if its the person
                break
    
        primary = []
        secondary = []
    
        with open(el, 'r') as f:
            all_trials = f.readlines()
    
        for trial in all_trials[1:]:
            parsed = [el.strip() for el in trial.split('\t')]
            relevant_data = parsed[2] + '_' + parsed[3] + '_' + parsed[4] # reward size, difficulty level, choice
            if parsed[1] == 'primary':
                primary.append('primary_' + relevant_data)
            else:
                secondary.append('secondary_' + relevant_data) 
    
        if random.random() < 0.5:
            first = random.choice(primary)
            second = random.choice(secondary)
        else:
            first = random.choice(secondary)
            second = random.choice(primary)
    
        actual = [first, second]
        decisions = [first.split('_')[3], second.split('_')[3]]
    
        #lowest, low, medium, high = t
    
        diffs = []
        rews = []
    
        # size, difficulty
        for tr, decision in zip(actual, decisions):
            if int(decision):
                tr = tr.split('_')
                rews.append(tr[0] + '_' + tr[1])
                diffs.append(tr[2])
    
        difficulty_lev = transform_information(diffs, elems)            # rename the variable so we can use the diffs for presenting the image later
    
        if len(difficulty_lev) > 1:
            if (difficulty_lev[0] == difficulty_lev[1]):
                if difficulty_lev[0] != 31: # largest possible index for an item in the array. 
                    difficulty_lev[0] = difficulty_lev[0] + random.choice([-1, 1]) # can pick any element one above or below 
                else:
                    difficulty_lev[0] = difficulty_lev[0] -1 # if it's the last one we can only go down. 
    
        run_fin_eff = len(difficulty_lev)                       # this way we make it run the correct number of times. 
    key_resp_14 = event.BuilderKeyResponse()
    text_109.setText(text_instr)
    # keep track of which components have finished
    cog_eff_instrComponents = [key_resp_14, text_109, text_110]
    for thisComponent in cog_eff_instrComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cog_eff_instr"-------
    while continueRoutine:
        # get current time
        t = cog_eff_instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *key_resp_14* updates
        if t >= 0.0 and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_109* updates
        if t >= 0.0 and text_109.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_109.tStart = t
            text_109.frameNStart = frameN  # exact frame index
            text_109.setAutoDraw(True)
        
        # *text_110* updates
        if t >= 1 and text_110.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_110.tStart = t
            text_110.frameNStart = frameN  # exact frame index
            text_110.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cog_eff_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cog_eff_instr"-------
    for thisComponent in cog_eff_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    cog_eff_instr_trial, run_cog_eff_instr = stop_instructions(cog_eff_instr_trial, texts_main, run_cog_eff_instr)
    
    if not run_cog_eff_instr:
        continueRoutine = False
        trials_10.finished = True
    
    # the Routine "cog_eff_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed run_cog_eff_instr repeats of 'trials_10'


# set up handler to look after randomisation of conditions etc
trials_13 = data.TrialHandler(nReps=run_fin_eff, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_13')
thisExp.addLoop(trials_13)  # add the loop to the experiment
thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
if thisTrial_13 != None:
    for paramName in thisTrial_13:
        exec('{} = thisTrial_13[paramName]'.format(paramName))

for thisTrial_13 in trials_13:
    currentLoop = trials_13
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
    if thisTrial_13 != None:
        for paramName in thisTrial_13:
            exec('{} = thisTrial_13[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cog_eff_fin_select"-------
    t = 0
    cog_eff_fin_selectClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    
    # if both picked are 0 
    if not len(difficulty_lev):
        fin_pic = gen_stim_path('empty')
        fin_diff = gen_stim_path('empty')
        fin_rew = gen_stim_path('empty')
        run_nasa = 0
        run_fin_eff_tr = 0
    
    elif len(difficulty_lev) == 1:
    
        if cog_eff_trial == 1:
            fin_pic = stim_list[difficulty_lev[0]]
    
            curr = rews[0]
            curr = curr.split('_')
    
            if curr[0] == 'primary':
                fin_rew = curr[1] + '_' + 'drops_' + fav_juice
            else:
                fin_rew = curr[1] + '_' + 'pounds'
    
            fin_rew = gen_stim_path(fin_rew)
        
            fin_diff = gen_stim_path(diffs[0])
        
            if et_connected:
                controller.subscribe()
        
        else:
            fin_pic = gen_stim_path('empty')
            fin_rew = gen_stim_path('empty')
            fin_diff = gen_stim_path('empty')
            run_nasa  = 0
            run_fin_eff_tr = 0
    else:
    
        fin_pic = stim_list[difficulty_lev[cog_eff_trial - 1]]
        fin_diff = gen_stim_path(diffs[cog_eff_trial - 1])
        curr = rews[cog_eff_trial - 1]
        curr = curr.split('_')
    
        if curr[0] == 'primary':
            fin_rew = curr[1] + '_' + 'drops_' + fav_juice
        else:
            fin_rew = curr[1] + '_' + 'pounds'
    
        fin_rew = gen_stim_path(fin_rew)
        
        if et_connected:
            controller.subscribe() 
    
    image_31.setImage(fin_diff)
    image_32.setImage(fin_rew)
    # keep track of which components have finished
    cog_eff_fin_selectComponents = [text_115, image_31, image_32]
    for thisComponent in cog_eff_fin_selectComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cog_eff_fin_select"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cog_eff_fin_selectClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_115* updates
        if t >= 0.0 and text_115.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_115.tStart = t
            text_115.frameNStart = frameN  # exact frame index
            text_115.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_115.status == STARTED and t >= frameRemains:
            text_115.setAutoDraw(False)
        
        # *image_31* updates
        if t >= 0.0 and image_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_31.tStart = t
            image_31.frameNStart = frameN  # exact frame index
            image_31.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_31.status == STARTED and t >= frameRemains:
            image_31.setAutoDraw(False)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_32.status == STARTED and t >= frameRemains:
            image_32.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cog_eff_fin_selectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cog_eff_fin_select"-------
    for thisComponent in cog_eff_fin_selectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # set up handler to look after randomisation of conditions etc
    cog_eff_final_data = data.TrialHandler(nReps=run_fin_eff_tr, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cog_eff_final_data')
    thisExp.addLoop(cog_eff_final_data)  # add the loop to the experiment
    thisCog_eff_final_data = cog_eff_final_data.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCog_eff_final_data.rgb)
    if thisCog_eff_final_data != None:
        for paramName in thisCog_eff_final_data:
            exec('{} = thisCog_eff_final_data[paramName]'.format(paramName))
    
    for thisCog_eff_final_data in cog_eff_final_data:
        currentLoop = cog_eff_final_data
        # abbreviate parameter names if possible (e.g. rgb = thisCog_eff_final_data.rgb)
        if thisCog_eff_final_data != None:
            for paramName in thisCog_eff_final_data:
                exec('{} = thisCog_eff_final_data[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "cog_eff_fin"-------
        t = 0
        cog_eff_finClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_24.setImage(fin_pic)
        cog_eff_fin_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        cog_eff_finComponents = [image_24, cog_eff_fin_resp]
        for thisComponent in cog_eff_finComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cog_eff_fin"-------
        while continueRoutine:
            # get current time
            t = cog_eff_finClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_24* updates
            if t >= 0.0 and image_24.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_24.tStart = t
                image_24.frameNStart = frameN  # exact frame index
                image_24.setAutoDraw(True)
            
            # *cog_eff_fin_resp* updates
            if t >= 0.0 and cog_eff_fin_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                cog_eff_fin_resp.tStart = t
                cog_eff_fin_resp.frameNStart = frameN  # exact frame index
                cog_eff_fin_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(cog_eff_fin_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if cog_eff_fin_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    cog_eff_fin_resp.keys = theseKeys[-1]  # just the last key pressed
                    cog_eff_fin_resp.rt = cog_eff_fin_resp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cog_eff_finComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cog_eff_fin"-------
        for thisComponent in cog_eff_finComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if cog_eff_fin_resp.keys in ['', [], None]:  # No response was made
            cog_eff_fin_resp.keys=None
        cog_eff_final_data.addData('cog_eff_fin_resp.keys',cog_eff_fin_resp.keys)
        if cog_eff_fin_resp.keys != None:  # we had a response
            cog_eff_final_data.addData('cog_eff_fin_resp.rt', cog_eff_fin_resp.rt)
        # the Routine "cog_eff_fin" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cog_eff_fin_answ"-------
        t = 0
        cog_eff_fin_answClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        
        stim_corr_ans = [2, 3, 2, 1, 3, 1, 5, 1, 3, 3, 4, 2, 3, 4, 1, 4, \
                         2, 5, 4, 2, 4, 2, 3, 3, 1, 4, 4, 2, 5, 5, 1, 2]
        
        
        corr_resp =  stim_corr_ans[difficulty_lev[cog_eff_trial - 1]] # this gets the index of the stim corr ans
        
        
        if int(cog_eff_fin_resp.keys) == stim_corr_ans[corr_resp]:
            feed = 'Correct!'
        
        else:
            feed = 'Incorrect!'
            fin_rew = gen_stim_path('empty')
        
        text_98.setText(feed)
        # keep track of which components have finished
        cog_eff_fin_answComponents = [text_98]
        for thisComponent in cog_eff_fin_answComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cog_eff_fin_answ"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cog_eff_fin_answClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_98* updates
            if t >= 0.0 and text_98.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_98.tStart = t
                text_98.frameNStart = frameN  # exact frame index
                text_98.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_98.status == STARTED and t >= frameRemains:
                text_98.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cog_eff_fin_answComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cog_eff_fin_answ"-------
        for thisComponent in cog_eff_fin_answComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        cog_eff_trial += 1
        thisExp.nextEntry()
        
    # completed run_fin_eff_tr repeats of 'cog_eff_final_data'
    
    # get names of stimulus parameters
    if cog_eff_final_data.trialList in ([], [None], None):
        params = []
    else:
        params = cog_eff_final_data.trialList[0].keys()
    # save data for this loop
    cog_eff_final_data.saveAsExcel(filename + '.xlsx', sheetName='cog_eff_final_data',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    cog_eff_final_data.saveAsText(filename + 'cog_eff_final_data.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    nasa_trials = data.TrialHandler(nReps=run_nasa, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('nasa_tlx.csv'),
        seed=None, name='nasa_trials')
    thisExp.addLoop(nasa_trials)  # add the loop to the experiment
    thisNasa_trial = nasa_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNasa_trial.rgb)
    if thisNasa_trial != None:
        for paramName in thisNasa_trial:
            exec('{} = thisNasa_trial[paramName]'.format(paramName))
    
    for thisNasa_trial in nasa_trials:
        currentLoop = nasa_trials
        # abbreviate parameter names if possible (e.g. rgb = thisNasa_trial.rgb)
        if thisNasa_trial != None:
            for paramName in thisNasa_trial:
                exec('{} = thisNasa_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "nasa_tlx"-------
        t = 0
        nasa_tlxClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if et_connected:
            controller.unsubscribe()
            controller.close_datafile()
        
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
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in nasa_tlxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "nasa_tlx"-------
        for thisComponent in nasa_tlxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stor_nasa_q.append([sav_mapping, rating_3.getRating()])
        
        row_len = 7
        
        tmp_trial += 1
        
        if tmp_trial == row_len: # end of questions about nasa
        
            complete = set_filename(part_char, 'nasa_tlx(nasa_tlx.csv)')
            nasa_q = open(complete, 'w')
            
            stor_nasa_q = sorted(stor_nasa_q, key=lambda x: x[0])
        
            for el1, el2 in stor_nasa_q:
                struct_1 += "nasa_q" + str(el1) + "\t"
            
            struct_1 += "reinforcer\t" + "sub_id\n"  #subid
        
            nasa_q.write(struct_1)
            
            
            for i in range(0, len(stor_nasa_q)):
                struct_2 += "{}\t"
        
            struct_2 += "{}\t{}\n"
        
            tmp_list = [el2 for el1, el2 in stor_nasa_q] 
         
            tmp_list.append(curr[0])
            tmp_list.append(sub_id)
        
            nasa_q.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3],
                                             tmp_list[4], tmp_list[5], tmp_list[6], tmp_list[7]))
            nasa_q.close()
            print("Successfully saved the NASA TLX dataset.")
        
            struct_1 = ''
            struct_2 = ''
            tmp_list = []
            tmp_trial = 0
        
            print("This is the tmp trial after nasa tlx {}".format(tmp_trial))
        
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
    thisExp.nextEntry()
    
# completed run_fin_eff repeats of 'trials_13'

# get names of stimulus parameters
if trials_13.trialList in ([], [None], None):
    params = []
else:
    params = trials_13.trialList[0].keys()
# save data for this loop
trials_13.saveAsExcel(filename + '.xlsx', sheetName='trials_13',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_13.saveAsText(filename + 'trials_13.csv', delim=',',
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
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in juice_evalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "juice_eval"-------
for thisComponent in juice_evalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
complete = set_filename(part_char, 'juice valuation')
juice_eval_mini = open(complete, 'w')

inputText = inputText + "\t" + part_char[1]

juice_eval_mini.write(inputText)
juice_eval_mini.close()
print("Successfully saved the juice evaluation.")
print("This is the tmp trial after juice eval {}".format(tmp_trial))
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
    for paramName in thisFinal_pic_eval_trial:
        exec('{} = thisFinal_pic_eval_trial[paramName]'.format(paramName))

for thisFinal_pic_eval_trial in final_pic_eval_trials:
    currentLoop = final_pic_eval_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFinal_pic_eval_trial.rgb)
    if thisFinal_pic_eval_trial != None:
        for paramName in thisFinal_pic_eval_trial:
            exec('{} = thisFinal_pic_eval_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ev_pic"-------
    t = 0
    ev_picClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # this is the question it randomly pulls from the .csv file
    pic_q = current_question
    
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ev_picComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ev_pic"-------
    for thisComponent in ev_picComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stor_pic_q.append([sav_mapping, rating_2.getRating()])
    tmp_trial += 1
    row_len = 7
    
    if tmp_trial == row_len: # end of questions about pictures
    
        stor_pic_q = sorted(stor_pic_q, key=lambda x: x[0])
    
        complete = set_filename(part_char, 'pic_q(pic_rating.csv)')
        pic_q_data = open(complete, 'w')
        
        for el1, el2 in stor_pic_q:
            struct_1 += "pic" + str(el1) + "\t"
        
        struct_1 += "sub_id\n"  #subid
    
        pic_q_data.write(struct_1)
        
        for i in range(0, len(stor_pic_q)):
            struct_2 += "{}\t"
    
        struct_2 += "{}\n"
    
        tmp_list = [el2 for el1, el2 in stor_pic_q] 
        tmp_list.append(sub_id)
    
        pic_q_data.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3],
                                         tmp_list[4], tmp_list[5], tmp_list[6]))
        pic_q_data.close()
        print("Successfully saved the picture evaluation dataset.")
    
        struct_1 = ''
        struct_2 = ''
        tmp_list = []
        tmp_trial = 0
        print("this is tmp trial after ev pic {}".format(tmp_trial))
    
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

# set up handler to look after randomisation of conditions etc
nfc_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nfc.csv'),
    seed=None, name='nfc_trials')
thisExp.addLoop(nfc_trials)  # add the loop to the experiment
thisNfc_trial = nfc_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNfc_trial.rgb)
if thisNfc_trial != None:
    for paramName in thisNfc_trial:
        exec('{} = thisNfc_trial[paramName]'.format(paramName))

for thisNfc_trial in nfc_trials:
    currentLoop = nfc_trials
    # abbreviate parameter names if possible (e.g. rgb = thisNfc_trial.rgb)
    if thisNfc_trial != None:
        for paramName in thisNfc_trial:
            exec('{} = thisNfc_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "nfc_scale"-------
    t = 0
    nfc_scaleClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    nfc_question = current_question
    
    nfc_scale_text.setText(nfc_question
)
    rating_4.reset()
    # keep track of which components have finished
    nfc_scaleComponents = [nfc_scale_text, rating_4]
    for thisComponent in nfc_scaleComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "nfc_scale"-------
    while continueRoutine:
        # get current time
        t = nfc_scaleClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *nfc_scale_text* updates
        if t >= 0.0 and nfc_scale_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            nfc_scale_text.tStart = t
            nfc_scale_text.frameNStart = frameN  # exact frame index
            nfc_scale_text.setAutoDraw(True)
        # *rating_4* updates
        if t >= 0.0 and rating_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_4.tStart = t
            rating_4.frameNStart = frameN  # exact frame index
            rating_4.setAutoDraw(True)
        continueRoutine &= rating_4.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nfc_scaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nfc_scale"-------
    for thisComponent in nfc_scaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stor_nfc_q.append([sav_mapping, rating_4.getRating()])
    
    nfc_trial += 1
    row_len = 18
    
    if nfc_trial == row_len: # end of questions about nasa
    
        complete = set_filename(part_char, 'nfc(nfc.csv)')
        nfc_q = open(complete, 'w')
    
        stor_nfc_q = sorted(stor_nfc_q, key=lambda x: x[0])
        
        for el1, el2 in stor_nfc_q:
            struct_1 += "nfc_" + str(el1) + "\t"
        
        struct_1 += "sub_id\n"  #subid
    
        nfc_q.write(struct_1)
        
        for i in range(0, len(stor_nfc_q)):
            struct_2 += "{}\t"
        print(len(stor_nfc_q))
        struct_2 += "{}\n"
    
        tmp_list = [el2 for el1, el2 in stor_nfc_q] 
        tmp_list.append(sub_id)
    
        nfc_q.write(struct_2.format(tmp_list[0], tmp_list[1], tmp_list[2], tmp_list[3],
                                    tmp_list[4], tmp_list[5], tmp_list[6], tmp_list[7],
                                    tmp_list[8], tmp_list[9], tmp_list[10], tmp_list[11],
                                    tmp_list[12], tmp_list[13], tmp_list[14], tmp_list[15], 
                                    tmp_list[16], tmp_list[17], tmp_list[18]))
    
        nfc_q.close()
    
        print("Successfully saved the NFC dataset.")
    
        struct_1 = ''
        struct_2 = ''
        tmp_list = []
    # store data for nfc_trials (TrialHandler)
    nfc_trials.addData('rating_4.response', rating_4.getRating())
    nfc_trials.addData('rating_4.rt', rating_4.getRT())
    # the Routine "nfc_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'nfc_trials'

# get names of stimulus parameters
if nfc_trials.trialList in ([], [None], None):
    params = []
else:
    params = nfc_trials.trialList[0].keys()
# save data for this loop
nfc_trials.saveAsExcel(filename + '.xlsx', sheetName='nfc_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
nfc_trials.saveAsText(filename + 'nfc_trials.csv', delim=',',
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
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
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
