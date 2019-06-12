# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:47:57 2019

@author: pengz
"""

'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root 
node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

 

Note:

    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    You may assume that next() call will always be valid, that is, there will be at least a next
    smallest number in the BST when next() is called.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.points = []
        while root:
            self.points.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmp = self.points.pop()
        point = tmp.right   ## 在找到当前最小点a后, 要先去他的右子树找, 因为他的最左边的左子节点已经找过了，所以去找右子树，a的右子树中会有下一个最小的，
                            ## 如果a没有右子树的话，才返回到a的父节点，就是下一个最小的
        while point:
            self.points.append(point)
            point = point.left  ## 但还是一样，一直往一个子树的最左边找
        return tmp.val
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.points) >0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()