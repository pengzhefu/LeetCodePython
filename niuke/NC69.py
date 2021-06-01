# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# �����е����������������������Ѿ�ָ���������޸ģ�ֱ�ӷ��ط����涨��ֵ����
#
# 
# @param pHead ListNode�� 
# @param k int���� 
# @return ListNode��
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