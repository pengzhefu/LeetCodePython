# -*- coding: utf-8 -*-
"""
Created on Wed May  8 04:11:06 2019

@author: pengz
"""
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

                   
'''
def permute(nums: [int]) -> [[int]]:
    ret = []
    n = len(nums)
    def swap(n,first,list1):  ## first就是当前要换的坐标，把他和后面的每一个都换一次
        if first == n:  ## swap结束的条件，就是first到达list以外了，
            ret.append(list1[:])  ## 这里要注意这里是用的一种复制，不能是直接list1
            return ret
        else:
            for i in range(first,n):
                list1[first], list1[i] = list1[i], list1[first]
                swap(n,first+1,list1)
                ## 还需要swap back!!!!
                '''
                the reason： recover the swap. eg: [1,2,3] swap to [2,1,3] and call recursion for 
[2,1,3]. then we need to swap back to [1,2,3] . next swap will be [3,2,1] then recursion and recover swap.
也就是说，再换了一次以后，要换回来，才能针对原来的顺序做另一种交换 
                '''
                list1[first], list1[i] = list1[i], list1[first]   
    swap(n,0,nums)
    return ret
    
a = permute([1,2,3])