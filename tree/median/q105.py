# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 01:25:43 2019

@author: pengz
"""

'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''
## 灵感来自https://www.youtube.com/watch?v=S1wNG5hx-30 但没有完全按照
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        current = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])  ## 知道顶点在in中的index的位置, 也能知道有多少左子树的大小
        current.left = self.buildTree(preorder[1:1+idx], inorder[:idx])  
        current.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return current