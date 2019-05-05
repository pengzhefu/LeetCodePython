# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:31:37 2019

@author: pengz
"""

'''
Given an array of integers A sorted in non-decreasing order, return an array of 
the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.

'''
def sortedSquares(A):  ## written by my own, just using append, without insert
    ret = []
    i = 0
    ## 先找到正负数的临界, when this while loop ends the A[i] is non-negative, A[i-1] is negative 
    while i < len(A):
        if A[i] <0:
            i = i+1
        elif A[i] >= 0:
            break
    if i == 0:   ## 只有正数
        for x in A:
            ret.append(x**2)
    elif i == len(A): ## 只有负数
        for x in range(len(A)-1,-1,-1):
            ret.append(A[x]**2)
    else:
        
        j = i-1    ## j is the max of negative
                   ## i is the min of positive
        while j >= 0 or i < len(A):
            if j < 0:  ## 说明负数的已经比较完了,把剩下的正数按顺序添加进去就行了
                for x in range(i,len(A)):
                    ret.append(A[x]**2)
                return ret
            elif i == len(A):   ## 说明正数的已经比较完了，接着只添加负数的就行了
                for x in range(j,-1,-1):
                    ret.append(A[x]**2)
                return ret
            else:
                print(j,i)
                if (A[i] ** 2) >= (A[j] ** 2):
                    ret.append(A[j] **2)
                    j = j-1
                else:
                    ret.append(A[i] **2)
                    i = i+1
    return ret
    
a = sortedSquares([-2,2,3,4])    