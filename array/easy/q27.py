# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:14:09 2019

@author: pengz
"""

"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
Subscribe to see which companies asked this question.
"""

def removeElement(nums, val):   ## Written by myself, and pass, but the time and space is not good
    geshu = len(nums) - 1
    i = 0
    while i <= geshu:
        if nums[i] == val:
            geshu -= 1
            nums.pop(i)
            continue
        else:
            i = i+1
        
    return len(nums)
    
a = removeElement([0,1,2,2,3,0,4,2], 2)

def removeElement2(nums: list, val: int) -> int:   ## idea from others, code written by myself
                                                    ## 这方法就是把所有的val都放到后面去
    i = 0
    length = len(nums)
    while i < length:    ## 当i == length的时候,说明从0到(length-1)这个范围内都没有val了,置换结束
        if nums[i] == val:
            nums[i], nums[length-1] = nums[length-1],nums[i]
            length = length - 1                   ## 记得一定要length-1，相当于把末尾往前提,下一个是val的放倒数第二个
                                                    ## 但是i不能动，因为可能换过来的还是val,要把这个val也放到后面
        else:
            i = i+1
    return length

def removeElement3(nums: list, val: int) -> int:  ## written by my own, maintain the original order
    res = len(nums)
    i = 0
    while i < res:
        if nums[i] == val:
            for j in range(i,res-1):
                nums[j] = nums[j+1]
            nums[res-1] = val
            res = res-1
            print(nums)
        else:
            i += 1
    return res
b = removeElement2([0,1,0,2,3,0,4,0], 0)
