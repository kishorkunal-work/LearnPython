# -*- coding: utf-8 -*-
"""
@author: kkunal

 Write a Python program to check whether a specified value is contained in a group of values.
Output:

print(is_group_member(list1 , 3))
True

print(is_group_member(list1 , 100))
False

"""

list1 = [1,5,8,3]
def is_group_member(group_data , n):
    for value in group_data:
        if (value == n):
            return True
    return False
        
print(is_group_member(list1 , 3))
print(is_group_member(list1 , 100))


