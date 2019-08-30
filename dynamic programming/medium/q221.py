# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:09:13 2019

@author: pengz
"""

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
matrix = [["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix2 = [["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["0","1","1","1","1"]]
## https://www.youtube.com/watch?v=FO7VXDfS8Gk
def maximalSquare(matrix: [[str]]) -> int:
    dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    res = 0
    for i in range(len(dp)):   ## 这个表格的意思, 就是说如果以这个matrix[i][j]的点作为
                                ##右下角的点, 那么能获取的最大的正方形边长是多少
        for j in range(len(dp[i])):
            if i == 0 or j == 0:  ## 表格边缘的(左上边缘), 就是原来matrix的值
                dp[i][j] = int(matrix[i][j])
            else:
                if matrix[i][j] != '0':  ## 是周围最小的值(左上,左,上)+上本身
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + int(matrix[i][j])
                else:  ## 如果不在边缘, 但是这个点的值为0, 那么表格的值就是0
                    dp[i][j] = int(matrix[i][j])
            res = max(res,dp[i][j])
    return dp,res**2
#    return dp

dp,res = maximalSquare(matrix2)