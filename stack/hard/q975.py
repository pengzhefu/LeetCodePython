# -*- coding: utf-8 -*-
"""
Created on Fri May 17 00:47:32 2019

@author: pengz
"""
'''
You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

    During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
    During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
    (It may be the case that for some index i, there are no legal jumps.)

A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.

 

Example 1:

Input: [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
From starting index i = 3, we can jump to i = 4, so we've reached the end.
From starting index i = 4, we've reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.

Example 2:

Input: [2,3,1,1,4]
Output: 3
Explanation: 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:

During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal to A[0].

During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in (A[2], A[3], A[4]) that is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3.

During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].

We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.

In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.

Example 3:

Input: [5,1,3,4,2]
Output: 3
Explanation: 
We can reach the end from starting indexes 1, 2, and 4.

 

Note:

    1 <= A.length <= 20000
    0 <= A[i] < 100000

'''
def oddEvenJumps(A: [int]) -> int:
    order = sorted(range(len(A)), key = lambda i: A[i])
    order_r = sorted(range(len(A)), key = lambda i: A[i],reverse = True)
    def make_order(index_list):  ## 总结一下就是,在整个过程中，stack用的都是递减栈，因为要保证我如果要pop出栈顶的元素，当前的元素
                                ## 也就是存在顺序中的index是比我栈顶存的index大的，也就是说我要的结果是比我大的index, 同时
                                ## 顺序已经排好了，从大到小或者从小到大，所以不用管大小，只要管index就行了
        res = [None] * len(index_list)
        stack = []## 应该是个单调递减栈, 因为是向右跳, 要的是比自己index大的, 所以是个递减栈
        idx = 0  ## the index for index_list
        while idx < len(index_list):
            if len(stack) == 0:
                stack.append(index_list[idx])  ## stack里面存的直接是B里面的项了，也就是原本list的排序的大小的index值
            else:
                if index_list[idx] < stack[-1]:
                    stack.append(index_list[idx])
                else:
                    tmp = stack.pop()
                    res[tmp] = index_list[idx]  ## 所以直接用stack返回的值，作为index, 而这时候的代表值应该是B[idx],有点绕，自己体会一下
                    continue
#            print(res)
            idx = idx+1
        return res
    even_jump = make_order(order_r)
    odd_jump = make_order(order)
    odd = [False for i in range(len(A))]
    even = [False for i in range(len(A))]  ## odd和even两个列表表示在这个index的时候，通过奇数跳或者偶数跳能不能到达终点
    odd[len(A)-1] = True
    even[len(A)-1] = True
    for i in range(len(A)-2, -1,-1):
        if odd_jump[i] != None:
            odd[i] = even[odd_jump[i]]  ## 因为进行完奇数跳以后，就要进行偶数跳，所以要看奇数跳以后的偶数跳能不能到终点
                                        ## 比如第一个数在第一次跳了以后，就要看他的偶数跳（第二次跳）能不能到达终点，或者是不是
                                        ## 已经到了终点
                                        ## 所以这个点的上升跳的结果等于他跳了以后的那个的下降跳的结果
        if even_jump[i] != None:
            even[i] = odd[even_jump[i]]  ## 因为进行完偶数跳以后，就要进行奇数跳，所以要看偶数跳以后的奇数跳能不能到终点
    return sum(odd)  ## 只看odd是因为每一个点最开始的都是奇数跳，第一次就是奇数
    