# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:46:49 2019

@author: pengz
"""

'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z 
where different letters represent different tasks. Tasks could be done without original order. 
Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must 
be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
'''

def leastInterval(tasks: [str], n: int) -> int:  ## 最大频率为k, 有k的总共有p个, ans是(k-1)*(n+1)+p, time O(n)
    counts = {}
    max_count =0
    num = 0
    for task in tasks:
        if task not in counts:
            counts[task] =1
        else:
            counts[task] +=1
        if counts[task] > max_count:   ## 顺便找出最大频率, 以及达到最大频率的个数
            max_count = counts[task]
            num = 1
        elif counts[task] == max_count:
            num +=1
    # print(num)
    ret = max(len(tasks),(max_count-1)*(n+1)+num)   ## 这一步要进行比较, 具体想法参考https://leetcode.com/problems/task-scheduler/discuss/308137/topic
    return ret

import heapq
def leastInterval2(tasks: [str], n: int) -> int:  ## 正规解法, 用heap, time is O(nlogn)
                                                    ## 这个也可以作为判断或者输出一个至少相隔n个字符的重排字符串的答案
    ret = 0
    counts = {}
    for task in tasks:
        if task not in counts:
            counts[task] =1
        else:
            counts[task] +=1
    heap = []  ## using maxHeap
    buf = []  ## 储存那些等等还要放回去的, 也就是剩余使用次数还>=1的
    for task in counts:
        heapq.heappush(heap,(-counts[task],task))
    while heap:
        slots = n+1   ## 因为间隔为n， 所以一排里面总共的坑位是n+1
        while slots > 0 and heap:   ## 这个heap条件是当所有的不同项目都插入过一次的时候, 可以就是用idle
            time, task = heapq.heappop(heap)
            slots -= 1  ## 坑位被占了一个, 需要减1
            ret += 1    ## 每次要记得让答案+1， 用了一个坑位
            if time < -1:  ## 一定是小于-1才行, 
                buf.append((time+1, task))   ## 相当于让还能用的次数减1, 然后重新进堆排
        for item in buf:    ## 要先把还能用的放回heap
            heapq.heappush(heap,item)
        if heap:   ## 这里有两种情况, 如果项目个数够插入坑位, 那么slots就会是0; 如果不够少于坑位数, 那么slots就等于需要的idle数
                   ## 然后一直到最后, heap都空了, 所有项目的每一个都用了, heap空的, 就也不需要加idle了
                   ## 所以,在这个判断之前，一定要先把heap还原
            ret += slots
        buf = []   ## 记得把buf每次都要清空
    return ret
    