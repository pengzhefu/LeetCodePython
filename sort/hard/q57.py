# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:04:34 2019

@author: pengz
"""

'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition 
to get new method signature.
'''
a = [[1,3],[6,9]]
b = [0,3]
def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:  ## code and idea from my own, time is O(n)
    ret = []
    i = 0
    if len(intervals) == 0:
        return [newInterval]
    while i < len(intervals):  ## 开始遍历, 找插入位置
        if intervals[i][0] < newInterval[0]:
            i =i+1
            if i >1:
                ret.append(intervals[i-2])
                
        elif intervals[i][0] == newInterval[0]:
            if intervals[i][1] < newInterval[1]:
                i =i+1
                if i >1:
                    ret.append(intervals[i-2])
            elif intervals[i][1] >= newInterval[1]:
                return intervals
            
        else:   ## 找到了插入位置, 插入位置为i, 也就是说intervals[i-1:]需要重新探索一遍
            ## 先处理前两个
            ## 其实就是处理起点的过程
            if i ==0:   ## 如果插在了起点, 就把最开始的起点设成他们就行了
                start = newInterval[0]
                end = newInterval[1]
            else:
                if newInterval[0] > intervals[i-1][1]:
                    ret.append(intervals[i-1])
                    start = newInterval[0]
                    end = newInterval[1]
                else:
                    start = intervals[i-1][0]
                    end = max(intervals[i-1][1],newInterval[1])
            j =i   ## 起始点, 相当于在q56中，从i=1开始遍历
            while j < len(intervals):
                if intervals[j][0] > end:
                    ret.append([start,end])
                    start = intervals[j][0]
                    end = intervals[j][1]
                else:
                    end = max(intervals[j][1],end)
                j =j+1
            ret.append([start,end])
            break   ## 完成，记得退出
        
        
        if i == len(intervals):  ## 如果i超出了边界, 说明要插入的位置在最后, 也就是比较一下intervals[-1]和newInterval就行了
            start,end = intervals[-1]
            if newInterval[0] <= end:
                ret.append([start,max(end,newInterval[1])])
            else:
                ret.append(intervals[-1])
                ret.append(newInterval)
#        print(ret)
    return ret

ret = insert(a,b)
