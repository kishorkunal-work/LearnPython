# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:37:40 2020

@author: kkunal

Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.

Output:
    
Enter the year : 2020

Enter the month : 05


      May 2020
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""


import calendar

y = int(input("Enter the year : "))
m = int(input("Enter the month : "))
print("\n")
print(calendar.month(y , m))
