# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:51:23 2020

@author: kkunal

P: Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

Output:

The examination will start from : 11 / 12 / 2014
    
"""

exam_st_date = (11, 12, 2014)

print("The examination will start from : " + str(exam_st_date[0]) +" / "+ str(exam_st_date[1]) +" / "+ str(exam_st_date[2]))

