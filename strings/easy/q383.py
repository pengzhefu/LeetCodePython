# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 03:23:05 2019

@author: pengz
"""
'''
 Given an arbitrary ransom note string and another string containing letters from 
 all the magazines, write a function that will return true if the ransom note can be 
 constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters. 
'''
def canConstruct(ransomNote: str, magazine: str) -> bool:  ## using dict, written by my own
    ret = {}
    for item in magazine:
        print(ret)
        if item not in ret.keys():
            ret[item] =1
        else:
            ret[item] +=1
    for char in ransomNote:
        if char in ret:
            if ret[char] == 0:
                return False
            else:
                ret[char] -=1
        else:
            return False
    return True

a = canConstruct("bbac",'ccccaaab')