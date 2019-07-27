# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:09:14 2019

@author: pengz
"""
'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''
def wiggleSort(nums: [int]) -> None:  ## time is O(nlogn)
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()  ## 先排序, 按从小到大
    i = 1
    while i+1 < len(nums):
        nums[i] ,nums[i+1] = nums[i+1], nums[i]
        i +=2  ## 然后对于偶数位, 但是index是奇数的每一项进行前后调整
        
def wiggleSort2(nums: [int]) -> None:  ## time is O(n)
    for i in range(len(nums)-1):
        if i % 2 ==0 and nums[i] > nums[i+1]:  ## 因为奇数项(index为偶数)的数要小, 所以如果比后面的大，就和后面的交换
            nums[i], nums[i+1] = nums[i+1], nums[i]
            continue
        if i %2 == 1 and nums[i] < nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            continue