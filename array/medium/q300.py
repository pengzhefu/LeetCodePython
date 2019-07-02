# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 03:48:43 2019

@author: pengz
"""
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
medium
'''
def lengthOfLIS(nums: [int]) -> int:  ## time is O(n^2)
    ## idea from https://blog.csdn.net/fuxuemingzhu/article/details/79820919
    ret = [1 for i in range(len(nums))]
    res = 0
    for i in range(0,len(nums)):
        tmp =1
        for j in range(i-1,-1,-1):  ## 往回每一格去看
            if nums[i] > nums[j]:   ## 去看是否比这一格的数字大
                tmp = max(tmp,ret[j]+1)  ## 如果比这一格数字大的话, 应该是这个格子的长度+1, 但是记得要去max比较，找整个的最大
        ret[i] = tmp
        res = max(res,ret[i])  ## 在遍历的过程中找结果
    return res

list1 = [10,9,2,5,3,7,101,18]
list2 = [2,10,12,1,3,4,5,6]

def lengthOfLIS2(nums: [int]) -> int:
    if nums is None or len(nums) == 0:
        return 0
    def get_insert_pos(item, alist):
        first = 0
        final = len(alist) -1
        found = False
        while not found and first <= final:  ##这个中止条件一定要记牢！
            mid = int((first+final)/2)
            if alist[mid] == item:
                found = True
            elif alist[mid] < item:
                first = mid + 1
            else:
                final = mid - 1
        if not found:  
            return first  ## 此时如果没找到的话，那么return的first的值就是这个数插入这个列表的index
                            ## 如果first直接等于列表长度, 就说明要放在最后
        else:   ## 如果found, 就返回mid, 因为是mid找到了
            return mid
    res = []
    for num in nums:
        if len(res) == 0 or res[-1] < num:
            res.append(num)
            continue
        insert_pos = get_insert_pos(num, res)
        res[insert_pos] = num  ## 找到了相应的插入位置以后，不是插入，是直接替换，这是重点

    return len(res)

ret = lengthOfLIS2(list1)