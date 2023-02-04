import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DefaultItems import OutputFolder


import matplotlib
#%matplotlib inline

matplotlib.style.use('ggplot')
ts = pd.Series(np.random.randn(10000), index=pd.date_range('1/1/2000', periods=10000))
ts = ts.cumsum()
plt.figure()
ts.plot()

path_and_file = os.path.join(OutputFolder,"foo.png")

plt.savefig(path_and_file, bbox_inches='tight')

plt.show()
