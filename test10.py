import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1)
y = np.sin(x)
plt.plot(x,y)
title = "Plot"
filename = "plot.png"
plt.title(title)
plt.savefig(filename)
plt.show(a)
