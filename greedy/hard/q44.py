# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:45:18 2019

@author: pengz
"""

'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''
'''
https://www.youtube.com/watch?v=Ak_GhOHkf8A
https://github.com/twood1/LeetCode/blob/master/Hard/WilcardMatching/WilcardMatching.py
'''
def isMatch(s: str, p: str) -> bool:
    dp = [[False]*(len(s)+1) for i in range(len(p)+1)]  ## dp[i][j]表明的是s[:j]和p[:i]是否匹配
    row = len(dp)
    col = len(dp[0])
#    print(row)  ## row是p的长度+1
#    print(col)  ## col是s的长度+1
    dp[0][0] = True
    ## Initialization dp form
    for i in range(0,row-1):   ## 如果s的长度为0, 那么
        if p[i] == '*':   ## 如果p那个是*, 结果就是上一个的结果
            dp[i+1][0] = dp[i][0]
        else:     ## 如果不是*, 直接false
            dp[i+1][0] = False
    ## start scanning
    for i in range(len(p)):   ## 按行搜索
        for j in range(len(s)):  ## 有个地方要注意, 表格里面的index都要+1，因为含了长度为0的时候
            if p[i] == '?' or p[i] == s[j]:   ## 如果当前的匹配, 那么要看各减1以后匹不匹配
                dp[i+1][j+1] = dp[i][j]  
            elif p[i] == '*':   ## 如果是*, 那么只要自己减一或者都减一或者那个减一有一个匹配就行，
                                ## 就是说，只要自己的上，或左，或左上有一个是True就行
                                ## 比如: ad和ad*, adc和ad*, ade和*a*, 最后这个是ad和*a并不匹配,但ad和*a*是匹配的
                dp[i+1][j+1] = dp[i][j] or dp[i+1][j] or dp[i][j+1]
    return dp[row-1][col-1]
                    
        
    

b = isMatch('adceb','*a*b')