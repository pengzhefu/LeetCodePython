# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:03:02 2019

@author: pengz
"""

'''
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, 
 return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
'''
def firstUniqChar(s: str) -> int:   ## Using dict then pass one time dict, the worst is O(2n)
    ret = -1
    ans = {}
    i = 0
    while i < len(s):
        if s[i] not in ans.keys():
            ans[s[i]] = [i]    ## using list to store the index
        else:
            ans[s[i]].append(i) 
        i += 1
    for k,v in enumerate(ans):
        if len(ans[v]) == 1:
            return ans[v][0]
    return ret
            
a = firstUniqChar('loveleetcode')

def firstUniqChar2(s:str) -> int:   ## The reason that this one faster is because using the inner func written in  C
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1