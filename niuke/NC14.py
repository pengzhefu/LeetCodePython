# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @return int整型二维数组
#
class Solution:
    def zigzagLevelOrder(self , root ):
        # write code here
        from collections import deque
        queue = deque()
        ret = []
        queue.append(root)
        level = 1
        if not root:
            return ret
        while len(queue) != 0:
            level_ret = deque()
            i = 1
            num = len(queue)
            while i <= num:
                vertex = queue.popleft()
                if vertex.left:
                    queue.append(vertex.left)
                if vertex.right:
                    queue.append(vertex.right)
                if level % 2 == 1:
                    level_ret.append(vertex.val)
                else:
                    level_ret.appendleft(vertex.val)
                i += 1
            ret.append(list(level_ret))
            level += 1
        return ret