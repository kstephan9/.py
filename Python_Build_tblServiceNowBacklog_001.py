
#logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)
#logging.disable(logging.INFO)

import os, sys
import logging, time, random

from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np
from itertools import groupby
import random
import string
import glob
from stat import *

from DefaultItems import LogFileFolder, OutputFolder, DataFolder, Raw_2Folder

now_is = datetime.now()
print(now_is)
print("ts: ", now_is.second)
ts = now_is.second

print("wd is: ", os.getcwd())

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 10000)

####
#### Create and configure logger
####

filename = "log_file.log"
lfp = os.path.join(LogFileFolder,filename)

LOG_FORMAT = "%(asctime)s - %(message)s - %(Levelname)s"
logging.basicConfig(filename = lfp, level = logging.DEBUG)
logger = logging.getLogger()

logging.debug(random.choice(['hello', 'hi']))
logging.debug(random.choice(['hello', 'hi']))
logging.debug(random.choice(['hello', 'hi']))
# Test the logger
#logger.info("Our first message.")

print("Logger level: ", logger.level)
def side_by_side(*objs, **kwds):
    from pandas.io.formats.printing   import adjoin
    space = kwds.get('space', 4)
    reprs = [repr(obj).split('\n') for obj in objs]
    print(adjoin(space, *reprs))

def crashreport(f):
    @functools.wraps(f)
    def _crashreport(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            crashlogger.exception(
                '{} crashed\n'.format(f,__name__)
            )
            raise
    return _crashreport


### making data frame from csv file
##data = pd.read_csv("nba.csv", index_col ="Name")
RawColumns = ['Number'
, 'Task type'
, 'Priority'
, 'Contact type'
, 'Opened'
, 'Opened by'
, 'Updated'
, 'Updated by'
, 'Affected User [Incident]'
, 'Sector [Incident]'
, 'Requested for [Request]'
, 'Sector'
, 'Short description'
, 'Description'
, 'Additional comments'
, 'Item [Requested Item]'
, 'State'
, 'Support Organization'
, 'Parent'
, 'Assignment group'
, 'Assigned to'
, 'Tier 1 resolvable? [Incident]'
, 'Work notes'
, 'Email'
, 'Employee number'
]

Columns = ['Number'
, 'Task type'
, 'Priority'
, 'Cdays_Assignee_AssigneeSupervisor'
, 'Cdays_Supervisor_Of_Assignee'
, 'Contact type'
, 'Opened'
, 'Opened by'
, 'Updated'
, 'Updated by'
, 'Affected User [Incident]'
, 'Sector [Incident]'
, 'Requested for [Request]'
, 'Sector'
, 'Short description'
, 'Description'
, 'Additional comments'
, 'Item [Requested Item]'
, 'State'
, 'Support Organization'
, 'Parent'
, 'Assignment group'
, 'Assigned to'
, 'Tier 1 resolvable? [Incident]'
, 'Work notes'
, 'Email'
, 'Employee number'
, 'Supervisor Of Assignee'
, 'Days'
]

tempColumns = ['Number'
, 'State'
, 'Opened'
, 'Assigned to'
, 'Email'
, 'Employee number'
]
wb = "Open Work_20191216.xlsx"
# https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=27s

#logging.debug(type(wb))
#logging.debug('debug message')
#logging.info('info message')
#logging.warn('warn message')
#logging.error('error message')
#logging.critical('critical message')

pnf = os.path.join(DataFolder, 'ServiceNowData', 'OpenWork', wb)
path=os.path.dirname(pnf)

#print("path: ", path)

files_in_path = glob.glob(os.path.join(path, '*.xls*'))

files_in_path = 'S:\\BAEIT\\ITIL\\PerformanceManagementTeam\\AssortedTasks\\Learning\\Python\\data\\ServiceNowData\\OpenWork\\Open Work_20200219A.xlsx'

print(files_in_path)

df = pd.read_excel(files_in_path,usecols=tempColumns)
print("df.head(): ", df.head())

pnf = os.path.join(Raw_2Folder,'tblPeopleSoftEmployeeSupervisorData_v05.xlsm')
#, 'Emp_Sup' 'Merge on EMPLID_NLZ'

df_Emp_Sup = pd.read_excel(pnf, sheet_name='Emp_Sup')

# https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html
df_merge_left = pd.merge(left=df, right=df_Emp_Sup, how='left', left_on='Employee number', right_on='EMPLID_NLZ' )

df_merge_left['now_is'] = now_is

df_merge_left.insert(2, 'Age_In_Days', now_is - df_merge_left['Opened'])


#print("line 172: ", df_merge_left['Age_In_Days'])

df_merge_left.insert(3, 'Computed Age', df_merge_left['Age_In_Days'].dt.days+ df_merge_left['Age_In_Days'].dt.components.hours/24.0)



#print("line 178: ", df_merge_left['Computed Age'].dtype)

#df_merge_left['yyy'] = np.round(df_merge_left['xxx'], decimals=0)*1000/1000

df_merge_left.insert(4, 'Rounded/Padded Age', np.round(df_merge_left['Computed Age'], decimals=0)*1000/1000)

#print("Line 184")

#zzzzzzzzzzzzz
#df_merge_left['Age_In_Days_ken']= df_merge_left['Age_In_Days'].astype(str)

#df_merge_left['ken'] = df_merge_left[['Age_In_Days_ken', 'Assigned to', 'Assigned to']].agg('_'.join, axis=1)

#print(type(df_merge_left['Age_In_Days_ken']))
#print(df_PeopleSoft.describe)

print("line 194: ", df_merge_left['Computed Age'].dtype)
print("line 195: ", df_merge_left['Rounded/Padded Age'].dtype)
print("line 196: ", df_merge_left['Age_In_Days'].dtype)

# df['strange'] = df['strange'].astype(str)

tempfn = os.path.join(OutputFolder,'temp' + str(ts) + '.xlsx')
df_merge_left.to_excel(tempfn)
print("Finished!")
