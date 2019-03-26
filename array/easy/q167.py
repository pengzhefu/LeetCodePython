# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:05:08 2019

@author: pengz
"""

'''
Given an array of integers that is already sorted in ascending order, find two numbers such that 
they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''

def twoSum(numbers, target):   ## Written by my own, concerning about q1, using dict. complexity is O(n)
    if len(numbers) < 2:
        return []
    else:
        i = 1
        dict1 = {}
        while i <= len(numbers):
            val = target - numbers[i-1]
            if val not in dict1.keys():
                dict1[numbers[i-1]] = i
                i = i+1
                print(dict1)
            else:
                return [dict1[val],i]
#a = twoSum([0,7,8,9],9)

def twoSum2(numbers,target):  ## 借鉴的方法，因为是已经排序好的，所以可以用双指针
    i = 0
    j = len(numbers)-1
    found = False
    while not found:
        if numbers[i] + numbers[j] > target:    ## 因为是递增，所以大了就要把大的往小了调
            j = j-1
        elif numbers[i] + numbers[j] < target:   ## 因为是递增，所以小了就要把小的往大了调
            i = i+1
        else:
            return [i+1,j+1]

a = twoSum2([0,7,8,9],7)        