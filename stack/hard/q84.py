# -*- coding: utf-8 -*-
"""
Created on Fri May 10 02:14:59 2019

@author: pengz
"""

'''
Given n non-negative integers representing the histogram's bar height where the width of 
each bar is 1, find the area of largest rectangle in the histogram.
Example:

Input: [2,1,5,6,2,3]
Output: 10

'''
'''
解释可以看:http://www.cnblogs.com/grandyang/p/4322653.html
http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
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
        print(stack)
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
                print(value)
                if value > ret:
                    ret = value
                continue   ## 要回去继续比, 不能换成另一个元素
        i = i+1
    return ret

heights = [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,10]
a = largestRectangleArea(heights)