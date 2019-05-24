# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:43:42 2019

@author: pengz
"""

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
方法是想找要知道达到这个距离，可以从i-1走一步过来,和i-2走两步过来,所以就是ans[i-1]+ans[i-2]共两种办法
'''

def climbStairs(n: int) -> int: ## dp method, not by myself, time is O(n), space is O(n)
                                ## 不能直接简单的递归，容易超时或者内存溢出, 需要用一个列表将之前的计算结果存起来直接调用
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        ret = [0] *n
        ret[0] = 1
        ret[1] =2
        for i in range(2,n):
            ret[i] = ret[i-1] + ret[i-2]
        return ret[n-1]
    
def climbStairs2(n: int) -> int:  ## dp method, bottoms up, time is O(n), space is O(1)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        ret = 0
        for i in range(3,n):
            ret = a+b
            a = b
            b = ret
        return ret