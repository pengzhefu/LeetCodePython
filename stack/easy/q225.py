# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:43:34 2019

@author: pengz
"""

'''
Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
'''
class MyStack():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.size = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.items = [x] + self.items
        self.size += 1
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.items.pop()
        self.size -=1
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.size >0:
            return self.items[0]
        else:
            return None
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0

class Stack():   ## a better solution, using deque to simulate queue
    # initialize your data structure here.
    def __init__(self):
        self.stack = collections.deque([])

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):     ## 这里用deque, 因为是模拟队列，所以只能从队列的左边取出，所以只有popleft()
        for i in range(len(self.stack) - 1):   ## 把前面的都按顺序挪到后面去，然后本来在队尾的就到了头部，最先取出
            self.stack.append(self.stack.popleft())

        self.stack.popleft()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0
print([2] + [1])
print([1] + [2])