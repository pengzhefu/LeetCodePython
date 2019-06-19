# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 00:45:59 2019

@author: pengz
"""
'''
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, 
we must pay them according to the following rules:

    Every worker in the paid group should be paid in the ratio of their quality compared to 
    other workers in the paid group.
    Every worker in the paid group must be paid at least their minimum wage expectation.

Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 

 

Note:

    1 <= K <= N <= 10000, where N = quality.length = wage.length
    1 <= quality[i] <= 10000
    1 <= wage[i] <= 10000
    Answers within 10^-5 of the correct answer will be considered correct.


'''
## 要有两个排序, 一个是从小到大的普通排列价性比(wage/quality)，一个是heap排列的quality,
## 每次有新的上来以后就要把之前最大的quality移除, 把总和减去那个以后再加上新的, 能这么做是因为每次的比例都是采取最高的那个,
## 而且这个已经按顺序排好了， 英文解释在下面
## https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)
import heapq
quality = [10,20,5]
wage = [70,50,30]
K = 2
def mincostToHireWorkers(quality: [int], wage: [int], K: int) -> float: ## code written by my own, idea not mine
    wq = sorted([[quality[i],wage[i]/quality[i]] for i in range(len(wage))], key = lambda item: item[1])
    heap = [] ## maxHeap
#    ret = float('inf')
    ret = 0
    tmp_sum = 0
    for i in range(K):
        tmp_sum += wq[i][0]
        heapq.heappush(heap,-wq[i][0])
    ret = wq[K-1][1] * tmp_sum
#    print(wq)
#    print(heap)
    for i in range(K,len(wq)):
        new_item = wq[i][1]
        tmp_sum = tmp_sum - (-heapq.heappop(heap)) + wq[i][0]
#        print(new_item*tmp_sum)
        ret = min(ret,new_item*tmp_sum)
        heapq.heappush(heap,-wq[i][0])
    return ret
    

ret = mincostToHireWorkers(quality, wage, K)