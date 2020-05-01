# -*- coding: utf-8 -*-
"""
Created on Fri May  1 06:37:40 2020

@author: kkunal

Write a Python program to get the the volume of a sphere with radius 6.

Output:

    904.7786842338604
    
"""

from math import pi

r= 6
d=2*r
area = (pi*d*d*d)/6
print(str(area))
