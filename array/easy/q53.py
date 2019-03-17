# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:20:51 2019

@author: pengz
"""

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):   ## 这道题没想出来，看的别人的solution
    maxSum = nums[0]  ## maxSum用来记录目前一路算过来以后的最大值
    curSum = nums[0]  ## curSum就是current sum,就是目前的总值，这个值会一直保留到变负数而且遇到一个比总值更大的数，相当于
                        ## 列表清空，重新开试
    for i in range(1,len(nums)):
        curSum = max(nums[i],nums[i]+curSum)  ## 用来应对在两个正数中间穿插了一个负数的情况，
                                                ## 1.可以在curSum和maxSum还是负数的时候，遇到正数马上转正
                                                ## 2.在遇到负数后，可以暂时先保存这个curSum的值，只要curSum的值还都比
                                                ## 后续遇到的大，就先保留，直到比某个数小了，或者变成负数以后遇到正数，
                                                ## 相当于列表清空重来一次
        maxSum = max(maxSum,curSum)  
    
    return maxSum

print(maxSubArray([-2,-1,-3,4,1,2,-1,-5,4]))
