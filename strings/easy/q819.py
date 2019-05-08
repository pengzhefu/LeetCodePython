# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:05:52 2019

@author: pengz
"""
'''
Given a paragraph and a list of banned words, return the most frequent word 
that is not in the list of banned words.  It is guaranteed there is at 
least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free 
of punctuation.  Words in the paragraph are not case sensitive.  
The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

 

Note:

    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph 
    may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.


'''
def mostCommonWord(paragraph: str, banned) -> str:   ## using dict, written by my own, time is O(m+l+m)
    res = {}  ## storing the result of passing paragraph
    i = 0
    while i < len(paragraph):
        tmp = ''
        if paragraph[i].isalpha() == False:  ## 从这个循环跳出来的时候, i在单词的第一个字符上了
#            print('not char')
            i = i+1
            continue
        while i < len(paragraph):    ## 这个循环去找一个完整的单词是什么
            if paragraph[i].isalpha() == True:
                tmp += paragraph[i]
                i = i+1
            else:
                break
        tmp = tmp.lower()
        if tmp in res:
            res[tmp] += 1
        else:
            res[tmp] = 1
#    return res
    for item in banned:
        if item in res:
            del res[item]
#    ret = sorted(res.items(), key = lambda item: item[1], reverse = True)   ## sort will spend more time
    ret = 0
    ans = ''
    for k in res:
        if res[k] > ret:
            ret = res[k]
            ans = k
    return ans
    

b = mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",banned = ["hit"])