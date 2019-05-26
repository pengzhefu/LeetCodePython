# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:03:36 2019

@author: pengz
"""

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''
## 解析看 youtube的花花酱刷题
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if not board or not word:
            return False
        if not board[0]:
            return False
        m = len(board)  ## 这是行数
        n = len(board[0])  ## 列数
        def search(idx, x, y):  ## x是第几行, y是第几列
            if idx == len(word):
                return True
            elif x >= m or y >= n or x <0 or y<0 or word[idx] != board[x][y]:
                return False
            else:  ## 只要进了这个循环，就说明当前走的这个字符是符合的，
                cur = board[x][y]  ## 把这个字符所代表的先存下来
                board[x][y] = ''   ##然后变成空，这样在后面的递归中就不会走这个格子了 
                found = search(idx+1, x-1, y) or search(idx+1,x+1,y) or search(idx+1,x,y+1) or search(idx+1,x,y-1)
                board[x][y] = cur  ## 最后再把他变回来，如果上面这条路不行，就恢复棋盘，再探索一次别的路
            return found
#        return any(search(0,i,j) for i in range(m) for j in range(n))  ## 这样可以返回所有起点位置的结果，
                                                                        ## 任意一个是True返回就是True
                                                                        ## 这个有点高级，换个思路
        result = False                                                                
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:  ## 找到了对应的起点
                    result = search(0,i,j)
                    if result:  ## 如果这个起点对应的是可以的, 就返回True
                        return True
                    else:   ## 如果这个起点对应的不行，就返回这个for循环，继续去找别的起点
                        continue
        return result  ## 如果一直连对应的起点都没有，就返回False,因为一开始result是False
                    

                    
        