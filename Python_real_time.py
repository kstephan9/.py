
# coding: utf-8

# In[ ]:


#https://gist.github.com/nikhilkumarsingh/1dcec96a1eb0aeb8975fc13ec5825d43


import time
import psutil
import matplotlib.pyplot as plt


# In[ ]:


#get_ipython().run_line_magic('matplotlib', 'notebook')
#plt.rcParams['animation.html'] = 'jshtml'


# In[ ]:


fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()


# In[ ]:


i = 0
x, y = [], []

while True:
    x.append(i)
    y.append(psutil.cpu_percent())

    ax.plot(x, y, color='b')

    fig.canvas.draw()

    ax.set_xlim(left=max(0, i-50), right=i+50)

    time.sleep(0.1)
    i += 1


# In[ ]:


plt.close()

