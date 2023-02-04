
import os
import pandas as pd
import xlrd
from DefaultItems import Raw_2Folder

#help(os.path.join)
fh = os.path.join(Raw_2Folder, "tblE005RemedyBacklog_YYYYMMDD_M.xlsx")

print("fh: ", fh)


df = pd.read_excel(fh, sheet_name='tblE005RemedyBacklog_YYYYMM_M')
#print(df.columns)
#print(df.dtypes)
print(df['Assignee.Corporate ID'])

