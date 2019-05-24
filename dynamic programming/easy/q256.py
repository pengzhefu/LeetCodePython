# -*- coding: utf-8 -*-
"""
Created on Tue May  7 03:12:17 2019

@author: pengz
"""

'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or 
green. The cost of painting each house with a certain color is different. You have to paint 
all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For 
example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of 
painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.

'''
def minCost(costs) -> int:  ## not written by my own, time O(n), space O(1)
    if len(costs) == 0:
        return 0
    elif len(costs) == 1:
        return min(costs[0])
    else:
        res = costs[0]
        n = len(costs)
        tmp = [0] *3
        for i in range(1,n):
            tmp[0] = min(res[1],res[2]) + costs[i][0]##形成一个新的数组，就是写出三种组合(1个index和另外两个中较小的index)
            tmp[1] = min(res[0],res[2]) + costs[i][1]
            tmp[2] = min(res[0],res[1]) + costs[i][2]
            res[:] = tmp[:]   ## 把这个新形成的数组作为结果
        return min(res)