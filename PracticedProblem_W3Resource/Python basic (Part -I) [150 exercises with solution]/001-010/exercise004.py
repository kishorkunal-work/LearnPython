# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:51:23 2020

@author: kkunal

P: Write a Python program which accepts the radius of a circle 
    from the user and compute the area.
    
Output:
    
    Input the radius of the circle : 2.3
    The circle area is : 16.619025137490002
    
"""

from math import pi

r = float(input ("Input the radius of the circle : "))

print("The circle area is : " + str(pi * r ** 2))

