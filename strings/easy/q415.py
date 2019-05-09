# -*- coding: utf-8 -*-
"""
Created on Wed May  1 03:38:47 2019

@author: pengz
"""

'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

'''
这道题关键就在于怎么获取用str表示的数字的大小，以及进位，可以用ord()函数帮助
'''
def addStrings(num1: str, num2: str) -> str:  ## method from others, code written by my own
    ret = ''
    carry = 0 ##用来表示进位
    i = len(num1)-1
    j = len(num2)-1
    while i >=0 or j >=0 or carry !=0:   ## 进位不为0的时候可能说明最前面需要补个1，循环也要继续
        if i>= 0:
            tmp1 = ord(num1[i]) - ord('0')
            i = i-1
        else:
            tmp1 = 0
        if j>=0:
            tmp2 = ord(num2[j])- ord('0')
            j = j-1
        else:
            tmp2 = 0
        tmp = tmp1+tmp2+carry
        ins = tmp % 10
        carry = tmp //10
        ret = str(ins)+ret
    return ret

a = addStrings(num1='1234',num2='8888')