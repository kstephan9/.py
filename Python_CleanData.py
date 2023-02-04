 





1 import pandas as pd 
2 
 
3 
 
4 # Read CSV files 
5 file_name = 'file.csv' 
6 df = pd.read_csv(file, low_memory=True) 
7 
 
8 # Filter column 
9 df = df.loc[df['Source Site'] == 'Amazon', :] 
10 
 
11 # Remove rows where all values are missing 
12 df.dropna(inplace = True, how='all') 
13 
 
14 # Remove rows where specific columns are missing values 
15 df.dropna(inplace= True, subset=['Source Site', 'Date'], how='any') 
16 
 
17 # Save Results 
18 df.to_csv(file_name, sep=',', encoding='utf-8', index=False) 
