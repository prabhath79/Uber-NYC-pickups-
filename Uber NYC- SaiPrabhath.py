#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import os


# In[3]:


files=os.listdir(r'C:\Users\Sai Prabhath\Documents\uber-pickups-in-new-york-city')[-7:]


# In[4]:


files


# In[5]:


files.remove('uber-raw-data-janjune-15.csv')


# In[6]:


files


# In[7]:


path=r'C:\Users\Sai Prabhath\Documents\uber-pickups-in-new-york-city'

final= pd.DataFrame()

for file in files:

   df=pd.read_csv(path+"/"+file,encoding='utf-8')
   final=pd.concat([final,df])


# In[8]:


final.shape


# In[9]:


df=final.copy()


# In[10]:


df.head()


# In[11]:


df.dtypes


# In[12]:


df['Date/Time']=pd.to_datetime(df['Date/Time'],format = '%m/%d/%Y %H:%M:%S')


# In[13]:


df.head()


# In[14]:


df['WeekDay']=df['Date/Time'].dt.day_name()


# In[15]:


df['day']=df['Date/Time'].dt.day


# In[16]:


df['minute']=df['Date/Time'].dt.minute


# In[17]:


df['hour']=df['Date/Time'].dt.hour
df['month']=df['Date/Time'].dt.month


# In[18]:


df.head()


# In[19]:


df.dtypes


# In[20]:


import plotly.express as px


# In[21]:


px.bar(x=df['WeekDay'].value_counts().index,
      y=df['WeekDay'].value_counts()
      )


# In[22]:


df['WeekDay'].value_counts()


# In[ ]:





# In[23]:


plt.hist(df['hour'])


# In[24]:


df['month'].unique()


# In[25]:


plt.figure(figsize=(40,20))

for i,month in enumerate(df['month'].unique()):
    plt.subplot(3,2,i+1)
    
    df[df['month']==month]['hour'].hist()


# In[ ]:





# In[26]:


df.head()


# In[27]:


import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot


# In[28]:


df.groupby('month')['hour'].count()


# In[29]:


trace1=go.Bar(x=df.groupby('month')['hour'].count().index,
       y=df.groupby('month')['hour'].count(),
       name='Priority'
)


# In[30]:


iplot([trace1])


# In[31]:


sns.distplot(df['day'])


# In[32]:


plt.figure(figsize=(10,6))

plt.hist(df['day'],bins=30,rwidth=0.5,range=(0.5,30.5))
plt.xlabel('date of the month')
plt.ylabel('journey')
plt.title('journey by month day')


# In[33]:


plt.figure(figsize=(20,8))
for i,month in enumerate(df['month'].unique(),1):
    plt.subplot(3,2,i)
    df_out=df[df['month']==month]
    plt.hist(df_out['day'])
    plt.xlabel('days in month'.format(i))
    plt.ylabel('total rides')


# In[36]:



sns.pointplot(x="hour",y="Lat",data=df)


# In[55]:



sns.pointplot(x="hour",y="Lat",data=df,hue='WeekDay')
ax.set_title('hours of day vs Latitude of the passenger')


# In[38]:


df.head()


# In[47]:


df['Base'].head()


# In[45]:


df.groupby(['Base','month'])['Date/Time'].count()


# In[41]:


df.groupby(['Base','month'])['Date/Time'].count().reset_index()


# In[56]:


plt.figure(figsize=(10,6))
sns.lineplot(x='month',y='Date/Time',hue='Base',data=base)


# In[ ]:




