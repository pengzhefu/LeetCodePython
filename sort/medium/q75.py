# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:32:13 2019

@author: pengz
"""

'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

    1. A rather straight forward solution is a two-pass algorithm using counting sort.
    2. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, 
    then 1's and followed by 2's.
    3. Could you come up with a one-pass algorithm using only constant space?

'''
nums2 = [2,0,2,1,1,0,1,2]
nums1 = [2,0,2,1,1,0]
def sortColors(nums: [int]) -> None:  ## code by my own, idea from https://www.youtube.com/watch?v=J9DgvL6L1nk
    """
    Do not return anything, modify nums in-place instead.
    """
    first = 0   ## first的左边只有0， 或者没有数字
    last = len(nums)-1   ## last的右边只有2，或者没有数字
    ## 先确定first和last的位置
    while first < len(nums) and nums[first] == 0:   ## 也就是第一个不为0的地方就是first
        first +=1
    while last >=0 and nums[last] == 2:   ## 也就是第一个不为2的地方就是last
        last -=1
    i = first   ## i从first开始遍历
    while i <= last:  ## 一直到超过last, 也就是i=last+1的时候, 跳出循环
        while nums[first] == 0 and first < len(nums):
            first += 1
        while nums[last] == 2 and last >= 0:
            last -=1
        if nums[i] == 0:
            if i > first:    ## 一定要是这个时候的0在first的后面的0， 才有交换的意义
                nums[i],nums[first] = nums[first],nums[i]
                first +=1
                continue   ## 交换以后, 移动的遍历指针先不要移动, 先让first或者last指针走到正确的位置, 而且可能需要交换多几次
                            ## 比如有可能和first交换过后，新来的又是2, 和last再交换一次
        if nums[i] == 2:
            if i < last:  ## 这个时候的2一定要是在last前面的2, 才有交换的意义
                nums[i],nums[last] = nums[last],nums[i]
                last -=1
                continue
        i = i+1
#    print(first,last)

sortColors(nums2)
sortColors(nums1)
        