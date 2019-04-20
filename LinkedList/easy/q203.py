# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:01:16 2019

@author: pengz
"""
'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def removeElements(self, head: ListNode, val: int) -> ListNode: ## time complexity is O(n), written by myself
        dummyhead = cur = ListNode(0)
        cur.next = head   ## 用cur来移动，把head接在后面
        while cur.next:   ## 就是只要cur.next还没移到None，也就是cur还没到最后一位的时候
            while cur.next and cur.next.val != val:
                cur = cur.next
            if cur.next:   ## if条件是为了排除当最后一位不等于val,这时候cur已经移到了最后一位,不应该再跳过了
                cur.next = cur.next.next    ## 进行跳过
        return dummyhead.next
    
    def removeElements2(self, head: ListNode, val: int) -> ListNode:   ## recursive version, not by myself
        if not head:
            return None
        if head.val == val:
            head = self.removeElements(head.next,val)
        else:
            head.next = self.removeElements(head.next,val)
        return head
    
    def removeElements3(self, head: ListNode, val: int) -> ListNode:   ## similar as the first one, not by myself
                                                                        ## 可能比方法1快
        node = head
        p = dum = ListNode(None)
        while node != None:       ## 这方法相当于把node的点添加进dum的后面
            if node.val == val:
                node = node.next  ## 相当于i= i+1
                p.next = None     ## 这一步非常必要，因为如果最后一位是val的话，需要变成none，就算之前是none只要在下一次改动就行了
            else:
                p.next = node
                node = node.next## 相当于i= i+1
                p = p.next
        return dum.next
            
            
            