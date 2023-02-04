
import os, sys
import logging, time, random
import string, random
from datetime import datetime
import pandas as pd
from itertools import groupby
import glob
from stat import *

from DefaultItems import ServiceNowDataOpenWorkFolder, LogFileFolder, OutputFolder


x = random.choices(string.ascii_lowercase, k = 20)
x = sorted(x)
groupby(x)

for key, group in (groupby(x)):
    print('key: ', key, ' group: ', list(group))

data = [
        ('111', 'KAT'),
        ('112', 'NOT'),
        ('113', 'NOT'),
        ('114', 'NOT')

]
data = sorted(data, key = lambda x: x[1])

print("data: ", data)
for key, group in (groupby(data, key = lambda x: x[1])):
    print('key: ', key, ' group: ', list(group))

def check_even(n):
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'

def grouper(iterable):
    iterable = sorted(iterable, key = check_even)
    print(iterable)
    grouped = groupby(iterable, check_even)
    for key, group in grouped:
        print("key", key, "group", list(group))

x = random.sample(list(range(1,50)), 30)

grouper(x)

