# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 01:19:12 2019

@author: pengz
"""
'''
ARRAY, EASY
'''

'''
Question 1 
Two Sum
'''

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum_p(nums, target):   ## Written by myself, 时间复杂度为O(N2)
    ret = []
    n = len(nums)
    for i in range(n):
        x = target - nums[i]
        for j in range(i+1,n):
            if nums[j] == x:
                ret.append(i)
                ret.append(j)
    return ret
print(twoSum_p(nums = [2, 7, 11, 15], target = 18))
#nums = [2, 7, 11, 15]
#for k,v in enumerate(nums):
#    print(k,v)
def twoSum(nums,target):   ## A better solution, 时间复杂度为O(N)，因为dict检查in是O(1),而list是O(n)
    dicts = {}
    ret = []
    for idx, num in enumerate(nums):
        val = target - num
        if val in dicts.keys():
            ret.append(dicts[val])
            ret.append(idx)
            return ret
        else:
            dicts[num] = idx
#    return ret
print(twoSum(nums = [2, 7, 11, 15], target = 18))