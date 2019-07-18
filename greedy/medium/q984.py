# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:10:52 2019

@author: pengz
"""

'''
Given two integers A and B, return any string S such that:

    S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
    The substring 'aaa' does not occur in S;
    The substring 'bbb' does not occur in S.

 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:

Input: A = 4, B = 1
Output: "aabaa"
'''
def strWithout3a3b(A: int, B: int) -> str: ## code and idea from my own, time is O(n)
    ret = ''
    if A == B:
        for i in range(A):
            ret += 'ab'
        return ret
    elif A >B:
        max_sym = 'a'
        min_sym = 'b'
        max_length = A
        min_length = B
    else:
        max_sym = 'b'
        min_sym = 'a'
        max_length = B
        min_length = A
    while max_length >=2 and max_length != min_length and min_length >0:
        ret += max_sym*2
        max_length -=2
        if min_length >0:
            ret += min_sym
            min_length -=1
    print(max_length,min_length)
    if max_length == min_length and min_length !=0:
        for i in range(min_length):
            ret += max_sym
            ret += min_sym
    elif max_length >0:
        ret += max_sym*max_length
    return ret
    

ret = strWithout3a3b(3,4)