# -*- coding: utf-8 -*-
"""
@Time       : 2019/3/11 22:24
@File       : 1-twoSum.py
@Author     : ZZShi
@Difficulty : easy
@Question   ：两数之和
@Describe   : 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""
import doctest


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> Solution().twoSum([2, 7, 11, 5], 9)
        [0, 1]
        """
        new_lst = [target - x for x in nums]
        for index, i in enumerate(new_lst):
            if i in nums and index != nums.index(i):
                return [index, nums.index(i)]

    def twoSum_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> Solution().twoSum_v1([2, 7, 11, 5], 9)
        [0, 1]
        >>> Solution().twoSum_v1([2, 2, 4, 7], 4)
        [0, 1]
        """
        nums_dict = {}
        for index, x in enumerate(nums):
            if target - x in nums_dict:
                return [nums_dict[target - x], index]
            nums_dict[x] = index


if __name__ == "__main__":
    doctest.testmod()

