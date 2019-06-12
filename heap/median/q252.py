# -*- coding: utf-8 -*-
"""
Created on Sat May 25 03:07:21 2019

@author: pengz
"""
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true

'''
class Solution: ## code written by my own, idea from https://www.youtube.com/watch?v=0roQnDBC27o
    def canAttendMeetings(self, intervals: [[int]]) -> bool:
        if len(intervals) == 0:
            return True
        start =[]
        end = []
        for item in intervals:
            start.append(item[0])
            end.append(item[1])
        start.sort()
        end.sort()
        i = 1  ## 是交错开的, 每一个后一位的start都应该大于等于end才能保证不重叠
        j = 0
        while i < len(start):
            if start[i] < end[j]:
                return False
            else:
                i =i+1
                j = j+1
        return True
    
print(5%2)