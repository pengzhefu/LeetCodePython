# -*- coding: utf-8 -*-
"""
Created on Thu May 23 00:24:16 2019

@author: pengz
"""

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.

hard

思路:遇到 '(' 就把之前的结果和符号push进stack. 遇到')'就把 当前结果*stack中的符号 再加上stack中之前的结果.
代码参考:https://blog.csdn.net/xudli/article/details/46554835 
'''
def calculate(s: str) -> int:  ## code written by my own
    stack1 = []  ## 用来存当前结果
    stack2 = []  ## 用来存离这个符号最近的符号
    ret = 0  ## final result
    sign = 1
    res = 0  ## temp result
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i = i+1
            continue
        elif s[i].isdigit():
            while i < len(s) and s[i].isdigit():   ## 一直算完整个数字
                res =  10*res + int(s[i])  ## 之所以要用10就是要算多位数, 比如112, 就是 10*0 +1 = 1, 10*1 + 1=11, 10*11+2 =112
                i =i+1
            ret += sign*res
            res = 0
            continue    ## 这里的continue是必须的,不然就会跳过这个非数字符号，因为跳出这个小while循环的时候,已经不在数字上了
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack2.append(sign)  ## 先把距离最近的符号存进去
            stack1.append(ret)   ## 然后把目前算出来的结果先放进去，因为括号总是跟在加减号的后面
            ret = 0  ## 要让ret变成0, 因为之前的已经存进去了, 要重新算这个括号里面的结果
            sign = 1 ## 符号也要重置，括号后的总是正数
        elif s[i] == ')':
            ret = ret *stack2.pop() + stack1.pop()  ## 把刚刚算出来的结果*符号然后和之前存下来的结果加和
            sign = 1  ## 算完一次以后，符号要重置
        i = i+1
    return ret

a = calculate('  6-(4+(2+3))')

def calculate3(s):   ## other's solution, faster
    ret = 0  ## final result
    sign = 1
    res = 0  ## temp result
    stack1 = []  ## 存结果的
    stack2 = []  ## 存符号的
    for char in s:
        if char == ' ':
            continue
        elif char.isdigit():
            res = 10*res + int(char)   ## 124： 10*0+1=1， 10*1+2 = 12， 10*12+4=124
        elif char == '+':
            ret += res*sign   ## 遇到加减号的时候，把刚刚的数字加上
            sign = 1
            res = 0    ## 然后要把tmp result的暂时清零
        elif char == '-':
            ret += res*sign
            sign =-1
            res = 0
        elif char == '(':
            stack1.append(ret)
            ret = 0     ## 遇到括号以后，当前结果要先归零，然后算完以后的再加
            stack2.append(sign)
            sign = 1
        elif char == ')':
            ret += res*sign   ## 先把最里面的括号里面的结果得出来
            res = 0    ## 
            ret = stack2.pop()*ret   ## 先乘以这个括号的正负
            ret = stack1.pop() + ret  ## 然后再加上括号之前的值
    ret += res*sign   ## 最后要再加一遍最后的数字
    return ret

c = calculate3('6-(4+(2+3))')
            