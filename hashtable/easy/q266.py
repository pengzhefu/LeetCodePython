# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:31:08 2019

@author: pengz
"""

'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "carerac"
Output: true

'''
## 不需要在乎顺序，可以重新排列字符串的顺序，所以重点在于个数
def canPermutePalindrome(s: str) -> bool:   ## 这道题因为一开始没理解意思，所以看到了提示
                                            ## 思路是当长度为偶数的时候，需要每一个出现的不同的字符的个数都为偶数才能回文
                                            ## 当长度为奇数时，只有一个字符出现个数为奇数，其他都为偶数才行
    ret = {}
#    if len(s) % 2 == 0: ## 偶数时候,
    for char in s:
        if char not in ret.keys():
            ret[char] = 1
        else:
            ret[char] += 1
        if ret[char] == 2:
            del ret[char]   ## 达到第一次偶数了就删掉这个key
    if len(s) %2 == 0:
        return ret == {}
    else:
        return len(ret) == 1
#    else:
#        for char in s:
#            if char not in ret.keys():
#                ret[char] = 1
#            else:
#                ret[char] += 1
#            if ret[char] == 2:
#                del ret[char]
#        return len(ret) == 1
    
a = canPermutePalindrome('aab')