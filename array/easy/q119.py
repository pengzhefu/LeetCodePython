# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 07:32:08 2019

@author: UPenn-BU-01
"""
'''
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''

## rowIndex from 0
def getRow(rowIndex):  ##别人的方法
                        ##整体思路大概为，先生成相应长度的全1列表，然后总共外迭代rowIndex-1次
                        ## 从输出第2行开始需要进行外迭代，那么每一次外迭代改变的都是让前(迭代+2)个
                        ## 数形成第(迭代+1)行的正确序列
                        ## 比如：输出第二行，就外迭代一次；输出第三行，总共外迭代两次，内迭代3次；
                        ## 输出第四行，外迭代3次，内迭代6次，
                        ## 因为，输出的行数，需要改变相应(行数-1)个数，而一定要从第一个数慢慢开始改
                        ## 从上一行，变到下一行，总共要变动(上一行行数)个数
    ret = [1] * (rowIndex+1)
    ##There are rowIndex-1 nums need to change in row #rowIndex
    for i in range(2,rowIndex+1):
        for j in range(i-1,0,-1):  ##从倒数第二个数开始改变，去掉首尾的两个1不能变化
                                     ## 从上一行，变到下一行，总共要变动(上一行行数)个数
            ret[j] = ret[j] + ret[j-1]   ##这里就类似之前的，用上一行的相同index的数加上上一行index-1的数得到正确的
            print(ret)
#        print(ret)
    return ret

a = getRow(4)