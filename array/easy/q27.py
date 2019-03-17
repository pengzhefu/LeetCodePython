# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:14:09 2019

@author: pengz
"""

"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
Subscribe to see which companies asked this question.
"""

def removeElement(nums, val):   ## Written by myself, and pass, but the time and space is not good
    geshu = len(nums) - 1
    i = 0
    while i <= geshu:
        if nums[i] == val:
            geshu -= 1
            nums.pop(i)
            continue
        else:
            i = i+1
        
    return len(nums)
    
a = removeElement([0,1,2,2,3,0,4,2], 2)