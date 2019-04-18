# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:15:29 2019

@author: pengz
"""

'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the 
position (0-indexed) in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

'''
## head里面是可以有重复数字的
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):    ## written by my own, using dict, space is O(n), time is O(n)
        """
        :type head: ListNode
        :rtype: bool
        """
        ret = {}
        while head:
            if head not in ret:  ## we could only use func in to test whether the key is in dict
                ret[head] = 1     ## key is not the value of head, but just the whole instance/obj of head
                head = head.next
            else:
                return True
        return False
    
    def hasCycle2(self,head):   ## 总共两个指针，如果是个circle，最后这两个不同速度的指针一定会相遇, space is O(1)
        fast = head  ## 总共两个指针，一个走得慢，一个走得快，
        slow = head   ## slow每次前进一格，fast前进两格
        
        while slow and fast and fast.next:   ##  需要两个指针以及他们的下一个都不是none，保证有效
                                                        ##这样就可以排除none和长度为1的时候
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  ##检查的不是值相不相等，是本身这个点是不是同一个点
                return True
        return False
            
            

