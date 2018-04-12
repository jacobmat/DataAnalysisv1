
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
df=pd.read_csv("D:\Personal\BA\sample files\diabetes.csv")
#
df.shape
# have 768 row with 9 column


# In[30]:


df.dtypes 
# All data types are numbers


# In[28]:


df.head()


# In[8]:


df.tail()


# In[3]:


df.describe()
# Appox 35% of patients are diabetes


# In[19]:


#normalize our data in order to visualize it better
df1= (df - df.mean()) / (df.max() - df.min())
df1.describe()


# In[26]:


df1.plot.box()
#


# In[17]:


df.hist(figsize=(12,8),bins=20)


# In[9]:


co = df.corr()
sns.heatmap(co, annot=True)


# In[10]:


sns.pairplot(df)

