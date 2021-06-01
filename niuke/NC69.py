# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        length = 0
        if not pHead:
            return None
        fast = pHead
        slow = pHead
        while fast:
            length += 1
            fast = fast.next
        if length < k:
            return None
        step = length - k
        while step >0:
            slow = slow.next
            step -=1
        return slow