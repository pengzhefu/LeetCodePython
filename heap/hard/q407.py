# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:22:36 2019

@author: pengz
"""

'''
Given an m x n matrix of positive integers representing the height of each unit cell in a 
2D elevation map, compute the volume of water it is able to trap after raining.

 

Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

 

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
'''

heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
'''
https://www.youtube.com/watch?v=cJayBq38VYw   !! 太厉害了！！
'''
import heapq
def trapRainWater(heightMap: [[int]]) -> int: ## code written by my own, idea not, genius idea
    heap = []
    ret = 0
    row = len(heightMap)
    col = len(heightMap[0])
    visited = {}
    for i in range(row):   ## first, put all boarders into heap
        for j in range(col):
            if i == 0 or i == row-1:
                heapq.heappush(heap,(heightMap[i][j], i, j))
                visited[(i,j)] = True
            elif j ==0 or j== col-1:
                heapq.heappush(heap,(heightMap[i][j], i, j))
                visited[(i,j)] = True
#    print(visited)
#    return heap
    max_val = 0
    while heap:
        val, r, c = heapq.heappop(heap)
        if val > max_val:  ## 如果pop出来的点的值大于当前的max, 就更新
            max_val = val
        if (r == 0 or r == row-1) and (c == 0 or c == col-1):  ## 在角落的四个点没有相邻点
            continue
        ## 把pop出来的周围的点遍历一下
        if (r-1,c) not in visited and r-1 >=0:  ## 如果是没遍历过的, 就放进heap
            heapq.heappush(heap,(heightMap[r-1][c], r-1, c))
            visited[(r-1,c)] = True  ## 用字典记录
            if heightMap[r-1][c] < max_val:   ## 如果周围的点有小于当前的max, 那么这个点可以成为坑
                ret += max_val - heightMap[r-1][c]
                
        if (r+1,c) not in visited and r+1 <row:
            heapq.heappush(heap,(heightMap[r+1][c], r+1, c))
            visited[(r+1,c)] = True
            if heightMap[r+1][c] < max_val:
                ret += max_val - heightMap[r+1][c]
                
        if (r,c-1) not in visited and c-1 >=0:
            heapq.heappush(heap,(heightMap[r][c-1], r, c-1))
            visited[(r,c-1)] = True
            if heightMap[r][c-1] < max_val:
                ret += max_val - heightMap[r][c-1]
                
        if (r,c+1) not in visited and c+1 <col:
            heapq.heappush(heap,(heightMap[r][c+1], r, c+1))
            visited[(r,c+1)] = True
            if heightMap[r][c+1] < max_val:
                ret += max_val - heightMap[r][c+1]
    return ret

ret = trapRainWater(heightMap)