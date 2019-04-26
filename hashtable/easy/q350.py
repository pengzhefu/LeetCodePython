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
def intersect(nums1, nums2):   ## Still using two dicts, written by my own, but this one is limited by memory
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

def intersect2(nums1, nums2):   ## written by my own, solve question3, encountered limited memory
    ret = []
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):   ## 和q349不一样的地方在于，重复的也需要添加
        while j < len(nums2) and nums2[j] < nums1[i]:  ## 记住只有目前小于nums1的时候，才需要一直挪
            j = j+1
        if j < len(nums2) and nums2[j] == nums1[i]:
            ret.append(nums1[i])
            j = j+1    ## 如果nums2中有一个加进来了，才需要把这个往后挪1
        i = i+1  ## 相当于nums1中的每个数都需要找一遍看看nums2剩下的一部分有没有和这个数相同的
    return ret

a= intersect(nums1 = [1,2,2,1], nums2 = [2,2])