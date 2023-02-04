# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 06:49:25 2019

@author: ken.stephani
"""

player_list = ['a', 'b', 'c', 'd', 'e', 'f']
ab_thresh = 5
hr_thresh = 7

dict_ab = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 50}
dict_hr = {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10, 'f': 3}
dict_result = {}
yes = 0
no = 0
total = 0
pctg = 0

for p in player_list:
    #dict_result[p] = "no"
    total = total + 1
    if dict_ab[p] >= ab_thresh:
        if dict_hr[p] >= hr_thresh:
            yes = yes + 1
            pctg = yes/total
            print(p, dict_ab[p], dict_hr[p], total, yes, pctg)
            dict_result[p] = "yes"
        else:
            dict_result[p] = "no"
            no = no + 1
    else:
        dict_result[p] = "no"

for p in dict_result:
    print("dict_result: ", p, dict_result[p])
