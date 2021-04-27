# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution1(self, pRoot): # 从上向下, 耗时多, 不属于标准解法
        # write code here
        def depth(root):
            """求当前节点的深度
            Args:
                root: 节点
            Returns:
                返回节点深度
            """
            # 节点为空，返回高度 0
            if not root:
                return 0
            # 否则返回左右子树最大高度值 +1
            return max(depth(pRoot.left), depth(pRoot.right)) + 1   # 这里加1是非常关键的！因为是计算总层数, 所以在自己这一层其实也是一个高度,就算是个空的也是一层

        # 根节点为空，直接返回 True
        if not pRoot:
            return True

        # 否则递归判断
        # 1. 当前子树是否平衡
        # 2. 当前子树左子树是否平衡
        # 3. 当前子树右子树是否平衡
        return abs(depth(pRoot.left)-depth(pRoot.right)) <= 1 and self.isBalanced(pRoot.left) and self.isBalanced(pRoot.right)

    def IsBalanced_Solution2(self, pRoot):  # 从下往上, 正经解法 https://segmentfault.com/a/1190000023661751
        def depth(root):
            if not root:
                return 0
            left_height = depth(root.left)
            if left_height == -1:
                return -1
            right_height = depth(root.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) <= 1:
                return max(left_height, right_height) +1
            else:
                return -1
        return depth(pRoot) >= 0
              

        
        