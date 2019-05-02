# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 02:24:53 2019

@author: pengz
"""

'''
Given an array of size n, find the majority element. The majority element is the element that 
appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''

def majorityElement(nums):## Written by my own, using dict, time complexity is O(N), since find in dict is O(1) 
    times = int(len(nums)/2)+1
    ret = {}
    for num in nums:
        if num not in ret.keys():
            ret[num] = 1
        else:
            ret[num] += 1
        if ret[num] == times:
            return num

def majorityElement2(nums):  ## method from solution
                            ## 原理很简单，因为出现次数要一半以上，所以排序后在最中间的就一定是他
    nums.sort()
    return nums[len(nums)//2]
a = majorityElement([2,2,1,1,1,2,2,3])