# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:51:57 2019

@author: pengz
"""

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

'''
def isValid(s: str) -> bool: ## written by my own, using stack, and the dict
    ret = []
    ans = {')':'(','}':'{',']':'['}
    i = 0
    while i < len(s):
        print(s[i])
        if s[i] not in ans:   ## 如果遇到opening braket, 就放进stack
            ret.append(s[i])
            i = i+1
        else:
            if len(ret) <1:   ## 要先判断stack里面有没有符号，如果都没有，直接return False
                return False
            else:
                tmp = ret[-1]   
                if ans[s[i]] == tmp:
                    ret.pop()
                    i = i+1
                else:
                    return False
    return ret == []
            