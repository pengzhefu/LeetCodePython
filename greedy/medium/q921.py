# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:38:17 2019

@author: pengz
"""

'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', 
and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting 
string valid.

 

Example 1:

Input: "())"
Output: 1

Example 2:

Input: "((("
Output: 3

Example 3:

Input: "()"
Output: 0

Example 4:

Input: "()))(("
Output: 4

 

Note:

    S.length <= 1000
    S only consists of '(' and ')' characters.

这道题我理解的意思是, 就是给定一个字符串只有括号的, 然后你可以再任意位置插入任意符号，让他有效
有效的意思还是, ')'的数量等于'('的数量, 而且能够匹配
'''
def minAddToMakeValid(S: str) -> int:  ## inspired by https://www.youtube.com/watch?v=9hl2ssw5wgo, time O(n)
    num_open = 0  ## record the number of unmatched (
    num_close = 0 ## record the number of unmatched )
    for char in S:
        if char == '(':
            num_open +=1
        else:
            num_open -=1
        if num_open <0:   ## 如果(的个数小于0,变成了-1,说明这时候就是多出来的), 就让没有匹配的)的个数+1, 但是没匹配的(仍然是0
            num_open =0   ## 所以, 要让这个个数变回0
            num_close +=1
    return num_open+num_close

print(5//2)