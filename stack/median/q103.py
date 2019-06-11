# -*- coding: utf-8 -*-
"""
Created on Wed May 22 01:10:01 2019

@author: pengz
"""
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        ret = []
        stack = []   ## stack是放每次那一层都有什么,
        stack.append(root)
        n = 1
        while len(stack) != 0 and root:
            tmp = []
            tmp_stack = []  ## tmp_stack是放这一层的下一层都有哪些点
            # print('stack')
            # for item in stack:
            #     print(item.val)
            #     print('=====')
            while stack:
                point = stack.pop()
                tmp.append(point.val)
                if n %2 != 0:   ## 奇数层，先放左边，再放右边
                    # print('here')
                    if point.left:
                        tmp_stack.append(point.left)
                    if point.right:
                        tmp_stack.append(point.right)
                else:   ## 偶数层，先放右边，再放左边
                    if point.right:
                        tmp_stack.append(point.right)
                    if point.left:
                        tmp_stack.append(point.left)
            ret.append(tmp)
            stack = tmp_stack[:]
            n +=1
        return ret