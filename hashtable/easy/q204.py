# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:39:47 2019

@author: pengz
"""

'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''
def countPrimes(n):   ## written by my own, time limit exceeded
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        pn = [2]
        cnt = 1
        for num in range(3,n):
            prime = True
            for i in pn:
                if num % i ==0:
                    prime = False
                    break
            if prime:
                cnt+=1
                pn.append(num)
            else:
                continue
        return cnt
#a = countPrimes(49979)
print(round(7**0.5))    
print(int(round(7**0.5)))
print(99//2+1)

def countPrimes1(n):   ## 借鉴的别人的,超级巧妙的方法！   需要额外空间O(n), 时间复杂度为O(nlogn)?
    if n <= 2:
        return 0
    res = [True] * n     ## 如果大于2，提前生成一张列表，长度为n,index就带表小于n的非0数:0...n-1,假设都是prime(True)
    res[0] = res[1] = False  ## 0，1都不是,先人工变False
    for i in range(2, n):   ## 从2开始,一直到n-1
                                ## 其实这里也还可以改进一下,就是可以不用到n-1,到根号n的向下取整就行了,也减少时间
        if res[i] == True:   ## 如果这个数是质数的话,那他的所有的倍数就都不是质数了
            for j in range(2, (n-1)//i+1):     ## 倍数从2开始，那最大到几倍呢,就应该是末尾的数(n-1)整除这个质数(i),
                                                ## 因为是range,所以要+1
                 ## 其实这里j的范围还有一个可以改进加速的方法,就是把2改成i:range(i, (n-1)//i+1) 
                 ## 因为其实小于自己的质数倍的数字在之前已经被其他的变成False了,不是质数倍的也被小于自己的数字的倍数包含了
                 ## 比如：如果是17,那么自己的2,3,5,7,11,13倍的都在之前这些质数的倍数包含了,
                 ## 4,6,8,10,12,14,16倍被2包含,15被3包含
                 ## 所以减少重复工作，可以从自己的本身倍数开始
                res[i*j] = False        ## 质数的倍数都不是质数,变False
    return sum(res)   ## 最后统计有多少个True就行了