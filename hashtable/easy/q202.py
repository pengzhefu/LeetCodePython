# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:08:47 2019

@author: pengz
"""

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the 
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
'''
def isHappy(n):     ## Using dict, written by my own
    happy = False
    ret = {}
    while not happy:
        res = 0
        for inte in str(n):
            res += int(inte)**2
        print(res)
        if res == 1:
            happy = True
        else:
            if res not in ret.keys():
                ret[res] = 1
                n =res
            else:
                break
    return happy

#print(isHappy(19))