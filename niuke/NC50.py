# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head , k ):
		# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/tu-jie-kge-yi-zu-fan-zhuan-lian-biao-by-user7208t/
        # write code here
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:  # 这个循环条件也很重要
            count = k
            while count and tail:  # 找剩下的还能不能翻转
                count -= 1
                tail = tail.next
            if not tail:  # 如果已经超出链表了, 直接break
                break
            head = pre.next
            while pre.next != tail:  # 局部做列表翻转, 用尾插法
                cur = pre.next  # 获取下一个元素, 其实pre一直没变, 只是pre.next一直在变
                pre.next = cur.next  # pre与cur.next连接起来,此时cur(孤单)掉了出来, cur就是要变的
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变 pre tail 的值
            pre = head  # head这时候已经是局部翻转完之后的最后一个了
            tail = head
        return dummy.next
        