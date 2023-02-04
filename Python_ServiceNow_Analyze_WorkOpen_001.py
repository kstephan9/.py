import os, sys
import datetime
import pandas as pd
import glob
from stat import *
from DefaultItems import ServiceNowDataFolder

filename = "Open Work_20191216.xlsx"

# https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=27s

#filename = "test.txt"
pnf = os.path.join(ServiceNowDataFolder, filename)

#f.readline() reads only the NEXT line!!

with open(pnf, 'r') as f: # a context manager
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end="")
        f_contents = f.read(size_to_read)
        #print(f.tell())



#df = pd.read_excel(pnf)
#print(df.head())


