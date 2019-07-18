# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 01:37:01 2019

@author: pengz
"""

'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method 
signature.
'''
def merge(intervals: [[int]]) -> [[int]]:   ## code and idea from my own, time is O(nlogn)
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals, key = lambda item:item[0])  ## 按开始时间排序
    ret = []
    start = intervals[0][0]
    end = intervals[0][1]
    i = 1
    while i < len(intervals):  ## 从第二个开始遍历
        if intervals[i][0] > end:
            ret.append([start,end])
            start = intervals[i][0]
            end = intervals[i][1]
        elif intervals[i][0] <= end:
            end = max(intervals[i][1],end)
        i =i+1
    ret.append([start,end])  ## 循环结束以后要记得一定添加一次, 因为如果到最后一个的话在循环里是无法添加的
    return ret
        

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[2,4],[1,10],[3,6],[0,7],[1,7]]
intervals1 = [[1,4],[4,5]]
b = merge(intervals2)


import heapq
def merge1(intervals: [[int]]) -> [[int]]: 
    ret = []
    if len(intervals) == 0:
        return ret
    heap = []
    for interval in intervals:
        heapq.heappush(heap,interval)
    min_start, max_end = heapq.heappop(heap)
    while heap:
        start, end = heapq.heappop(heap)
        if start > max_end:
            ret.append([min_start,max_end])
            min_start = start
            max_end = end
        elif start <= max_end:
            max_end = max(end,max_end)
    ret.append([min_start,max_end])## 循环结束以后要记得一定添加一次, 因为如果到最后一个的话在循环里是无法添加的, 或者最后的max_end的结果
    return ret

ret = merge1(intervals2)