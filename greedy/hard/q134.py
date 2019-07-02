# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:04:04 2019

@author: pengz
"""

'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

    If there exists a solution, it is guaranteed to be unique.
    Both input arrays are non-empty and have the same length.
    Each element in the input arrays is a non-negative integer.

Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

'''
'''
https://www.cnblogs.com/boring09/p/4248482.html
啥总和非负的数列，一定存在一个位置开始累计加和始终为非负。假如这个位置不存在，即从数列所有位置开始算累加和，一定算到某处就为负了。
那么这个某处之后的部分的和一定是正的，还比这个之前的负数和的绝对值大。
那我现在就从这个某处之后的点开始走，全程和都不会是负的了。与条件相反，证出来了
'''
def canCompleteCircuit(gas: [int], cost: [int]) -> int:  ## code written by my own, inspired by others 
    if sum(cost) > sum(gas):  ## 如果总和就小了, 就直接返回-1
        return -1
    else:
        start = 0  ## 从0开始作为起点，开始找
        remain = 0
        idx = None
        step = 0
        while step < len(gas):   ## 走一圈的话, 应该是从那个起点能走总共list长度的步数
            if step == 0:   ## 一开始还没走的时候, 让idx变成起点
                idx = start
            remain += gas[idx]   ## 添加在当前点的补充
            if remain >= cost[idx]:  ## remain要大于当前移动一个需要的大小, 才能移动到下一格
                remain = remain - cost[idx]  ## 减去需要消耗的量
                idx += 1  ## 移动一格
                step += 1 ## 步数+1
                if idx == len(gas):  ## 如果idx超出了, 那就变0
                    idx =0
            else:   ## 如果不能移动，
                start = idx+1    ## 可以把起点放到我们现在不能移动的这个点的之后一个点
                                ## 因为如果从i开始到j都会remain变成负数, 因为remain在i肯定要是正数才会开始移动, 
                                ## 那么i+1,i+2...到j也会变成负数,所以新的起点选成 j+1就行
                if start == len(gas):
                    start = 0
                remain =0  ## remain清零
                step =0   ## 步数清零
        return start
    
gas  = [5,1,2,3,4]
cost = [4,4,1,5,1]

ret = canCompleteCircuit(gas,cost)