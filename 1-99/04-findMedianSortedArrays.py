# -*- coding: utf-8 -*-
"""
@Time       : 2019/3/13 19:26
@File       : 4-findMedianSortedArrays.py
@Author     : ZZShi
@Difficulty ：hard
@Question   : 寻找两个有序数组的中位数
@Describe   : 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
        请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
        你可以假设 nums1 和 nums2 不会同时为空。
"""
import doctest


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :param nums1:
        :param nums2:
        :return:
        >>> Solution().findMedianSortedArrays([1, 3], [2])
        2.0
        >>> Solution().findMedianSortedArrays([1, 3], [2, 4])
        2.5
        """
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        return (nums1[int((length - 0.5) // 2)] + nums1[int((length + 0.5) // 2)]) / 2

    def findMedianSortedArrays_v1(self, nums1, nums2):
        """
        :param nums1:
        :param nums2:
        :return:
        >>> Solution().findMedianSortedArrays_v1([1, 3], [2])
        2
        >>> Solution().findMedianSortedArrays_v1([1, 3], [2, 4])
        2.5
        """
        merge_lst = sorted(nums1 + nums2)
        length = len(merge_lst)
        is_odd = length % 2
        half = length // 2
        return merge_lst[half] if is_odd else (merge_lst[half - 1] + merge_lst[half]) / 2


if __name__ == "__main__":
    doctest.testmod()
