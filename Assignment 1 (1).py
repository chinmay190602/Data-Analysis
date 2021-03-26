#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# ## Python Basic Programs

# ### 1. Print Hello world! :

# In[ ]:


print("Hello world!")


# ### 2. Declare the following variables: Int, Float, Boolean, String & print its value.
# 

# In[ ]:


a = 10
print(a, "is of type", type(a))

b = 5.0
print(b, "is a type of", type(b))

c = []
print(c, "is", bool(c))

d = [0]
print(d, "is", bool(d))

e = 0.0
print(e, "is", bool(e))

my_string = "Hello"
print(my_string, type(my_string))

my_strings = """Hello, welcome to my world"""
print(my_strings, type(my_string))


# ### 3. Program to calculate the Area Of Triangle:

# In[ ]:


a = float (input ('Enter first side: '))
b = float (input ('Enter second side: '))
c = float (input ('Enter third side: '))

# semi-perimeter
s = (a + b + c) / 2

# area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print ('The area of the triangle is %0.2f' %area)


# ### 4. Program to calculate area of a square.

# In[ ]:


s = int(input('Enter side: '))
area = s * s
print("{} is area of sqaure".format(area))


# ### 5. Program to swap two variables:

# In[ ]:


x = input ('Enter value of x: ')
y = input ('Enter value of y: ')

temp = x
x = y
y = temp

print ('the value of x after swapping: {}'.format(x))
print ('the value of y after swapping: {}'.format(y))


# ### 6. Program is to check if a number is positive, negative or zero.

# In[ ]:


num = float(input("Enter number"))
if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")


# ### 7. Program is to check if a number is Even or Odd.

# In[ ]:


n = int(input('Enter a number'))
if n % 2 == 0: 
    print('{} is an even number.'. format(n))
else:
    print('{} is an odd number.'.format(n))


# ### 8. Program to print Odd number within a given range.

# In[ ]:


lower= int (input ("Enter the lower limit for the range :"))
upper= int (input ("Enter the upper limit for the range :"))
for i in range (lower, upper+1):
    if (i%2 != 0):
        print (i)


# ### 9. Python program to find the factorial of a number.

# In[ ]:


n = int(input ("Enter number :"))
fact = 1
while (n>0):
    fact =fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)


# ### 10. Program to reverse a given number.

# In[ ]:


n=int (input ("Enter number: "))
rev =0
while (n>0):
    dig =n%10
    rev =rev*10+dig
    n =n//10
print ("Reverse of the number:", rev)


# ### 11. Program to find out the sum of N Natural numbers.

# In[ ]:


num = int (input ("Enter a number: "))
if num < 0:
    print ("Enter a positive number")
else:
    sum = 0


# ## Strings

# ### 1. Program to reverse a string.

# In[ ]:


a=str(input ("Enter a string: "))
print("Reverse of the string is: ")
print(a[::-1])


# ### 2. Program to check if string is palindrome or not:

# In[ ]:


my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list (my_str) == list(rev_str):
    print("It is palindrome")
else:
    print("It is not palindrome")


# ### 3. Python Program to Replace all Occurrences of ‘a’ with $ in a String from user:

# In[ ]:


string = input("Enter string :")
string= string.replace('a','$')
string= string.replace('A','$')
print("Modified string:")
print(string)


# ### 4. Python Program to Count the Number of Vowels in a String Input Two Strings and Display the Larger String without Using Built-in Functions:

# In[ ]:


string = input("Enter string:")
vowels = 0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels = vowels + 1
        print("Vowel number {}".format(vowels))
        print(i)

string1 = input("Enter first string :")
string2 = input("Enter second string :")
count1=0
count2=0
for i in string1:

    count1=count1+1
for j in string2:
    count2=count2+1
if (count1<count2):
    print ("Larger string is :")
    print (string2)
elif(count1==count2):
    print("Both strings are equal.")
else:
    print("Larger string is:")
    print(string1)


# ### 5. Count the number of digits & letter in a string:

# In[ ]:


string = input("Enter string :")
word = input("Enter word :")
a= []
count= 0

a=string.split(" ")
for i in range (0, len(a)):
    if (word == a[i]):
        count = count+1
        print ("Count of the word is:")
        print(count)


# ### 6. Count Number of Lowercase Characters in a String:

# In[ ]:


string = input ("Enter string:")
count = 0
for i in string:
    if (i.islower()):
        count = count + 1
        print("The number of lowercase characters is :")
        print(count)
    else:
        print("please use lower case")


