# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 03:41:14 2019

@author: pengz
"""

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''
## 使用dp, 详细说明可以看笔记,https://www.youtube.com/watch?v=oDhu5uGq_ic
def maxProfit(k: int, prices: [int]) -> int:
    if k >= int(len(prices) / 2):  ## 如果交易次数达到一半或以上(取下限), 那就是相当于计算递增区间的所有累加结果就行了
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res 
    if len(prices) == 0 or k == 0:  ## base case
        return 0
    ret = 0
    dp = [[0 for i in range(len(prices))] for i in range(k+1)]
    for i in range(1,len(dp)):
        maxdiff = dp[i][0] - prices[0]
        for j in range(1,len(dp[i])):
            maxdiff = max(maxdiff,dp[i-1][j]-prices[j])
            dp[i][j] = max(dp[i][j-1],prices[j]+maxdiff)
            ret = max(ret,dp[i][j])
    return ret
#    return dp

b = maxProfit(2,[2,4,1])