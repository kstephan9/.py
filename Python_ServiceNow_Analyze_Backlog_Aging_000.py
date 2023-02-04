#### https://www.youtube.com/watch?v=eWRtrPeJoyA
#### Automate Excel using Python | Excel Hacks with Pandas

####
#### Uses python\data\SuperStore\superstore_dataset2011-2015.csv
####

import os, sys
import numpy as np
import logging, time, random

from datetime import datetime
import pandas as pd
import glob
from stat import *


import pandas as pd
import os
from openpyxl import load_workbook
import xlsxwriter
from shutil import copyfile

# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 25)

number = 9999/89
print(f'yes: {number:.02f}')

#file=input('File Path: ')
file = 'Y:\BAE Reporting\ForBobNorstern_2020\All_test.xlsx'
print(file)
extension = os.path.splitext(file)[1]
filename = os.path.splitext(file)[0]
pth=os.path.dirname(file)
newfile=os.path.join(pth,filename+'_2'+extension)

df=pd.read_excel(file, sheet_name='data')
#colpick=input('Select Column: ')
#cols=list(set(df[colpick].values))
#delta = pd.datetime.now() - df['Opened']


nnow = pd.datetime.now()
# http://www.datasciencemadesimple.com/difference-two-dates-days-weeks-months-years-pandas-python-2/
df['delta_days'] = nnow - df['Opened']
#pd.options.display.float_format = '{:,.1f}'.format

df['delta_days'] = df['delta_days']/np.timedelta64(1,'D')
#print(df['diff_days'], type(df['diff_days']))

#prod_df = df.groupby(['Parent', 'Task type']).count()
prod_df = df.groupby(['Parent', 'Task type']).mean()


print(df.columns)

#print(prod_df)


df.groupby(
    ['Opened', 'Assignment group']
).agg(
    {
        # Find the min, max, and sum of the duration column
        'delta_days': [min, max, sum],
        # find the number of network type entries
        'Assignment group': "count",
        # minimum, first, and number of unique dates
        #'date': [min, 'first', 'nunique']
    }
)

print(df)


df.to_excel("aaa.xlsx")
prod_df.to_excel("aaa2.xlsx")


print("Finished!")

#df=pd.read_excel(file, sheet_name='data)
#colpick=input('Select Column: ')
#cols=list(set(df[colpick].values))