# ### 7. Program to check if a Substring is Present in a Given String:

# In[ ]:


string = input("Enter string: ")
sub_str = input("Enter word : ")
if (string.find(sub_str)==-1):
    print ("Substring not found in string!")
else:
    print("Substring in string!")


# ## Conditional statements

# ### 1. W. A P. which takes one number from 0 to 9 from the user and prints it in the word. And if the word is not from 0 to 9 then it should print that number is outside of the range and program should exit.

# In[ ]:


n = int(input("Enter number: "))

if n == 0:
    print("Zero")
elif n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
elif n == 8:
    print("Eight")
elif n == 9:
    print("Nine")
else:
    print("Invalid output")


# ### 2. W. A P. to implement calculator but the operation to be done and two numbers will be taken as input from user:- Operation console should show below:-
# Please select any one operation from below:-
# 1. To add enter 1
# 2. to subtract enter 2
# 3. To multiply enter 3
# 4. To divide enter 4
# 5. To divide and find quotient enter 5
# 6. To divide and find remainder enter 6
# 7. To find num1 to the power of num2 enter 7
# 8. To Come out of the program enter 8

# In[ ]:


n1 = float(input("Enter a number "))
n2 = float(input("Enter a number "))
op = input("Enter the operator ")
1 == '+'
2 == '-'
3 == '*'
4 == '/'
5 == '//'
6 == '%'
7 == '**'
8 == exit()
if op == '1':
    print(n1 + n2)
elif op == '2':
    print(n1 - n2)
elif op == '3':
    print(n1 * n2)
elif op == '4':
    if n2 == 0:
        print("Invalid input")
    else:
        print(n1 / n2)
elif op == '5':
    print(n1 // n2)
elif op == '6':
    print(n1 % n2)
elif op == '7':
    print(n1 ** n2)
elif op == '8':
    quit()
else:
    print('Invalid output')
   


# ### 3. W A P to check whether a year entered by user is an leap year or not?
#  Check with below input:-
# 1. leap year:- 2012, 1968, 2004, 1200, 1600,2400
# 2. Non-leap year:- 1971, 2006, 1700,1800,1900

# In[ ]:


year = int(input('Enter an year: '))
if year % 4 == 0:
    print('Divisible by 4')
    if year % 100 == 0:
        print('Divisible by 100')
        if year % 400 == 0:
            print('Divisible by 400')
            print('Year is a leap year')
        else:
            print('not Divisible by 400')
            print('Year is not a leap year')
    else:
        print('Not Divisible by 100')
        print('Year is a leap year')
else:
    print('Not Divisible by 4')
    print('Year is not a leap year')


# ### 4. W A P which takes one number from the user and checks whether it is an even or odd number? If it even then prints number is even number else prints that number is odd number.
# 

# In[ ]:


n = input('Enter a number: ')

if n.isdigit():
    n = int(n)
    if n%2 == 0:
        print('{} is an even number.'.format(n))
    else:
        print('{} is an odd number.'.format(n))
else:
    print('Invalid input!!!')


# ### 5. W A P which takes two numbers from the user and prints below output:-
# -num1 is greater than num2 if num1 is greater than num2
# 
# -num1 is smaller than num2 if num1 is smaller than num2
# 
# -num1 is equal to num2 if num1 and num2 are equal
# 
# Note: -
# 1. Do this problem using if - else

# In[ ]:


num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

if num1 > num2:
    print("1st Number is greater then 2nd Number")
elif num1 == num2:
    print("Both numbers are equal")
elif num1 < num2:
    print("1st Number is smaller then 2nd Number")
else:
    print("Invalid input")


# 2. Do this using ternary operator

# In[ ]:


num1, num2 =float(input("Enter 1st Number: ")), float(input("Enter 2nd Number: "))

print ("Both 1st Number and 2nd Number are equal" if num1 == num2 else "1st Number is greater than 2nd Number"
        if num1 > num2 else "1st number is smaller then 2nd Number")


# ### 6. W A P which takes three numbers from the user and prints below output:-
# -num1 is greater than num2 and num3 if num1 is greater than num2 and num3
# 
# -num2 is greater than num1 and num3 if num2 is greater than num1 and num3
# 
# -num3 is greater than num1 and num2 if num3 is greater than num1 and num2
# 
# Note:-
# 1. Do this problem using if - elif - else

# In[21]:


num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))
num3 = float(input("Enter 3rd Number: "))

if (num1 > num2 and num1 > num3):
    print("1st Number is greater then 2nd & 3rd Number")
