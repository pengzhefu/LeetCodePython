# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:44:24 2019

@author: pengz
"""
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:   ## using split func, written by my own
        list1 = s.split(' ')
        print(list1)
        if len(list1) >= 1:
            for i in range(len(list1)-1,-1,-1):
                if len(list1[i]) >=1:
                    return len(list1[i])
            return 0
        else:
            return 0
        
def lengthOfLastWord2(s: str) -> int:   ## using two pointers, written by my own
    ret = 0
    i = len(s) -1
    while i>= 0:
        if s[i] == ' ':   ## 跳过末尾的所有空格
            i = i-1
            continue
        if i != 0:    ## 找到第一个字符，然后如果这个字符不是首位
            for x in range(i,-1,-1):   ## 用for循环往前数，
                if s[x] != ' ':   ## 如果不是空格，就加一
                    ret = ret+1
                else:   ## 在for循环中，如果找到的已经不是空格了，直接break输出
                    break
            return ret
        else:      ## 如果找到的第一个字符是首位，直接返回1
            ret = ret+1
            return ret
    return ret

a = lengthOfLastWord2("a")
            
                