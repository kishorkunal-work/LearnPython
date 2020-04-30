# -*- coding: utf-8 -*-
"""
Write a Python program to display the current date and time.

Output:
    20-04-30 14:49:47
    
"""
import datetime

print(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))