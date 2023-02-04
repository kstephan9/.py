'''
doc string
'''

import os
import pandas as pd
import xlrd
from DefaultItems import Raw_2Folder

#help(os.path.join)
fh = os.path.join(Raw_2Folder, "ForDan_20190429.xlsm")
print(fh)

#workbook = xlrd.open_workbook(fh)
with xlrd.open_workbook(fh) as mywb:
    mysheets = mywb.sheet_names()
    print("Line 17: ", mysheets[0])
    #sheet_ListOfTables = mysheets[0]
    #print("Line 19: Sheet name: %s" % sheet_ListOfTables)
    sheet_Sheet1 = mywb.sheet_by_name('Sheet1')

    # pull the first row by index
    row = sheet_Sheet1.row(0)

    # print 1st row values and types
    from xlrd.sheet import ctype_text

    print("[Sheet Name] (Column #) type:value")
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        print('[%s] (%s) %s %s' % (sheet_Sheet1.name,idx, cell_type_str, cell_obj.value))

print("Line 25: ", sheet_Sheet1.cell_value(0,1))
#df1.head()

