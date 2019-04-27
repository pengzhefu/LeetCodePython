# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 04:45:42 2019

@author: pengz
"""

'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
'''
class Solution:
    def convertToTitle(self, n: int) -> str:   ## using str, written by my own
        if n <= 0:
            return ''
        ans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret = ''
        base = 0       ## 相当于添加到第几位了
        while n > 0:
            tmp = int(n / (26 ** base))    ## 当要添加到的那一位时，需要先用目前的数除以26的相应次方(个位0，十位1)
                                            ## 然后再用相除以后的结果去找余数！(除以26的相应次方是因为这是1-26)
                                            ## 找到的余数就是在当前这一位要添加的数
            val = tmp % 26
            if val == 0:
                char = 'Z'
                n = n - 26*(26**base)
            else:
                char = ans[val-1]
                n = n - val*(26**base)
            ret = char + ret
            base += 1
                
        return ret