#!/usr/bin/env python
# coding: utf-8

# # Case Study 2

# In[100]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings 
warnings.filterwarnings('ignore')


# In[126]:


## Load practice.csv file as a data-frame and perform following operations on the data-frame
df = pd.read_csv("practice.csv")
df.head()


# In[32]:


## Display all columns
df.columns


# In[33]:


## create numerical and categorical columns list\
num = df.select_dtypes('number').head()
col = df.select_dtypes('object').head()
print(num)
print(col)


# In[34]:


## display size of the data-frame
df.shape


# In[36]:


## rename column MSSubClass -> SubClass, MSZoning -> Zones
df = df.rename(columns = {'MSSubClass':'SubClass', 'MSZoning':'Zones'})
df.head()


# In[39]:


## display distinct values for Zoning, LotShape, LotConfig
zone = df['Zones'].unique()
lot_shape = df['LotShape'].unique()
lot_config = df['LotConfig'].unique()
print(zone)
print(lot_shape)
print(lot_config)


# In[43]:


## display count of distinct values for Zoning, LotShape, LotConfig
zone = df['Zones'].nunique()
lot_shape = df['LotShape'].nunique()
lot_config = df['LotConfig'].nunique()
print('Zones: {}'.format(zone))
print('LotShape: {}'.format(lot_shape))
print('LotConfig: {}'.format(lot_config))


# In[46]:


## max, min of column YearBuilt
maximum = df.YearBuilt.max()
maximum = df.YearBuilt.min()
print('maximum: {}, minimum: {}'.format(maximum,maximum))


# In[50]:


df.head()


# In[76]:


## create a new column “year_diff’. This will be holding difference of current year and YearBuilt
df['year_diff']=df.apply(lambda x: 2021 - x['YearBuilt'],axis=1)
df.head()


# In[32]:


## display distinct MSZoning for each OverallQual
df[['MSZoning','OverallQual']].head(10)


# In[98]:


## What is the maximum LotArea where  BsmtExposure = Mn?
df[df.BsmtExposure == 'Mn']['LotArea'].max()


# In[114]:


## Sort dataframe based on following columns and orders: MSSubClass; ascending, YearBuilt; descending
print(df.MSSubClass.sort_values(ascending=True).head())
print(df.YearBuilt.sort_values(ascending=False).head())


# In[113]:


## What is average OverallQual.
df.OverallQual.mean()


# In[130]:


## convert column ‘YearBuilt’ into date type.
df['YearBuilt']= pd.to_datetime(df['YearBuilt'])
df.info()


# In[133]:


## Group by YearBuilt and find maximum OverallQual
df.groupby('YearBuilt')['OverallQual'].max()


# In[164]:


## Load the practice.csv again with MSSubClass as new index
df1 = pd.read_csv("practice.csv")
df1.set_index('MSSubClass')


# In[165]:


## Convert LotArea as numpy array
s_array = df1['LotArea'].to_numpy()
s_array


# In[167]:


## In column MasVnrArea replace 0 with -1\
df1.replace(to_replace =0,
                 value =-1)


# In[169]:


## Check if there is/are any Null values (NaN) in the data given
df1.isnull().sum()


# In[172]:


## Display percentage of missing values in each column if any
percent_missing = df1.isnull().sum()/len(df1)*100
mising_value_df1 = pd.DataFrame({'column_name': df1.columns,
                               "percent_missing_values": percent_missing})
mising_value_df1


# In[176]:


## Select records where LotConfig is Inside
df1[df1.LotConfig == 'Inside']


# In[177]:


## Make a new dataframe with only numeric columnsSubClass)
new_df = df1.select_dtypes('number')
new_df


# In[178]:


## Make a new dataframe with only factorial/string columns
new_df1 = df1.select_dtypes('object')
new_df1


# In[181]:


## Drop column ExterQual
df1.drop(columns = ['ExterQual']).head()


# In[182]:


## Group data on LotShape and find average LotArea
df.groupby('LotShape')['LotArea'].mean()


# In[187]:


## Write code to get a pivot table as shown (average of MSSubClass)
pd.pivot_table(df, 'MSSubClass', ['MSZoning', 'LotShape'], aggfunc = 'mean')

