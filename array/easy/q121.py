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
    if len(prices) <= 1: 
        return 0
    price = prices[0]
    profit = prices[1] - prices[0]
    for i in range(1,len(prices)):
        price = min(prices[i],price)
        profit = max(profit, prices[i]-price)
    return profit
b = maxProfit2([7,1,5,3,6,4])