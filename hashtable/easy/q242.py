# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:26:41 2019

@author: pengz
"""

'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

'''
所谓 anagram, 就是两个词所用的字母及每个字母的个数都是一样的，但是，字母的位置（可以）不一样。
比如 abcc 和 cbca 就是 anagram.
'''

## 还有更好的方法是对两个字符串进行排序，只要排序完的结果相等就是anagram
def isAnagram(s: str, t: str) -> bool:  ## Using dict, written by my own
    ana = False
    ds = {}
    if len(s) != len(t):
        return ana
    i = 0
    while i <len(s):
        if s[i] not in ds.keys():
            ds[s[i]] = 1   ## 记录出现次数就行
        else:
            ds[s[i]] += 1
        i = i+1
    for char in t:
        if char not in ds.keys():
            return ana
        else:          ## 遍历t, 有一个，就减去一次次数
            ds[char] -= 1
            if ds[char] == 0:   ## 到0了就删掉
                del ds[char]
    if ds == {}:    ## 如果都为0都删掉了，就说明是一样的
        ana = True
        return ana
    return ana
print(isAnagram('ab','ab'))
