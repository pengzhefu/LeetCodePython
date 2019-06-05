# -*- coding: utf-8 -*-
"""
Created on Thu May  9 05:36:03 2019

@author: pengz
"""

## hard题！
'''
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it is able to trap after raining.
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

hard problem
'''
## 方法1的讲解链接:http://www.cnblogs.com/grandyang/p/8887985.html
def trap(height: [int]) -> int:  ## code written by my own, method depends on monotonous stack, decreasing
                                ## time is O(n), space is O(n)
                                ## 单调栈里面，所有的值都会入一遍栈
    if not height:
        return 0
    stack = []
    length = len(height)
    ret = 0
    i = 0   ## 坐标, stack要存的是坐标
    while i < length:
#        print(stack)
        if len(stack) == 0:
            stack.append(i)
        elif height[i] <= height[stack[-1]]:
            stack.append(i)
#            print('now the stack is', stack)
        else:
            if len(stack) == 1:
                stack.pop()
                stack.append(i)
#                continue
            else:
                low = stack.pop()   ## 底是第一个从stack取出的，也就是还没pop时候stack种的顶部，stack里的最小值
                right = height[i]   ## 右边界是当前值，
                left = height[stack[-1]]  ## 左边界是把上面的最小值取出来以后，此时的栈顶,
#                print('低点为',low,height[low])
#                print('右边界为',i,right)
#                print('左边界为',stack[-1],left)
                tmp = (min(right,left) - height[low]) *(i - stack[-1]-1)  ## 取小的左右边界作为上边界，长就是坐标差
                ret += tmp
#                print(ret)
#                print('now the stack is',stack)
#                print('=========================')
                continue    ## 不能移动坐标，要把这个当前值操作到直到入栈为止
        i = i+1
#    print(stack)
    return ret

height = [0,1,0,2,1,0,1,3,2,1,2,1]
a = trap(height)
'''
dp方法解析链接:http://www.cnblogs.com/grandyang/p/4402392.html
找左边最大是:比较list[i]和dp[i-1],
'''
def trap2(height: [int]) -> int:  ## dp method, from solutions, time is O(2n), space is O(n)
    if not height:
        return 0
    dp_left = [0] * len(height)
    ## first iteration, finding the max in its left
    for i in range(len(height)):
        if i == 0:
            dp_left[i] = height[i]
        else:
            dp_left[i] = max(dp_left[i-1],height[i])
    print(dp_left)
    ## second iteration, finding the max in its right, and compare to select min, and compare to value
#    dp_right = [0] * len(height)
    ret = 0
    for i in range(len(height)-1,-1,-1):
        if i == len(height)-1:
            tmp = 0
            right = height[i]
        else:
            right = max(height[i],tmp)
        tmp = right  ## 用tmp来存储前一个节点的右边最大值是多少
        value = min(right,dp_left[i])
        if value > height[i]:
            ret += (value - height[i])
    return ret
#height = [0,1,0,2,1,0,1,3,2,1,2,1]
b = trap2(height)

'''
https://leetcode.com/articles/trapping-rain-water/#, approach 4
'''
def trap3(height: [int]) -> int:  ## 这方法是dp的升级版，减少时间复杂度和空间复杂度，
                                ## 根本原因其实是在left_max和right_max中, 一般取小的那一个，和list的值比较
                                ## time is O(n), space is O(1)
    if not height:
        return 0
    left_max = 0
    right_max = 0
    left = 0
    right = len(height)-1
    ret = 0
    while left < right:   ## 谁小,动谁，因为是要取小的那个
        if height[left] < height[right]:  ## 如果左边的小, 说明左边的left_max会小，
            if height[left] > left_max:
                left_max = height[left]
            else:
                value = left_max - height[left]
                ret += value
            left += 1
        else:  ## 如果右边的小, 说明右边的right_max会小, 最后也是用这个去减list的值
            if height[right] > right_max:
                right_max = height[right]
            else:
                value = right_max - height[right]
                ret += value
            right -= 1
    return ret

c = trap3(height)
