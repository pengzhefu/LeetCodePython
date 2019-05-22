# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:23:56 2019

@author: pengz
"""

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest 
element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
## 我的第二道medium的题
def partition(nums,first,last):   ## 快排的方法
    pivot = nums[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and nums[leftmark] <= pivot:
            leftmark +=1
        while leftmark <= rightmark and nums[rightmark] >= pivot:
            last -=1
        if leftmark > rightmark:
            done = True
        else:
            nums[leftmark], nums[rightmark] = nums[rightmark], nums[leftmark]
    
    nums[first], nums[rightmark] = nums[rightmark], nums[first]
    return rightmark
        
def findKthLargest(nums: list, k: int) -> int:   ## written by my own
    target = len(nums) -k   ## 目标index
    index = partition(nums,0,len(nums)-1)
    while index != target:
        if index < target:
            tmp = index
            index = partition(nums,tmp+1,len(nums)-1)
        elif index > target:
            tmp = index
            index = partition(nums,0,tmp-1)
    return nums[index]



#nums = [3,2,3,1,2,4,5,5,6]
import heapq
nums = []
heapq.heappush(nums,1)
heapq.heappush(nums,2)
heapq.heappush(nums,3)
heapq.heappush(nums,1)
heapq.heappush(nums,10)
heapq.heappush(nums,6)
if len(nums) >5:
    heapq.heappop(nums)
#heapq.heapify(nums)
#heapq.heappush(nums,1)
#heapq.heappop(nums)
def findKthLargest2(nums: list, k: int) -> int:   ## using min heap
    ## 最小堆的话，最上面(根部)是最小的数，而且在迭代的过程中，只要这个数(a)大于最小堆的最小数，就把这个最小的数由a替换掉
    ## 这样当遍历全部数之后，相当于最小堆里面存了前k个最大的数，而且这个最小堆的最小数就是第K大的数，是这个堆里第k大，也是最小
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap) >k:
            heapq.heappop(min_heap)   ## heappop是直接丢出min heap的最小值，相当于在size >k之后在堆往里加比最小值大的数
    return min_heap[0]
    