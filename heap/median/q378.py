# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:28:23 2019

@author: pengz
"""

'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the 
kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''
import heapq
def kthSmallest(matrix: [[int]], k: int) -> int: ## just using maxHeap, code written by my own, time is O(min(K,N)+K∗logN)
        # ret = 0
    if len(matrix) == 0:
        return 0
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            heapq.heappush(heap,-matrix[i][j])
            if len(heap) >k:
                heapq.heappop(heap)
    return -heap[0]

'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search
'''
def kthSmallest2(matrix: [[int]], k: int) -> int:  ## great solution and idea! time is O(N∗log(max−min))
                                                    ## space is O(1)
    start = matrix[0][0]
    end = matrix[len(matrix)-1][len(matrix[0])-1]
    count = 0
#    print(smaller)
#    print(larger)
    while start < end:  ## 这个循环条件也要注意，因为如果是找最小的, 就会返回start, 这时候end==start， 但是count最小只能到2
#        print(start)
        mid = (start+end)/2
        row = len(matrix)-1   ## 注意起始的查询位置，应该是最左下角
        col = 0
        n = len(matrix)
        count = 0   ## 每次循环开始前都要进行一遍归0
        larger = matrix[len(matrix)-1][len(matrix[0])-1]  ## 同时这个矩阵里的最大的数和最小的数也要再设置一遍
        smaller = matrix[0][0]                              ## 相当于每次都是整个矩阵重新数一遍
        while row >=0 and col <n:## 注意这个循环条件！，数有多少个数小于mid
            if matrix[row][col] > mid:
                larger = min(larger,matrix[row][col])
                row = row-1   ## 大了把行往上移
            else:
                smaller = max(smaller,matrix[row][col])
                count += (row +1)   ## row+1是因为小了就要往右移,那么那一列的到row这一行的所有都小,个数应该是row+1, 因为
                                    ## 是从0开始
                col +=1   ## 小了把列往右移
        if count > k:
            end = smaller
        if count <k:   ## 如果找到的 <=中位数的个数比k少，说明要提高起点
            start = larger
        if count ==k:
            return smaller
    return start

ret = kthSmallest2([[1,2],[1,3]],1)
    
            
        