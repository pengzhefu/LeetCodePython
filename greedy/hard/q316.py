# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 02:42:41 2019

@author: pengz
"""
'''
Given a string which contains only lowercase letters, remove duplicate letters so that every \
letter appear once and only once. You must make sure your result is the smallest in lexicographical 
order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"

Example 2:

Input: "cbacdcbc"
Output: "acdb"

'''

'''
code written by my own, idea inspired by https://www.youtube.com/watch?v=SrlvMmfG8sA
'''
def removeDuplicateLetters(s: str) -> str:  ##字典序是根据两个字符串第一个不同的字符决定
    ret = []
    used = {}  ## 记录这个字符是否已经出现在了最后答案中，
    count = {}  ## 记录每个字符的出现次数
    for char in s:  ## 先遍历第一遍, 找出个数
        if char not in count:
            count[char] = 1
        else:
            count[char] +=1
    # print(count)
    for char in s:   ## 第二遍遍历, 开始添加答案
        if len(ret) == 0:   ## 如果此时什么都没有, 先添加
            ret.append(char)
            count[char] -=1    ## 个数要减1
            used[char] = True  ## 然后标记为已经用过了
        else:
            if char > ret[-1] and char not in used:  ## 如果要添加的是目前答案最后一位的后面的字母，而且没用过，就直接添加
                ret.append(char)
                count[char] -=1
                used[char] = True
            elif char < ret[-1] and char not in used:   ## 如果要添加的是当前答案最后一位的前一位字母
                while len(ret) >0 and char < ret[-1] and count[ret[-1]] > 0:  ## 如果答案的最后一个字母在后面还有，
                                                                    ## 也就是count>=1, 还能添加，那么就删掉, 直到
                                                                    ## 答案变成空或者答案的最后一位再要添加的字母之前
                                                                    ## 或者这个答案的最后一位在后面无法添加了,count=0了
                    tmp = ret.pop()
                    del used[tmp]
                ret.append(char)
                used[char] = True
                count[char] -=1
            elif char in used:   ## 如果发现是已经用过的，
                count[char] -=1  ## 那么只让个数减1，其他什么都不操作
        # print(ret)
    return ''.join(ret)
                