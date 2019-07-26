# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:55:00 2019

@author: pengz
"""

'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''
class Solution:
    def largestNumber1(self, nums: List[int]) -> str: ## https://www.jianshu.com/p/960cf375c40a, time is O(n^2)
        def compare(x,y):  ##重点在于怎么比较, 其实就是两两比较的时候,把两个拼起来, 进行比较, 然后传递比较
            res = int(x+y) - int(y+x)
            if res >=0:   ## 如果大于, 那就没必要换位
                return False
            else:
                return True
        
        tmplist = [str(num) for num in nums]
        for i in range(len(nums)):  
            for j in range(i,len(nums)):  ## 每结束一次这个循环，就是那个范围内的第一个是那个范围内的大的,
                                        ## 是先把最大的放到最前面, 然后是第二大的, 有点像插入排序
                if compare(tmplist[i],tmplist[j]):
                    tmplist[i],tmplist[j] = tmplist[j],tmplist[i]
        
        ret = ''
        for res in tmplist:
            ret += res
        if ret[0] == '0':
            return '0'
        else:
            return ret
        
from functools import cmp_to_key
class Solution2:  ## 用python3 内置的sort的比较办法
    def largestNumber(self, nums: List[int]) -> str:  ## http://www.pythontip.com/coding/report_detail/3116/
        tmplist = [str(num) for num in nums]
        tmplist.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        ret = ''.join(tmplist)
        if ret[0] == '0':
            return '0'
        else:
            return ret