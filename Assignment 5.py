#!/usr/bin/env python
# coding: utf-8

# # Numpy

# ## 1. Write a Python program to print the NumPy version in your system.

# In[4]:


import numpy as np
print(np.version.version)


# ## 2. Write a Python program to convert a list of numeric value into a one- dimensional NumPy array.

# In[ ]:


lst = [23,34,5,6,6,777,12,54,65]

arr = np.array(lst)
print(arr)


# ## 3. Write a Python program to create an array with values ranging from 12 to 38.

# In[ ]:


arr = np.array(range(12,39))
print(arr)


# ## 4. Write a Python program to convert a list and tuple into arrays.

# In[ ]:


lst = [1,2,3,4,56,78,8]
tpl = (1,2,3,5,6)

arr = np.array(lst)
arr2 = np.array(tpl)

print(arr)
print(arr2)


# ## 5. Write a Python program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.

# In[ ]:


arr = np.array([1,2,3,4,56,78,8])
print("The number of elements in the array are {} \nThe size of single element is {} \nThe Total bytes consumesd is {}".format(len(arr),(arr.nbytes/len(arr)),arr.nbytes)) 


# ## 6. Write a Python program compare two arrays using numpy.

# In[ ]:


lst = np.array([1,2,3,4,56,78,8])
lst1 = np.array([1,2,3,4,56,78,8])

print(np.array_equal(lst, lst1))


# ## 7. Write a Python program to get the number of nonzero elements in an array.

# In[ ]:


lst = np.array([1,2,3,4,0,56,78,0,8,0])
print(np.count_nonzero(lst))


# ## 8. Write a Python program to check whether the numpy array is empty or not.

# In[ ]:


arr=np.array([1,2,3,5,56,464,54,76,516,9,6])
arr2 = np.array([])
tp=[arr,arr2]
for i in tp:
    if (i.size ==0):
        print('Empty')
    else:
        print("Not empty")


# ## 9. Write a Python program to get the powers of an array values element-wise.

# In[ ]:


arr = np.array([1,2,3,4,5])
np.power(arr, 2)


# ## 10.Write a Python program to stack two arrays: 
# ### 1) row-wise 
# ### 2) column-wise

# In[ ]:


# 1) Row-wise
Arr1 = np.linspace(1,20,50)
Arr2 = np.linspace(21,40,50)
print(np.row_stack(Arr1))
print(np.row_stack(Arr2))


# In[ ]:


# 2) Column-wise
Arr1 = np.linspace(1,20,50)
Arr2 = np.linspace(21,40,50)
print(np.column_stack(Arr1))
print(np.column_stack(Arr2))


# # Pandas (Series and DataFrame)

# In[2]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# ## 1. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

# In[5]:


ds = pd.Series([1,3,5,7,9])
print(ds)


# ## 2. Write a Python program to convert a Panda module Series to Python list and its type.

# In[15]:


ds = pd.Series([1,3,5,7,9])
print(ds)
print(type(ds))
print(ds.tolist())
print(type(ds.tolist()))


# ## 3. Write a Python program to add, subtract, multiple and divide two Pandas Series.

# In[21]:


df1 = pd.Series([1,3,5,7])
print(df1)
df2 = pd.Series([2,4,6,8])
print(df2)
df3 = df1 + df2
print(df3)
df4 = df1 - df2
print(df4)
df5 = df1 * df2
print(df5)
df6 = df1 / df2
print(df6)


# ## 4. Write a Python program to compare the elements of the two Pandas Series.

# In[22]:


sd1 = pd.Series([1,3,5,7])
print(sd1)
sd2 = pd.Series([2,4,6,8])
print(sd2)
print(sd1 == sd2)
print(sd1 > sd2)
print(sd1 < sd2)


# ## 5. Write a Python program to display the following data column wise.

# In[32]:


exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
 
df = pd.DataFrame(exam_data)
print(df)


# ## 6. Write a Python program to create and display a Data Frame from a specified dictionary data which has the index labels.

# In[34]:


xc = pd.DataFrame(exam_data, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(xc)


# ## 7. Write a Python program to select the specified columns and rows from a given Data Frame.

# In[36]:


print(xc.iloc[[1, 3, 5, 6], [1, 3]])


# ## 8. Write a Python program to select the rows the score is between 15 and 20 (inclusive).

# In[37]:


print(xc[xc['score'].between(15, 20)])


# ## 9. Write a Python program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

# In[39]:


print(xc[(xc['attempts'] < 2) & (xc['score'] > 15)])


# ## 10. Write a Python program to append a new row 'k' to Data Frame with given values for each column. Now delete the new row and return the original data frame.

# In[58]:


xc.loc['k'] = ['Chinmay', 18.5, 1, 'yes']
print(xc)
xc = xc.drop('k')
print(xc)


# ## 11. Write a Python program to sort the data frame first by 'name' in descending order, then by 'score' in ascending order.

# In[59]:


xc.sort_values(by=['name', 'score'], ascending=[False, True])
print(xc)


# ## 12. Write a Python program to insert a new column in existing DataFrame.

# In[74]:


xc['A'] = 5
print(xc)


# ## 13. Write a Python program to change the name 'James' to 'Suresh' in name column of the data frame.

# In[85]:


xc['name'] = xc['name'].replace('James', 'Suresh')
print(xc)


# In[ ]:




