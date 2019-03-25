# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 06:38:15 2019

@author: UPenn-BU-01
"""
'''
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

def generate(numRows):  ## Written by my own, time complexity is O(n^2) maybe
    ret = [[1]*(i+1) for i in range(numRows)]
    i = 2
    while i < numRows: ## 要输出三行及以上的情况  
        for k in range(1,i): ##就是去掉开头和结尾的两个1
            ret[i][k] = ret[i-1][k-1]+ret[i-1][k]
        i = i+1
    return ret

a = generate(9)
