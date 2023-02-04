# https://www.youtube.com/watch?v=QAkOnV1-lIg#
#
#
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

import pandas as pd
import pandas_datareader.data as web

#import sklearn
#import beautifulsoup4
style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end   = dt.datetime(2019, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)

df.to_csv('tesla.csv')

df = pd.read_csv('tesla.csv', parse_dates = True, index_col=0)
#print(df.head())
#print(df.shape)
#print(df.describe)
#df.plot()
#plt.show()
#df['Adj Close'].plot()
#df[['Open', 'High']].plot()
#plt.show()

# Create a column
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True) # no need sunce we used min_periods=0
print(df.dtypes)

print(df.head())

df[['Adj Close',
 '100ma']].plot()
plt.show()

####################################

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
# use sharex = ax1 to allow ax2 and ax1 to stay together when magnified
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()


# https://www.youtube.com/watch?v=QAkOnV1-lIg
print("Done!")



