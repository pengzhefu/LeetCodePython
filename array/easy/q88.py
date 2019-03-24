# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:06:15 2019

@author: UPenn-BU-01
"""

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) 
    to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


'''
def merge(nums1, m, nums2, n):  ## Written by my own
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0  ## index of nums1
        j = 0  ## index of nums2
        while i < m and j < n:
            if nums2[j] < nums1[i]: ##if there should be a number inserted 
                for k in range(len(nums1)-1,i,-1):  ## all nums in 1 should backward one
                   nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j = j+1 ## the index of nums2 should plus 1
                m = m+1 ## the number of nums which are not 0 increase 1
            i = i+1 ## the index of nums1 should plus1
        if j < n:  ## if there is some nums in nums2 larger than all of nums in nums1
            for nums in nums2[j:]:
                nums1[m] = nums   ## subsititue directly
                m = m+1

list1 = [5,6,14,0,0,0,0,0]
list2 = [2,2,4,6,7]
merge(list1,3,list2,5)

def merge2(nums1,m,nums2,n):   ## Using sorted func, but faster than what I wrote
    nums1[:] = sorted(nums1[:m]+nums2)

nums1 = [1,2,6,0,0,0]
nums2 = [3,7,9]
merge2(nums1,3,nums2,3)