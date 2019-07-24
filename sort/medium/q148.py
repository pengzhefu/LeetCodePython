# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:24:48 2019

@author: pengz
"""

'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#方法1参考： https://blog.csdn.net/fuxuemingzhu/article/details/79630742
class Solution:   ## 这道题有用到递归, 这方法时间是O(nlogn),但空间也是O(logn)， 不是O(1)
    def mergeList(self, l1: ListNode,l2: ListNode) -> ListNode:  ## 这就是很简单的两个已经排好序的链表的合并
        if not l1:
            return l2
        if not l2:
            return l1
        dummyhead = ListNode(0)
        cur = dummyhead
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next  ## 记得头也要移动
        if l1 == None:
            cur.next = l2
        if l2 == None:
            cur.next = l1
        return dummyhead.next
    
    def sortList(self, head: ListNode) -> ListNode:
        ## 首先, 利用快慢指针，把list进行一半分割
        if not head or not head.next: return head
        pre, slow, fast = head, head, head   ## 用这个方法可以避免递归过深, 但是不清楚原因
        while fast and fast.next:   ## 这是找一半的重要条件！ 只要fast和fast.next就行了！
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        ## 然后, 通过递归，不断进行分割+合并
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        ## 会切到最小以后才进行合并
        return self.mergeList(l1, l2)

#方法2参考：https://leetcode.com/problems/sort-list/discuss/206679/python-merge-sort-from-bottom-to-top-space-o1-time-on-log-n    
class Solution1:  ## 属于bottom-up， space O(1), time O(nlogn)
    def mergeList(self, l1: ListNode,l2: ListNode):  ## 这就是很简单的两个已经排好序的链表的合并
        dummyhead = ListNode(0)
        cur = dummyhead
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 == None:
            cur.next = l2
        if l2 == None:
            cur.next = l1
        while cur.next:  ## 要让cur走到这一组合并后的list的最末端, 也就是None前的最后一个节点
            cur = cur.next
        return [dummyhead.next,cur]  ## 返回这个list和这个list的最后一个点
    
    def split(self, head, n):  # Splits the list into two parts, first n element and the rest.
    # Returns the head of the rest， 把剩下部分的第一个拿出来
    ## 所以这个返回的是head割除了n之后剩余的rest, 但是这个时候head也只剩那n个,所以拿来拼的是那个head, 不是rest
        while n >1 and head:
            head = head.next
            n -=1
        if head:  ## 这一步其实是split的补充, 相当于n=1的时候, 还要割一次
            rest = head.next   ## 然后rest其实是割完了的头
        else:
            rest = None
        if head:
            head.next = None ## 把刚刚分出去的那部分全部弄没，相当于彻底割掉
        return rest
    
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        ## get the length of the whole list:
        length = 1
        cur = head.next
        while cur:
            length +=1
            cur = cur.next
        
        dummyhead = ListNode(0)
        dummyhead.next = head  ## 先把没排序的head直接加在dummyhead后面
        n = 1
        while n <length:
            ## 大致过程为： 先一个一个割开, 然后拼到一起, 再一个一个割开,再拼到一起,这是第一遍；
            ## 然后第二遍就是两个两个割开, 把这两两按顺序拼一起... 第三遍是4个4个割开, 拼一起这样
            #
            cur = dummyhead.next  ## cur就是head的头的第一个 
            tail = dummyhead   ## 然后tail每次就记录新加进来的排好东西的尾部
            while cur:
                l = cur  ## 这是第一个
                r = self.split(l, n)  ## 这是割完以后的第一个，最开始是第二个，其实这里才相当于把l割出来了
                cur = self.split(r, n)  ## 然后继续割，最开始的话出来第三个，其实这里才相当于把r割出来了
                ## 进行完这一步后, r的最后就是None了
                ## 所以一定要割两次，分成三部分，才能把前两部分没有多余内容进行合并排序
                merged = self.merge(l, r)  ## 然后进行合并
                tail.next = merged[0]   ## 先把合并好的贴到后面
                tail = merged[1]   ## 然后直接tail跳到结尾处, 相当于下一个弄好的要再接在结尾处后面
            # n = n << 1 
            n = n*2  ## 最开始是1个1个, 然后是2个2个, 4个4个...
        return dummyhead.next
    
    