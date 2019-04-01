# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:10:50 2019

@author: pengz
"""

'''
Given a list of words and two words word1 and word2, return the shortest distance 
between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
def shortestDistance(words, word1, word2):   ## Written by my own, using dict
    res = {}
    i = 0
    dist = len(words) 
    while i < len(words):
        if words[i] == word1:
            res[word1] = i
            change = True
        elif words[i] == word2:
            res[word2] = i
            change = True
        i = i+1
        if word1 in res.keys() and word2 in res.keys() and change:
            dist = min(dist,abs(res[word1]- res[word2]))
            change = False
    return dist

words1 = ["practice", "makes", "perfect", "coding", "makes"]        
a = shortestDistance(words1,word1 = "makes", word2 = "coding")   