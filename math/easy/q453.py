# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:06:57 2019

@author: pengz
"""

'''
Given a non-empty integer array of size n, find the minimum number of moves required to 
make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''
def minMoves(nums) -> int:   ## written by my own, the key is to find the min value of nums, time is O(2n)
    pivot = nums[0] 
    ret = 0
    i = 1
    for i in range(1,len(nums)):
        if nums[i] < pivot:
            pivot = nums[i]
    for i in range(0,len(nums)):
        ret += nums[i] - pivot
    return ret

def MinMax(nums) -> int:   ## 分治法找一个数组种的最大最小数, time is O(3n/2)
    i = 0
    j = 1
    res_min = 1000
    res_max = -900
    while i <= len(nums) -1:
        if i < len(nums) -1:
            j = i + 1
            if nums[i] <= nums[j]:
                if nums[i] < res_min:
                    res_min = nums[i]
                if nums[j] > res_max:
                    res_max = nums[j]
            else:
                if nums[j] < res_min:
                    res_min = nums[j]
                if nums[i] > res_max:
                    res_max = nums[i]
        else:
            if nums[i] > res_max:
                res_max = nums[i]
            if nums[i] < res_min:
                res_min = nums[i]
        i += 2
    return res_min,res_max

        
        