# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 01:21:46 2019

@author: pengz
"""

'''
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations 
for every word following rules below.

    1.Begin with the first character and then the number of characters abbreviated, which followed by the 
    last character.
    2.If there are any conflict, that is more than one words share the same abbreviation, a longer prefix 
    is used instead of only the first character until making the map from word to abbreviation become unique. 
    In other words, a final abbreviation cannot map to more than one original words.
    3.If the abbreviation doesn't make the word shorter, then keep it as original.

Example:

Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

Note:

    Both n and the length of each word will not exceed 400.
    The length of each word is greater than 1.
    The words consist of lowercase English letters only.
    The return answers should be in the same order as the original array.
'''
## code from https://leetcode.com/problems/word-abbreviation/discuss/318318/python3-easy-solution-beats-92
from collections import defaultdict
def wordsAbbreviation(words: [str]) -> [str]:
    groups = defaultdict(list)  ## 里面这个list是说明value的基本形式就是list, 如果是单个的话也是list形式保存
    for i, w in enumerate(words):
        groups[(w[0], w[-1], len(w))].append((i, w))  ## 所以这里采用上append
    ## 所以groups的key是这个word的(首字符,尾字符,长度), value是相应的单词的index和他本身
    ret = [word[0]+str(len(word)-2)+word[-1] if len(word)>3 else word for word in words]  ## 先进行粗略缩写
    def abbreviate(group,start,leng):## the words in tuple(index+word), start char, the length of word
        def trim(group, prefix):  ## prefix是缩写以后的前缀长度
            if prefix >= leng - 2:  ## 如果prefix过长
                for i, w in group:  ## i,w分别是index, word
                    ret[i] = w
            elif len(group) == 1:  ## 如果进行一次trim以后, 没有重复了,也就是value的个数变为1
                i, w = group[0]
                if prefix >= leng - 2: ret[i] =  w  ## 如果prefix过长
                else:
                    ret[i] = w[:prefix] + str(leng - prefix - 1) + w[-1]
            else:   ## 这个是最关键的一步, 要进行trim
                prefix += 1  ## 先说明prefix长度要增加了,
                dup = defaultdict(list)  ## 新建一个dup, 用来看新的prefix会不会还重复
                for i,w in group:
                    dup[w[prefix-1]].append((i, w))  ## 新的dup的key只有新的前缀了, 只要这个不一样就行
                for g in dup.values():
                    trim(g, prefix)  ## 然后再对trim以后的每一个进行检验
                
        if len(group) <=1:  ## 如果只有一个, 没必要trim
            return 
        else:
            trim(group,1)
    for key, group in groups.items():
        abbreviate(group,key[0],key[2])
    return ret

a, b = wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])
