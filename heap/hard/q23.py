# -*- coding: utf-8 -*-
"""
Created on Fri May 24 02:10:57 2019

@author: pengz
"""
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

hard

讲解: https://www.youtube.com/watch?v=Jq6QWstM66s
    https://www.youtube.com/watch?v=ptYUCjfNhJY
'''


import heapq
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeKLists(lists: [ListNode]) -> ListNode:  ## idea not by myself, using divide and conquer
                                                ## time is O(nklogk) = O(Nlogk)
    def merge2Lists(l1,l2):
        dummyhead = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur =cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummyhead.next
    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) ==2:
        l1 = lists[0]
        l2 = lists[1]
    else:
        first = 0
        last = len(lists)
        mid = (first+last)//2
        l1 = mergeKLists(lists[0:mid+1])
        l2 = mergeKLists(lists[mid+1:])
    return merge2Lists(l1,l2)

def mergeKLists2(self, lists):   ## 这个方法用了minheap, 本来是可以的, 但现在好像在leetcode通不过了,思想就是那两个链接
                                ## time is O(nklogk) = O(Nlogk)
    minHeap, head = [(node.val, node) for node in lists if node], ListNode(0)
    heapq.heapify(minHeap)
    p = head
    while minHeap:
        _, node = heapq.heappop(minHeap)
        if node.next: heapq.heappush(minHeap, (node.next.val, node.next))
        p.next = node
        p = p.next
    return head.next

'''
方法2在本地可以跑，在leetcode跑不了，所以换一个priority queue, 但是本地又跑不了, leetcode也跑不了
'''
from Queue import PriorityQueue
def mergeKLists3(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    dummyhead = cur = ListNode(0)
    q = PriorityQueue()
    for head in lists:
        if head:
            q.put((head.val, head))  ## 用val来进行排序，排序整个tuple
    while not q.empty():
        val, node = q.get()    ## get也相当于pop
        cur.next = ListNode(val)
        cur = cur.next
        node = node.next   ## 要找刚刚找出来的下一个
        if node:
            q.put((node.val, node))
    return dummyhead.next