# -*- coding: utf-8 -*-
"""
Created on Thu May  9 02:33:42 2019

@author: pengz
"""

'''
 You are given two arrays (without duplicates) nums1 and nums2 where nums1’s 
 elements are subset of nums2. Find all the next greater numbers for nums1's elements 
 in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its 
right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for 
    it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
这道题的意思是，每个nums1的数，然后去找他在nums2的位置以后，第一个比他大的数，所以只要针对nums2这个大集进行操作就行了
这题没有写出来，看的答案，用的stack，好像还属于单调栈的一种?
这道题用的就是单调递减栈，而且是从左往右遍历，可以找到这个元素的右边，从左起第一个比他大的数
单调递增栈，而且是从左往右遍历，可以找到这个元素的右边，从左起第一个比他小的数
这里的单调增或者减，都是从底 ——> 顶
'''

nums2 = [2,3,5,1,0,7,3]

            
def nextGreaterElement(nums1: [int], nums2: [int]) -> [int]:  ## method from solution, code written by myself
                                        ## 这道题要用到一个stack,来保证一个单调性， space O(m+n), time O(m+n)
    stack = []
    ret = {}
    i = 0
    while i < len(nums2):
        if len(stack) == 0:
            stack.append(nums2[i])   ## 如果栈是空的，就把当前遍历到的元素加进去
        else:
            if nums2[i] <= stack[-1]:   ## 如果比当前栈顶的还小，就也加进去
                stack.append(nums2[i])
            else:
                tmp = stack.pop()    
                ret[tmp] = nums2[i]
                continue  ## 注意，这里需要直接返回循环，i不能变，因为stack中还有别的也可能需要用到当前nums2[i]
                          ## 比如现在nums2[i] =7, stack中有[5,3], 那么先要3和7配对，然后5和7配对，直到有比7大的，或者栈空了
                          ## 要把这个元素放到栈底
        i = i+1
    if len(stack) !=0:
        for char in stack:
            ret[char] = -1
    ans = []
    for char in nums1:
        ans.append(ret[char])
    return ans