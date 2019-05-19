# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:23:58 2019

@author: pengz
"""
'''
Let's call an array A a mountain if the following properties hold:

    A.length >= 3
    There exists some 0 < i < A.length - 1 such that 
    A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that 
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1

Example 2:

Input: [0,2,1,0]
Output: 1

Note:

    3 <= A.length <= 10000
    0 <= A[i] <= 10^6
    A is a mountain, as defined above.

'''

def peakIndexInMountainArray(A: list) -> int:
    first = 0
    last = len(A) -1
    while first <= last:
        mid = (first+last) //2
#        print(first,last,mid)
        if mid == 0 or mid == len(A) -1:
            return mid
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:   
            return mid
        elif A[mid] > A[mid-1] and A[mid+1] > A[mid]:   ## 如果递增
            first = mid+1
        elif A[mid] < A[mid-1] and A[mid+1] < A[mid]:  ## 如果递减
            last = mid   ## 这里最好不要-1，有可能mid刚好是峰值
    return first
            
A = [6,7,8,10,20,19,13,12]
a = peakIndexInMountainArray(A)
        
        