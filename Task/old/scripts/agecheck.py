options = [(1, [0.2, 0.2, 0.2]), \
           (2, [0.2, 0.2, 0.2]), \
           (3, [0.2, 0.2, 0.2]), \
           (4, [0.2, 0.2, 0.2]), \
           (5, [0.2, 0.2, 0.2]), \
           (6, [0.2, 0.2, 0.2])]

from copy import deepcopy

def color_change(picked_opt, options):
    copy_options = deepcopy(options) # this way we preserve the original

    ch_option = [1, 0.84, 0.0]
    unch_col = [0.2, 0.2, 0.2]

    for indx, option in enumerate(options):
 #       print(indx, option)
        if str(option[0]) == picked_opt:
            tmp = list(options[indx]) # hack to remove issues with deleting
 #           print(tmp)
            del tmp[1]
            tmp.append(ch_option)
            copy_options[indx] = tuple(tmp)
            print(copy_options)
        else:
			print(indx)
			print(tuple([indx+1, unch_col]))
			copy_options[indx] = tuple([indx+1, unch_col])
    return copy_options
	
	

picked_opt = '2'
x = color_change(picked_opt, options)
print(x)