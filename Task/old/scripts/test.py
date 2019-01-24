
import collections

dd = collections.defaultdict()
dd.setdefault('apple', [])
dd.setdefault('pin', [])
dd.setdefault('ora', [])

dd.setdefault('1', [])
dd.setdefault('2', [])
dd.setdefault('3', [])
dd.setdefault('4', [])

dd['apple'].append([1,2,3,4,5,6])
dd['apple'].append([1,3,3,4,5,6])
dd['apple'].append([1,4,3,4,5,6])
dd['pin'].append([2,4,3,4,5,6])
dd['pin'].append([2,3,3,4,5,6])
dd['pin'].append([2,2,3,4,5,6])
dd['ora'].append([5,2,3,4,5,6])
dd['ora'].append([5,3,3,4,5,6])
dd['ora'].append([6,4,3,4,5,6])

tmp_list = []

print(len(dd.values()))

dd = {k:v for k, v in zip(dd.keys(), dd.values()) if len(v)}

print(dd)

for key, values in zip(dd.keys(), dd.values()):
    tmp_val = 0
    for value in values: 
        tmp_val += int(value[0]) # we take the first value because that denotes the response
        print("this is the int {} going into tmp val {} for key {}".format(int(value[0]), tmp_val, key))

    tmp_len = len(dd[key])
    print("this is tmp len {}".format(tmp_len))
    tmp_list.append((key, tmp_val/tmp_len)) # we get the mean (we ask them 3 questions)