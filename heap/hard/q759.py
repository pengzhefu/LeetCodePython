# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 01:22:04 2019

@author: pengz
"""

'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all 
employees, also in sorted order.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

 

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

 

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, 
not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, 
and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:

    1. schedule and schedule[i] are lists with lengths in range [1, 50].
    2. 0 <= schedule[i].start < schedule[i].end <= 10^8.

NOTE: input types have been changed on April 15, 2019. Please reset to 
default code definition to get new method signature.
'''
schedule1 = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
schedule2 = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
#all_schedule = []
#for employee in schedule:
#    for time in employee:
#        all_schedule.append(time)
#all_schedule.sort(key = lambda item:(item[0],item[1]))
def employeeFreeTime1(schedule: [[[int]]]) -> [[int]]:  ## idea inspired by Huahua, code written by my own
                                                        ## space is O(n),time is O(nlogn)
    ret = []
    all_schedule = []
    for employee in schedule:
        for time in employee:
            all_schedule.append(time)
    all_schedule.sort(key = lambda item:(item[0],item[1]))  ## 先排序，按起始时间
    print(all_schedule)
    i = 0
    interval = None
    res = None
#    print(len(all_schedule))
    while i < len(all_schedule):
        print(i,interval)
        if i ==0:
            interval = all_schedule[0]
            i += 1
            continue
        else:
            if all_schedule[i][0] > interval[1]:   ## interval[0]是目前的起始时间, interval[1]是当前结束时间
                                                    ## 如果起始时间晚于当前结束时间, 
                res = [interval[1],all_schedule[i][0]]  ## 添加进来的是[当前结束时间, 起始时间]
                interval = all_schedule[i]
            else:
                if interval[1] < all_schedule[i][1]:   ## 如果早于当前结束时间， 而且新的结束时间更晚,更新结束时间
                    interval[1] = all_schedule[i][1]
        if res:
            ret.append(res)
            res = None
        i +=1
    return ret

#ret = employeeFreeTime1(schedule2)
import heapq
#all_schedule = []
#for employee in schedule1:
#    for time in employee:
#        all_schedule.append(time)
#heapq.heapify(all_schedule)
        
def employeeFreeTime2(schedule: [[[int]]]) -> [[int]]:  ## using heap, space is O(n), time is O(nlogn)
    ret = []
    all_schedule = []
    for employee in schedule:
        for time in employee:
            all_schedule.append(time)
    heapq.heapify(all_schedule)
    start, end = heapq.heappop(all_schedule)
    max_end = end
#    print()
    while all_schedule:
        start, end = heapq.heappop(all_schedule)
#        print(start,end)
#        print(max_end)
#        print('============')
        if start > max_end:  ## 这是两个分开的if
            ret.append([max_end,start])
        if end > max_end:   ## 更新结束时间
            max_end = end
#        else:
#            max_end = max(end,max_end)
    return ret

ret2 = employeeFreeTime2(schedule2)