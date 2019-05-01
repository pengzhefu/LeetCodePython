# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:56:17 2019

@author: pengz
"""

'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6

 

Example 2:

Input: [1,2,3,4]
Output: 24

 

Note:

    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''
## 这题要考虑存在负数的情况
class Solution:    
    def maximumProduct(self, nums) -> int:    ## solution的方法，先按升序进行排列，然后比较
                                            ## time is O(nlogn)
                                                ## index=0 or 1的两个数可能是绝对值最大的两个负数，然后和最大的三个数乘积
                                                ## 进行比较
        nums.sort()
        n = len(nums)
        return max(nums[0]*nums[1]*nums[n-1],nums[n-3]*nums[n-2]*nums[n-1])
    
def maximumProduct2(nums) -> int:   ## min1最小，max3最大
                                    ## time is O(n)
    ## 先在最开始的三个中进行排序
    if nums[2] >= nums[1] and nums[2] >= nums[0]:
        max3 = nums[2]
        if nums[1] >= nums[0]:
            min2 = max2 = nums[1]
            min1 = max1 = nums[0]
        else:
            min2 = max2 = nums[0]
            min1 = max1 = nums[1]
    elif nums[1] >= nums[2] and nums[1] >= nums[0]:
        max3 = nums[1]
        if nums[2] >= nums[0]:
            min2 = max2 = nums[2]
            min1 = max1 = nums[0]
        else:
            min2 = max2 = nums[0]
            min1 = max1 = nums[2]
    elif nums[0] >= nums[2] and nums[0] >= nums[1]:
        max3 = nums[0]
        if nums[2] >= nums[1]:
            min2 = max2 = nums[2]
            min1 = max1 = nums[1]
        else:
            min2 = max2 = nums[1]
            min1 = max1 = nums[2]
    ## Starting scan
    for i in range(3,len(nums)):
        if nums[i] > max3:
            max1 = max2
            max2 = max3
            max3 = nums[i]
        elif nums[i] > max2:
            max1 = max2
            max2 = nums[i]
        elif nums[i] > max1 :
            max1 = nums[i]
        elif nums[i] < min1:
            min2 = min1
            min1 = nums[i]
        elif nums[i] < min2:
            min2 = nums[i]
    return max(min1*min2*max3,max1*max2*max3)
    


a,b,c = maximumProduct2([9,1,2,3,4,5,-1,-2,-3,14,7,-9])
            
            
        