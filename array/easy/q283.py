# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 02:37:20 2019

@author: pengz
"""

'''
Given an array nums, write a function to move all 0's to the 
end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
'''

def moveZeroes(nums):   ## written by my own, using double pointer
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 ## finding 0
        j = 0 ## finding not 0 and the index > i
        done = False
        while not done:  
            while nums[i] != 0:     ## 先找到0
                i = i+1
                if i >= len(nums):
                    done = True
                    break
            while nums[j] == 0 or j <=i:  ## 然后找到在刚刚找到的0后面的那个不为0的数
                j = j+1
                if j >= len(nums):
                    done = True
                    break
            
            if not done:
                nums[i], nums[j] = nums[j],nums[i]
            print(nums)
nums = [1,2,0,3,0,12,3,0,4,0,0,5,0]
moveZeroes(nums)


def moveZeroes1(nums):   ## 别人的方法，也类似于双指针，其实就是直接把不为0的数，一个个换到最前面去,
                            ## 但是这种方法如果开头的非0数比较多，会调换次数较多
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
            print(nums)  
#moveZeroes1(nums)