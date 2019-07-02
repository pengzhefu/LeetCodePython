# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 02:59:16 2019

@author: pengz
"""

'''
Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

medium
'''
def threeSum(nums: [int]) -> [[int]]:  ## idea from https://blog.csdn.net/weixin_41463193/article/details/91859621#commentsedit, 思路3
    ret = []
    if len(nums) <3:
        return ret
    nums = sorted(nums)  ## 先排序, 从小到大
    # print(nums)
    for i in range(0,len(nums)):  ## i可以一直到最后, 当j或k不能移动的时候, 就要移动i, 并重置j和k
                                    ## j或者k不能移动的情况, 就是j和k已经相邻了
        if i >0 and nums[i] == nums[i-1]:  ## 去重, 找到下一个不一样的
            continue
        j = i+1  ## i后面的一位
        k = len(nums)-1  ## 每次都是最后一个
        while (j <k):   ## 这是最关键的, j一定要在k左边
            if nums[j] + nums[k] == -nums[i]:
                ret.append([nums[i],nums[j],nums[k]])  
                if j<k:  ## 当找到了一个配对以后， 先不移动i, 是把j和k各往中间移一步 
                    j =j+1
                    k =k-1
                while j<k and nums[j]== nums[j-1]:  ##去重, 找到下一个不一样的
                    j = j+1
                while j<k and nums[k] == nums[k+1]: ## 去重,找到下一个不一样的
                    k =k-1
            elif nums[j] +nums[k] < -nums[i]:   ## 如果小了, 就移动j
                if j <k:
                    j =j+1
                    while j<k and nums[j] ==nums[j-1]:
                        j = j+1
            elif nums[j] + nums[k] > -nums[i]:  ## 如果大了, 就移动k
                if j <k:
                    k = k-1
                    while j<k and nums[k] == nums[k+1]:
                        k =k-1
    return ret
                