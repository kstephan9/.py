### logging: https://www.youtube.com/watch?v=ONCVvS-gDMA&feature=youtu.be

#logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)
#logging.disable(logging.INFO)

import os, sys
import logging, time, random

from datetime import datetime, timedelta
import dateutil.parser
import pandas as pd
import glob
from stat import *

from DefaultItems import ServiceNowDataFolder, LogFileFolder, ServiceNowDataOpenWorkFolder
from DefaultItems import getDuration
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

def atest():
    print("141: ", getDuration(then)) # E.g. Time between dates: 7 years, 208 days, 21 hours, 19 minutes and 15 seconds
    print("141 years: ", getDuration(then, now, 'years'))      # Prints duration in years
    print("141 days: ", getDuration(then, now, 'days'))       #                    days
    print("141 hours: ", getDuration(then, now, 'hours'))      #                    hours
    print("141 minutes: ", getDuration(then, now, 'minutes'))    #                    minutes
    print("141 seconds: ", getDuration(then, now, 'seconds'))    #                    seconds




def main():
    print("Line 56")
    wb = "Open Work_20200204.xlsx"
    pnf = os.path.join(ServiceNowDataOpenWorkFolder, wb)
    path=os.path.dirname(pnf)
#    print("pnf: ", pnf)
#    files_in_path = glob.glob(os.path.join(path, '*.xls*'))
    files_in_path = glob.glob(os.path.join(path, wb))
    #myprefix = ServiceNowDataFolder + '\\'

    #files_in_path.sort(reverse=False)

    all_data_df = pd.DataFrame()

    ar1 = wb.split("\\")
    ar2 = ar1[-1].split(".")
    ar3 = ar2[0].split("_")
    YYYYMMDD = ar3[1]
    ymdt = pd.to_datetime(YYYYMMDD)
    ymdt = pd.to_datetime("2/4/2020")
    #ymdt = datetime.now()
    _year = ymdt.year
    _mon = ymdt.month_name()
    _mon3 = ymdt.month_name()[0:3]
    _dow3 = ymdt.weekday_name[0:3]
#    _dow3 = ymdt.day_name
    _doy =  (ymdt - datetime(_year, 1, 1)).days + 1

    df_temp = pd.read_excel(pnf)
    df_temp['Opened'] = pd.to_datetime(df_temp['Opened'])
    diff = ymdt - df_temp['Opened']
    print("type(ymdt): ",type(ymdt))

    then = df_temp['Opened']
    now = datetime.now()

    print("type(then): ",type(then),"type(now): ",type(now))

    dhs =  getDuration(then, now, 'seconds')
    dbd = dhs/(3600*24)
    print("99 dhs: ", dhs, dbd)


    df_temp.insert(0, "fDate", YYYYMMDD, True)
    df_temp.insert(0, "diff", diff, True)

    frames = [all_data_df, df_temp]
    all_data_df = pd.concat(frames, axis=0)

    print(all_data_df)
    td = datetime.now() - df_temp['Opened']
    tdim = td / timedelta(minutes=1)
#    print("tdim: ", tdim)

    # Example usage
    then = datetime(2020, 2, 3, 0, 0, 0)

    now = datetime.now()

 #   dhm =  getDuration(then, now, 'minutes')+getDuration(then, now, 'hours')*60+getDuration(then, now, 'days')*24*60
    dhs =  getDuration(then, now, 'seconds')
    dbd = dhs/(3600*24)
    print("dhs: ", dhs, dbd)


#    timeDifference = datetime.now() - dateutil.parser.parse("2/3/2020")
#    time_difference_in_minutes = (int(timeDifference.days) * 24 * 60) + int((timeDifference.seconds) / 60)
#    print("tdim: ", time_difference_in_minutes)


if __name__ == "__main__":
    main()
