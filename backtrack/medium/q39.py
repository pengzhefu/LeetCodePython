# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:18:04 2019

@author: pengz
"""

'''
Given a set of candidate numbers (candidates) (without duplicates) and a target 
number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
## 还是没想出来，看的别人答案
def combinationSum(candidates: [int], target: int) -> [[int]]:
    ret = []
    candidates.sort()
    def backtrack(candidates,target,list1):
        if target == 0:
            ret.append(list1[:])
            return ret
        for idx, num in enumerate(candidates):
            if target < num:  ## 如果小于了，因为有过排序，就没必要继续后面的了，可以跳出循环，
                break
            else:
                backtrack(candidates[idx:],target-num,list1+[num])  ## 这里不用append是有可能有None的情况
    backtrack(candidates,target,[])
    return ret

a = combinationSum([1,2,3,4],10)