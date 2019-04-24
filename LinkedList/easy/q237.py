# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:04:24 2019

@author: pengz
"""

'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9
 after calling your function.

Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 
after calling your function.

 

Note:

    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.

'''
## 这道题的重点在于，我们现在给的不是一个完整的node的list，而是单独的一个node，那么怎么删掉这个node呢？
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):  ## not written by my own
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''
        因为这道题给的只是一个node，所以不能用以前想到的用前面的替换的方法，不能用q203那种
        所以只要直接用后面的值替换掉这个node，再把后一个节点删除就行
        '''
        node.val = node.next.val  ## 后面的节点的值替换掉这个节点
        node.next = node.next.next ## 删掉后面的节点
