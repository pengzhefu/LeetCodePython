# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:36:36 2019

@author: pengz
"""
'''
Given two strings S and T, return if they are equal when both are typed into empty 
text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(M+N) time and O(1) space?
'''
## 这道题我又又又又没写出来！！！主要是要O(n)的time和O(1)的space
def backspaceCompare(S: str, T: str) -> bool:  ## method from solution, using list, space O(m+n), time O(m+n)
    ret_s = []
    ret_t = []
    for item in S:
        if item != '#':
            ret_s.append(item)
        else:
            if len(ret_s) != 0:   ## empty list can not pop
                ret_s.pop()   
    for item in T:
        if item != '#':
            ret_t.append(item)
        else:
            if len(ret_t) != 0:
                ret_t.pop()
    return ret_s == ret_t

def backspaceCompare2(S: str, T: str) -> bool:   ## other's solution, time O(m+n), space is O(1)
    i = len(S) - 1
    j = len(T) - 1        
    ci = 0  ## 把这个存#的也看成一个stack
    cj = 0
    
    while i >= 0 or j >= 0:
        while i >= 0:     ## if的顺序很重要！，而且没有continue， 先确定不是#了再往前移和拿掉#
            if S[i] == "#":   
                i -= 1
                ci +=1
            elif ci > 0:
                i -= 1
                ci -= 1
            else:    ## 这种情况是如果当前index指向的是字母，而且后头还没有跟着#
                break  
            
        while j >= 0:
            if T[j] == "#":
                j -= 1
                cj +=1
            elif cj > 0:
                j -= 1
                cj -= 1
            else:
                break
        if i < 0: 
            return j < 0            
        if j < 0: 
            return i < 0                
        if S[i] != T[j]: 
            return False
        i -= 1
        j -= 1             

    return True
        
a = backspaceCompare2('ab#c','ad#c')    
            