# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 01:16:24 2019

@author: pengz
"""

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by 
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
## 这道题没想出来，看的discuss和别人的讲解,重点是dummy head的作用
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:    ## Using a O(1) space, time complexity
                                                                        ## is O(m+n)
        dummyhead = cur = ListNode(0)   ## dummy head is used to initialization, assuring the cur could have next
                                         ## 移动的是cur，用cur来作为添加的位置, dummyhead是整个开头,为了方便初始化
        while l1 and l2:        
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummyhead.next
    
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:   ## find-in solution,
                                                                        ## 相当于往l1里面插l2的东西
        dummyhead = cur = ListNode(0)
        cur.next = l1
        while l1 and l2:
            if l1.val <= l2.val:
                l1 = l1.next
            else:  ##如果l2的更小，就要往这个位置插l2的这个元素了
                nxt = cur.next  ## 把原来的先存了,然后再放到插入的l2的后面 
                cur.next = l2
                tmp = l2.next   ## 然后因为要把原来cur后面的放到插入的l2的元素后面，所以原来l2元素的后面的也要先存起来
                l2.next = nxt   ## 把原来cur的后面的放到插入的l2的后面
                l2 = tmp  ## 就相当于把l2往自己的下面挪了一次
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummyhead.next
        
    

#def mergetwolist(x,y):
#    ret = []
#    i = 0
#    j = 0
#    while i < len(x) or j < len(y):
##        print(i)
##        print(j)
#        if i >= len(x):
#           ret.append(y[j])
#           j += 1
#        elif j >= len(y):
#            ret.append(x[i])
#            i += 1
#        else:
#            if x[i] <= y[j]:
#                ret.append(x[i])
#                i = i+1
#            else:
#                ret.append(y[j])
#                j = j+1
#    return ret
#
#c = mergetwolist([1,2,4,8,9,10],[1,1,3,4,5])         