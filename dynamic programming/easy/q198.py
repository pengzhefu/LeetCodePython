# -*- coding: utf-8 -*-
"""
Created on Tue May  7 02:24:57 2019

@author: pengz
"""

'''
You are a professional robber planning to rob houses along a street. Each 
house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

'''
def rob(nums: list) -> int:  ## written by my own, using similar method as q70 and maxsum, time O(n), space O(n)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        ret = [0] *len(nums)
        ret[0] = nums[0]
        ret[1] = max(nums[0],nums[1])
        n = len(nums)
        for i in range(2,n):
            ret[i] = max(ret[i-2]+nums[i],ret[i-1])  
        return ret[n-1]

def rob2(nums: list) -> int:  ## an optimization, space O(1), time O(n)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
#        ret = [0] *len(nums)
        f1 = nums[0]  ## f1就是离当前的隔一个的max value
        f2 = max(nums[0],nums[1])   ## f2就是紧靠当前的max value
        n = len(nums)
        for i in range(2,n):
            f3 = max(f1+nums[i],f2)
            f1 = f2  ## 进行更新
            f2 = f3  ## 进行更新
        return f2    ## 最后return的是f2,可以防止只有两个的时候的情况