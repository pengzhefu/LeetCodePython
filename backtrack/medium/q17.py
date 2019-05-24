# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:01:42 2019

@author: pengz
"""

'''
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
def letterCombinations(digits: str) -> [str]:  ## not written by my own, genius work!
                                                ## time is O(3^N * 4^M), space the same
    phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    output = []  ## 最后要return的
    
    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
            print(combination)
            return output
        # if there are still digits to check
        else:
            # iterate over all letters which map 
            # the next available digit
            for letter in phone[next_digits[0]]:  ##next digits的第0项是会一直变的，因为总是nextdigits = nextdigits[1:]
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])  ## 有一个letter就要调用一次这个func,
    if digits:
        backtrack("", digits)   ## 一开始的combination是空的
    return output

b = letterCombinations('23')