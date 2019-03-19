# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:01:38 2019

@author: pengz
"""
'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''
def plusOne(digits):   ## Written by myself, a little bit slower
    if digits[len(digits)-1] != 9:
        digits[len(digits)-1] = digits[len(digits)-1] +1
        return digits
    else:
        ret = []
        str1 = ''
        for num in digits:
            str1 += str(num)
        print(str1)
        res = int(str1)+1
        res = str(res)
        print(res)
        for item in res:
            ret.append(int(item))
        return ret
#print(plusOne([9]))

def plusOne2(digits):  ## Someone wrote on leetcode, a little bit faster
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits)-1-i))  ## 直接按位算成了正数
    return [int(i) for i in str(num+1)]

#print(plusOne2([9]))

def plusOne3(digits):    ## A Great Solution, using recursion idea.
    def pOne(digits, i):
        if i > 0: # If it is not the first digit
            if digits[i] == 9:
                digits[i] = 0
                return pOne(digits, i - 1) # To handle some crazy cases e.g. 9999999999
            else:
                digits[i] += 1 # Normal case
                return digits
        else: # First digit
            if digits[i] == 9:
                digits[i] = 0
                digits = [1] + digits # 9 + 1 = 10 at the first beginning. An extra space is needed
            else:
                digits[i] += 1 # If the first digit is not 9, we just add it by 1.
            return digits
    return pOne(digits, len(digits)-1)
#print(plusOne3([9]))

def plusOne4(digits):  ## Another great solution, similar to solution3，时间复杂度O(n)
    digits[len(digits)-1] += 1   ## 先直接对最后一位加1
    for i in range(len(digits)-1,0,-1):  ## 然后从最后一位开始遍历，一直到idx=1,也就是第二位
        if digits[i] == 10:          ## 如果发现有一位变10了，说明要进位
            digits[i] = 0               ## 那么这一位就变成0
            digits[i-1] += 1             ## 前一位+1
        else:
            return digits            ## 一旦最后一位加上了1都不是10，直接return就行
    if digits[0] == 10:             ## 最后再去看第一位，如果第一位是9因为有可能第二位之前也是9，加了1进位变成0，
                                    ## 第一位的9变成10
        digits[0] = 0               ## 那么把10变成0
        digits.insert(0,1)          ## 再给列表最前面插入1,增位,完事
        return digits
    return digits           ## 如果第一位不是9，第二位的9进位变成0后给的1就直接给第一位加1，然后return
print(plusOne4([0]))