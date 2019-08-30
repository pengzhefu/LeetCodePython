# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 00:16:55 2019

@author: pengz
"""

'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
def levelOrder(root: TreeNode) -> [[int]]:  ## 用deque实现queue的功能, 也就是FIFO, 用来实现BFS
    queue = deque() ## 用deque的原因是因为popleft是O(1), 不然list的pop(0)的时间是O(n)
    queue.append(root)
    ret = []
    if not root:
        return ret
    while len(queue) != 0:
        num = len(queue)  ## 这一层需要的pop次数
        i = 1
        tmp = []
        while i <= num:   ## pop出这一层的就行了, 下一层的会添加进来
            vertex = queue.popleft()  ## 先pop出这一层的第一个点
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
            tmp.append(vertex.val)
            i += 1
        ret.append(tmp)
    return ret

## https://www.youtube.com/watch?v=IWiprpdSgzg   给DFS的解释
def levelOrder2(root: TreeNode) -> [[int]]:  ## 用DFS解, 因为是按层来所以比较关键的就是要知道目前到了第几层
    ret = []
    def dfs(node,level,ret):
        if not node: ## base case
            return 
        if level >= len(ret): ## 这里一定是大于等于, 用等于是为了满足一开始还在第一层的时候, 初始化, 就需要用等于来添加
                                ## 这里level也相当于是一个针对这每个小list的index
            ret.append([])  ## 也就是说每到新的一层, 记得要添加进一个新的list, 用来装这一层的点
        ret[level].append(node.val)  ## 把这点在相应的level的小list里添加上
        dfs(node.left, level+1, ret) ## 这两步就相当于DFS里的, 深度优先, 先往深一层level走
        dfs(node.right, level+1, ret)
    dfs(root,0,ret)
    return ret