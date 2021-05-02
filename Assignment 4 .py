#!/usr/bin/env python
# coding: utf-8

# # File Input output Handling

# ## 1. Python Program to Read the Contents of a File

# In[ ]:


file = open('tryfile.txt', 'w')
file.write('This is a example')
file.close()
with open('tryfile.txt','r') as f:
    print(f.read())
f.close()


# ## 2. Python Program to Count the Number of Words in a Text File

# In[ ]:


with open('tryfile.txt','r') as f:
    v = f.read()
    print(len(v.split(' ')))
f.close()


# ## 3. Python Program to Copy the Contents of One File into Another

# In[ ]:


f=open('tryfile.txt','r')
f1=open('tryfile2.txt','w')
for i in f:
    f1.write(i)
f.close()
f1.close()

f1=open('tryfile2.txt','r')
print(f1.read())


# ## 4. Python Program to Read a File and Capitalize the First Letter of Every Word in the File

# In[ ]:


with open('tryfile.txt', 'r') as f:
    for line in f:
        l=line.title()
        print(l)


# # Exception Handling

# ## 1. WAP to read input from user. Allow the user to enter more numbers as long as the user enters valid integers. Terminate the program with proper message when they entered value is anything except integer.

# In[ ]:


while True:
    try:
        num = int(input("Please enter an integer: "))
    except ValueError:
        print("Not valid integer! Please try again ...")
        break


# ## 2. WAP to read input from a user. Allow the user to enter more numbers as long as the user enters valid numbers. Terminate the program with proper message when the user enters a value anything except valid number.

# In[ ]:


while True:
    try:
        num = input("Please enter a number: ")
        if num.isdigit():
            continue
        else:
            a==num
    except:
        print("Not a number. Please try again")
        break
        
    # Different methods
# while True:
#     try:
#         num = float(input("Please enter an number: "))
#     except ValueError:
#         print("Not a valid number! Please try again ...")
#         break
        

# flag = True      
# while flag:
#     try:
#         num = input("Please enter a number: ")
#         if num.isdigit():
#             continue
#         else:
#             flag = False
#             a==num
#     except:
#         print("Not a number. Please try again")    


# ## 3. WAP to read input from a user. Allow the user to enter more numbers as long as the user enters valid numbers. Terminate the program with proper message when the user enters a value anything except valid number. Allow wrong entry 'N' times.

# In[ ]:


cnt=0
while cnt<3:
    try:
        num = input("Please enter a number: ")
        if num.isdigit():
            continue
        else:
            cnt=cnt+1
            a==num
    except:
        print("Not a number. Please try again. You have {} more chances.".format(3-cnt))

  # Different methods
# flag = True      
# while flag:
#     try:
#         num = input("Please enter a number: ")
#         if num.isdigit():
#             continue
#         else:
#             flag = False
#             a==num
#     except:
#         print("Not a number. Please try again. You have 2 more chances.")
#         try:
#             num = input("Please enter a number: ")
#             if num.isdigit():
#                 continue
#             else:
#                 flag = False
#                 a==num
#         except:
#             print("Not a number. Please try again. You have 1 more chance.")
#             try:
#                 num = input("Please enter a number: ")
#                 if num.isdigit():
#                     continue
#                 else:
#                     flag = False
#                     a==num
#             except:
#                 print("Not a number.")



# po=0
# def check(cnt):
#     while True:
#         try:
#             num = input("Please enter a number: ")
#             if num.isdigit():
#                 continue
#             else:
#                 a==num
#         except:
#             print("Not a number. Please try again. You have {} more chances.".format(3-cnt))
#             cnt=cnt+1
#             return cnt
# while po<=3:
#     po=check(po)


# # Regular Expression

# ## 1. Validate email id using Regular Expression

# In[ ]:


import re


# In[ ]:


emails = ['xyz1@gmail.com', 'poi456@gmail.org','Rts7@gmail.org', 'JKL@gmail.com', 'ABC2@gmail.com', 'abc_1@gmail.com','1@gmail.com']

for email in emails:
    if re.search(pattern='^[a-zA-Z]+[0-9]*@gmail\.(com|org|net)$', string= email):
        print(email,' => Valid Email')
    else:
        print(email, ' => Invalid Email')


# ## 2.Validate a mobile Phone Number with country code using Regular Expression

# In[ ]:


phone_numbers = ['99161798123', '+91 991-617-9812','+19 9916179812','91 9916179812','195555555551','195555555551a']

for number in phone_numbers:
    if re.search(pattern='^(\+91 )\d{3}-\d{3}-\d{4}$', string= number):
        print(number,' => Valide Number')
    else:
        print(number, ' => Invalid Number')


# ## 3. Validate a credit card number using Regular Expression

# In[ ]:


credit_cards = ['5123-4567-8912-3456', '61234-567-8912-3456', '4123356789123456', '5133-3367-8912-3456']

for number in credit_cards:
    if re.search(pattern='^\d{4}-\d{4}-\d{4}-\d{4}$', string= number):
        print(number,' => Valid card')
    else:
        print(number, ' => Invalid card')


# ## 4. Find all numbers in a string using regular expression: 

# In[ ]:


string = 'adbv345hj43hvb42'
numbers = re.findall('[0-9]+', string)
print(numbers)

