# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:34:32 2019

@author: pengz
"""

'''
Convert a BST to a sorted circular doubly-linked list in-place. Think of 
the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
'''
 ## 这道题没写出来, 看的别人答案，重点是要用一个inorder的遍历来把BST变成一个按顺序的linkedlist,这人是个天才！
class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeToDoublyList(self, root: Node()) -> Node():
        if not root: 
            return None
        dummy = Node(0, None, None)  ## 用一个dummy来初始化
        prev = dummy   ## 但是其实移动的是prev
        stack = []  ## 用stack来进行中序遍历
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left= prev  ## 这是第一个和中序遍历不一样的一步, 取出这个点以后, 先让他的前面和之前找到的点连起来，
                            ## 他的左边是前一个取出的点，
            prev.right = node   ## 然后让前一个取出的点的右边是这个点，完成一个circular
            prev = node     ## 然后把这个点变成前一个点
            node = node.right   ## 然后进行中序遍历，往右找
        dummy.right.left = prev   ## 把刚刚找到的prev的linkedlist插进去dummy中 （右边的左边就是头的后面）
        prev.right = dummy.right  ## 再把dummy里本来后面的东西插到刚刚完成的linkedlist的右边
        return dummy.right   ## 最后