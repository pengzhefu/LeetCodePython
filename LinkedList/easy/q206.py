# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:57:47 2019

@author: pengz
"""

'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def reverseList(self, head: ListNode) -> ListNode:   ## iteratively, written by my own, time O(n),space O(n)
        dummyhead = ListNode(0)
        while head:
            ins = ListNode(head.val)     ## 先创造目前的这个点的node
            ins.next = dummyhead.next    ## 把现在已经有的后面的所有关系放到创造的node的后面
            dummyhead.next = ins         ## 再把创造的node插到最开头
            head = head.next             ## 往下继续遍历
        return dummyhead.next
    
    
    def reverseList2(self, head: ListNode) -> ListNode:  ## recursively, not by myself, space & time is O(n)
        '''
        Solution: Start with node curr as head. 
        1. If curr is null, return. 
        2. If curr’s next element is null, this means it is the last node, so 
        make this as head because the last node will be the head of reversed list. Return. 
        3. Recursively traverse the list. 
        4. Set curr.next.next to curr. 
        5. Set curr.next to null
        '''
        if head== None or head.next == None: 
            return head
        else:
            
            ins = self.reverseList2(head.next)    ## 一直往后面找，相当于把前面的点放进一个stack里，搞完这个点的
                                                  ## 下一个后，会取出这个点来操作
            '''
            Assume from node nk+1 to nm had been reversed and you are at node nk.
            n1 → … → nk-1 → nk → nk+1 ← … ← nm
            We want nk+1’s next node to point to nk.
            So,
            nk.next.next = nk;
            nk.next = null;
            '''
            head.next.next = head   ## 这是最关键一步！让自己的下一个的下一个指回自己
            head.next = None        ## 然后因为自己相当于变成了最后一个点，那么自己的下一个就应该是None
                                    ## 相当于后面的都已经reverse过了，当前head的next是已经reverse过的最后一个点
                                    ## 然后让head.next的next指向head，相当于在已经reverse的里面插入head
            return ins              ## 关键是return的不是head,是由函数进行生成的node(list)
        
        
    def reverseList3(self, head: ListNode) -> ListNode:   ## reverse in-place, written by my own
                                                            ## idea from Haiming, space is O(1)?
        tail = None
        while head:
            tmp = head.next     ## 先把head后面的存下来
            head.next = tail    ## 然后把head后面的变成目前的tail,像一开始的话就是1后面变成跟着None,
                                ## 第二轮的话就是2后面变成跟着1+None
            tail = head         ## 更新tail，让tail变成目前的
            head = tmp          ## 往后遍历head
        return tail
            
            
        
    