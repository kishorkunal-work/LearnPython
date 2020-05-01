# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:37:40 2020

@author: kkunal

Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

Output:

    9 days, 0:00:00
    
"""

from datetime import date

d1  = date(2014, 7, 2)
d2  = date(2014, 7, 11)

print(d2-d1)
