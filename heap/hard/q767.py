# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:20:31 2019

@author: pengz
"""

'''
Given a string S, check if the letters can be rearranged so that two characters that are 
adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

    S will consist of lowercase letters and have length in range [1, 500].
'''
'''
idea from https://www.youtube.com/watch?v=nUQTAtpyw3s
'''
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        numbs = {}
        heap = []  ## 用最大堆
        ret = ''
        if len(S) == 0:
            return ret
        if len(S) == 1:
            return S
        for  char in S:
            if char not in numbs:
                numbs[char] = 1
            else:
                numbs[char] += 1
        for key in numbs:
            if numbs[key] > (len(S)+1)/2:  ## 如果长度超过一半就肯定不行, 这里的长度记得一定要加一
                return ret
            heapq.heappush(heap,(-numbs[key],key))
        lastC = None   ## lastC的作用是解决有频率一样的字母的问题
        while len(heap) > 1:
            tmp1 = heapq.heappop(heap)[1]  ## 直接先找出最多的两个
            tmp2 = heapq.heappop(heap)[1]
            if tmp1 != lastC:   ## 如果拿出来的第一个和上一个放进去的不一样
                ret += tmp1
                ret += tmp2
                lastC = tmp2
            elif tmp1 == lastC and tmp2 == lastC:
                return ''
            else:   ## 如果拿出来的第一个和上一个放进去的一样, 那就用第二个
                ret += tmp2
                ret += tmp1
                lastC = tmp1
            ## 更新一下他们的值，重新放入max heap
            numbs[tmp1] -=1
            if numbs[tmp1] >0:
                heapq.heappush(heap,(-numbs[tmp1],tmp1))
            numbs[tmp2] -=1
            if numbs[tmp2] >0:
                heapq.heappush(heap,(-numbs[tmp2],tmp2))
        if len(heap) >0:  ## 最后剩的那个, 虽然我加了判断条件, 但其实可以直接加上
            if heap[0][1] != lastC:
                ret += heap[0][1]
            else:
                return ''
        return ret
            
        
            
            
            
        
        