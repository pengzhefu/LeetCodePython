# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:40:58 2019

@author: pengz
"""

'''
Design a class to find the kth largest element in a stream. Note that it is the kth 
largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer 
array nums, which contains initial elements from the stream. For each call to the 
method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.

easy
'''
import heapq
class KthLargest():   ## 思想就是用一个minheap维护出前k大的数

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for num in self.nums:
            heapq.heappush(self.heap,num)
            if len(self.heap) >k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:   ## 一开始可能heap的长度不够长，先添加
            heapq.heappush(self.heap,val)
            return self.heap[0]
        if val <= self.heap[0]:  ## 如果要添加进来的数都比heap最小的数小，那就不管
            return self.heap[0]
        else:   ## 添加的新的大于minheap最小的数，重新排列一次
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
            return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)