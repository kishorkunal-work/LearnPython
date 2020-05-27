# -*- coding: utf-8 -*-
"""
@author: kkunal

 Write a Python program to print out a 
 set containing all the colors from 
 color_list_1 which are not present 
 in color_list_2.
 
Output:

{'White'}

"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green" , "Black"])
        
print(color_list_1.difference(color_list_2))


