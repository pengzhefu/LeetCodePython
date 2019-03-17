# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:14:12 2019

@author: pengz
"""

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

def searchInsert(nums, target):   ## Written by myself, 时间复杂度O(n)
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)
a = searchInsert([1,3,5,6], 5)

def searchInsert2(nums, target):  ## 记住这种已经排序好了的列表！找位置或者判断在不在列表内，用二分搜索最快！
                                    ## 时间复杂度为O(logN)
    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = int((first+last)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            first = mid+1
        else:
            last = mid - 1
    return first

b = searchInsert2([1,3,5,6], 7)

