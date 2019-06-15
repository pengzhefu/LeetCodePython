# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:58:30 2019

@author: pengz
"""

'''
Given an array nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''
#nums = [1,3,-1,-3,5,3,6,7]
#a = max(nums)
def maxSlidingWindow1(nums:[int], k: int) -> [int]:  ## easy solution, code written by my own, but not O(n) time
                                                        ## 
    '''
    Brute force的方法简单optimize一下可以快好多，每移一次就判断一下前一次的最大值是不是这次被踢出去的那个值，
    如果是的话重新求max，不是的话只需要求前一次最大值和这次新加入的值的max
    '''
    ret = []
    if len(nums) == 0:
        return ret
    if len(nums) <k:
        return ret
    j = 0
    i = k
    delete = nums[0]
    while i<=len(nums):
        tmp_list = nums[j:i]
        if j == 0:
            res = max(tmp_list)
        else:
            if delete == res:
                res = max(tmp_list)
            else:
                res = max(res,nums[i-1])
#        print(tmp_list)
        ret.append(res)
        delete = tmp_list[0]
        j +=1
        i +=1
    return ret

a = maxSlidingWindow1(nums = [1,3,1,2,0,5],k = 3)

import collections
#d = collections.deque()
def maxSlidingWindow2(nums:[int], k: int) -> [int]:  ## idea from https://www.youtube.com/watch?v=G70qltIBF40
                                                    ## 单调队列的方法, time is O(n)
                                                    ## 这个单调队列是一个递减队列!!最大值就是这个deque的第一个数
    ret = []
    if len(nums) == 0:
        return ret
    if len(nums) <k:
        return ret
    d = collections.deque()
    for i in range(k):   ## 初始化第一个deque窗口
        if len(d) == 0:
            d.append(nums[i])
        else:
            if nums[i] <= d[-1]:
                d.append(nums[i])
            else:
                while len(d) !=0 and nums[i] > d[-1]:  ## 如果大于, 就要把前面小的都给丢了,
                    d.pop()
                d.append(nums[i])
    res = d[0]
    ret.append(res)
    idx1 = 0   ## window的最前端
    idx2 = k   ## 移了一次后，window的最后端
#    print(d)
    while idx2 < len(nums):
        if res == nums[idx1]:  ## 如果之前的最大值是要被移走的，那么就popleft, 把那个最大值拿出来
            d.popleft()
        if len(d) == 0:
            d.append(nums[idx2])
        else:
            if nums[idx2] <= d[-1]:
                d.append(nums[idx2])
            else:
                while len(d) !=0 and nums[idx2] > d[-1]:
                    d.pop()
                d.append(nums[idx2])
        res = d[0]
        ret.append(res)
        idx1 +=1
        idx2 +=1
        print(d)
    return ret
b = maxSlidingWindow2(nums = [1,-1],k = 1)
