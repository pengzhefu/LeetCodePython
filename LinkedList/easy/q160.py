# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:10:00 2019

@author: pengz
"""

'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

1.    
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two 
lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


2.
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 
if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, 
it reads as [3,2,4]. There are 3 nodes before the intersected node in A; 
There are 1 node before the intersected node in B.

3.
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
'''
## 这道题有个trick,就是相当于两个list都由两个指针分别遍历一遍，这样的话遍历的总长度就一样了，当有了一样的点，就是intersection点
'''
举例说明:
If two linked lists have intersection, we can find two observations:

They must have same nodes after the intersection point.
L1+L2 must have same tail from the intersection point as L2 + L1. For example,

L1 = 1,2,3
L2 = 6,5,2,3

L1+L2 = 1,2,3,6,5,(2,3)
L2+L1 = 6,5,2,3,1,(2,3)

然后如果他们没有intersection的话，其实最后也会相等，跳出，因为那个时候都是None
而且a的指针跳到b和b的指针跳到a只能有一次，也只会有一次，因为会先判断他们相不相等，然后才是看是不是none会不会跳出
'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def getIntersectionNode(self, headA, headB):   ## The method is from solution, wrote the code by my own
                                                    ## 时间复杂度是O(m+n),space is O(1)
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:   ## 当有任何其中一个是none的话
            return None
        pA = headA
        pB = headB
        jumpA = True
        jumpB = True    ## 可以用jumpA和jumpB来确保只跳一次，但其实可以不用，因为一样长度后如果都没有最后就都是相等的None
        while pA != pB:
            if pA != None:
                pA = pA.next
            else:
                pA = headB
            
            if pB != None:
                pB = pB.next
            else:
                pB = headA
        
        return pA      ## if null, return None, pA == pB == None
    
    def getIntersectionNode2(self, headA, headB):      ## not written by my own, saw it from discussion
                                                        ## 思想就是把长的多出来的那部分剪掉，这样可以两条同时开始traverse
                                        ## 时间复杂度是O(m+n+2*min(m,n)),space is O(1)
        if not headA or not headB:   ## 当有任何其中一个是none的话
            return None
        lengthA = 0
        pA = headA
        lengthB = 0
        pB = headB
        while pA != None:
            lengthA += 1
            pA = pA.next
        
        while pB != None:
            lengthB += 1
            pB = pB.next
        
        pA = headA
        pB = headB
        if lengthA >= lengthB:
            diff = lengthA - lengthB
            for i in range(diff):  ## 让pA往后移多出来的长度
                pA = pA.next
            
            while pA != pB:
                pA = pA.next
                pB = pB.next
            return pA
        else:
            diff = lengthB - lengthA
            for i in range(diff):  ## 让pA往后移多出来的长度
                pB = pB.next
            
            while pA != pB:
                pA = pA.next
                pB = pB.next
            return pB
        
        def getIntersectionNode3(self, headA, headB):   ## 这个方法要用到jump这个限制条件
                                                        ## 方法1不需要是因为会让pA去等于None,而这个方法是
                                                        ## 不让指针移到none，后一个如果是none直接跳到另一个list,
            if not headA or not headB:
                return None
            pA = headA
            pB = headB
            jumpA = True
            jumpB = True    
            while pA != pB:
                if pA.next == None and jumpB:
                    pA = headB
                    jumpB = False
                else:
                    pA = pA.next
                
                if pB.next == None and jumpA:
                    pB = headA
                    jumpA = False
                else:
                    pB = pB.next
            
            return pA      ## if null, return None, pA == pB == None
        
            