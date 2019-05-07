# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 01:49:28 2019

@author: pengz
"""

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

'''
def countAndSay(n: int) -> str:   ## method from others, 
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    current = '11'
    for x in range(1,n-1):   ## 因为已经直接规定了n=1和n=2的情况，所以当n大于3的时候，需要进行n-2次循环
        count = 1   ## 开始进行数数
        ret = ''
        for j in range(len(current)):   ## 开始进行数数
            if j < len(current)-1:
                if current[j] == current[j+1]:   ## 如果这一个和后一个相等，那么就count+1，就相当于连续的数量加一
                    count = count + 1
                else:
                    ret += str(count) + current[j]
                    count = 1
            else:
                ret += str(count) + current[j]
        current = ret    ## 让current变成当前得到的,然后继续进行
    return ret
                
def countAndSay2(n: int) -> str:   ## method from others, recursive version
    if n == 1:
        return '1'
    else:
        lastone = countAndSay2(n-1)
        new = ''
        count = 1
        for j in range(len(lastone)):   ## 因为是递归，所以就不需要再用到多一层for循环从2开始算，只要计算上一次的就行
            if j != len(lastone) -1:
                if lastone[j] == lastone[j+1]:
                    count += 1
                else:
                    new += str(count) + lastone[j]
                    count = 1
            else:
                new += str(count) + lastone[j]
        return new
            
            