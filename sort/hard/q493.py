# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 03:51:43 2019

@author: pengz
"""
'''
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

Note:

    The length of the given array will not exceed 50,000.
    All the numbers in the input array are in the range of 32-bit integer.
'''
    
#[4,5,6]
#[1,2,3]
import bisect
def reversePairs(nums: [int]) -> int:  ##using bisect, similar as q315, time is O(nlgn) in average, worst O(n^2)
    if not nums:
        return 0
    ret = 0
    ## 关键就在于, 每次放进去的都是二倍的值
    tmp = [2*nums[len(nums)-1]]  ## 记得这里要放进去的是二倍以后的, 从最后一位开始放
    for i in range(len(nums)-2,-1,-1):
        ret += bisect.bisect_left(tmp,nums[i])
        bisect.insort(tmp,2*nums[i])  ## 这里要插入的也是乘以二倍以后的 
    return ret


## 两个讲解：https://www.youtube.com/watch?v=tmzg_XGg5dw https://www.youtube.com/watch?v=TXOXKILPMVI
## 代码Java合理版：https://leetcode.com/problems/reverse-pairs/discuss/97280/very-short-and-clear-mergesort-bst-java-solutions
## Python参考: https://leetcode.com/problems/reverse-pairs/discuss/237205/Python-merge-sort-solution-with-explanation
def reversePairs1(nums: [int]) -> int: ## time O(nlgn)
    def mergeSort(array,start,end):  ## array is a list, start & end are the indexs, return type is int
        if start >= end:
            return 0
        mid = start + (end-start)//2
        count =0  ## count一开始等于0
        count += mergeSort(array, start,mid)  ## 先一直分到最小一片, 然后再进行排序, 跟mergeSort一样
        count += mergeSort(array, mid+1,end)  ## 先一直分到最小一片, 然后再进行排序, 跟mergeSort一样
        
        ## 比纯mergeSort添加的一步, 先找出来有多少个符合要求i < j and nums[i] > 2*nums[j]的, 然后再排序
        p = start
        q = mid+1
        ## 其实这相当于两段, 前start - mid是一段已经排好的, mid+1 - end是另一段已经排好的, 顺序都是从小到大的
        ## 而这两段里本身, 再之前的递归里是已经有数过了, 所以比较这两段就行了
        while p <= mid and q <=  end:
            if nums[p] > 2*nums[q]:
                count += mid-p+1  ## 就如果p已经满足条件了, 那么比p大的都会满足条件, 那么这一段一共有mid-p+1个
                q +=1  ## 然后移动q, 看看是不是比后半段的更大的也满足要求
            else:
                p +=1  ## 如果不满足,就要找前一段里更大的,
        
        ## 找完个数以后, 再进行sort
        array[start : end + 1] = sorted(array[start : end + 1])  ## 这里偷懒, 用了内置sort方法, 避免TLE
        ## 用下面这段会TLE
#        left, right = nums[start:mid+1], nums[mid+1:end+1]
#        idx = start
#        p1, p2 = 0, 0
#        while p1 < len(left) or p2 < len(right):
#            if p1 < len(left) and (p2 == len(right) or left[p1] < right[p2]):
#                nums[idx] = left[p1]
#                p1 += 1
#            else:
#                nums[idx] = right[p2]
#                p2 += 1
#            idx += 1
        return count
    return mergeSort(nums,0,len(nums)-1)
                
        