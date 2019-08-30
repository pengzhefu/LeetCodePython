# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 01:21:53 2019

@author: pengz
"""

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  ## code written by my own
        dummyhead = ListNode(0)
        cur = dummyhead
        jinwei = 0
        while l1 and l2:
            tmp1 = l1.val
            tmp2 = l2.val
            res = tmp1 + tmp2 + jinwei  ## res记录暂时加的结果
            if res >= 10:
                # print('here')
                res = res -10
                jinwei = 1
            else:
                jinwei = 0
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1 and jinwei != 0:
                res = l1.val +jinwei
                if res >=10:
                    jinwei =1
                    res = res-10
                else:
                    jinwei = 0
                cur.next = ListNode(res)
                cur = cur.next
                l1 = l1.next
            cur.next = l1
        if l2:
            while l2 and jinwei != 0:
                res = l2.val +jinwei
                if res >=10:
                    jinwei =1
                    res = res-10
                else:
                    jinwei = 0
                cur.next = ListNode(res)
                cur = cur.next
                l2 = l2.next
            cur.next = l2
        if jinwei ==1:
            cur.next = ListNode(jinwei)
        return dummyhead.next