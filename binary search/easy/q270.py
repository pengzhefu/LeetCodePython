# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:20:25 2019

@author: pengz
"""

'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

'''
## 这道题我没写出来，看的别人的答案
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:   ## 这道题其实很简单，就相当于在这个列表里要找最小，
                                                                    ## 随着index增加一直更新
        ret = root.val   ## ret就是最后要输出的答案
        while root:
            if abs(root.val - target) < abs(ret-target):    ## 如果这个值变小了,那就更新ret, 否则就一直不更新
                ret = root.val
            if target > root.val:
                root = root.right
            elif target < root.val:
                root = root.left
            else:
                return root.val
        return ret
        
        
            