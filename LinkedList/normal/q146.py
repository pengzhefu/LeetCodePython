# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 04:49:21 2019

@author: pengz
"""

'''
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

思路:双向链表(插入删除移动是O(1))，dict的查找是O(1)
这道题有一点要说明的是, 可能会再输入相同的key, 但是不同的value. 就相当于更新value
'''
## https://www.youtube.com/watch?v=R0GTqg3pJKg
## https://shenjie1993.gitbooks.io/leetcode-python/146%20LRU%20Cache.html
class DoubleNode():  ## 双向链表中的结点
    def __init__(self,key,value): ## 本来应该是只有value的, 但这道题中要key-value存储查找, 所以多了一个key
        self.key = key
        self.value = value
        self.prev = None  ## 前后都是None一开始
        self.next = None
    

class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dic = {}   ## 用来进行查找的dict, 字典的key是key,字典的value是这个node
        ## 创造一个初始的双向链表
        self.head = DoubleNode(0,0)
        self.tail = DoubleNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self,DoubleNode):  ## 删掉least used结点
#        DoubleNode.next.prev = DoubleNode.prev
#        DoubleNode.prev.next = DoubleNode.next
        prev = DoubleNode.prev
        nex = DoubleNode.next
        prev.next = nex
        nex.prev = prev
    
    def add(self,DoubleNode):  ## 这里把最新的东西加在链表头部
        DoubleNode.prev = self.head
        ## 接下来两步是先把头后面的插在新的node后面
        DoubleNode.next = self.head.next
        self.head.next.prev = DoubleNode
        ## 然后再把头接在新的node前面, 和第一步呼应
        self.head.next = DoubleNode
        
        
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            tmpNode = self.dic[key]
            ## 因为调用了这个node, 所以要进行移动
            ## 先删除
            self.remove(tmpNode)
            ## 再添加到头部成为最新
            self.add(tmpNode)
            return tmpNode.value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:  ## key已经存在, 相当于更新value
            new = DoubleNode(key,value)  ## 先创造新的
            old = self.dic[key]
            self.remove(old)  ## 删掉旧的
            self.add(new)  ## 把新的加到头部
            self.dic[key] = new  ## 最后要再更新字典！一开始忘了
        elif key not in self.dic:  ## 如果是个新的key
            if self.size == self.capacity:  ## 如果容量已经达到了上限, 要先删除 
                discard = self.tail.prev ## 要抛弃的点
                del self.dic[discard.key]
                self.remove(discard)
                self.size -=1
            tmpNode = DoubleNode(key,value) ## 先新建结点
            self.add(tmpNode)  ## 然后添加
            self.dic[key] = tmpNode ## 用dict来建立联系
            self.size += 1



        
    