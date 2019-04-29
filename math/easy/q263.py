# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:37:23 2019

@author: pengz
"""
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.

Note:

    1. 1 is typically treated as an ugly number.
    2. Input is within the 32-bit signed integer range: [−231,  231 − 1].
'''
## 这题没有想出来，看的答案
## 思路是就让这个数除以2或3或5(每一次都看能整除哪个，能一直整除的到最后会变成1)
## 如果中间有不能被这三个数任意一个整除的情况发生，那就说明不是，return false
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        while num > 1:
            if num % 2== 0:
                num = num //2
            elif num % 3 == 0:
                num = num //3
            elif num % 5 == 0:
                num = num //5
            else:
                return False
        return True