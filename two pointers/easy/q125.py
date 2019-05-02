# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 03:53:50 2019

@author: pengz
"""

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

'''
def isPalindrome(s: str) -> bool:  ## written by my own， two pointer
    if len(s) <= 1:
        return True
    first = 0
    last = len(s) -1
    while first <= last:
        ## 先让first和last都指到字母上
        # if s[first].isalpha() == False and s[first].isdigit() == False:
        #     first += 1
        #     continue
        while first <= last and s[first].isalnum() == False:
            first += 1
            # print(first)
        # if s[last].isalpha() == False and s[last].isdigit() == False:
        #     last -=1
        #     continue
        while first <= last and s[last].isalnum() == False:
            last -= 1
        if first <= last:
            if s[first].lower() == s[last].lower():
                first += 1
                last -=1
            else:
                return False
    return True


def isPalindrome2(s: str) -> bool:  ## written by my own， two pointer
    if len(s) <= 1:
        return True
    first = 0
    last = len(s) -1
    while first <= last:
        ## 先让first和last都指到字母上
         if s[first].isalpha() == False and s[first].isdigit() == False:
             first += 1
             continue
         
         if s[last].isalpha() == False and s[last].isdigit() == False:
             last -=1
             continue
         
         if s[first].lower() == s[last].lower():
            first += 1
            last -=1
         else:
            return False
    return True
a = isPalindrome('.,')