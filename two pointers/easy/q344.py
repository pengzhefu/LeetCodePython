# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 23:45:28 2019

@author: pengz
"""

'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input 
array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''
class Solution:
    def reverseString(self, s) -> None:   ## written by my own
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s)-1
        while first <= last:
            s[first],s[last] = s[last],s[first]
            first+=1
            last -=1