# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
Given a non-negative integer num, repeatedly add all its digits until the result 
has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
def addDigits(num: int) -> int: ## using loop function, want O(1), written by my own
    x = num
    ret = 0
    done = False
    while not done:
        print(x)
        while x > 0:
            ret += x % 10
            x = x//10
        if ret < 10:
            return ret
        else:
            x = ret
            ret = 0
            continue
    return ret

def addDigits2(self, num: int) -> int:  ## method from discussion, the key is %9. 
    if num == 0:
        return 0
    else:
        if num % 9 == 0:
            return 9
        else:
            return num % 9