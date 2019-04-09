# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:19:57 2019

@author: pengz
"""

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true

Example 2:

Input:  "88"
Output: true

Example 3:

Input:  "962"
Output: false

'''
def isStrobogrammatic(num: str) -> bool:
#    done = False
    ans = {'1':'1','9':'6','6':'9','8':'8'}
    i = 0
    res = ''
    while i < len(num):
        
        if num[i] not in ans.keys():
            print('not')
            return False
        else:
            res = ans[num[i]] + res
        i = i+1
    print(res)
    if res == num:
        return True
    else:
        return False
a = isStrobogrammatic("88")
#print('69'=='69')