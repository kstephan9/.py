
# coding: utf-8

# ## Title, description

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'inline')

#%load_ext autoreload
#%reload_ext autoreload 2
#%load_ext version_information
#%version_imformation numpy, scipy, matplotlib, pandas
import os
import pandas as pd
import xlrd
import calendar
calendar.setfirstweekday(calendar.SATURDAY)

from matplotlib import pyplot as plt
from DefaultItems import Raw_2_FileLocation
#Raw_2_FileLocation = r'Y:\BAE Reporting\Morning Reports\Raw_2'
filename = 'tblE005RemedyBacklog_YYYYMMDD_M.xlsx'
TabName = 'tblE005RemedyBacklog_YYYYMM_M'
file_path = os.path.join(Raw_2_FileLocation,filename)
#backlog = pd.read_excel(file_path, 'tblE005RemedyBacklog_YYYYMM_M', index_col = 'Incident Number')
backlog = pd.read_excel(file_path, 'tblE005RemedyBacklog_YYYYMM_M', index_col = 4)
#backlog = pd.read_excel(file_path, 'tblE005RemedyBacklog_YYYYMM_M')


# # Convert 'Last Resolved Date' to type datetime

# In[2]:


### No Need For This - backlog['Submit Date'] = pd.to_datetime(backlog['Submit Date'], errors='coerce')


# In[3]:


#backlog.dtypes


# In[4]:


backlog.index.values


# In[5]:


backlog.shape


# In[6]:


def get_dom_sub(dt):
    return dt.day

backlog['dom'] = backlog['Submit Date'].map(get_dom_sub)


# In[7]:


def get_month_sub(dt):
    return dt.month

backlog['month'] = backlog['Submit Date'].map(get_month_sub)


# In[8]:


def get_dayofweek_sub(dt):
    return dt.dayofweek

backlog['dayofweek'] = backlog['Submit Date'].map(get_dayofweek_sub)


# In[9]:


backlog['sgn'] = backlog['Support Group Name'];


# In[10]:


backlog['caldays'] = backlog['Calendar Days']
backlog['so'] = backlog['Support Organization']
backlog['sga'] = backlog['Support Group Admin']
backlog['YYYYMMDD'] = backlog['Submit Date'].dt.strftime('%Y-%m-%d').astype('str')
backlog['YYYYMM'] = backlog['Submit Date'].dt.strftime('%Y-%m').astype('str')


# In[11]:


backlog['10ma'] = backlog['caldays'].rolling(window=10, min_periods=0).mean()


# In[12]:


bl = backlog[['10ma','YYYYMMDD', 'YYYYMM','VIP', 'Priority', 'caldays', 'so', 'sga', 'Incident Type Summary','Status','month','dayofweek','dom']]


# In[13]:


print(bl)


# In[ ]:


#print(bl.dtypes)


# In[14]:


print(bl.index.values)


# In[15]:


#print(bl.dtypes)


# In[16]:


plt.rcParams['figure.figsize'] = [16, 9]
plt.plot_date(bl['YYYYMM'], bl['caldays'], linestyle='solid')
plt.gcf().autofmt_xdate()
#plt.xlim(1, 1)
plt.tight_layout()
plt.xlabel('Submit Date')
plt.ylabel('Calendar Days')
plt.legend()
plt.figure(figsize=(120,110))
plt.show()


# In[17]:


def count_rows(rows):
    return len(rows)

#by_date = bl1.groupby('dom').apply(count_rows)
by_YYYYMM = bl.groupby('YYYYMM').apply(count_rows)


# In[18]:


by_cross = bl.groupby('caldays dom'.split()).apply(count_rows).unstack()


# In[19]:


import seaborn
seaborn.heatmap(by_cross);
plt.gca().invert_yaxis()
plt.title('My Title')
plt.grid()


# In[ ]:


by_cross_sga = bl.groupby('caldays sga'.split()).apply(count_rows).unstack()


# In[ ]:


by_cross_sga


# In[ ]:


seaborn.heatmap(by_cross_sga);
plt.gca().invert_yaxis()
plt.title('My Title')
plt.grid()


# In[ ]:


by_cross_so = bl.groupby('so caldays'.split()).apply(count_rows).unstack()


# In[ ]:


by_cross_so


# In[ ]:


seaborn.heatmap(by_cross_so);
#plt.gca().invert_yaxis()
plt.title('My Title')
plt.figure(figsize=(120,110))
plt.grid()


# In[ ]:


by_cross_sga = bl.groupby('sga caldays'.split()).apply(count_rows).unstack()


# In[ ]:


by_cross_sga


# In[ ]:


seaborn.heatmap(by_cross_sga, annot=True);
#plt.gca().invert_yaxis()
plt.title('My Title')
plt.grid()


# In[ ]:


bl.index.values


# In[22]:





# In[ ]:


ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
#bl.index.values

#ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1)

ax1.plot(bl['Incident Number'], bl['10ma'] )
#ax1.plot(bl.index, bl['caldays'] )
#ax2.bar(bl.index, bl['10ma'] )
plt.show()

