# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:37:18 2019

@author: pengz
"""

class MyQueue():  ## queue的重点就是刚放进去的会在最后一个，最先放进去的在最前面，pop也是把之前的放进去
    ## 也就是说，用stack模拟，只能有pop(从stack的队尾出去)和append(添加进队尾), written by my own

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []   ## buffer stack
        self.stack2 = []  ## data stack
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack2.append(x)
        self.size += 1
        
        

    def pop(self) -> int:   ## 先把后面的所有元素放入buf的stack中，（顺序会和本来的相反），然后剩一个了pop，再用pop把他们
                            ## append回来，就是正确的原来顺序了
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size == 1:
            buf = self.stack2.pop()
        else:
            for i in range(self.size-1):
                self.stack1.append(self.stack2.pop())
            buf = self.stack2.pop()
            tmp = len(self.stack1)
            for i in range(tmp):
                self.stack2.append(self.stack1.pop())
            
        self.size -=1
        return buf
        

    def peek(self) -> int:   ## 最先放进去的元素就在开头
        """
        Get the front element.
        """
        return self.stack2[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0
        