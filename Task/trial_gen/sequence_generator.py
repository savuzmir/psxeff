import random
import matplotlib
import os

# the experimental file should have 1 trial more for it to run nicely in the main part because it would exit otherwise.

# Overall structure
# 528 trials:
#	- primary (264)
#		- hard (132)
#			- low (68)
#				- left (34)
#					. congruent (24)					   # .5 prob
														   # .25 prob
#					. nogo (10)						       # .25 prob
#				- right (34)
#					. congruent (24)
#					. nogo (10)
#			- high (68)
#				- left (34)
#					. congruent (24)
#					. nogo (10)
#				- right (34)
#					. congruent (24)
#					. nogo (10)
#		- easy (132)
#			- low (68)
#				- left (34)
#					. congruent (24)

#					. nogo (10)
#				- right (34)
#					. congruent (24)
#					. nogo (10)
#			- high (68)
#				- left (34)
#					. congruent (24)
#					. nogo (10)
#				- right (34)
#					. congruent (24)
#					. nogo (10)
#	- secondary (264)
#		- hard (132)
#			- low (68)
#				- left (34)
#					. congruent (24)
#					. nogo (10)
#				- right (34)
#					. congruent (24)
#					. nogo (10)
#			- high (68)
#				- left (40)
#					. congruent (24)
#					. nogo (10)
#				- right (40)
#					. congruent (24)
#					. nogo (10)
#		- easy (132)
#			- low (68)
#				- left (34)
#					. congruent (24)
#					. nogo (10)
#				- right (34)
#					. congruent (24)
#					. nogo (10)
#			- high (68)
#				- left (34)
#					. congruent (24)
#					. nogo (10)
#				- right (34)
#					. congruent (24)
#					. nogo (10)

len_trials = 540
# 12 practice trials would they receive 1 trial of each condition.  mean there are 780 - 10 = 768

rew_cond = ['low', 'high']   								# .5
diff_cond = ['easy', 'hard'] 								# .5
trial_type = ['congruent', 'nogo']			# .5, .25, .25
position = ['left', 'right'] 

begin_nr = 100
len_participants = 50

half_participants = begin_nr + int(round(len_participants/2))

sub_ids = ['part_' + str(el) for el in range(begin_nr, begin_nr + len_participants+1)]

def write_final(struct, file, pos, abs_trial):

	for trial in pos:
	#        print(trial)
		tr, reinf, rew, diff, position, trial_type, stimulus, correct_resp = trial
		trial_info  = [abs_trial, reinf, rew, diff, position, trial_type, stimulus, correct_resp]
		abs_trial += 1
	
		file.write(struct.format(trial_info[0], \
										  trial_info[1], \
										  trial_info[2], \
										  trial_info[3], \
										  trial_info[4], \
										  trial_info[5], \
										  trial_info[6], \
										  trial_info[7]))
										  
	return abs_trial

def evaluate_truth(i, len_congruent, len_incongruent, position): 		# we generate the main sequence first and randomise it afterwards

	if i <= len_congruent:
		trial_type = 'congruent'
		correct_resp = 'f'												# make the left side the default 
		
#	elif len_congruent < i <= len_incongruent:
#		trial_type = 'incongruent'
#		correct_resp = 'f'
		
	else:
		trial_type = 'nogo'
		correct_resp = ''
	
	if position == 'right':

		if correct_resp == 'f': 									    # if it's empty it should stay empty
			correct_resp = 'k'

	stimulus = position + '_' + trial_type	
	out = [trial_type, stimulus, correct_resp]
	
	return out

def write_sequence_gen(i, len_congruent, len_incongruent_nogo, len_left_right, position, abs_trial, block):

	if position == 'left':
		trial_type, stimulus, correct_resp = evaluate_truth(i, len_congruent, len_congruent+len_incongruent_nogo, position)
	
	elif position == 'right':
		trial_type, stimulus, correct_resp = evaluate_truth(i, len_left_right + len_congruent, len_left_right+len_congruent+len_incongruent_nogo, position)
		
	reinf, rew, diff = str(block).strip("[]").replace("'", "").replace(",", "").split(' ')
	    
	trial_info = [abs_trial, reinf, rew, diff, position, trial_type, stimulus, correct_resp]
	
	return trial_info


for participant in sub_ids:
    reinforcer = ['primary', 'secondary']						# .5

    if int(participant.split('_')[1]) % 2:						# for half of them
#		print(int(participant.split('_')[1]) )
#		print(half)
        reinforcer = ['secondary', 'primary']		
    else:
        reinforcer = ['primary', 'secondary']

    design_matrix = [       [reinforcer[0], rew_cond[0], diff_cond[0]], \
					 [reinforcer[0], rew_cond[0], diff_cond[1]], \
				         [reinforcer[0], rew_cond[1], diff_cond[0]], \
					 [reinforcer[0], rew_cond[1], diff_cond[1]], \
					 [reinforcer[1], rew_cond[0], diff_cond[0]], \
					 [reinforcer[1], rew_cond[0], diff_cond[1]], \
					 [reinforcer[1], rew_cond[1], diff_cond[0]], \
					 [reinforcer[1], rew_cond[1], diff_cond[1]]]

    cwd = os.getcwd()               
    complete = cwd + '/' + participant + '.csv'

    trial_sequence = open(complete, 'w')

    header = "trial,reinforcer,reward_size,difficulty,position,trial_type,stimulus,correct_resp\n"
    main_file = "{},{},{},{},{},{},{},{}\n"

    trial_sequence.write(header)									#header

    reinf, rew, diff = str(design_matrix[0]).strip("[]").replace("'", "").replace(",", "").split(' ')

    len_block = len_trials/len(design_matrix)

    stimulus = ''

    tr_ctr = len_block  													# due to python loop

    abs_trial = 1

    len_left_right = 34
    len_congruent = 24
    len_incongruent_nogo = 10

    switch = 0 

    practice_trials = []
    practice_trial = 1
    all_trials = []

    for block in design_matrix:

        for i in range(1, tr_ctr):
            if i <= len_left_right: 											# for the first 52
		
                position = 'left'
                out = write_sequence_gen(i, len_congruent, len_incongruent_nogo, len_left_right, position, abs_trial, block)
#		print(out)
#                if not switch:
 #                   if abs_trial <= 12:
  #                      practice_trials.append(out)
   #                     switch = 1
                abs_trial += 1
                all_trials.append(out)
				
            else:
		
                position = 'right'
                out = write_sequence_gen(i, len_congruent, len_incongruent_nogo, len_left_right, position, abs_trial, block)
#                if not switch:
 #                   if abs_trial <= 12:
  #                      practice_trials.append(out)
   #                     switch = 1

                abs_trial += 1
                all_trials.append(out)


	# now we need to randomise
 
    print(practice_trials)
    half = int(round(abs_trial/2))

    first_half = all_trials[:half]
    second_half = all_trials[half:]

    random.shuffle(first_half)
    random.shuffle(second_half)

    random.shuffle(first_half)

    abs_trial = 1
#    print(practice_trials)
#    write_final(main_file, trial_sequence, practice_trials, practice_trial)  
    tmp = write_final(main_file, trial_sequence, first_half, abs_trial)
    write_final(main_file, trial_sequence, second_half, tmp)
 
    trial_sequence.close()

print("Successfully saved the trial sequences.")

























