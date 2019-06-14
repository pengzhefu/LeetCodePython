# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 01:06:56 2019

@author: pengz
"""

'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, 
then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.
'''
import heapq
def topKFrequent(words:[str], k: int) -> [str]:
    freqs = {}  ## key is the word, and the value is its times
    for word in words:
        if word not in freqs:
            freqs[word] = 1
        else:
            freqs[word] +=1
    heap = []  
    for key in freqs:
        heapq.heappush(heap,(-freqs[key],key))   ## 因为要按顺序从大到小, 所以要加个负号变成最大堆, q347没有一定要求顺序
    ret = []
    i = 0
    while i < k:
        ret.append(heapq.heappop(heap)[1])
        i = i+1
    return ret
