# -*- coding: utf-8 -*-
"""
Created on Wed May 22 00:57:31 2019

@author: pengz
"""

'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        ret = []
        stack = []
        while root or stack:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.right
            if stack:
                tmp = stack.pop()
                root = tmp.left
        ret.reverse()
        return ret