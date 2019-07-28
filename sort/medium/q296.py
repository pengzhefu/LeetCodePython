# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 01:39:17 2019

@author: pengz
"""

'''
A group of two or more people wants to meet and minimize the total travel distance. 
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.


'''

## https://www.cnblogs.com/grandyang/p/5291058.html  具体解释可以看这里
def minTotalDistance(grid: [[int]]) -> int:  ## time is O(nlogn)
    list_x = []
    list_y = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                list_x.append(i)
                list_y.append(j)
    list_x.sort()  ## 要排序
    list_y.sort()
    i = 0
    j = len(list_x)-1
    ret1 = 0 ## 给x的距离
    ret2 = 0 ## 给y的距离
    while i < j:
        ret1 += (list_x[j] - list_x[i])
        ret2 += (list_y[j] - list_y[i])
        i +=1
        j -=1
    return ret1+ret2