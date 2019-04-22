# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:47:34 2019

@author: pengz
"""

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def isPalindrome(self, head: ListNode) -> bool:    ## Written by my own, not in O(n), 
                                                        ## time is O(3n) and space is O(n) not O(1)
        dummyhead = ListNode(0)
        cur = head
        while cur:
            tmp = ListNode(cur.val)
            tmp.next = dummyhead.next
            dummyhead.next = tmp
            cur = cur.next
        # new = dummyhead.next
        while dummyhead.next and head:
            if dummyhead.next.val != head.val:
                return False
            dummyhead.next = dummyhead.next.next
            head = head.next
        return True
    
    def isPalindrome2(self, head: ListNode) -> bool: ## idea inspired by Haiming, code written by my own
        if head == None or head.next == None:
            return True
        latter = self.findLatter(head)
        latter = self.reverseList(latter)
        while latter:
            if head.val != latter.val:
                return False
            latter = latter.next
            head = head.next
        return True
    def findLatter(self, head: ListNode) -> ListNode: ## 找中点
                                                    ## 用快慢指针找列表的后一半,当如果是奇数的时候,slow中间;
                                                    ## 偶数的话,slow偏左，所以要取后一半，就要输出slow.next
        fast = head
        slow = head
        while fast.next and fast.next.next:     ## 当快指针到达极限,不能再跳，(位于跳出边缘时候),slow到了目标位置
                                                ## 这个限制条件是要根据长度的奇偶数,
            slow = slow.next
            fast = fast.next.next
        return slow.next      ## 这题只取slow.next，不用分情况讨论是因为奇数长度的话只需要不含中点的后一半  
    def reverseList(self,head:ListNode) -> ListNode:  ## in-place reverse method, like q206, O(1) space
        tail = None
        while head:
            tmp = head.next
            head.next = tail
            tail = head
            head = tmp
        return tail
    