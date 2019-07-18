# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:51:54 2019

@author: pengz
"""

'''
 A string S of lowercase letters is given. We want to partition this string into as many parts 
 as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.
'''
S = "ababcbacadefegdehijhklij"
S2 = 'abcd'
def partitionLabels(S: str) -> [int]:  ## inspired by https://www.youtube.com/watch?v=ED4ateJu86I, time is O(2n)
    ret = []
    index = {}
    i = 0
    print(len(S))
    while i < len(S):   ## 先遍历一遍, 把每一个字符的最远的index记录下来
        if S[i] not in index:
            index[S[i]] = i
        else:
            index[S[i]] = i
        i +=1
    j = 0  ## 再遍历一遍
    end = 0
    steps = 0
    ans = 0
    extend = 0
    while j < len(S):  ## 从头开始遍历
        ## 会在找到一串以后, 才返回到这个大while开头
        end = index[S[j]]  ## 找开头这个字符的最远点
        steps = end-j   ## 需要移动的次数是最远点减当前
        ans = end-j+1  ## 长度是需要移动的次数+1
        j = j+1   ## 然后开始移动
        while steps >0 and j < len(S):
            if index[S[j]] <= end:  ## 如果在这中间的这个字符的最远点，小于开头的字符的最远点
                steps -=1   ## 相当于可以成功移一次, 步数减1
                j =j+1  ## 移动index
            else:   ## 如果在中间的这个字符的最远点, 大于开头的点的最远点, 那么就要更新这一串的最远点
                extend = index[S[j]] -end    ## 距离差是多少 
                ans += extend   ## 对于长度更新
                end += extend   ## 对于最远点更新
                steps += extend  ## 对于要移动的次数更新，值得注意的是这里的steps其实和之前有没有移动过无关,
                                   ## 其实就相当于剩下的还需要移的次数
                                   ## 更新以后回到里面的这层while循环
#        print(steps)
        ret.append(ans)   ## 当steps ==0的时候,就说明这一串结束了, 可以直接append进去,
    return ret

ret = partitionLabels(S)