# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:57:57 2019

@author: pengz
"""

'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

    Each element in the result must be unique.
    The result can be in any order.
'''

def intersection(nums1, nums2):   ## Using only one dict, written by my own, time is O(m+n), space is O(m)
    ret = []
    ans1 = {}
    for item in nums1:   
        if item not in ans1.keys():
            ans1[item] = 1
        else:
            ans1[item] += 1
    for item in nums2:
        if item in ans1.keys() and ans1[item] !=0:
            ret.append(item)
            ans1[item] = 0
    return ret

#a = intersection(nums1 = [1,2,2,1], nums2 = [2,2])

def intersection2(nums1, nums2):   ## Using sort and double pointers, 
                                    ## 就是先排序，index1的作用是找到nums1中不重复的下一个，
                                    ## 然后不需要怕nums2中的重复的，因为跳过了nums1中重复的一直找就行了
    ret = []
    nums1.sort()
    nums2.sort()
    index1 = 0
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
       pt = nums1[index1]
       while j < len(nums2) and nums2[j] < pt:
           j = j+1
       if j < len(nums2) and nums2[j] == pt:
           ret.append(nums2[j])
       while i < len(nums1) and nums1[i] == nums1[index1]:
           i = i+1
       index1 = i
    return ret

b = intersection2(nums1 = [1,2], nums2 = [1,1])