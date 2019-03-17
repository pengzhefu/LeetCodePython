# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 01:16:03 2019

@author: pengz
"""


"""
Given a sorted array, remove the duplicates in place such that each element appear 
only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
Subscribe to see which companies asked this question.
"""

def removeDuplicates(nums): ## Written by my own, exceed time limits,时间复杂度估计为O(n^n)
    stop = False
    while not stop:
        for i in range(len(nums)):
            if i == len(nums) - 1:
                stop = True
                break
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                break
    return len(nums)


#a = removeDuplicates([0,0,1,1,1,2,2,3,3,4])

def removeDuplicates2(nums): ## 就是用个双指针，一个指针(i)往后遍历, 一个指针index记录目前最新的不重复的那个数的值，
                                ## 然后一旦发现和现在的不一样了，就把那个放到现在最新的不重复的数的位置+1的位置，成为最新
                                    ##时间复杂度为O(n)
    if not nums:
        return 0
    index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:  ## 发现有新的(不一样)的了，就要把他放到后面一个
            index = index + 1
            nums[index] = nums[i]

    return index + 1 ##(index+1)才是最后的长度
b = removeDuplicates2([0,0,1,1,1,2,2,3,3,4])