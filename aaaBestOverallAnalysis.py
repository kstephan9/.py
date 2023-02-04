
# coding: utf-8


import os
from DefaultItems import Python_Base_Class, Python_Folder, Python_Data_Folder, Raw_2Folder, dbz

import pandas as pd

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 10000)

from matplotlib import pyplot as plt

#get_ipython().run_line_magic('matplotlib', 'inline')
print("ken xxx")

filename1 = "Uber.csv"
csv1 = os.path.join(Python_Data_Folder,filename1)

ri = pd.read_csv(csv1)
print("yy")
filename2 = "PyCon_2018_01of10_ted.csv"
csv2 = os.path.join(Python_Data_Folder,filename2)

ted = pd.read_csv(csv2)
print( ted.head(2))
ri.duration.plot()



ri.shape



ri['Date/Time'] = ri['Date/Time'].map(pd.to_datetime)



def get_dom(dt):
    return dt.day

ri['dom'] = ri['Date/Time'].map(get_dom)
ri.dtypes



def get_year(dt):
    return dt.year

ri['year'] = ri['Date/Time'].map(get_year)
ri.dtypes



def get_hour(dt):
    return dt.hour

ri['hour'] = ri['Date/Time'].map(get_hour)
ri.dtypes



def get_year(dt):
    return dt.year

ri['year'] = ri['Date/Time'].map(get_year)
ri.dtypes


def get_weekday(dt):
    return dt.weekday

ri['weekday'] = ri['Date/Time'].map(get_weekday)
ri.dtypes


from matplotlib import pyplot as plt

plt.hist(ri.dom, bins = 30, rwidth = 0.8, range=(0.5, 30.5))
plt.xlabel('date of month')
plt.ylabel('frequency')
plt.title('Frequency by DoM')
plt.legend()



#for k, years in ri.groupby('year'):
#    print((k, len(years)))

def count_rows(rows):
    return len(rows)

by_date = ri.groupby('dom').apply(count_rows)
by_date
plt.plot(by_date)



for k, rows in ri.groupby('dom'):
    print((k, len(rows)))


plt.bar(range(1,31), by_date)



by_date_sorted = by_date.sort_values()



plt.bar(range(1,31), by_date_sorted)
plt.xticks(range(1,31), by_date_sorted.index)
plt.xlabel('date of month')
plt.ylabel('frequency')
plt.title('Frequency by DoM')
#plt.xticks(dom, [str(i) for i in y], rotation=90)
plt.tight_layout()
plt.legend()
("")


# ## analysis by hour


plt.hist(ri.hour, bins=24, range=(0.5, 24))


# ## by weekday


#plt.hist(ri.weekday, bins=7, range=(-0.5, 6.5), rwidth=0.8)


# # cross analysis (hour, dow)


by_cross = ri.groupby('hour dom'.split()).apply(count_rows).unstack()



import seaborn
seaborn.heatmap(by_cross)


# # by lat and nong


plt.hist(ri['Lat'], bins=100, range=[40.5, 41])



plt.hist(ri['Lon'], bins=100, range=[-74.5, -73.5], color='g', alpha=0.5, label='longitude')
plt.grid()
plt.twiny()
plt.hist(ri['Lat'], bins=100, range=[40.5, 41], color='r', alpha=0.5, label='latitude')
plt.twiny()
plt.grid()
plt.ylim(20000,21000)
plt.legend(loc='best')

