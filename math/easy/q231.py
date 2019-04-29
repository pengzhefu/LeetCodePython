# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:21:56 2019

@author: pengz
"""
'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false


'''
def isPowerOfTwo(n: int) -> bool:  ## written by my own, the worst time is O(logN)
    if n <= 0:
        return False
    while n > 1:
        if n/2 !=  n//2:
            return False
        else:
            n = n/2
    return True
