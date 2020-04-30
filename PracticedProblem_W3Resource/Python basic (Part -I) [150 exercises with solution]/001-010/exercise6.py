# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:51:23 2020

@author: kkunal

P: Write a Python program which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers.

Output:
Enter comma separated sequence of number : 34,23,43
List :  ['34', '23', '43']
Tuple :  ('34', '23', '43')
    
"""

items = input("Enter comma separated sequence of number : ")
list = items.split(",")
tuple = (*list,)

print("List : " ,list)
print("Tuple : " , tuple)

