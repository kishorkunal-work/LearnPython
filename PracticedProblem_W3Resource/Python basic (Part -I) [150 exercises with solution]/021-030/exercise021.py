# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:01:59 2020

@author: kkunal

Write a Python program to find whether a given number (accept from the user) is even or odd, 
print out an appropriate message to the user.

Output:

Enter a num : 32
This is even

Enter a num : 31
This is odd

"""
num = int(input("Enter a num : "))
mgs = ""
if num % 2 == 0:
    mgs = "This is even"
else :
    mgs = "This is odd"

print(mgs)
