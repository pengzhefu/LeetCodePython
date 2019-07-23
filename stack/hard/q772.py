# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:17:51 2019

@author: pengz
"""
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and 
closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the 
range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
'''
## https://medium.com/@CalvinChankf/solving-basic-calculator-i-ii-iii-on-leetcode-74d926732437
def calculate3(s):   ## other's solution, time is O(n^2),
    if len(s) ==0:
        return 0
    stack = []
    sign = '+'  ## previous sign
    num =0  ## tmp result
    i =0  ## the index of s
    while i <len(s):
        c = s[i]
        if c.isdigit():
            num = 10*num + int(c)
        if c == '(':  ## 遇到相应的 ")"
            # find the corresponding ")"
            pCnt = 0
            end = 0
            clone = s[i:]
            while end < len(clone):
                if clone[end] == '(':
                    pCnt += 1
                elif clone[end] == ')':
                    pCnt -= 1
                    if pCnt == 0:
                        break
                end += 1
            # do recursion to calculate the sum within the next (...)
            num = self.calculate(s[i+1:i+end])
            i += end
            
        if i == len(s)-1 or (c == '+' or c == '-' or c == '*' or c == '/'):  ## 这部分是CalculatorII
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1]*num
            elif sign == '/':
                stack[-1] = int(stack[-1]/float(num))
            sign = c
            num = 0
        i +=1
    return sum(stack)