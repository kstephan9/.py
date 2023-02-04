### logging: https://www.youtube.com/watch?v=ONCVvS-gDMA&feature=youtu.be

#logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)
#logging.disable(logging.INFO)

import os, sys
import logging, time, random

from datetime import datetime
import pandas as pd
import glob
from stat import *

from DefaultItems import ServiceNowDataFolder, LogFileFolder

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




wb = "Open Work_20191216.xlsx"
# https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=27s

#logging.debug(type(wb))
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')

pnf = os.path.join(ServiceNowDataFolder, wb)
path=os.path.dirname(pnf)

files_in_path = glob.glob(os.path.join(path, '*.xls*'))
myprefix = ServiceNowDataFolder + '\\'
files_in_path = [myprefix + 'asmt_assessment_instance_cancelled_20200120.xlsx',
 myprefix + 'asmt_assessment_instance_readytotake_20200120.xlsx',
 myprefix + 'asmt_assessment_instance_complete_20200120.xlsx']



print(files_in_path)
files_in_path.sort(reverse=False)

####
#### Combine multiple spreadsheets
####


all_data_df = pd.DataFrame()

for afile in files_in_path:
    '''
    ar1 = afile.split("\\")
    ar2 = ar1[-1].split(".")
    ar3 = ar2[0].split("_")
    YYYYMMDD = ar3[1]
    #ymdt = datetime.strptime(str(YYYYMMDD), '%Y%m%d').strftime('%Y-%m-%d')
    ymdt = pd.to_datetime(YYYYMMDD)
    _year = ymdt.year
    _mon = ymdt.month_name()
    _mon3 = ymdt.month_name()[0:3]
    _dow3 = ymdt.weekday_name[0:3]
#    _dow3 = ymdt.day_name
    _doy =  (ymdt - datetime(_year, 1, 1)).days + 1
    #print(YYYYMMDD, _year, _mon, _mon3, _dow3, _doy)
#    print("afile: ", ar1[-1], "ar2[0]: <", ar2[0], ">", YYYYMMDD)
'''
    df_temp = pd.read_excel(afile)
#    df_temp.insert(0, "fDate", YYYYMMDD, True)
    frames = [all_data_df, df_temp]
#    frames = [all_data_df]
    all_data_df = pd.concat(frames, axis=0)
   #print(all_data_df.tail(3))
else:
    pass

#   fDate   Number  Task type   Priority    Contact type    Opened  Opened by   Updated Updated by  Affected User [Incident]    Sector [Incident]   Requested for [Request] Sector  Short description   Description Additional comments Item [Requested Item]   State   Parent  Assignment group    Assigned to Tier 1 resolvable? [Incident]   Work notes

#prod_df = all_data_df.groupby(['fDate', 'Task type']).count()
#print(prod_df.head())

#prod_df.to_excel("aaa.xlsx")
all_data_df.to_excel("aaa.xlsx")
#newfile=os.path.join(path, filename+'_2'+extension)
'''
mydict = {'abc': 1}
for index, row in prod_df.head().iterrows():
    print("117: ", index, row['Opened'])
    x = row['Opened']
    print("x:", x)
    mydict[x] += 1
'''
