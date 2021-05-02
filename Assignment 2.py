#!/usr/bin/env python
# coding: utf-8

# # List & Tuple

# ## 1. Program to Find the Largest Number in a List:

# In[ ]:


lst = [22,33,55,77,99,12,59]
print(max(lst))


# ## 2. Program to Put Even and Odd elements in a List into Two Different Lists:

# In[ ]:


elst = []
olst = []
for i in range(101):
    if i%2==0:
        elst.append(i)
    else:
        olst.append(i)
print("This is even list {}".format(elst))
print("This is odd list {}".format(olst))


# # 3. Program to Read a List of Words and Return the Length of the Longest one

# In[ ]:


a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
maxw=len(a[0])
tempw=a[0]
for i in a:
    if len(i)>maxw:
       maxw=len(i)
       tempw=i
print("The word with the longest length is:")
print(tempw)


# ## 4. Create a List of Tuples with the First Element as the Number and Second
# ## element as the Square of the Number:

# In[ ]:


l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2)
for x in range(l_range,u_range+1)]
print(a)


# ## 5. Program to Remove the Duplicate Items from a List:

# In[ ]:


a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)


# ## 6. WAP to check if this tuple (20, 20, 30, 30, 30, 40, 40, 40, 10) is in
# ## ascending/ descending or in random order without inbuilt function.

# In[ ]:


my_list = [20,20,30,30,30,40,40,40,10]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)


# # Dictionary

# ## 1. Program to Check if a Given Key Exists in a Dictionary or Not:

# In[ ]:


d={'A':1,'B':2,'C':3}
key=input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")


# ## 2. Program to Sum All the Items in a Dictionary:

# In[ ]:


dic={'a':2,'b':5,'c':6}
print("Total sum of values in the dictionary:")
print(sum(d.values()))


# ## 3. Program to Remove the Given Key from a Dictionary:

# In[ ]:


d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=input("Enter the key to delete(a-d):")
if key in d: 
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)


# ## 4. Write a Python program to iterate over dictionaries using for loops:

# In[ ]:


d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 


# ## 5. Write a Python program to sort a dictionary by key:

# In[ ]:


color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))


# # Set

# ## 1. Python Program to Count the Number of Vowels Present in a String using Sets:

# In[ ]:


s=input("Enter string:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)


# ## 2. Python Program to Check Common Letters in Two Input Strings:

# In[ ]:


s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)


# ## 3. Python Program that displays which Letters are in the First String but not in the Second:

# In[ ]:


s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)-set(s2))
print("The letters are:")
for i in a:
    print(i)


# ## 4. Python Program that displays which Letters are Present in Both the Strings:

# In[ ]:


s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)|set(s2))
print("The letters are:")
for i in a:
    print(i)


# ## 5. Python Program that displays which Letters are in the Two Strings but not in both:

# In[ ]:


s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)


# # List comprehension & list generator

# ## 1. WAP to add elements of the two lists:
# ### List1=[6,9,7,5,10]
# ### List2=[10,20,30,50,7]

# In[ ]:


list1 = [6,9,7,5,10]
list2 = [10,20,30,50,7]
sum_list = []
for (item1, item2) in zip(list1, list2):
    sum_list.append(item1+item2)

print(sum_list)


# ## 2. WAP to add square root of the list elements: [5,7,9,10,11]

# In[ ]:


numbers = [5,7,9,10,11]

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)


# ## 3. WAP to create 2’s multiplication table.

# In[ ]:


num = 2
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# ## 4. WAP to return lower case version of list of characters of the string given by a user

# In[ ]:


strg = str(input("ENTER WORD IN UPPER CASE"))
print("The original string is : " + str(strg))
res = [char for char in strg if char.islower()]
print("The lowercase characters in string are : " + str(res))

