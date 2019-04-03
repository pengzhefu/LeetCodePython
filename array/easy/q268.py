# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 01:14:46 2019

@author: pengz
"""

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement 
it using only constant extra space complexity?
'''
def missingNumber(nums):   ## 用的是数学方法，借鉴的, time complexity is O(n)
    sumnum = 0
    for num in nums:
        sumnum += num
    exp = int((0 + len(nums))*(len(nums)+1)/2)
    res = exp - sumnum
    return res
a = missingNumber([9,6,4,2,3,5,7,0,1])

## Another Solution, using bit manipulation,用了按位异或
def missingNumber1(nums):  ## time complexity is O(n)
    res = 0   ## 必须是用0
    for i in range(len(nums)+1):    ## 大概思想就是:用原本应该有的最大项(len(num)+1,也就是n)去和每一个原本完整的nums
                                    ## 的每一位异或,然后再和现在差一个的列表的异或,那么少的那一个就无法自己两个相同的
                                    ## 异或变0，就多出来了，0^n=n, n^n=0
                                    ## range(len(nums)+1) 应该是包含0...n, n = len(nums)
        res ^= i   ## 这些都是原本应该有的
    for num in nums:
        res ^= num
    return res
b = missingNumber1([9,6,4,2,3,5,7,0,1])