# -*- coding:utf-8 -*-

"""
数组中有一个数字出现的次数超过数组长度的一半，
请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
[1,2,3,2,2,2,5,4,2] -> 2
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers or len(numbers) == 2:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        mem = dict()
        count = 0
        res = 0
        for n in numbers:
            if n not in mem:
                mem[n] = 1
            else:
                mem[n] += 1
                if mem[n] > count:
                    count = mem[n]
                    res = n
        return res if count > int(len(numbers)/2) else 0