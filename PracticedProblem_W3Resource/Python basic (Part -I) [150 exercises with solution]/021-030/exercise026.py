# -*- coding: utf-8 -*-
"""
@author: kkunal

 Write a Python program to create a histogram from a given list of integers.
Output:

histogram character to print : #
#
#####
########
###

"""
char = input("histogram character to print : ")
list1 = [1,5,8,3]
def createHistogram(group_data):
    for n in group_data:
        output = ''
        times = n
        while(times > 0):
            output += char
            times-=1
        print(output)
        
createHistogram(list1)