elif (num2 > num1 and num2 > num3):
    print("2nd Number is greater then 1st & 3rd Number")
elif (num3 > num1 and num3 > num2):
    print("3rd Number is greater then 1st & 2nd Number")
else:
    print("Invalid input")


# 2. Do this using ternary operator

# In[26]:


num1, num2, num3 =float(input("Enter 1st Number: ")), float(input("Enter 2nd Number: ")), float(input("Enter 3rd Number: "))
 
mx = (num1 if (num1 > num2 and num1 > num3) else
     (num2 if (num2 > num1 and num2 > num3) else num3))

print("Largest number among is " + str(mx))


# ## Loops - for loop, while loop

# ### 7. Write a Python program to find the length of the my_str using loop
# 
# Input:- 'Write a Python program to find the length of the my_str'
# 
# Output:- 55

# In[ ]:





# ### 8. Write a Python program to find the total number of times letter 'p' is appeared in the below string using loop:-
# 
#  Input:- 'peter piper picked a peck of pickled peppers.\n'
# 
#  Output:- 9

# In[ ]:





# ### 9. Q. Write a Python Program, to print all the indexes of all occurrences of letter 'p' appeared in the string using loop:-
# 
#  Input: - 'peter piper picked a peck of pickled peppers.'
# 
#  Output:-
#  0
#  6
#  8
#  12
#  21
#  29
#  37
#  39
#  40

# In[ ]:





# ### 10. Write a python program to find below output using loop:-
# 
#  Input: - 'peter piper picked a peck of pickled peppers.'
# 
#  Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']

# In[ ]:





# ### 11. Write a python program to find below output using loop:-
# 
#  Input: - 'peter piper picked a peck of pickled peppers.'
#     
#  Output:- 'peppers pickled of peck a picked piper peter'

# In[ ]:





# ### 12. Write a python program to find below output using loop:-
# 
#  Input: - 'peter piper picked a peck of pickled peppers.'
#     
#  Output:- '.sreppep delkcip fo kcep a dekcip repip retep'
# 

# In[ ]:





# ### 13. Write a python program to find below output using loop:-
# 
#  Input: - 'peter piper picked a peck of pickled peppers.'
# 
#  Output:- 'retep repip dekcip a kcep fo delkcip sreppep'

# In[ ]:





# ### 14. Write a python program to find below output using loop:-
# 
#  Input: - 'peter piper picked a peck of pickled peppers.'
# 
#  Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'
# 

# In[ ]:





# ### 15. Write a python program to find below output using loop:-
# 
#  Input: - 'Peter Piper Picked A Peck Of Pickled Peppers.'
# 
#  Output:- 'Peter piper picked a peck of pickled peppers'

# In[ ]:





# ### 16. Write a python program to implement index method using loop. If sub_str is found in my_str then it will print the index of first occurrence of first character of matching string in my_str:-
# 
#  Input: - my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
# 
#  sub_str = 'Pickl'
# 
#  Output:- 29
# 

# In[ ]:





# ### 17. Write a python program to implement replace method using loop. If sub_str is found in my_str then it will replace the first occurrence of sub_str with new_str else it will will print sub_str not found:-
# 
#  Input: - my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
# 
#  sub_str = 'Peck', new_str = 'Pack'
# 
#  Output: - 'Peter Piper Picked A Pack Of Pickled Peppers.'
# 

# In[ ]:





# ### 18. Write a python program to find below output (implements rjust and ljust) using loop:-
# 
#  Input: - 'Peter Piper Picked A Peck Of Pickled Peppers.'
# 
#  sub_str ='Peck',
# 
#  Output:- '*********************Peck********************'

# In[ ]:





# ### 19. Write a python program to find below output using loop:-
# 
#  Input:- 'This is Python class', sep = ' is',
# 
#  Output:- ['This', 'Python class']
# 

# In[ ]:





# ### 20. WAP to read input from user. Allow the user to enter more numbers as long as the user enters valid integers. Terminate the program with proper message when they entered value is anything except integer.
# 

# In[ ]:





# ### 21. WAP to read input from a user. Allow the user to enter more numbers as long as the user enters valid numbers. Terminate the program with proper message when the user enters a value anything except valid number.

# In[ ]:





# ### 22. WAP to read input from a user. Allow the user to enter more numbers as long as the user enters valid numbers. Terminate the program with proper message when the user enters a value anything except valid number. Allow wrong entry 'N' times.
# 

# In[ ]:




