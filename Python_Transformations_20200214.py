
## https://www.youtube.com/watch?v=p42e8NBnrGI&t=517s

import os
import pandas as pd

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 10000)

import seaborn as sns

from DefaultItems import DataFolder, LogFileFolder

# Create and configure logger
import logging

log_file_name = "log_file.log"
lfp = os.path.join(LogFileFolder, log_file_name)

LOG_FORMAT = "%(asctime)s - %(message)s - %(Levelname)s"
logging.basicConfig(filename = lfp, level = logging.DEBUG)
logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")

print("Logger level: ", logger.level)


filename = "ExcelVsPandas_data.xls"

pnf = os.path.join(DataFolder,filename)
#print(pnf)

df=pd.read_excel(pnf)

df['price']=df['price'].astype('int64')

df['price_sqft']=df['price']/df['sqft_lot']
df=df.sort_values(by=['price_sqft'], ascending=False)

# Find the count of sales and mean price in each city by bedroom

dfpiv=pd.pivot_table(df,index=['city'], values=['price', 'price'], columns=['bedrooms'], aggfunc=['count','mean'], fill_value=0)
dfpiv.head()
#print(df.head())
#print(dfpiv.head())

dfpiv.to_excel('dfpiv.xlsx')

# Let's append the average 5 year appreciation rate by city using a vlookup in excel and similar in pandas

df_appre=pd.read_excel(pnf, sheet_name='city_AA')
df_results=df.merge(df_appre, on='city')
#print('\nline 53: results: \n', df_results.head())

#print('\nline 55: \n', df_results.loc[df_results['city']=='Medina'].head())

filter1 = (df_results['city'] == 'Medina') | (df_results['city'] == 'Kent')

r2 = df_results.loc[filter1]

#r2 = results.loc[results['city']=='Medina']

#r2 = results.loc[results['city']=='Medina']

r2.to_excel('r2.xlsx')

graph = sns.barplot(x='bedrooms', y='price_sqft', data=r2, palette='Blues_d', errwidth=0)
#print(graph.show())

#print(df.describe())
