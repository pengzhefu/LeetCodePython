# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:49:06 2019

@author: pengz
"""

'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''

import heapq
'''
Adding a number num:

    1. Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi. 
    So remove the largest element from lo and offer it to hi.
    2. The min-heap hi might end holding more elements than the max-heap lo, 
    after the previous operation. We fix that by removing the smallest element from hi and offering it to lo.

The above step ensures that we do not disturb the nice little size property we just mentioned.
'''
class MedianFinder():   ## using two heaps, idea from solution, written by my own, time is O(logN)
                      ## time = O(5logN) + O(1)
 '''
Adding number 41
MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
Median is 41
=======================
Adding number 35
MaxHeap lo: [35]
MinHeap hi: [41]
Median is 38
=======================
Adding number 62
MaxHeap lo: [41, 35]
MinHeap hi: [62]
Median is 41
=======================
Adding number 4
MaxHeap lo: [35, 4]
MinHeap hi: [41, 62]
Median is 38
=======================
Adding number 97
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97]
Median is 41
=======================
Adding number 108
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97, 108]
Median is 51.5
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []  ## 最小堆储存比较大的那一半
        self.maxheap = []  ## 最大堆储存比较小的那一半, 输出的时候记得取反

    def addNum(self, num: int) -> None:
        tmp = -num
        heapq.heappush(self.maxheap,tmp)  ## 新添加的数都先进最大堆，也就是前一半
        if len(self.maxheap) > 1:    ## 实现第一步，添加了以后把最大堆(前一半)的最大的放进最小堆中
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):  ## 实现第二步, 如果最小堆的个数比最大堆的多,把最小堆的最小的移到最大堆
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):  ## 如果现在总共是奇数个数
            return float(-self.maxheap[0])
        elif len(self.maxheap) == len(self.minheap): ## 偶数个数
            ret = (-self.maxheap[0] + self.minheap[0])/2.0
            return ret


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()