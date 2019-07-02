# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:29:26 2019

@author: pengz
"""

'''
Suppose you have a random list of people standing in a queue. Each person is described 
by a pair of integers (h, k), where h is the height of the person and k is the number of people 
in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
'''
Why does it work?
    - Once an element is placed, its 'k' cannot be violated with smaller elements.
    - You have to insert in increasing rank 'k' so that 'k' keeps its meaning

'''
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
def reconstructQueue(people: [[int]]) -> [[int]]:  ## time is O(n^2), inspired by https://blog.csdn.net/fuxuemingzhu/article/details/68486884
    ret = []
    people = sorted(people, key = lambda item: (item[0],-item[1]),reverse = True)  ## 先排序
#    print(people)
    max_height = people[0][0]
    for person in people:
        if person[0] == max_height:
            ret.append(person)
        else:
            ret.insert(person[1],person)  ## 如果不是最高的, 就把他插在他改插的位置
    return ret

b = reconstructQueue(people)