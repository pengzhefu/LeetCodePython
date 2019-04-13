# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:48:03 2019

@author: pengz
"""

'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
def intersect(nums1, nums2):   ## Still using two dicts, written by my own
    ret = []
    ans1 = {}
    ans2 = {}
    for item in nums1:
        if item not in ans1.keys():
            ans1[item] = 1
        else:
            ans1[item] += 1
#    print(ans1)
    for item in nums2:
        if item in ans1.keys():    ## 出现在了nums1中的话
            if item in ans2.keys():
                if ans2[item] < ans1[item]:   ## 且次数还没达到这个在nums1中的出现次数
                    ret.append(item)
                    ans2[item] += 1
                else:
                    pass
            else:
                ans2[item] = 1
                ret.append(item)
    return ret

a= intersect(nums1 = [1,2,2,1], nums2 = [2,2])