# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 03:56:14 2019

@author: pengz
"""
'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and 
others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list 
does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

'''
https://www.polarxiong.com/archives/LeetCode-448-find-all-numbers-disappeared-in-an-array.html
'''
def findDisappearedNumbers(nums: [int]) -> [int]:  ## 就是因为每一个都可以对应一个index, 
    for n in nums:
        nums[abs(n) - 1] = -abs(nums[abs(n) - 1])   ## 把有的那个的数字作为index, 让那个数变成负的
                                                    ## 记得是要减1的, 因为index是从0开始的
#        print(nums[abs(n)-1])
    return [i + 1 for i, n in enumerate(nums) if n > 0]  ## 重新遍历一遍, 如果有正数, 说明这个index不存在, 那么返回+1的值

nums = [4,3,2,7,8,2,3,1]
ret = findDisappearedNumbers(nums)
