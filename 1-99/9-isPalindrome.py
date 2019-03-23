# -*- coding: utf-8 -*-
"""
@Time   : 2019/3/22 22:44
@File   : 9-isPalindrome.py
@Author : ZZShi
@Difficulty：简单
@Question: 回文数
@Describe: 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
import doctest


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        >>> Solution().isPalindrome(121)
        True
        >>> Solution().isPalindrome(-121)
        False
        >>> Solution().isPalindrome(10)
        False
        """
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    doctest.testmod()
