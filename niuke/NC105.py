#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 请实现有重复数字的升序数组的二分查找
# 给定一个 元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1
# [1,2,4,4,5],4 -> 2
# [1,2,4,4,5],3 -> -1
# [1,1,1,1,1],1 -> 0
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def search(self , nums , target ):
        # write code here
        res = 0
        if not nums or nums[0] > target or nums[-1] < target:
            return -1
        found = False
        while not found:
            mid = int(len(nums) / 2)
            if mid == 0:
                return res + mid if nums[mid] == target else -1
            if nums[mid] == target:
                while nums[mid-1] == target and mid >0:
                    mid -=1
                return res + mid
            elif nums[mid] < target:
                res += mid
                nums = nums[mid:]
            elif nums[mid] > target:
                nums = nums[:mid]