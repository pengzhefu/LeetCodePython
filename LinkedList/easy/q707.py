# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:13:21 2019

@author: pengz
"""
'''
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly 
linked list. A node in a singly linked list should have two attributes: val and next. val is the 
value of the current node, and next is a pointer/reference to the next node. If you want 
to use the doubly linked list, you will need one more attribute prev to indicate the previous node 
in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

    get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    addAtHead(val) : Add a node of value val before the first element of the linked list. After 
    the insertion, the new node will be the first node of the linked list.
    addAtTail(val) : Append a node of value val to the last element of the linked list.
    addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. 
    If index equals to the length of linked list, the node will be appended to the end of linked list. 
    If index is greater than the length, the node will not be inserted.
    deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Note:

    All values will be in the range of [1, 1000].
    The number of operations will be in the range of [1, 1000].
    Please do not use the built-in LinkedList library.

'''
## 这道题改版了，还有index为负数的时候的插入！
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
class MyLinkedList():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.head
        i = 0
        while cur and i < index:
            i += 1
            cur = cur.next
        if cur and i== index:
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, 
        the new node will be the first node of the linked list.
        """
        tmp = ListNode(val)
        tmp.next = self.head
        self.head = tmp
        self.size += 1
        return self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = ListNode(val)
        if not self.head:
            self.addAtHead(val)
        elif not self.head.next:
            self.head.next = tmp
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = tmp
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the 
        end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur = self.head
        if not cur:
            if index == 0:
                self.addAtTail(val)
                self.size += 1
            else:
                return None
        elif not cur.next:
            if index == 0:
                self.addAtHead(val)
                self.size += 1
            elif index == 1:
                self.addAtTail(val)
                self.size += 1
            else:
                return None
        else:
            if index == 0:
                self.addAtHead(val)
                self.size += 1
            else:
                tmp = ListNode(val)
                i = 0
                pre = None
                while i < index and cur:
                    i = i+1
                    pre = cur
                    cur = cur.next
                if pre and i == index:
                    tmp.next = pre.next
                    pre.next = tmp
                self.size += 1
                    

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head:
            return None
        elif not self.head.next:
            if index == 0:
                self.head = None
                self.size -= 1
            else:
                return None
        else:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
            else:
                if index > self.size:
                    return None
                else:
                    cur = self.head
                    i = 0
                    pre = None
                    while i < index and cur:
                        i += 1
                        pre =cur
                        cur = cur.next
                    if cur and i == index:
                        pre.next = cur.next
                    self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get()
obj.addAtHead(1)
obj.addAtHead(3)
obj.addAtTail(2)   ## 顺序是[3,1,2]
#print(obj.head.val)
#print(obj.head.next.val)
#print(obj.head.next.next.val)
#print(obj.get(2))
obj.addAtIndex(4,4)   ## 顺序是[3,1,2,4]
print(obj.head.val)
print(obj.head.next.val)
print(obj.head.next.next.val)
#print(obj.head.next.next.next.val)
print(obj.size)
obj.deleteAtIndex(0)
print('=====================')
print(obj.head.val)
print(obj.head.next.val)
#print(obj.head.next.next.val)
print(obj.size)
#obj.addAtIndex(index,val)
#obj.deleteAtIndex(index)