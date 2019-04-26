# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:32:32 2019

@author: pengz
"""

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this 
problem, assume that your function returns 0 when the reversed integer overflows.
'''
def reverse(x: int) -> int:   ## written by my own, using str 
    if x > 2147483646 or x < -2147483647:
            return 0
    tmp = str(abs(x))
    ret = ''
    if x>=0:
        for i in tmp:
            ret = i+ ret
        if int(ret) > 2147483646:
            return 0
        else:
            return int(ret)
    else:
        i = 0
        while i < len(tmp):
            ret = tmp[i] + ret
            i += 1
        ret = 0 - int(ret)
        if ret < -2147483647:
            return 0
        else:
            return ret

def reverse2(x: int) -> int:   ## written by my own, more mathematic
    tmp = abs(x)
    i = 1
    ## 首先找出这个数一共几位
    while tmp % (10*i) != tmp:
        i = i * 10
#    print(i)
    ans = 0
    num = 10
    while i >= 1:   ## 然后把这个数每次和10相除的余数找出来，就是每一位的数,大于等于1就是一直算到个位就行了
        last = tmp % num   ## 通过和10相除找余数来找每一位
        ans += last * i   ## 每次都要记得乘相应位数
        tmp = int(tmp/10)   ## 找完以后记得把这个数也要除以10，取整数部分
        i = int(i/10)
    if x >0:
        if ans > 2147483646:
            return 0
        else:
            return ans
    else:
        if (0-ans) < -2147483647:
            return 0
        else:
            return (0-ans)
            
'''
To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.

//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;

Luckily, it is easy to check beforehand whether or this statement would cause an overflow.

To explain, lets assume that rev\text{rev}rev is positive.
'''
def reverse3(x: int) -> int:   ## method from solution, and code written by my own, time is O(logn)
    tmp = abs(x)
    ret = 0
    ## 这方法就是不找位数了,先从个位数开始变,每加多一位就把之前的结果乘以10然后加上取到的余数(要加的位)
    while tmp > 0:    ## 注意限制条件,应该是要大于0
       ret = ret * 10 + (tmp % 10)
       tmp = tmp // 10   ## 这是除取整的方法
    if x >=0:
        return ret
    else:
        return 0-ret
a = reverse3(-67)