# -*- coding: utf-8 -*-
"""
Created on Sat May 25 02:06:59 2019

@author: pengz
"""

'''
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

medium, 
idea 1 from https://www.youtube.com/watch?v=0roQnDBC27o
按我理解的话，关键点就在于，同一个时段内如果有超过一个起始时间，那么要用的房间数就要加一
因为移动一次end，相当于腾出来一间房间，
'''
import heapq
class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if len(intervals) == 0:
            return 0
        start = []
        end = []
        for meeting in intervals:
            start.append(meeting[0])
            end.append(meeting[1])
        start.sort()
        end.sort()
        i = 1  ## the index for start time, 从1开始是因为start[0]肯定小于end[0], 但是要找的是大于start[0]但小于end[0]的
        j = 0  ## the index for end time
        ret = 1   ## 至少需要一个, 如果列表不为0
        while j < len(end)-1:  ## 最大的那个end可以不用管
            if i < len(start):
                if start[i] < end[j]:
                    ret = ret+1
                    i = i+1
                else:   ## 如果start的大于当前end的了,
                    j =j+1   ## 首先要先把end往后移一个
                    i = i+1  ## 移动start是因为要找在这个区间里，比这个最小的start要大的仍然小于移动后的end的个数，所以start
                            ## 跟着移动， 可以这么理解：移动以后的end可以比这个start大了，但是只有一个start小于这个end的话，
                            ## ret不加1, 那么start就往后移1,大于这个end了,那么end也要往后移，直到有至少两个start小于当前end
            else:
                break
        return ret
    
    def minMeetingRooms2(self, intervals: [[int]]) -> int: ## time is O(nlogn), space is O(n)
        ## idea from https://www.youtube.com/watch?v=wB884_Os58U
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[0])  ## 先把输入的数按照起始时间排序
        heap = []
        heapq.heappush(heap,intervals[0][1])  ## 把最早开始的会议的结束时间输入
        i = 1
        # print(heap[0])
        while i < len(intervals):
            if intervals[i][0] >= heap[0]:   ## 如果下一个要开始的会议的开始时间，晚于当前heap最早的结束时间, 
                                            ## 就更新那个的结束时间
                tmp = heapq.heappop(heap)
                heapq.heappush(heap,intervals[i][1])
            else:   ## 如果早于，就要添加
                heapq.heappush(heap,intervals[i][1])
            i = i+1
        return len(heap)  ## heap的大小就是会议室数量
            