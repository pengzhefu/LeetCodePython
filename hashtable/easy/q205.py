# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:48:33 2019

@author: pengz
"""

'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
'''
def isIsomorphic(s: str, t: str) -> bool:   ## Two, all written by my own, perfer the later one
#    iso = False
#    i = 0
#    ds = {}
#    dt = {}
#    while i < len(s):
##        char = s[i]
#        if s[i] not in ds.keys() and t[i] not in dt.keys():
#            ds[s[i]] = t[i]
#            dt[t[i]] = s[i]
#        elif s[i] not in ds.keys() and t[i] in dt.keys():
#            break
#        elif s[i] in ds.keys() and t[i] in dt.keys():
#            if ds[s[i]] == t[i] and dt[t[i]] == s[i]:
#                i = i+1
#                continue
#            else:
#                break
#        elif s[i] in ds.keys() and t[i] not in dt.keys():
#            break
##        print(ds)
#        i += 1
#    if i == len(s):
#        iso = True
#        return iso
#    else:
#        return iso
    iso = False
    i = 0
    ds = {}  ## Note the corresponding letter in t
    dt = {}  ## Note which letter is used
    while i < len(s):
        if s[i] not in ds.keys():   
            if t[i] not in dt.keys():   ## if there is a new letter in s, it should be new in both s and t
                ds[s[i]] = t[i]
                dt[t[i]] = 'used'
            else:
                break
        else:
            if ds[s[i]] == t[i]:  ## if there is an old letter in s, the corresponding letter in t should be the same
                i = i+1
                continue
            else:
                break
        i = i+1
    if i == len(s):
        iso = True
        return iso
    else:
        return iso
a = isIsomorphic("paper","title")