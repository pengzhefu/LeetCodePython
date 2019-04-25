# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:53:22 2019

@author: pengz
"""

'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

 

Note:

    The number of nodes in the given list will be between 1 and 100.

'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def middleNode(self, head: ListNode) -> ListNode: ## using two pointer, fast & slow, written by my own
        if not head or not head.next:
            return head
        else:
            fast = head
            slow = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            if fast.next:    ## 如果fast指针没到末尾,还有fast.next， 说明原来长度为偶数
                return slow.next
            else:            ## 如果fast指针到了末尾,没有fast.next了， 说明原来长度为奇数
                return slow