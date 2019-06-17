# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:55:30 2019

@author: pengz
"""

'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, 
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? 
If it is impossible, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

 

Note:

    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

这道题有一个需要注意的地方是，起始点是给你选好的, 就能作为起始点的只有在time里面开头的那个点
'''
import heapq
import collections
def networkDelayTime(times: [[int]], N: int, K: int) -> int:  ## N是总共有几个点, K是起点
                                                            ## 用的dijkstra, time is O(n)
    graph = collections.defaultdict(dict)
    for u, v, w in times:
        graph[u][v] = w
    print(graph)
    dist = {}
    heap = []
    heapq.heappush(heap,(0,K))  ## 先初始化最小堆,加入的方式是用tuple构成(这个点和起点的距离,这个点)
    while len(heap) != 0:
        weight, point = heapq.heappop(heap)  ## weight是距离,point是点, 首先会找出来每一层离起始点距离最小的点
        if point not in dist:
            dist[point] = weight   ## 可以直接用weight的原因是因为在添加heap的过程中有进行修改,而且是heap, 小的先出来,
                                    ## 后面的大的因为添加过所以就忽略了
            for connect_point in graph[point]:   ##
                heapq.heappush(heap, (dist[point] + graph[point][connect_point], connect_point))
                
        print(heap)
    if len(dist) == N:
        return max(dist.values())
    else:
        return -1

#a = networkDelayTime(times = [[1,2,1],[2,1,3]], N = 2, K = 2)

def networkDelayTime2(times: [[int]], N: int, K: int) -> int:  ## Bellman-Ford
    dist = [float("inf") for _ in range(N)]
    dist[K-1] = 0   ## 让起点的距离变0
#    print(dist)
    for _ in range(N-1):   ## 一定要循环N-1次， 因为如果一开始扫到的点不是起点, 那一开始就不会更新, 需要慢慢更新
        for u, v, w in times:  ## u是起点(tmp), v是终点， w是距离 
            if dist[u-1] + w < dist[v-1]:   ## 要小了才更新
                dist[v-1] = dist[u-1] + w   ## 到v这个点的距离 = 起点到u这个点的距离 + w
#            print(dist)
#        print('======')
    return max(dist) if max(dist) < float("inf") else -1

b = networkDelayTime2([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2)