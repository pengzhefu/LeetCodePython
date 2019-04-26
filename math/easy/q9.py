# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:47:39 2019

@author: pengz
"""

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the 
same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
'''
def isPalindrome(x: int) -> bool:   ## reverse the num, written by my own, similar as 17
    if x <0:
        return False
    elif x >= 0 and x <= 9:
        return True
    else:
        up = 100  ## 首先获取位数,这里选100因为至少是两位数
        while x % up != x:
            up = up * 10
        up = int(up/10)
        tmp = x
        res = 0 ## 开始进行倒转
        while up >= 1:   ## 一直进行到个位数:
            num = tmp % 10
            res += num * up
            tmp = int(tmp/10)
            up = int(up/10)
        return res == x

def isPalindrome2(x: int) -> bool: ## idea from q7 method3, code written by my own
    if x <0:
        return False
    else:
        tmp = x
        ret = 0
        while tmp >0:     ## 这个循环条件很重要,因为当只剩个位数时候， 除以10，得到的商就是0，其实就循环完了
            ret += ret*10 + (tmp%10)
            tmp = tmp//10
        return tmp == x