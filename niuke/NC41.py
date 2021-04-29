#
# 
# @param arr int整型一维数组 the array
# @return int整型
#

"""
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
[2,3,4,5] -> 4
[2,2,3,4,3] -> 3
"""
class Solution:
    def maxLength(self , arr ):
        # write code here
        start = 0  # 最长的起始位
        mem = set()
        res = 0
        for i in range(len(arr)):
        	while arr[i] in mem:
        		mem.remove(arr[start])  # 当遇到了重复的时候, 要一直将已经形成的窗口的重复之前的部分(含重复的)都要踢出, 因为是要子串，也就是连续的
        		start += 1
        	mem.add(arr[i])
        	res = max(res, i - start+1)
        return res







list1 = [2,3,4,3,5]  # answer should be 3
list2 = [2,3,4,3,5,6]  # answer should be 4