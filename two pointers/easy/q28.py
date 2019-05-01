# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 00:59:27 2019

@author: pengz
"""

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().
'''
def strStr(haystack: str, needle: str) -> int:   ## written by my own, exceed time limit, time is O(mn)
    ret = -1
    if len(haystack) < len(needle):
        return ret
    if len(needle) == 0:
        return 0
    i = 0   ## pointer for haystack
    while i < len(haystack):
        j = 1  ## pointer for needle
        if haystack[i] != needle[0]:
            i += 1
        else:
            tmp = i
            tmp += 1
            while tmp < len(haystack) and j < len(needle):
                if haystack[tmp] == needle[j]:
                    tmp += 1
                    j+=1
                else:
                    break
            if j == len(needle):
                return i
            else:
                i += 1
    return ret


def strStr2(haystack: str, needle: str) -> int:   ## method from others, 其实可以不用看全部！发现长度不够直接跳出就好了啊！
                                                    ## time is O((m-n)*n)
    if len(needle) == 0:
        return 0
    for i in range(0,len(haystack)-len(needle)+1):  ## i is the pointer for haystack
        j = 0   ## j is the pointer for needle
        while j < len(needle) and haystack[i+j] == needle[j]:
            j += 1
        if j == len(needle):
            return i
    return -1
            
def strStr3(haystack: str, needle: str) -> int:   ## the best method, from others, still O((m-n)n)
    for i in range(0,len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

def strStr4(haystack: str, needle: str) -> int:   ## try using KMP, time is O(m+n), space is O(n)
                                                    ## written by my own
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    table = getNext(needle)
    i = 0   ## pointer for haystack
    j = 0   ## pointer for needle
#    while i < len(haystack) and j < len(needle):         ## this method not by my own
#        if haystack[i] == needle[j]:   ## 出现相等的情况
#            i += 1
#            j += 1
#            if j == len(needle):   ## 如果这时候j都已经走完了，就说明有，就输出i-j就是目标值
#                return i-j
#        else:   ## 如果不相等
#            if j == 0:
#                i += 1
#            else:    ## 如果这时候j还没有到0，那么haystack不需要移动，i不需要移动
#                j = table[j-1]
    while i < len(haystack):      ## the code written by my own
            if haystack[i] != needle[j]:
                if j == 0:   ## KMP有一点不同,就是如果needle的index没有到0, haystack的index不能移动,停在不相等的那个点上就行
                    i += 1
                else:
                    j = table[j-1]
            else:
                pass_j = j
                tmp = i+1
                j += 1
                while tmp < len(haystack) and j < len(needle) and haystack[tmp] == needle[j]:
                    tmp += 1
                    j += 1
                if j == len(needle):
                    return i - pass_j
                else:
                    j = table[j-1]
                    i = tmp
    return -1

def getNext(s:str) -> list: ## find the next arraylist for substring, written by my own, and its correct
    ret = [0] * len(s)
    i = 1  ## suffix pointer
    j=0   ## prefix pointer
    while i < len(s):    ## i只扫一遍,每一遍都一定会有结果
        if s[i] == s[j]:
            ret[i] = j+1
            j = j+1
        else:
            if j == 0:
                ret[i] = 0
            else:
                while j >0 and s[i] != s[j]:   ## 不相等的时候,就要替换j的数值,跳出条件是相等了或者j到0了
                    j = ret[j-1]       ## 注意移动的是j，是前缀！不是后缀
                if s[i] == s[j]:   ## 如果相等，就算到0了，也是 val = j+1
                    ret[i] = j+1
                    j += 1    ## 如果match了j就一定要加一！
                else:    ## 如果一直不相等，而且到了j=0跳出，就直接为0
                    ret[i] = 0
        i = i+1
    return ret
#a = getNext('ababcaabc')
b = strStr4("mississippi","issip")
a = strStr4('hello','ll')
d = strStr4('ababaabbbbababbaabaaabaabbaaaabbabaabbbbbbabbaabbabbbabbbbbaaabaababbbaabbbabbbaabbbbaaabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaabbbabb','abbabbbabaa')
#c = create_next('ababcaabc')

a1 = getNext('abbabbbabaa')