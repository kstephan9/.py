import os, sys
import re
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import glob
from stat import *
from DefaultItems import DataFolder

filename = "test1.xlsx"

# https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=27s

pnf = os.path.join(DataFolder, filename)

#f.readline() reads only the NEXT line!!


df = pd.read_excel(pnf, parse_dates=True)
i=0
for x, v1 in enumerate(df['Date']):
    i+=1
    y, m, d = v1.split('-')
    #print(i, y, m, d)
    d = datetime.date(int(y), int(m), int(d))
    print(i, x, d.strftime("%A"))
#print(type(d))
#print(d)

#d = "20190413"
#m = re.search(r'({0-9]{4})({0-9]{2})({0-9]{2})', d)
#if m:
#    _len, _pre = map(int, m.groups())
#    print(_len, _pre)
#else:
#    print("29")

'''
index_date = df.columns.get_loc('Date')
#print("type: ", type(index_date))
pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='ignore')
#df['Date'] = df['Date'].dt.date.apply(lambda x: x.year, x.month, x.day)

print(df.dtypes)
print(df.head())
date_pattern = r'({0-9]{4}-{0-9]{2}-{0-9]{2})'
#print(type(df['Date']))

import re
for row in range(1, len(df)):
    date = re.search(date_pattern, df.iat(row, index_date))

#df.plot()
#plt.show()



#print(df.head())

'''
