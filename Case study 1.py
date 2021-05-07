#!/usr/bin/env python
# coding: utf-8

# # Case Study 1

# ## Dataset Description: The file consists of start-ups investment details.

# In[42]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings 
warnings.filterwarnings('ignore')

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# ### 1.Read the given comma separated values as dataframe (investments.csv)

# In[43]:


df = pd.read_csv('investments.csv')
df.head()


# ### 2.List out all column names.

# In[46]:


col = df.columns
print(list(col))


# ### 3.Create a dataframe with numerical columns.

# In[47]:


new_df = df.select_dtypes('number')
new_df.head()


# ### 4.Create a dataframe with categorical columns.

# In[48]:


new_df = df.select_dtypes('object')
new_df.head()


# ### 5.Get a summary on the data and draw inferences if any.

# In[7]:


df.describe()


# ### 6.Display duplicate rows.

# In[49]:


df.duplicated().sum()


# ### 7.For each column find out the percentage of missing values.

# In[59]:


df.isnull().sum()/len(df)*100
mising_value_df = pd.DataFrame({'column_name': df.columns,
                               "percent_missing_values": percent_missing})
missing_value_df


# ### 8.Find count of ‘name’ in each ‘country_code’.

# In[65]:


df.groupby('country_code')['name'].count().head()


# ### 9.What is the percentage of the companies which have status ‘acquired’ or ‘operating’?

# In[66]:


df[df.status.isin(['acquired','operating'])].shape[0]/len(df)*100


# ### 10.What is the percentage of the companies which have status ‘acquired’ and 'operating'?

# In[69]:


df[df.status.isin(['acquired' and 'operating'])].shape[0]/len(df)/100


# ### 11.Filter records having missing values in column ‘year_founded’.

# In[72]:


df[df.founded_year.isna()].head()


# ### 12.Create a column ‘category_list_count’ having count of category lists.

# In[15]:


df['category_list_count'] = df.category_list.apply(lambda row : len(str(row).split('|')) - 2)
df.loc[:,['category_list','category_list_count']].head()


# ### 13.Find average funding_total_usd for each country_code.

# In[16]:


df.funding_total_usd = df.funding_total_usd.apply(lambda x : x.replace(',',''))
df.funding_total_usd = df.funding_total_usd.apply(lambda x : x.replace('-','0'))
df.funding_total_usd = df.funding_total_usd.astype(float)
df.groupby('country_code')['funding_total_usd'].mean()


# ### 14.Find total funding_total_usd for each country_code.

# In[17]:


df.groupby('country_code')['funding_total_usd'].mean()


# ### 15.Find average funding_total_usd in each country_code and region.

# In[18]:


pd.pivot_table(df, 'funding_total_usd', ['country_code', 'region'], aggfunc='mean')


# ### 16.How many companies have got just 1 round of funding?

# In[76]:


### including duplicates
print(df[df.funding_rounds == 1]['name'].shape[0]) 
### excluding duplicates
print(len(df[df.funding_rounds == 1]['name'].unique())) 
## excluding duplicates and nan
print(df[df.funding_rounds == 1]['name'].nunique()) 
### including duplicates but excluding nan
print(df[df.funding_rounds == 1]['name'].count()) 


# ### 17.Perform mapping on status column; acquired -> A, operating -> O and closed -> C.

# In[20]:


df.status.apply(lambda s: 'A' if s == 'acquired' else 'O' if s == 'operating' else 'C' if s=='closed' else 'NA').head()


# ### 18.How many companies have ‘debt_financing’ above zero?

# In[21]:


### including duplicates
print(df[df.debt_financing > 0]['name'].shape[0]) 
### excluding duplicates
print(len(df[df.debt_financing > 0]['name'].unique())) 
## excluding duplicates and nan
print(df[df.debt_financing > 0]['name'].nunique()) 
### including duplicates but excluding nan
print(df[df.debt_financing > 0]['name'].count()) 


# ### 19.Create a column ‘homepage’ to store company name from ‘homepage_url’: For example: If url is http://www.waywire.com, name is waywire.

# In[22]:


import re

df.homepage_url.apply(lambda url: re.sub(pattern = ('http://www.|.com|/|http:|.org'), repl = '', string = str(url), flags= re.I)).head()


# ### 20.Find the count of companies in each of the markets.

# In[23]:


df.groupby('market')['name'].count()


# ### 21.Find the count of companies in each of the markets and store the new column ‘cnt_name’ in the original dataframe.

# In[24]:


df['cnt_name'] = df.groupby('market')['name'].transform('count')
df.head()


# ### 22.Rename ' funding_total_usd ' to 'funding_total_usd'

# In[25]:


df.rename(columns = {'funding_total_usd':'funding_total_USD'})


# ### 23.Fill missing values in column ‘city’ with ‘other_city’

# In[26]:


df.city.fillna('other_city', inplace = True)
df


# ### 24.For each row in column ‘funding_total_usd’, calculate actual – average value for each group ‘city’

# In[27]:


df.groupby('city')['funding_total_usd'].transform(lambda x: x - np.mean(x)).head()


# ### 25.Normalize ‘‘funding_total_usd’ at country level.

# In[28]:


df.country_code.fillna('other_country', inplace = True)
df.groupby('country_code')['funding_total_usd'].transform(lambda x: x/np.max(x)).head()


# ### 26.What is the average ‘funding_total_usd’ for each city?

# In[29]:


df.groupby('city')['funding_total_usd'].mean().head()


# ### 27.Plot histogram/distribution of ‘funding_total_usd’ and provide insights if any.

# In[32]:


plt.hist(df.funding_total_usd)
plt.xlabel('Funding total USD')
plt.ylabel('Count')
plt.title('Histogram of funding total USD')
plt.show()


# ### 28.What is maximum ‘funding_total_usd’ for each market status?

# In[33]:


df.groupby('status')['funding_total_usd'].max()


# ### 29.How many years has it been since each company was founded?

# In[34]:


from datetime import datetime
df['cmpany_age'] = datetime.today().year -  df.founded_year
df.head()


# ### 30.Visualize ‘grant’ distribution.

# In[35]:


x = df.groupby('market')[['grant']].max().reset_index().sort_values('grant', ascending = False)[0:10]
plt.figure(figsize = (20,5))
plt.bar(x.market, x.grant)
plt.title('Top 10 markets with high grants')


# ### 31.Visualize ‘debt_financing’ distribution.

# In[37]:


fig, ax = plt.subplots(1,2,figsize = (20,5))
ax[0].hist(df.grant)
ax[0].set_xlabel('grant')
ax[0].set_ylabel('count of grant')
ax[0].set_title('histogram of grant')

ax[1].hist(np.log1p(df.grant), color = 'g')
ax[1].set_xlabel('log of grant')
ax[1].set_ylabel('count of grant')
ax[1].set_title('histogram of log transformed grant')
plt.show()


# ### 32.Display proportion of companies status.

# In[38]:


df.groupby('status')[['name']].count()/len(df)*100


# ### 33.How many US states are available?

# In[39]:


df[df.country_code == 'USA']['state_code'].nunique()


# ### 34.create column ‘cmt_address’ by joining country code, state code, region and city.

# In[40]:


df['cmt_address']  = df.country_code + '-' + df.state_code + '-' + df.region + '-'+ df.city
df.head()


# ### 35.select columns with underscore in their names.

# In[41]:


df.filter(regex = '_').head()


# In[ ]:




