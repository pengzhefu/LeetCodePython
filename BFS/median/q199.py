# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 03:15:34 2019

@author: pengz
"""

'''
Given a binary tree, imagine yourself standing on the right side of it, return the 
values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
def rightSideView(root: TreeNode) -> [int]:  ## 先用BFS试一下
    ret = []
    queue = deque()
    queue.append(root)
    if not root:
        return ret
    while len(queue) !=0:
        num = len(queue) ## 
        i = 1
        while i <= num:
            vertex = queue.popleft()
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
            if i == num:
                ret.append(vertex.val)
            i += 1
    return ret

def rightSideView1(root: TreeNode) -> [int]:  ## DFS
    ret = []
    res = []
    def dfs(node,level,ret):
        if not node:
            return 
        if level >= len(ret):
            ret.append([])
        ret[level].append(node.val)
        dfs(node.left, level+1, ret)
        dfs(node.right, level+1, ret)
    dfs(root,0,ret)
    for tmp in ret:
        res.append(tmp[-1])
    return res