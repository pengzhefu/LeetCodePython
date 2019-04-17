# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:10:03 2019

@author: pengz
"""
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head: ListNode) -> ListNode:   ##借鉴的方法,相当于 change-in,在linkedlist内部修改
                                                    ## 
    cur = head
    while cur and cur.next:   ## 因为也需要比较.next，所以需要.next也不是none
                                ## 如果.next是none了，说明到最后一个点了，不需要再进行比较
        if cur.val == cur.next.val:  ## 如果前后两个相等，跳过这个next，连接下一个next
            cur.next = cur.next.next    ## 但是这时候cur不往前移，只有找到前后不一样的值才往前移
        else:                       ## 如果前后两个不等,那就直接移动cur的坐标就行
            cur = cur.next
    return head    ## return的是head,用cur来改，要把改了以后的返回

def deleteDuplicates2(head: ListNode) -> ListNode:       ## written by my own, using similar method in q21
    dummyhead = cur = ListNode(0)
    cur.next = head   ## 先把head的都放到进来，
    cur = cur.next    ## 移动cur来不要重复的，来确定放置的位置
    while head:
        pivot = cur.val   ## 标杆值
        while head is not None and head.val == pivot:   ## 当head的等于标杆值的，就跳过
                                                        ## 所以对于linkedlist的跳过，一般都应该用while，不要用if
            ## 而且还要注意在进行跳过的时候要有不能为None的条件,因为None就没有next了
            head = head.next
        cur.next = head    ## 把这个head添加进来
        cur = cur.next    ## 把cur往下移，来连接下一个新的
    return dummyhead.next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

#a = deleteDuplicates2(head)

def deldup(x):   ## x is a list
    pivot = x[0]
    ret = [x[0]]
    i = 0
    while i < len(x):
        if x[i] == pivot:    ## 对于list,用if来判断进行跳过就方便狠毒
            i = i+1
        else:
            ret.append(x[i])
            pivot = x[i]
        
    return ret

#i = deldup([1,1,2,3,3,4,5,5,5,6,7,7,8,8])
#print(i)      