# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:24:33 2019

@author: pengz
"""
'''
 Given an array of integers and an integer k, you need to find the number of unique k-diff 
 pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i 
 and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].

'''
def findPairs(nums:list, k: int) -> int:  ## not using dict, written by my own
    ret = 0
    if len(nums) <=1 or k < 0:
        return ret
    nums.sort()
    slow = 0  ## suffix pointer
    fast = 1  ## prefix pointer
    done = False
    while not done:
        if slow == fast:   ## 要保证slow和fast不在一起
            if fast < len(nums)-1:
                fast += 1
            else:    ## 如果slow和fast都在最后了，那说明遍历结束了，直接break退出
                break
        if abs(nums[slow]-nums[fast]) == k:
            ret += 1
            tmp = nums[fast]
            if fast < len(nums)-1:   ## 找到一对后，移动fast一直到一个新的数出现，来避免重复的对
                while fast < len(nums)-1 and nums[fast] == tmp:
                    fast += 1
                if nums[fast] == tmp:   ##如果fast一直到了最后一位,还是和之前重复,说明没有了,可以直接break
                    break
            else:
                done = True
        elif abs(nums[slow]-nums[fast]) < k:   ## 小于了就要移动fast
            if fast < len(nums) -1:
                fast+= 1
            else:   ## 到最后一位了,退出
                done = True
        elif abs(nums[slow]-nums[fast]) > k:    ## 大于了就移动slow
            if slow < fast and slow < len(nums) -1:   ## 这里要允许slow可能和fast重合，但是一旦重合了，就会在循环最开始移动fast
                slow += 1
            else:
                done = True   
    return ret

def findPairs2(nums:list, k: int) -> int:   ## using dict, written by my own, 用dict来避免重复的对
    ret = {}
    if len(nums) <=1 or k < 0:
        return len(ret)
    nums.sort()
    slow = 0  ## suffix pointer
    fast = 1  ## prefix pointer
    done = False
    while not done:
        if slow == fast:   ## 要保证slow和fast不在一起
            if fast < len(nums)-1:
                fast += 1
            else:    ## 如果slow和fast都在最后了，那说明遍历结束了，直接break退出
                break
        if abs(nums[slow]-nums[fast]) == k:
            if nums[slow] not in ret:
                ret[nums[slow]] = nums[fast]
            if fast < len(nums)-1:
                fast += 1
            else:
                done = True
        elif abs(nums[slow]-nums[fast]) < k:
            if fast < len(nums) -1:
                fast+= 1
            else:
                done = True
        elif abs(nums[slow]-nums[fast]) > k:
            if slow < fast and slow < len(nums) -1:
                slow += 1
            else:
                done = True   
    return len(ret)
b = findPairs([-2,-4,-9,-1,0,9,8,16,4,2,3,-5], k = 2)    
    