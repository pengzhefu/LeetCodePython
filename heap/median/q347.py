# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:23:53 2019

@author: pengz
"""
'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import collections
nums = [2,2,1,1,1,1,1,3,1,1,1]
count = collections.Counter(nums)   ## collection的counter可以直接生成排序好的dict
def topKFrequent1(nums: [int], k: int) -> [int]:  ## code by my own, idea from https://www.youtube.com/watch?v=lm6pBga98-w
                                                    ## time is O(n), space is O(n)
    if len(nums) <k:
        return None
    freqs = {} ## key是num, value是freq
    buckets = {} ## key是freq, value是num的list, buckets就是把所有同频率的数组合到了一起
    for num in nums:
        if num not in freqs:
            freqs[num] =1
        else:
            freqs[num] +=1
    max_freq = 1
    for key in freqs:   ## 确认最大频率, 还有就是形成buckets
        freq = freqs[key]
        if freq > max_freq:
            max_freq = freq
        if freq not in buckets:
            buckets[freq] = [key]
        else:
            buckets[freq].append(key)
    ret = []
    for i in range(max_freq,0,-1):   ## 然后从最大频率开始往下找，
        if i in buckets:
           ret += buckets[i]
        else:   ## 如果没有这个频率的数字就跳过
            continue
        if len(ret) >= k:
            return ret
    return ret


import heapq
#heap = []
#nums = [(1,2),(3,1),(4,1),(2,4),(3,8),(5,9)]
#for num in nums:
#    heapq.heappush(heap,num)
def topKFrequent2(nums: [int], k: int) -> [int]:  ## using minheap?, time is O(nlogk), space is O(n)
    if len(nums) <k:
        return None
    freqs = {} ## key是num, value是freq
    for num in nums:
        if num not in freqs:
            freqs[num] =1
        else:
            freqs[num] +=1
    heap  = []
    for key in freqs:
        heapq.heappush(heap,(freqs[key],key))  ## 要让minheap排序就要变成tuple
        if len(heap) >k:
            heapq.heappop(heap)
    ret = []
    for item in heap:
        ret.append(item[1])
    return ret
        


