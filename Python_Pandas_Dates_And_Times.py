# https://anaconda.org/conda-forge/vega_datasets


import datetime
import pandas as pd

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 10000)

import numpy as np
from vega_datasets import data as vds

date_range = pd.date_range(start='1-1-16', end='1-11-16')
print(date_range)

df_a = pd.DataFrame(np.random.rand(16).reshape(4,4), index=['r1', 'r2', 'r3', 'r4']
    , columns=['c1','c2','c3','c4'])
print(df_a)
print(df_a < 0.5)
missing_obj = np.nan
series_obj = pd.Series([missing_obj, 2, 3, missing_obj, 5, 6, missing_obj, 8])
#print('line 18: ',series_obj.isnull())
filled_obj = series_obj.fillna(0)
#print('line 20: ', filled_obj)
df_filled = pd.DataFrame(series_obj)
#print('line 22: ',df_filled.reshape(2,4))


df = pd.DataFrame({'col 1': ['one', 'one', 'one', 'two', 'two',
                            'two','three'],
                    'col 2': ['A', 'B', 'C', 'A', 'B', 'C', 'D'],
                    'col 3': [1, 2, 3, 4, 5, 6, 7],
                   'col 4': ['x', 'y', 'z', 'q', 'w', 't', 'u']})
#df

print('line 32: \n',df)
#print('line 33: \n', df.iloc[[1,2], [2,3]])
print('\nline 34: \n', df.pivot(index='col 1', columns = 'col 2', values='col 3'))
print('\nline 35: \n', df.pivot(index='col 1', columns = 'col 2', values='col 4'))
