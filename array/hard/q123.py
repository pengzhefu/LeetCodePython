# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:44:03 2019

@author: pengz
"""

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

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
def maxProfit(prices: [int]) -> int: ## idea from https://www.youtube.com/watch?v=xwYFIspPswU
    if len(prices) <2:
        return 0
    ret1 = [0 for i in range(len(prices))]
    min_price1 = prices[0]
    profit1 = 0
    for i in range(1,len(prices)):    ## 先从头开始扫第一遍, 把每个点卖出的最大获利算出来, 在ret1中
        min_price1 = min(min_price1,prices[i])
        profit1 = max(profit1,prices[i]-min_price1)
        ret1[i] = profit1
    min_price2 = prices[len(prices)-1]
    max_sell = prices[len(prices)-1]
    profit2 = 0
    res = ret1[len(prices)-1] + profit2
    for i in range(len(prices)-2,-1,-1):    ## 然后再从后往前扫一遍, 就是找出来每个在这个点卖出之后，剩下的一部分array的最大收益
        min_price2 = min(prices[i],min_price2)  ## 先和当前最低价比较
        if prices[i] > max_sell:   ## 如果价格比能卖出的最高价格都要高了,就需要更新最高价格和最低进价
                                    ## 因为进价永远在售出之前, 也就是如果要用这个更高的卖价, 只能在他之前重新找
            max_sell = prices[i]
            min_price2 = prices[i]
        res = max(res,ret1[i]+max_sell-min_price2)   ## 然后每次都不断比较, 就不存第二次结果了
        # print(min_price2)
        # print(max_sell)
        # print(res)
        # print('=======')
    return res

prices = [2,5,7,1,4,3,1,3]
def maxProfit2(prices: [int]) -> int:  ## 使用dp, 详细说明可以看笔记,https://www.youtube.com/watch?v=oDhu5uGq_ic
    dp = [[0 for i in range(len(prices))] for i in range(2+1)]  ## 这里是k+1， k是交易次数
    res = 0
    for i in range(1,2+1):
        maxdiff = dp[i][0] - prices[0]
        for j in range(1,len(prices)):
            maxdiff = max(maxdiff,dp[i-1][j]-prices[j])  ## 先找出最大价格差
            dp[i][j] = max(dp[i][j-1], prices[j]+maxdiff)
            res = max(res,dp[i][j])
    return res


ret = maxProfit2(prices)