# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:01:59 2020

@author: kkunal

Write a Python program to count the number 4 in a given list.

Output:

Enter series : 3 4 5 6 5 4 3 4 5 6
Number of 4 in the list :  3

"""
num = list(map(int ,input("Enter series : ").split(" ")))

def count4(lst):
   count = 0;
   for n in lst:
       if n== 4:
           count = count + 1
    
   return count

print("Number of 4 in the list : " , count4(num))
