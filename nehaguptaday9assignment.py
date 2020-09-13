#!/usr/bin/env python
# coding: utf-8

# # to check whether the number is prime or not and then doing unit testing on it via pylint and unit testing library

# In[65]:


get_ipython().system('pip install pylint')


# In[76]:


get_ipython().run_cell_magic('writefile', 'checkprimenumber.py', '\'\'\' it ia a program to check whether given number is  prime or not\'\'\'\nnum = int(input("Enter a number: "))  \n    \nif num > 1:  \n    for i in range(2, num):  \n        if (num % i) == 0:  \n            print(num, "is not a prime number")  \n            print(i, "times", num//i, "is", num)  \n            break  \n    else:  \n        print(num, "is a prime number")  \nelse:  \n    print(num, "is not a prime number")  ')


# In[77]:


get_ipython().system(' pylint "checkprimenumber.py"')


# # end--------
