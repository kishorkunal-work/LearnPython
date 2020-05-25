# -*- coding: utf-8 -*-
"""
@author: kkunal

 Write a Python program to concatenate all elements in a list into a string and return it.
Output:

hello hi how are you

"""

list1 = ['hello','hi','how','are','you']
def listToString(group_data):
    output = ''
    for n in group_data:
        output += n + " "
    print(output)
        
listToString(list1)


