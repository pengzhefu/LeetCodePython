# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:26:52 2019

@author: pengz
"""
'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution():
    def addBinary(self, a: str, b: str) -> str:   ## method from an array question
        num_a = int(a)
        num_b = int(b)
        res = str(num_a+num_b)
        nums = []
        for i in range(0,len(res)):
            nums.append(int(res[i]))
        ret = ''
        i = len(nums)-1
        while i >= 1:
            if nums[i] == 0 or nums[i] == 1:
                ret = str(nums[i]) + ret
            elif nums[i] == 2:
                nums[i-1] += 1
                ret = '0' + ret
            elif nums[i] == 3:
                nums[i-1] += 1
                ret = '1' + ret
            i = i-1
        if nums[0] == 1 or nums[0] == 0:
            ret = str(nums[0]) + ret
        elif nums[0] == 2:
            ret = '10' + ret
        elif nums[0] == 3:
            ret = '11' + ret
        return ret
    
    def addBinary2(self, a: str, b: str) -> str:   ## a recursive method, not by my own
        if len(a)==0: 
            return b
        if len(b)==0: 
            return a
        if a[-1] == '1' and b[-1] == '1':    ## 两个都是1,那就先添0，然后前面的数的结果要加1，所以是调了两次函数本身
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':   ## 两个都0，添0，然后往前走就行了
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:                   ## 两个是1或0，那就添1，然后往前走
            return self.addBinary(a[0:-1],b[0:-1])+'1'
    
