# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:24:47 2019

@author: pengz
"""

'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since 
each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad 
one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version 
is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''
## 这道题这么简单居然没有做出来!!! Bad总在Good的右边, 让first成为最左边的,last是最右边,当first到了last右边,
## 说明这时候first的位置就是临界位置
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    first = 1
    last = n
    while first <= last:
        mid = (first +last)//2
        if isBadVersion(mid) == True:
            last = mid-1
        else:
            first = mid+1
    return first
