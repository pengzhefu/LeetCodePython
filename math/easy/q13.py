# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:49:40 2019

@author: pengz
"""

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written 
as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle 
applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
def romanToInt(s: str) -> int:    ## using dict, written by my own
    num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    combine = {'V':'I','X':'I','C':'X','L':'X','D':'C','M':'C'}
    res = 0
    i = len(s) -1
    while i >= 0:
        if i !=0:     ## 要把第一位单独拿出来算
            tmp = s[i]       ## 用tmp记下当前的罗马字母
            val = num[tmp]   ## 获取对应的数值
            if tmp in combine:   ## 如果是有可能和别的字母进行组合的数字
                while i >= 1 and s[i-1] == combine[tmp]:   ## i >= 1是为了看这个是不是到头了,如果到头了就没必要看了
                                                        ## 同时要确保前面的依然是可行组合
                    val = val - num[combine[tmp]]
                    i = i-1
                res = res + val    ## 结束循环算出这个组合以后才加到结果
                i = i-1
            else:     ## 就其实不管这个数字是不是除了I以外的数，我都要减一往下
                res += val
                i = i-1
        else:
            res += num[s[i]]
            i = i-1
    return res

a = romanToInt('IV')

def romanToInt2(s: str) -> int:   ## others method, the highest index is great
                                    ## 这方法利用了其实整个数字从前往后是从大到小，如果前面的比后面小，说明要减去
    num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ret = 0
    highest = 0
    for i in range(len(s)-1,-1,-1):   ## 所以循环先从最后一位开始
        tmp = num[s[i]]
        if tmp >= highest:      ## 如果遍历到的比当前记录的最大罗马字母要小，那就是要减去的
            ret += tmp
            highest = tmp
        else:
            ret -= tmp
    return ret
