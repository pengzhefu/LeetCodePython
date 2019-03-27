# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:37:17 2019

@author: pengz
"""

'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it 
should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''
def containsDuplicate(nums):
    dupl = False
    dict1 = {}
    while not dupl:
        for num in nums:
            if num not in dict1.keys():
                dict1[num] = 1
                print(dict1)
            else:
                dupl = True
                break
        break
    return dupl
nums= [1,1,1,3,3,4,3,2,4,2]
a = containsDuplicate(nums)