#!/usr/bin/env python
# coding: utf-8

# # Functions

# ## 1. Define a Sum Function which accepts variable number of integers as an arguments.

# In[6]:


def sum(x, y):
    return x + y
print(sum(10, 50))


# ## 2. WAF to find factorial of a positive number. Return -1 if input to the function is any invalid input.

# ### 3. Using for loop

# In[17]:


num = 5
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# ### 4. Using while loop

# In[25]:


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
print(factorial(-1))


# ### 5. Using recursive function(note:recursive functionare computationally expensive)

# In[15]:


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 9
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# ## 6. WAF to swap two numbers.

# In[34]:


def swap_numbers(n1,n2):
    
    t = n1
    n1 = n2
    n2 = t
    
    return n1,n2
print(swap_numbers(5,6))


# ## 7. WAF to implement basic calculator.

# In[41]:


def calculator(n1,n2,op):
    if op =='+':
        return n1+n2
    elif op =='-':
        return n1-n2
    elif op == '*':
        return n1*n2
    elif op == '/':
            if n2 == 0:
                return "Invalid input"
            else:
                return n1/n2
    else:
        return'...Error...'
print(calculator(2,5,'*'))


# ## 8. Write a lambda function which find square of anumber

# In[45]:


square = lambda x: x ** 2
print(square(5))


# ## 9. Declare a List with Numbers from 1 to 100 using List Comprehension. Use the lambda and filter function to filter all even numbers.

# In[46]:


lst = [4,5,6,7,9,10,42,33,66,7,22,3]
lst_out = []
for each in lst:
    if each%2 == 0:
        lst_out.append(each)
print(lst_out)


# ## 10. [‘male’,’female’,’male’,’female’,’male’,’female’,’female’,’female’] => Replace ‘male’ with 0 and ‘female’ with 1 using lambda function and map function

# In[48]:


def replace_lst(sent, a1, a2):
    newSent = map(lambda x: x if(x != a1 and x != a2) else a1 if x == a2 else a2, sent)
    return ''.join(newSent)

print(replace_lst([‘male’,’female’,’male’,’female’,’male’,’female’,’female’,’female’], 0,1 ))


# ## 11.Find Fibonacci series for given length using lambda and reduce function

# In[51]:


from functools import reduce


# In[53]:


reduce(lambda x,y : x + [ x[-2] + x[-1]], range(10), [0,1])


# ## 12.Find intersection of two arrays using lambda and filter function

# In[62]:


array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2)) 
print ("\nIntersection of the arrays: ",result)


# ## 13.WAF to check the type of the data with the signature as follow: def find_type(var):

# In[77]:


def find_type(var):
    return type(var)
print(find_type(True))
print(find_type(4))
print(find_type([3, 4, 5, 6]))


# ## 14. WAF to check if a number is even or odd using lambda expression.

# In[83]:


lst = [1,2,3,4,5,6,7,8,9,10]
def filter_even(n):
    return n%2 == 0

print(list(filter(filter_even, lst )), 'Even list')
def filter_odd(n):
    return n%2 != 0
print(list(filter(filter_odd, lst)), 'Odd list')


# ## 15.WAF to return appropriate message as follows:
# ### If the sequence is in ascending order: return “Ascending order”
# ### If the sequence is in descending order: return “Descending order” Else: “Random order”

# In[45]:


def seq(n):
    if max(n) == n[-1] and min(n) == n[0]:
        return "Ascending order"
    elif max(n) == n[0] and min(n) == n[-1]:
        return "Descending order"
    else:
        return "Random order"   
print(seq((10,10,20,30,20,20)))
print(seq((20,20,30,30,30,40,40,40)))
print(seq((20,20,30,30,30,29,40,40,40)))
print(seq((20,20,30,30,30,40,40,40,10)))
print(seq((20,20,20,30,30,30,40,40,40)))
print(seq((20,20,30,30,30,40,40,40,31)))
print(seq((40,40,40,30,20,20,20)))
print(seq((40,40,40,30,20,20,20,10)))
print(seq((40,40,40,30,10,20,20)))

