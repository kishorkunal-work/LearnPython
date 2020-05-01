# -*- coding: utf-8 -*-
"""
@author: kkunal

Write a Python program to test whether a number is within 100 of 1000 or 2000.

Output:

    Enter your lucky number : 1001
    True
    
    Enter your lucky number : 800
    False
    
"""

num = int(input("Enter your lucky number : "))

def near_thousand(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <= 100))

print(near_thousand(num))
