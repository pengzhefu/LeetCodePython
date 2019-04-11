# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:46:43 2019

@author: pengz
"""

'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a 
non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be 
separated by a single space.
'''


## 还有一种方法是，pattern是dict,str是个set,一定要两边都没有的才能添加进dict和set中，否则，返回false
'''
 所以其实是有两种情况返回false:
     1. pattern出现了已知的字符，但对应过去的str中和已经记录的不符
     2. patter出现了新的字符，但对应过去的str中出现的单词在之前已经出现过
     '''
def wordPattern(pattern: str, str: str) -> bool:  ## Written by my own, using two dicts
    list_str = str.split(' ')
    if len(pattern) != len(list_str):
        return False
    ans1 = {}
    ans2 = {}
    i = 0
    pat = True
    while i < len(pattern) and pat:
        if pattern[i] not in ans1.keys() and list_str[i] not in ans2.keys():   ## 如果一开始对于两边都是新的
            ans1[pattern[i]] = list_str[i]
            ans2[list_str[i]] = pattern[i]
            i = i+1
        else:   ## 然后保证两边都是对的，但其实比较一个就行了，因为最先添加的就是对的，所以保证其中一个在dict里的对应正确就行
                ## 如果其中有一个对应不正确，那就是直接不对了
                ## 这里用两个dict和if-else是为了避免dict中如果出现不存在的key的查询，会直接返回错误
                ## 这里的if-else是为了看究竟新的是在pattern中还是在str中
            if pattern[i] in ans1.keys():      ## 如果发现存在pattern的dict就有，
                if ans1[pattern[i]] != list_str[i]:   ## 但是和已经记录的情况不符
                    return False
                else:   ## 发现记录相符就行，直接往后继续看
                    i = i+1
            else:
                if ans2[list_str[i]] != pattern[i]:
                    return False
                else:
                    i = i+1
    return pat
    

a = wordPattern('abaa','dog cat dog dog')