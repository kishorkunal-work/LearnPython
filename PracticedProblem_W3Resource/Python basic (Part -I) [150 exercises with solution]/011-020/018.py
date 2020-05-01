# -*- coding: utf-8 -*-
"""
@author: kkunal

Write a Python program to test whether a number is within 100 of 1000 or 2000.

Output:

    Enter your lucky numbers : 3 4 5
    12
    
    Enter your lucky numbers : 3 3 3
    27
    
"""

num = list(map(int , input("Enter your lucky numbers : ").split(" ")))

def sum_thrice(a,b,c):
    sum = a+b+c
    if a==b==c:
        sum = sum*3
    return sum

print(sum_thrice(num[0],num[1],num[2]))
