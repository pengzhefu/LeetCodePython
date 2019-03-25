# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:12:50 2019

@author: UPenn-BU-01
"""

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you 
must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


'''
'''
这道题没有想出来，看了答案，但这道题其实有一个很巧的解法的方面。
就是其实他的最大输出，就应该是他其中的每一个递增序列的（最大-最小）的差值的总和。
从example可以看出来，如果整个是个递增序列，那么res就是最后-第1；如果递减，那么就为0.
'''
def maxProfit(prices):
    res = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            res = res + prices[i] - prices[i-1]  ## 这也是递增序列求和的一种，用每两项的差的总和
                                                    ## 就等于递增序列最大项减最小项的值
    return res
a = maxProfit([7,1,5,3,6,4])