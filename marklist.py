# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 05:55:27 2021

@author: aginash
"""

print ("Welcome")

mark_in_maths = int(input("Enter your Mathematics mark out of 100:"))
mark_in_science = int(input("Enter your Science mark out of 100:"))
mark_in_malayalam = int(input("Enter your Malayalam mark out of 100:"))
total = mark_in_maths + mark_in_science + mark_in_malayalam 
if total > 90 and mark_in_maths >= 30 and mark_in_science >= 30 and mark_in_malayalam >=30 :
    if total >= 270:
        print("congratulation you passed with distinction")
    elif total >= 240 and total < 270:
        print("congratulation you passed with first class")
    elif total >= 90 and total < 240:
        print("congratulation you passed with second class")
else :
    print("you failed")