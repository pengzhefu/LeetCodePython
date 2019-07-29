# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 00:26:38 2019

@author: pengz
"""
'''
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

import bisect
data = []
a = bisect.bisect_left(data,5)

## https://blog.csdn.net/qq_28327765/article/details/84674868 方法二

def countSmaller(nums: [int]) -> [int]:  ## 用二分搜索法
    ret = [0] * len(nums)
    tmp = []
    for i in range(len(nums)-1, -1,-1):
        ret[i] = bisect.bisect_left(tmp,nums[i])  ## 这个其实是先看出nums[i]在tmp中如果从左开始插入, 会在哪个index插入
                                                ## 返回的值其实就相当于, 这个tmp的list中有几个小于要插入的nums[i], 但
                                                ## 其实nums[i]不会插入tmp中
        bisect.insort(tmp,nums[i])   ## 这一步就要插入, 实际上是会按照从小到大的顺序排序
    return ret


def countSmaller1(nums: [int]) -> [int]:
    ret = [0] * len(nums)
    
    return ret
