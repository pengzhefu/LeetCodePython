# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:39:02 2019

@author: pengz
"""

'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
 

Follow up:
Could you solve it using only O(1) extra space?
 

Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
'''
## 这道题的第二种方法就一直没写对！！！要多写几遍！要记住！
def compress(chars:list) -> int:   ## try O(1) space， written by my own
    if len(chars) <=1:
        return len(chars)
    i = len(chars) -1
    while i >= 0:
        ret = 1
        if i != 0:
            if chars[i] != chars[i-1]:
                i = i-1
            else:
                while i > 0 and chars[i] == chars[i-1]:   ## 计算连续的个数,跳出这个循环的时候,i应该在连续的第一个
                    ret += 1
                    tmp = i
                    i = i-1
                    chars.pop(tmp)
                index = i+1
                x = 0
                ins = str(ret)
                while x < len(ins):
                    chars.insert(index,ins[x])
                    x = x+1
                    index = index+1
                    # i = i-1      ## 是不需要 i-1的，因为不i-1的话，会发现现在的char[i]和char[i-1]是不一样的,
                                    ## 从上面的if去 i-1,
        else:
            i=i-1
    return len(chars)
            
def compress2(chars:list) -> int:  ## using two pointers, i and index, i遍历list, index做插入位置
    i =0
    index =0    ## index既是插入数字的位置，也是要插入相对应字母的位置，先插入字母，然后index+1就可以是数字了
    while i < len(chars):
        tmp = chars[i]
        count =  0
        while i < len(chars) and chars[i] == tmp:   ## 这个循环跳出的时候i已经在不同的字母的第一位了
            i= i+1
            count= count+1
        chars[index] =tmp   ## 如果之前有插入过次数,那么这时候的index也是插入过次数的后一位,应该拿来放字母
                            ## 这个字母需要用之前缓存的tmp的字母，此时i已经在和tmp不同的字母的首位了
        index =index + 1
        if count > 1:
            for c in str(count):
                chars[index] = c
                index =index + 1
    return index
    
chars = ["a","a","a","a","a","a","a","b","b","c","d","d","e"]
a = compress2(chars)
                    
                
                