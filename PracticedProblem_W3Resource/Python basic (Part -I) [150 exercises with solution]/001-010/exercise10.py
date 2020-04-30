# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:51:23 2020

@author: kkunal

P: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

Output:

Sample value of n is 10
Expected Result :  102030
    
"""

n = int(input("Sample value of n is "))

result = str(n + int(str(n)+str(n)) + int("%s%s%s" % (n,n,n)))

print("Expected Result : " ,result)

