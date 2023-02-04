###
import datetime
from datetime import datetime
from datetime import date

import pandas as pd
import numpy as np

now_is = datetime.now()
print(now_is)


df = pd.Series()

print(df)

print(df.describe)

print(type(df))


np.random.seed(0)
rng = pd.date_range('2019-01-15', periods=5, freq='M')
df = pd.DataFrame( rng, columns=['value'])

df['mydiff'] = now_is - df['value']
print(df.describe)
print ("line 28: ", df['mydiff'].dtype)
print("29", df['mydiff'].dt.days, "hours:", df['mydiff'].dt.components.hours)
df['xxx'] = df['mydiff'].dt.days+ df['mydiff'].dt.components.hours/24.0
#print("30", df['mydiff'], df['mydiff'].dt.days, "hours:", df['mydiff'].dt.components.hours)
print (df)


print("Finished!")



