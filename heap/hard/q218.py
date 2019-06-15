# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:53:58 2019

@author: pengz
"""

'''
https://leetcode.com/problems/the-skyline-problem/
For instance, the dimensions of all buildings in Figure A are recorded as: 
    [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] 
that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. 
Note that the last key point, where the rightmost building ends, is merely used to mark the termination of 
the skyline, and always has zero height. Also, the ground in between any two adjacent buildings 
should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
    [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
'''
import heapq
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12],[15, 20, 10], [19, 24, 8]]
buildings2 = [[1,2,1],[1,2,2],[1,2,3]]
buildings3 = [[0,2,3],[2,5,3]]
'''
idea from https://www.youtube.com/watch?v=GSBLe8cKu0s
'''
def getSkyline(buildings: [[int]]) -> [[int]]:   ## time is O(nlogn), space is O(n)
    points = []
    delete = {}  ## record the point that should be removed, key is the height, value is times
                ## delete里面的key都是正的，
    for building in buildings:   ## 这道题第一个trick的地方: 对形成的点进行排序,有几个要求
                                ## 1. 在同一个点上，上升的要出现在下降的之前
                                ## 2. 都是上升的话, 最高的一定要在最前面, 是个降序
                                ## 3. 都是下降的话, 最矮的一定要在最前面, 是个升序
        tmp1 = [building[0],-building[2]]
        tmp2 = [building[1],building[2]]
        points.append(tmp1)
        points.append(tmp2)
    points.sort(key=lambda x: (x[0], x[1]))
    print(points)
    max_value = 0   ## max_value永远大于等于0!!!!
    heap = []  ## used as max heap, 都是负数在里面
    heapq.heappush(heap,max_value)
    ret = []
    for point in points:
        if point[1] <0:   ## point[1] <0, 是负数, 说明是上升
            heapq.heappush(heap,point[1])  ## 最大堆需要用负号来完成, 所以这里直接添加point[1]
            if -point[1] > max_value:
                max_value = -point[1]  ## 更新max_value
                ret.append([point[0],max_value])  ## 一旦max_value有变化, 就要添加这个点，最关键的一步
        else:
            tmp = -point[1]  ## 要删的值, 这里要取负数！
            if tmp == heap[0]: ## 如果要删的值就是目前heap里面的最大值，那就删掉
                heapq.heappop(heap)
                while heap[0] in delete:   ## 如果删掉后的heap的开头也是我们之前要删的, 就进行
                    value = heap[0]  ## 先暂存下来这个值是多少
                    heapq.heappop(heap)
                    delete[value] -=1
                    if delete[value] ==0:
                        del delete[value]
                if -heap[0] < max_value:   ## 这里的heap[0]一定要取反!，因为heap里面的值都是负的
                    max_value = -heap[0]
                    ret.append([point[0],max_value]) ## 一旦max_value有变化, 就要添加这个点，最关键的一步
            else:  ## 如果要删的值并不是最大的,不在堆顶,就先记下来
                if tmp not in delete:
                    delete[tmp] =1
                else:
                    delete[tmp] +=1
                ## 因为目前最大的值没有删掉, 没有变化, 所以不添加点到结果里面
    return ret

points = getSkyline(buildings3)
class Solution:
    def getSkyline2(self, buildings: [[int]]) -> [[int]]:
        points = []
        for b in buildings:
            points.append((b[0], -b[2]))
            points.append((b[1], b[2]))
        points.sort(key=lambda x: (x[0], x[1]))
        print(points)
        # prev stores the current height
        prev = 0
        pq = [0]
        results = []
        for p in points:
            if p[1] < 0:
                heapq.heappush(pq, p[1])
            else:
                if -p[1] in pq:    ## 这里会展现一下怎么用heap自带的func进行指定元素的删除
                    i = pq.index(-p[1])
                    pq[i] = pq[-1]
                    pq.pop()
                    if i < len(pq):
                        heapq._siftup(pq, i)
                        heapq._siftdown(pq, 0, i)
            current = -pq[0]
            if prev != current:
                results.append((p[0], current))
                prev = current
        return results