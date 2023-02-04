import os
import datetime
import pandas as pd
import xlrd

df_x = pd.read_excel('test.xlsx','Sheet2')
print("line 7: ", df_x.columns)

#df_sheet2 = pd.DataFrame()
df_sheet2 = pd.concat([df_x['userfolder'], df_x['Datetime Recorded in Database']], axis = 1)
print("line 11: ", df_sheet2.head())
print("Line 13: ", df_sheet2.head())

df_sheet2['mdt'] = pd.to_datetime(df_sheet2['Datetime Recorded in Database'])
#print("13 Type: ", type(df_sheet2['mdt']))
print("\n")
print("line 17: ", df_sheet2.columns)
del df_sheet2['Datetime Recorded in Database']
print("line 19: ", df_sheet2.dtypes)
print("line 18: ", df_sheet2.head())

print("line 21: ", df_sheet2['mdt'].dt.day)
#print("line 19: ", type(df_sheet2['mdt'].dt.day))
#print("line 20: ",df_sheet2.dtypes)
#print("Month: ", df_sheet2['MyDateTime'].pd.to_datetime.dt.month)

#print(df_sheet2.columns)
#print(df_sheet2.head())

#ufo = pd.read_csv('http://bit.ly/uforeports')

#print(ufo.head())
#print("ufo\n")





