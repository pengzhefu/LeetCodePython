# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:53:51 2019

@author: pengz
"""

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.

'''
def calculate(s: str) -> int:
    s = s.strip()
    stack1 = []  ## 存之前的result
#    ret = 0 ## final result
    res = 0 ## temp result
    sign = '+'  ## previous sign
    for i,char in enumerate(s):  ## 用到enumerate是因为还要处理等式中最后一个数字
        if char == ' ':
            continue
        if char.isdigit():
            res = 10*res + int(char)
        if i == len(s)-1 or char == '+' or char == '-' or char == '*' or char == '/':
            ## 如果i是最后一位了, 还要处理一下最后一个数字
            if sign == '+':
                stack1.append(res)
                res =0
            elif sign == '-':
                stack1.append(-res)
                res =0
            elif sign == '*':
                tmp = stack1.pop()
                stack1.append(tmp*res)
                res =0
            elif sign == '/':
                top = stack1.pop()
                if top < 0:  ## 如果小于0
                    stack1.append(int(top / res))
                else:
                    stack1.append(top // res)
                res =0
            sign = char
            
    return sum(stack1)

b = calculate("2*(5+5*2)/3+(6/2+8)")