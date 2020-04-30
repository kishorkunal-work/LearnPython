# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:51:23 2020

@author: kkunal

P: Write a Python program to accept a filename from the user and print the extension of that.

Output:
Enter file Name : something.py
Extension :  py
    
"""

items = input("Enter file Name : ")
namelist = items.split(".")

print("Extension : " , namelist[-1])

