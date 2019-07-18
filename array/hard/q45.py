# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:05:02 2019

@author: pengz
"""
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.

'''
'''
idea inspired by https://www.youtube.com/watch?v=r3pZd9ghqxk, 但最好看自己的解释
'''
def jump(nums: [int]) -> int:
    step = 0
    curMax = 0    ## 记录当前的index走的一步之后，最远能到的index
    nextMax = 0  ## 记录下一步能走到的最远的index
    idx = 0
    target = len(nums) -1
    idx_max =0   ## 记录下一步能走到的最远的那个index，是从哪个index走的
#    print('target',target)
    while idx < target:
        nextMax = idx + nums[idx]   ## 先找到这一个起点能走到的
        step += 1   ## 走了一步了，步数+1
        curMax = nextMax   ## 用cur来记录
#        print('idx',idx,'step',step,'curMax',curMax)
        while idx <= curMax and idx < target:  ## 找如果要走下一步的话, 要走到最远的距离的index要是多少
            tmp = idx + nums[idx]
            if tmp >= nextMax:   ## 如果能比nextMax大, 就说明能走的更远, 要找这个起点index, 作为我们下一步要去的起点
                nextMax = tmp
                idx_max = idx   ## 用idx_max来记录此时的起点index,
            idx +=1
        idx = idx_max   ## 作为下一步要去的起点
        if curMax >= target:
#            print('here')
            return step
    return step


nums = [1,2,1,1,1]
nums1 = [2,3,1,1,4]
nums2 = [1,2,3]
ret = jump(nums1)