# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:22:11 2019

@author: UPenn-BU-01
"""
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


'''

def maxProfit(prices):  ## Exceed time limit,time complexity = O(n^2)
    i = 0
    res = 0
    while i <= len(prices) -2:
        buy = prices[i]
        sell = prices[i+1]
        for k in range(i+1,len(prices)):
            if prices[k] > sell:
                sell = prices[k]
        if (sell - buy) > res:
            res = sell-buy
        i = i+1
    return res

a = maxProfit([7,6,4,3,1])

def maxProfit2(prices):   ## written by my own, concerning about q53
                            ## and, time complexity is O(n)
    if prices == []: 
        return 0
    else:
        res = 0
        cur_res = 0
        min_buy = prices[0]
        for i in range(0,len(prices)-1):
            min_buy = min(min_buy, prices[i])  ##相当于在这一次循环中，每次都会判断最低进价
            cur_res = max(cur_res, prices[i+1] - min_buy) ## 如果最近进价不变，相当于就只更新卖价
                                                            ##就算进价更新了，也只能从更新的idx之后找
                                                            ##卖价，所以继续循环就好了
            res = max(res, cur_res)     ##将现在的结果和已经保存的最小结果进行比较
        return res
b = maxProfit2([7,1,5,3,6,4])