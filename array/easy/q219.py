# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:26:36 2019

@author: pengz
"""

'''
Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference 
between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''
def containsNearbyDuplicate(nums, k):  ## Written by my own, using dict, time complexity is O(n)
    dupl = False
    dict1 = {}
    i = 0
    idx2 = 0
    while i < len(nums):
        if nums[i] not in dict1.keys():
            dict1[nums[i]] = i
        else:
            idx2 = i
            if idx2 - dict1[nums[i]] <=k:
                dupl = True
                break
            else:
                dict1[nums[i]] = i  ##如果这两个不行,就把后一个当作第一个，再继续找下一个一样的，再计算
        i = i+1
    return dupl
nums = [1,0,1,1]
k = 1
a = containsNearbyDuplicate(nums,k)