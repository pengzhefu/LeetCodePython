# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 03:02:53 2019

@author: pengz
"""

'''
You are playing the following Flip Game with your friend: Given a string that 
contains only these two characters: + and -, you and your friend take turns to flip 
two consecutive "++" into "--". The game ends when a person can no longer make a move 
and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]

Note: If there is no valid move, return an empty list [].

'''
class Solution:
    def generatePossibleNextMoves(self, s: str):  ## written by my own
        ret = []
        if len(s) <=1:
            return ret
        for i in range(len(s)-1):   ## 因为只用比较到最后两个,所以i可以最长到len(s)-2,也就是倒数第二位就行了
            # if i != len(s) -1:
            if s[i] == '+' and s[i] == s[i+1]:
                i = i+1
                if s[i] == '+':
                    reverse = '--'
                if i == 1:    ## 如果刚好前两个都是+
                    new = reverse + s[i+1:]
                else:    ## 如果连续两个+不在前两个
                    new = s[:i-1] + reverse + s[i+1:]
                ret.append(new)
        return ret