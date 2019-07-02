# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:27:57 2019

@author: pengz
"""

'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

'''
def candy(ratings: [int]) -> int:  ## code and idea from my own, 就是找出递增和递减区间
    increase = 1
    decrease = 1
    if len(ratings) == 0:
        return 0
    if len(ratings) == 1:
        return 1
    ret = [1] * len(ratings)
    idx = 0
    while idx < len(ratings):
        if idx+1 < len(ratings):
            if decrease == 1 and ratings[idx+1] > ratings[idx]:  ## 找递增区间
                increase +=1
                idx += 1
            elif increase == 1 and ratings[idx+1] < ratings[idx]:  ## 找递减区间
                decrease +=1
                idx +=1
            elif increase == 1 and decrease == 1 and ratings[idx+1] == ratings[idx]:
                ret[idx+1] = 1
                idx +=1
            else:   ## 此时的idx是截止区间，也就是递增或者递减区间的
                if increase > 1:
                    for i in range(idx-increase+2,idx+1):
                       ret[i] = ret[i-1] +1
                    increase = 1   ## 进行递增区间的修改, 然后重置, 但是index不能移动!
                elif decrease > 1:
                    ret[idx] =1
                    for i in range(idx-1, idx-decrease,-1):
                       ret[i] = max(ret[i],ret[i+1] +1)   ## 这一步比较重点, 因为有可能递减区间的开头也是递增区间的
                                                           ## 末尾, 所以需要用max来比较一下, 递增区间的尾巴大一点, 就
                                                           ## 要选大的那个
                    decrease = 1   ## 进行递减区间的修改, 然后重置， 但是index不能移动
        else:  ## 说明这个时候已经移到了最后一位,
            if increase > 1:
                for i in range(idx-increase+2,idx+1):
                   ret[i] = ret[i-1] +1
                increase = 1   ## 进行递增区间的修改, 然后重置
            elif decrease > 1:
                ret[idx] =1
                for i in range(idx-1, idx-decrease,-1):
                   ret[i] = max(ret[i],ret[i+1] +1)
                decrease = 1   ## 进行递减区间的修改, 然后重置
            print(ret)
            break  ## 到最后一位了, 直接退出
        print(ret)
    return sum(ret)

ratings = [1,2,3,4,4,2,1]
ret = candy(ratings)
        