# -*- coding: utf-8 -*-
"""
Created on Thu May  2 02:46:54 2019

@author: pengz
"""

'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique 
(except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

 

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000
Medium
'''
import heapq
nums = []
dict1 = {'1':-2,'2':-4,'3':-6,'-9':-8}
heapq.heappush(nums,dict1)
#heapq.heappush(nums,dict1['2'])
#heapq.heappush(nums,dict1['3'])
#heapq.heappush(nums,-1)
#heapq.heappush(nums,-10)
#heapq.heappush(nums,-7)
#heapq.heappush(nums,-6)
#heapq.heappush(nums,-9)
#if len(nums) > 7:
#    heapq.heappop(nums)
#heapq.heappushpop(nums,-11)
def kClosest(points, K: int):   ## using heapq to make a max heap, written by my own, the quickest and best
    ret = []
    heap = []
    tmp = {}   ## key is the dist, and the value is the list of points
    for item in points:
        res = -(item[0] **2 + item[1] **2)   ## 添加负号是要让最小堆变成最大堆来使用
        if res not in tmp:
            tmp[res] = [item]
        else:
            tmp[res].append(item)
        heapq.heappush(heap,res)
        if len(heap) > K:
            heapq.heappop(heap)
    i = 0
    while i < len(heap):   ## 防止重复的
        for points in tmp[heap[i]]:
            ret.append(points)
        buf = heap[i]
        while i < len(heap) and heap[i] == buf: ## 这一步防止重复
            i= i+1
    return ret
import random
def kClosest2(points, K: int):  ## using quicksort solution, method from the solution
    dist = lambda i: points[i][0]**2 + points[i][1]**2   ## dist是由迭代器产生的，所以其实不占空间，但也没法直接返回

    def sort(i, j, K):
        # Partially sorts A[i:j+1] so the first K elements are
        # the smallest K elements.
        if i >= j: return

        # Put random element as A[i] - this is the pivot
        k = random.randint(i, j)
        points[i], points[k] = points[k], points[i]

        mid = partition(i, j)
        if K < mid - i + 1:
            sort(i, mid - 1, K)
        elif K > mid - i + 1:
            sort(mid + 1, j, K - (mid - i + 1))

    def partition(i, j):   ## 这就是快排的方法
        # Partition by pivot A[i], returning an index mid
        # such that A[i] <= A[mid] <= A[j] for i < mid < j.
        oi = i
        pivot = dist(i)
        i += 1

        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j: break
            points[i], points[j] = points[j], points[i]

        points[oi], points[j] = points[j], points[oi]
        return j

    sort(0, len(points) - 1, K)
    return points[:K]

def kClosest3(points, K): ## written by my own, but not better than the solution, exceed time limit
    dist_list = []   ## storing dist
    res = {}        ## stroing points
    ret = []
    for point in points:
        dist = point[0] **2 + point[1] **2
        dist_list.append(dist)
        if dist in res:
            res[dist].append(point)
        else:
            res[dist] = [point]
    target = K-1
    index = partition(dist_list,points,0,len(dist_list)-1)
    while index != target:
        if index > target:
            index = partition(dist_list,points,0,index-1)
        elif index < target:
            index = partition(dist_list,points,index+1,len(dist_list)-1)
    return points[:K]

def partition(self, nums, points, first,last):
    pivot = nums[first]
    leftmark = first +1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and nums[leftmark] <= pivot:
            leftmark += 1
        while leftmark <= rightmark and nums[rightmark] >= pivot:
            rightmark -=1
        if leftmark > rightmark:
            done = True
        else:
            nums[leftmark], nums[rightmark] = nums[rightmark], nums[leftmark]
            points[leftmark], points[rightmark] = points[rightmark], points[leftmark]   ## 换nums的时候顺便换了points
    nums[first], nums[rightmark] = nums[rightmark], nums[first]
    points[first], points[rightmark] = points[rightmark], points[first]   ## 换nums的时候顺便换了points
    return rightmark