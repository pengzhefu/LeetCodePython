# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:32:11 2019

@author: pengz
"""

'''
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Note:

    The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
    The size of flights will be in range [0, n * (n - 1) / 2].
    The format of each flight will be (src, dst, price).
    The price of each flight will be in the range [1, 10000].
    k is in the range of [0, n - 1].
    There will not be any duplicated flights or self cycles.

'''
import collections
n =3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src =0
dst =2
K =1
'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/214627/Dynamic-Programming-Python-Easy-to-Understand
'''
def findCheapestPrice(n, flights, src, dst, K):  ## using dynamic programing, time is O(km) —— O(km^2)
                                                                ## space is O(km) —— O(n)
    dp = [[float('inf')] *n for i in range(K+2)]   ## K+2是行数, n是列数, 代表城市数
                                            ## dp这个表格表示的是src到各个点在最多K+1步的时候的最便宜价格
    for i in range(K+2):   ## 之所以是K+2, 是因为总共是0到K+1步，K个stop，总共K+1步
        dp[i][src] = 0

    graph = collections.defaultdict(dict)
    for u, v, weight in flights:
        graph[u][v] = weight   ## graph也相当于cost
        if u == src:
            dp[1][v] = min(dp[1][v],weight)   ## 1就是只走一步，没有stop
#    print(graph)
#    return graph
    price = float('inf')
    for i in range(1,K+2):
        ## 用这两个循环在每次最多i个stop的时候, 利用所有点到各自的点的距离,来更新dp table
        for u in range(n):  ## u是起点,城市标号是0 —— n-1
            for v in graph[u]:  ## v是u能到的终点
#            for v in range(n):  ## v是终点
#                if v != u and u in graph and v in graph[u]:
                    dp[i][v] = min(dp[i][v],dp[i-1][u]+graph[u][v])##如果本来这个src无法到达这个u,那就也不会更新这个价格,
                                                                    ## 因为都是inf, 所以比较的两个对象才是
                                                                    ## dp[i][v]和dp[i-1][u]+graph[u][v]
                                                                    ## 注意一定是dp[i][v]
                    if v == dst:
                        price = min(price,dp[i][dst])
    return price if price != float('inf') else -1


ret = findCheapestPrice(n,flights,src,dst,K)

import heapq
'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/267200/Python-Dijkstra
'''
def findCheapestPrice2(n, flights, src, dst, K):  ## using Dijkstra, time is O(m + nlogn).
                                            ##  m is number of edges and n is number of nodes.
    graph = collections.defaultdict(dict)
    for u, v, cost in flights:
        graph[u][v] = cost
        
    max_step = K+1
    heap = [(0,src,1)]  ## 点的排列形式为(price, point, steps)
    while heap:
        price,point,step = heapq.heappop(heap)
        if point == dst:   ## 因为heap本身是最小堆，所以已经返回的就是最小的了，如果pop出来的是dst, 可以直接return
            return price
        if step <= max_step:  ## 这里面最关键的就是这个， step需要小于等于k+1才行, 因为最少走一步，最多能走K+1步，
                                ## 所以超过K+1步后，heap里面不再放进去新的了
            for connect_point in graph[point]:
                heapq.heappush(heap,(price+graph[point][connect_point], connect_point, step+1))
    return -1


    
    
    