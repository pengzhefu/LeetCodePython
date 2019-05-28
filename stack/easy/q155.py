# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:18:55 2019

@author: pengz
"""

'''
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack():   ## written by my own， using two stacks

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.size = 0
        self.minList = []   ## 重点是新用一个list来存每一次的最小值！因为这个stack只能从末尾一个个走，所以会按顺序离开
                            ## 所以如果有最小值的更新，就放到这个列表的末尾，如果这个最小值被pop了，这个列表的最后一个也pop

    def push(self, x: int) -> None:
        self.items.append(x)
        if self.size == 0:
            self.minList.append(x)
        else:
            if x <= self.minList[-1]:
                self.minList.append(x)
        self.size += 1
        
    def pop(self) -> None:
        if self.size >0:
            tmp = self.items.pop()
            if tmp == self.minList[-1]:
                self.minList.pop()
            self.size -=1
        else:
            return None

    def top(self) -> int:
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.minList) >0:
            return self.minList[-1]
        else:
            return None

class MinStack2():   ## method from other， using one stack

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == 0:
            self.items.append((x,x))   ## 添加的东西变成tuple,第一项是添加的数，第二项是添加以后应有的最小值
        else:
            self.items.append((x,min(self.items[-1][1],x)))  ## 比较一下
        self.size += 1
        
    def pop(self) -> None:
        if self.size >0:
            self.items.pop()
            self.size -=1
        else:
            return None

    def top(self) -> int:
        if len(self.items) > 0:
            return self.items[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if len(self.items) >0:
            return self.items[-1][1]
        else:
            return None
# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())