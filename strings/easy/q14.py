# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:03:48 2019

@author: pengz
"""
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

'''

def longestCommonPrefix(strs) -> str:   ## written by my own, time is O(mn)
    ret = ''
    if len(strs) ==0:
        return ret
    elif len(strs) == 1:
        return strs[0]
    else:
        n = len(strs)   ## n是有几个组
        min_length = len(strs[0])  ## 求出里面最短的那个
        for item in strs:
            if len(item) < min_length:
                min_length = len(item)     
        i = 0
        while i < min_length:   
            tmp = strs[0][i]
            m = 0
            while m < n:
                if strs[m][i] == tmp:    ## 只要不相等，就直接退出
                    m = m+1
                else:
                    break
            if m == n:   ## 只有所有组都有这个字符，才能添加这个字符
                ret += tmp
            else:    ## 中间有一个达不到标准，就直接断了就行，因为是从头开始的
                break
            i = i+1
        return ret

def longestCommonPrefix2(strs) -> str:   ## idea from solutions, code written by myself， time is O(mn)
                                            ## 这方法就是一个一个比较，从头两个开始比较，一直比较到最后一个(如果ret一直不空)
    ret = ''
    if len(strs) ==0:
        return ret
    elif len(strs) == 1:
        return strs[0]
    else:
        i = 1   ## i is the index of items in strs list
        ret = strs[0]
        while i < len(strs):
            j = 0  ## is the index of string
            tmp = ret   ## 把上一次的结果赋给tmp, 用来做这一次的比较
            ret = ''    ## 结果还是输出到ret
#            print('ready to compare')
#            print('tmp is ',tmp)
#            print('the index for strs is ',i)
            while j < len(tmp) and j < len(strs[i]):
                if tmp[j] != strs[i][j]:
                    break
                else:
                    ret = ret + tmp[j]
                j = j+1
            if ret == '':
                break
            else:
                i = i+1
        return ret
    
def longestCommonPrefix3(strs) -> str:
    pass
                
a = longestCommonPrefix2(["dog","racecar","car"])