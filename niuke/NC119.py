# -*- coding:utf-8 -*-
"""
给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组
这道题根源就是排序, 所有就简单用了快排+base case
"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        res = []
        if len(tinput) < k:
            return res
        def quick_sort(arr,firstIndex,lastIndex):
            if firstIndex<lastIndex:
                divIndex=Partition(arr,firstIndex,lastIndex)

                ## 相当于在递归，分成两组后每次都进行同样的处理
                quick_sort(arr,firstIndex,divIndex)       
                quick_sort(arr,divIndex+1,lastIndex)
            else:
                return

        ## 将数组分为两组，第一个基准数复位
        def Partition(arr,firstIndex,lastIndex):
            i=firstIndex-1
            pivot = arr[lastIndex]
            for j in range(firstIndex,lastIndex):
                if arr[j]<=pivot:
                    i=i+1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]
            return i
        
        quick_sort(tinput, 0, len(tinput)-1)
        return tinput[:k]