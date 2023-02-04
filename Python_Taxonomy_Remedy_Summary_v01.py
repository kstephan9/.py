from DefaultItems import DataFileLocation
from DefaultItems import RecursiveList
from pathlib import Path

import xlrd
import matplotlib.pyplot as plt
import urllib
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import csv

import sys


class Test:
    pass


DataFileLocation = 'S:\BAEIT\ITIL\PerformanceManagementTeam\AssortedTasks\Learning\Python\data'


filename = 'TigerTeamData_ByWeek_20181006_Through_20190628_Special.xlsm'
fullname = DataFileLocation + '\\' + filename


def main():

    # recursively list files in directory
    # RecursiveList(DataFileLocation)

    filename = 'TigerTeamData_ByWeek_20181006_Through_20190628_Special.xlsm'
    fullname = DataFileLocation + '\\' + filename
    d = {}
    wb = xlrd.open_workbook(fullname)
    sh = wb.sheet_by_name('data')

    # load list fhand_list with content of Summary column
    fhand_list = []
    row_count = 16535
    for i in range(row_count):
        cell_value_id = sh.cell(i, 8).value
        fhand_list.append(cell_value_id)

    biglist = []
    for fh in fhand_list:
        biglist.append(fh.split())

    biggerlist = []
    for bl in biglist:
        for bl2 in bl:
            biggerlist.append(bl2)

    # for bl in biggerlist:
    #    print("biggerlist:", bl)

    dict1 = dict()
    for c in biggerlist:
        # if le not in let:
        #     let[le] = 1
        # else:
        #     let[le] = let[le] + 1
        dict1[c] = dict1.get(c, 0) + 1

    r0 = list()
    r1 = list()
    i = 0
    # print("Number of items in dict1: ", dict1.items()
    for key in dict1:
        key_stripped = key
        key_stripped = key_stripped.strip()
#        print("67 key_stripped: <", key_stripped, ">", dict1[key], len(key_stripped))
        r0.append((key_stripped, dict1[key_stripped]))  # this adds a tuple to list r
        r1.append((dict1[key_stripped], key_stripped))  # this adds a tuple to list r

    for element in r0:
        print("r0 element, a list: ", element)

    for element in r1:
        print("r1 element, a list: ", element)

    r0.sort(reverse=True)

    r0s = list()
    for word, length in r0:
        r0s.append(word)

    #print("r0s: ", r0s)
    print("Items in dict1: ", )
    #
    # use tuple to sort a dictionary by either key or value
    #

    d = {'a': 10, 'b': 1, 'c': 22}
    print(d)

    l_val = list()
    l_key = list()

    for key, val in d.items():
        l_key.append((key, val))
        l_val.append((val, key))

    l_val.sort(reverse=True)

    print("l_key: ", l_key)
    print("l_val: ", l_val)


if __name__ == "__main__":
    main()
