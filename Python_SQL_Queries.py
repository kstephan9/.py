 





1 import pyodbc 
2 import os 
3 import pandas as pd 
4 
 
5 
 
6 # Set up Credentials 
7 user = os.environ['USER'] 
8 password = os.environ['PASS'] 
9 dsn = list(pyodbc.dataSources().keys())[0] # You can also enter the Data Source Name (DNS) manually  
10 
 
11 # Establish Connection 
12 cnxn = pyodbc.connect('DSN={};UID={};PWD={}'.format(dsn, user, password)) 
13 
 
14 # Execute query and save results into dataframe 
15 query = "SELECT * FROM ITEMS;" 
16 df = pd.read_sql(query, cnxn) 
