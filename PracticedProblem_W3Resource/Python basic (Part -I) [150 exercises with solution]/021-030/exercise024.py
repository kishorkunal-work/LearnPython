# -*- coding: utf-8 -*-
"""
@author: kkunal

 Write a Python program to test whether a passed letter is a vowel or not.

Output:

enter a character: asdf
Please enter single character

enter a character: a
its a vowel

enter a character: 4
its not a vowel

"""

def isVowel(s):   
   vowels = ["a","e","i","o","u"]
   if (len(s) > 1):
       print("Please enter single character")
   else:
       if(vowels.__contains__(s)):
           print("its a vowel")
       else:
           print("its not a vowel")


isVowel(input("enter a character: "))


