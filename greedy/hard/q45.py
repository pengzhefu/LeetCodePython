# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 02:46:00 2019

@author: pengz
"""

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''
'''
https://www.youtube.com/watch?v=r3pZd9ghqxk
'''
def canJump(nums: [int]) -> bool:
    total = len(nums) -1  ## 目标index
    i = 0  ## 起始点
    if not nums:
        return False
    if nums[i] == 0 and total > 0:  ## 如果第一个是0并且长度大于1
        return False
    max_end = 0
    end = 0
    while i < total:
        end = i + nums[i]   ## 每次都看看当前这个点能到的最远距离
        max_end = max(end,max_end)  ## 更新目前能到的最大距离
        if max_end >= total:  ## 若大于等于目标
            return True
        if max_end >= i+1:   ## 若最大距离能到下一个点， 才移动
            i = i+1
        else:  ## 不能就break
            break
    if max_end >= total:
        return True
    else:
        return False