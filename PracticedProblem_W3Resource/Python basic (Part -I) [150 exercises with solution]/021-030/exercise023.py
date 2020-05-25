# -*- coding: utf-8 -*-
"""
@author: kkunal

 Write a Python program to get the n (non-negative integer) 
 copies of the first 2 characters of a given string. 
 Return the n copies of the whole string if the length is less than 2

Output:

enter magic string : sdfsdfsdf

enter n to copy : 2
sdsd


enter magic string : a

enter n to copy : 4
aaaa

"""

def nTimesfirst2char(s, n):   
   if len(s) > 2:
       print(s[:2]*n)
   else:
       print(s * n)


str = input("enter magic string : ")
times = int(input("enter n to copy : "))

nTimesfirst2char(str , times)


