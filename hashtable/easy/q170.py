# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:20:51 2019

@author: pengz
"""

'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


'''
class TwoSum:   ## 允许有重复的数字添加进来 , written by my own.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = {}
        

    def add(self, number: int) -> None:    ## 记录加入的数字和次数
        """
        Add the number to an internal data structure..
        """
        if number not in self.items.keys():
            self.items[number] = 1
        else:
            self.items[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        find = False
        for item in self.items:
            target = value - item
            if target in self.items.keys():
                if target == item:
                    if self.items[item] > 1:
                        find = True
                        break
                    else:
                        continue
                else:
                    find = True
                    break
        return find
        


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(0)
obj.add(0)
print(obj.items)
param_2 = obj.find(0)
print(param_2)