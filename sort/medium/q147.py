# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:06:56 2019

@author: pengz
"""

'''
Algorithm of Insertion Sort:

    Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    It repeats until no input elements remain.


Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
其实就是对于linked list进行插入排序
medium
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode: ## https://blog.csdn.net/fuxuemingzhu/article/details/80785630
        if not head or not head.next:  ## 当linked list的长度小于2的时候
            return head
        dummyhead = ListNode(0)  ## linked list必备一步
        dummyhead.next = head
        while head.next:
            if head.val <= head.next.val:   ## 如果这个小于后面的, 说明正常, 继续往后遍历
                head = head.next
            else:
                ## 下面这两行是一个完整的拿出一个node的代码
                tmp = head.next  ## 要拿出来的是小的那个，把小的插到前面去
                head.next = head.next.next  ## 把小的拿出来以后, 要把他(小的)后面的再连接覆盖回去(到大的后面), 这一步非常重要！！！
                                            ##这两步加起来才是完整的从一个linked list里面取出node的步骤
                node = dummyhead  ## node是遍历整个dummyhead开始
                while node.next and node.next.val < tmp.val:  ## 然后找到比这个tmp大的第一个点,从头开始找
                                                            ## 但是条件要记得确保有node.next, 所以是用node.next
                                                            ## 找到了node.next大于tmp, 但是node是小于tmp的
                    node = node.next
                ## 下面这两句是一个完整的插入一格node的两行代码
                tmp.next = node.next
                node.next = tmp
        return dummyhead.next
        