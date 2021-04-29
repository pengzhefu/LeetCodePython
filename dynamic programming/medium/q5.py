# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:47:42 2019

@author: pengz
"""
'''
Given a string s, find the longest palindromic substring in s. You may assume 
that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

'''
## dp的题, 没做出来，看的答案,medium的题

'''
分析如下： 
j-i<2是为了当首尾两个相等的时候，中间只有零个或者一个字符的话，可以直接返回True
然后去查看Table[i+1][j-1]是为了看，去掉这首尾相同的两个字符以后，这个内含的字符串是不是True的，如果是，就直接更新
i代表开头的index，j代表结尾的index，如果Table[i][j] == True,就是说明从i到j这一段是回文的
https://blog.csdn.net/fuxuemingzhu/article/details/79573621
'''
s = 'babad'
#dp = [[0 for i in range(len(s))] for i in range(len(s))]
def longestPalindrome(s):  ## not written by my own, time is O(n^2), space is O(n^2) 
    dp = [[0 for i in range(len(s))] for i in range(len(s))]
    res = ""
    for i in range(len(s) - 1, -1 , -1):  ## 从最末尾开始找
        for j in range(i, len(s)):   ## 一开始的时候，肯定是长度为一，就i和j相同，所以会直接返回true，然后再从i往后找
            if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1] == 1):  ## 如果s[i]和s[j]不相等也没关系, 会一直往后找,
                                                                    ## 如果找到相等的，再验证往里缩的是不是True或者
                                                                    ## 中间是不是只有一个字符了
                dp[i][j] = 1
                if res == "" or len(res) < j - i + 1: ## 如果当前答案空的或者没有新找到的长
                    res = s[i:j+1]
    return res

a = longestPalindrome(s)