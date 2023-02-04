import os
import sqlite3
import xlwings as xw
import pandas as pd

from DefaultItems import DataFolder
from DefaultItems import Raw_2Folder

fNAP = os.path.join(Raw_2Folder,"NAPSData_roc.csv")
dfnap = pd.read_csv(fNAP)
print(dfnap.head())
