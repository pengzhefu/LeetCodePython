# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:45:52 2019

@author: pengz
"""

'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
def findNthDigit(n: int) -> int:
    base = 0
    while n >0:    ## 先用base知道是几位数
        base += 1
        count = 9 * (10 ** (base-1))   ## the number of digits in every base
        length = count * base    ## 每次某位数的总长度，比如二位数就是 2*90
        tmp = n   ## 用tmp记录一下
        n = n - length
    start = 10 ** (base-1)    ## 这个长度的起始数
    num_pre = start + (tmp // base)-1   ## 然后获取离目标数最近的数，减1是因为从起始数开始的,(也有可能刚出结果小于起始数)
    rest = tmp % base    ## 算余数，看看是后面那一位数的哪一位
    if rest == 0:
        return num_pre % 10
    else:
        diff = base - rest
        num_last = num_pre + 1
        num_last = num_last // (10**diff)    ## 直接除以10^(差值)就行了，因为差值就是从末尾开始数需要去掉的位数
        return num_last % 10