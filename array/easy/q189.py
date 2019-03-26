# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:47:18 2019

@author: pengz
"""

'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
'''

def rotate(nums, k):   ## written by my own, time complexity is O(n)
        """
        Do not return anything, modify nums in-place instead.
        """
        ## this just like the right rotate, from the bottom to head, 
        ## using reversal
        def reversal(list1,start,end):
            while start <= end:
                tmp = list1[start]
                list1[start] = list1[end]
                list1[end] = tmp
                start = start+1
                end = end-1
        times = k%len(nums)
        reversal(nums,0,len(nums)-1)
        reversal(nums,0,times-1)
        reversal(nums,times,len(nums)-1)
#def reversal(list1,start,end):
#    while start <= end:
#        tmp = list1[start]
#        list1[start] = list1[end]
#        list1[end] = tmp
#        start = start+1
#        end = end-1

a = [1,2]
rotate(a,3)
def rotate1(nums, k):   ## Time exceeded, O(n*k)
        """s
        Do not return anything, modify nums in-place instead.
        """
        ## this just like the right rotate, from the bottom to head, 
        ## using reversal
        times = k%len(nums)
        i = 1
        while i <= times:
            tmp = nums[-1]
            for j in range(len(nums)-1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = tmp
#            print('换了一次')
#            print(i)
            i = i+1
#b = [1,2,3,4,5,6,7]
#rotate1(b,3)        