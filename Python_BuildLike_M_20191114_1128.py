import os
import xlwings as xw
import pandas as pd

from DefaultItems import DataFolder
from DefaultItems import Raw_2Folder

fNAP = os.path.join(Raw_2Folder,"NAPSData_roc.csv")
dfnap = pd.read_csv(fNAP)
dfnap.head()

dfnap.to_excel('dfnap.xlsx')
wbTest = xw.Book('dfnap.xlsx')




fM = os.path.join(Raw_2Folder,"tblE005RemedyBacklog_YYYYMMDD_M.xlsx")
pnf1 = os.path.join(DataFolder,fM)



df2_ColumnList1 = []
# df2_ColumnList1.append('Remedy Link')
df2_ColumnList1.append('VIP')
df2_ColumnList1.append('Priority')
# df2_ColumnList1.append('Calendar Days')
df2_ColumnList1.append('Incident Number')
df2_ColumnList1.append('Summary')
df2_ColumnList1.append('Incident Type Summary')
df2_ColumnList1.append('Submit Date')
# df2_ColumnList1.append('Target Date')
df2_ColumnList1.append('Status')
df2_ColumnList1.append('Status Reason')
# df2_ColumnList1.append('Last Resolved Date')
df2_ColumnList1.append('Site')
df2_ColumnList1.append('Location ID')
df2_ColumnList1.append('City')
df2_ColumnList1.append('State Province')
df2_ColumnList1.append('Zip Code')
df2_ColumnList1.append('Customer.Full Name')
df2_ColumnList1.append('Customer Login ID')
df2_ColumnList1.append('Assignee.Full Name')
df2_ColumnList1.append('Assignee Login ID')
df2_ColumnList1.append('Support Group Name')
df2_ColumnList1.append('Support Group Admin')
df2_ColumnList1.append('Backlog Range')
df2_ColumnList1.append('Calendar Days.1')
df2_ColumnList1.append('REQ #')
df2_ColumnList1.append('Incident Type')
df2_ColumnList1.append('Organization')
df2_ColumnList1.append('Department')
df2_ColumnList1.append('Product Categorization Summary')
df2_ColumnList1.append('Reported Source')
df2_ColumnList1.append('Vendor Ticket Number')
df2_ColumnList1.append('Support Organization')
df2_ColumnList1.append('Tier 1 Redirect')
df2_ColumnList1.append('Resolved First Call')
df2_ColumnList1.append('Calendar Hours')
df2_ColumnList1.append('Business Hours')
df2_ColumnList1.append('Product Name')
df2_ColumnList1.append('Operational Categorization Summary')
df2_ColumnList1.append('Phone Number Business')
df2_ColumnList1.append('Phone Number Mobile')
df2_ColumnList1.append('Assignee.Corporate ID')
df2_ColumnList1.append('Customer.Corporate ID')
df2_ColumnList1.append('CI')
df2_ColumnList1.append('No Comments for 3 days')
df2_ColumnList1.append('Not Commented for More Than 15 Days')
df2_ColumnList1.append('REQ #.1')
df2_ColumnList1.append('Notes')
df2_ColumnList1.append('AsOf')


df2 = pd.read_excel(pnf1, sheet_name="tblE005RemedyBacklog_YYYYMM_M"
    , usecols=df2_ColumnList1)

print(df2.columns)

#df2_ColumnList0 = df2.columns

#print(df2_ColumnList0)
df2.to_excel('output.xlsx')
wbTest = xw.Book('output.xlsx')

condition_nap = dfnap['ID'].isin(df2['Assignee.Corporate ID'])

filtered_by_nap2 = df2.loc[condition_nap]
filtered_by_nap2.to_excel('filtered_by_nap2_output.xlsx')
wbTest = xw.Book('filtered_by_nap2_output.xlsx')

notfiltered_by_nap2 = df2.loc[~condition_nap]
notfiltered_by_nap2.to_excel('notfiltered_by_nap2_output.xlsx')
wbTest = xw.Book('notfiltered_by_nap2_output.xlsx')

