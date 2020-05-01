# -*- coding: utf-8 -*-
"""
@author: kkunal

Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.

Output:

Your statement : this yours
Is this yours
    
"""

stmt = input("Your statement : ")

def add_Is_inFront(str):
    if len(str) >= 2 and str[:2]=="Is":
        return str
    else:
        return "Is " + str 
        

print(add_Is_inFront(stmt))
