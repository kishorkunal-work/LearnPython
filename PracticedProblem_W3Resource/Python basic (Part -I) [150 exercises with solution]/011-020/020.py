# -*- coding: utf-8 -*-
"""
@author: kkunal

Write a Python program to get a string which is n (non-negative integer) copies of a given string.

Output:

Your statement : hh

Times : 4
hh
hh
hh
hh
    
"""

stmt = input("Your statement : ")
times = int(input("Times : "))

def multiply_str(str , n):
        return (str + "\n") * n
        

print(multiply_str(stmt , times))
