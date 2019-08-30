# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:48:04 2019

@author: pengz
"""

'''
Given a string containing just the characters '(' and ')', find the length of the longest 
valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''
## https://www.youtube.com/watch?v=M1Vw5Tk1rw4 或者看笔记
def longestValidParentheses(s: str) -> int:
    ret = 0
    if len(s) <2:
        return ret
    leftmost = -1  ## 初始的leftmost值
    stack = []  ## 
    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                leftmost = i
            else:
                stack.pop()
                if len(stack) == 0:
                    ret = max(ret,i-leftmost)
                else:
                    ret = max(ret,i-stack[-1])
        i +=1
    return ret
    
    
    