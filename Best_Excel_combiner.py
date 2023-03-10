#### https://www.youtube.com/watch?v=eWRtrPeJoyA
#### Automate Excel using Python | Excel Hacks with Pandas

####
#### Uses python\data\SuperStore\superstore_dataset2011-2015.csv
####
import glob
import os
import pandas as pd

file=input('File Path: ')
pth=os.path.dirname(file)
extension = os.path.splitext(file)[1]
files = glob.glob(os.path.join(pth, '*.xls*'))
newfile=os.path.join(pth,'combined.xlsx')
df = pd.DataFrame()
for f in files:
    data = pd.read_excel(f)
    df = df.append(data)

df.to_excel(newfile, sheet_name='combined', index=False)
print('Completed')
