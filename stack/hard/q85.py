# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:19:47 2019

@author: pengz
"""

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

和q84结合一起的解法,相当于dp+stack, 详细解释在https://www.youtube.com/watch?v=2Yk3Avrzauk
就相当于从第一行开始，每一行往上构成一个直方图,然后每次计算一次这个直方图的最大面积，然后比较
关键是构成直方图，如果到这一行的时候，这一列的元素是0，那么这一列的值就是0，如果不是0，那么就是上一行的时候的直方图的值+1

'''
def largestRectangleArea(heights:[int]) -> int:  ## using stack, increasing, code written by my own, time is O(n)
                                                ## space is O(n)
    if not heights:
        return 0
    ret = 0
    heights.append(0)   ## 先在最后一个添上0, 这样才能保证能把所有的项都遍历一次
    stack = []   ## stack记录的是坐标
    i = 0
    while i < len(heights):
#        print(stack)
        if len(stack) == 0:
            stack.append(i)
        else:
            if heights[i] >= heights[stack[-1]]:  ## 大于等于的话,就继续放进来
                stack.append(i)
            else:
                if len(stack) == 1:
                    tmp = stack.pop()
                    value = heights[tmp] * i   ## 如果栈里只有一个，那就要用这个最小的元素乘以当前的index值
                else:
                    tmp = stack.pop()
                    value = heights[tmp] * (i-stack[-1]-1)  ## 如果栈里还有别的元素，那么长度是当前使用的项的index，和
                                                            ## 再pop以后的栈顶，也就是这个栈刚刚第二大的元素的index
                                                            ## 之差，再减一
#                print(value)
                if value > ret:
                    ret = value
                continue   ## 要回去继续比, 不能换成另一个元素
        i = i+1
    return ret
def maximalRectangle(matrix: [[str]]) -> int:  ## space is O(n,列数), time is O(mn) 
    if not matrix:
        return 0
    if not matrix[0]:
        return 0
    curleft = [0 for i in range(len(matrix[0]))]
    ret = 0
    for i in range(len(matrix)):   ## 从第一行开始
        if i == 0:
            for j in range(len(matrix[i])):
#                print(matrix[i][j])
                curleft[j] = int(matrix[i][j])   ## 第一行就和matrix的第一行一样
#                print(curleft[j])
        else:
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':     ## 如果这里是1,那就是上一行的结果加1 
                    curleft[j] = curleft[j] +1
                elif matrix[i][j] == '0':   ## 如果是0, 直接清零
                    curleft[j] = 0
#        print(curleft)
        tmp = largestRectangleArea(curleft)
        if tmp > ret:
            ret = tmp
    return ret

matrix= [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
b = maximalRectangle(matrix)
    
