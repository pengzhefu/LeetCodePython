"""
假设你有一个数组，其中第\ i i 个元素是股票在第\ i i 天的价格。
你有一次买入和卖出的机会。（只有买入了股票以后才能卖出）。请你设计一个算法来计算可以获得的最大收益。

示例1
输入
[1,4,2]
返回值
3
示例2
输入
[2,4,1]
返回值
2
"""

#
# 
# @param prices int整型一维数组 
# @return int整型
#
class Solution:
    def maxProfit(self , prices ):
        if len(prices) <= 1:
            return 0
        price = prices[0]
        profit = prices[1] - prices[0]
        for i in range(1, len(prices)):
            price = min(price, prices[i])
            profit = max(profit, prices[i] - price)
        return profit