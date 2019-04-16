# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:12:33 2019

@author: pengz
"""

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
def frequencySort(s: str) -> str:  ## Written by my own, with knowing how to sort dict in value or key
    ret = ''
    ans = {}
    for char in s:
        if char not in ans.keys():
            ans[char] = 1
        else:
            ans[char] += 1
    res = sorted(ans.items(),key = lambda item:(item[1]),reverse = True)
    for item in res:
        ret += item[0] * item[1]
    return ret
dict1 = {1:1,2:2,4:1}
b = sorted(dict1.items(),key = lambda item:(item[0]),reverse = True)   ## 如果index是0的话就是按key，1的话按value

#c = frequencySort('tree')