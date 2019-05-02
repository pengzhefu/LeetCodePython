# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 02:17:58 2019

@author: pengz
"""
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
'''
class Solution:
    def reverseVowels(self, s: str) -> str:  ## written by my own
        set_v = ('a','e','i','o','u','A','E','I','O','U')
        first = 0
        last = len(s)-1
        ret = ''
        tmp = []
        for i in range(0,len(s)):
            tmp.append(s[i])
        while first < last:
            while first< last and tmp[first] not in set_v:
                first = first+1
            while first < last and tmp[last] not in set_v:
                last = last-1
            if first < last:
                if tmp[first] in set_v and tmp[last] in set_v:
                    tmp[first],tmp[last] = tmp[last],tmp[first]
                first += 1
                last -=1
        for i in range(0,len(tmp)):
            ret += tmp[i]
        return ret