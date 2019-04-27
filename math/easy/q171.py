# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 05:17:01 2019

@author: pengz
"""

'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        base = 0
        i = len(s)
        ret = 0
        while i > 0:
            val = ans.index(s[i-1]) + 1
            ret += val * (26**base)
            i = i -1
            base = base + 1
        return ret