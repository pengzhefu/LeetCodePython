# -*- coding: utf-8 -*-
"""
Created on Fri May  3 02:56:49 2019

@author: pengz
"""

'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

'''
def searchMatrix(matrix, target):  ## written by my own! the solution call it as search space reduction
                                    ## time is O(n+m)
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    n = len(matrix)  ## 先获取m,n的值, n是行数,m是列数
    if n == 0:
        return False
    else:
        m = len(matrix[0])
    if m ==0:
        return False
    i = 0  ## 先从第一行开始
    while i < n:   ## i是行, j是列
        j = 0  ## 每一行从第一列开始
        while j < m:
            if matrix[i][j] < target:  ## 如果小于的话, 先移动列
                j += 1
            elif matrix[i][j] == target:
                return True
            else:   ## 如果大于的话, 就说明在这个点之后的右,下,或者右下方都不符合要求了, 因为都比这个点大
                if j == 0:  ## 如果这已经是第一列了, 那么没有符合要求的了
                    return False
                else:  ## 如果不是, 那就把这一列作为新的边界条件,然后会跳出, 往下一行的第一列重新开始找
                    m = j
        i = i+1  
    return False
#a = searchMatrix(, 2)

### 这个方法从solution看的，其实就相当于每一行和每一列都用一次二分搜索, time is O(log(n!))
def binary_search(self, matrix, target, start, vertical):
    lo = start
    if vertical:
        hi = len(matrix[0])-1 
    else: 
        hi = len(matrix)-1

    while hi >= lo:
        mid = (lo + hi)//2
        if vertical: # searching a column
            if matrix[start][mid] < target:
                lo = mid + 1
            elif matrix[start][mid] > target:
                hi = mid - 1
            else:
                return True
        else: # searching a row
            if matrix[mid][start] < target:
                lo = mid + 1
            elif matrix[mid][start] > target:
                hi = mid - 1
            else:
                return True
    
    return False

def searchMatrix2(self, matrix, target):
    # an empty matrix obviously does not contain `target`
    if not matrix:
        return False

    # iterate over matrix diagonals starting in bottom left.
    for i in range(min(len(matrix), len(matrix[0]))):    ## 
        vertical_found = self.binary_search(matrix, target, i, True)
        horizontal_found = self.binary_search(matrix, target, i, False)
        if vertical_found or horizontal_found:
            return True
    
    return False



## divide and conquer, from the solution, time is O(nlogn)
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:   ## base case1
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:   ## base case2
                return False

            mid = left + (right-left)//2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up   ## 从上往下找, 按行来
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            ## 去他的左下方（如果遍历的都小于）和右上方（如果都大于）， 不会去左上方和右下方
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)

        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)