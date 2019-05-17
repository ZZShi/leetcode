# -*- coding: utf-8 -*-
"""
@Time       : 2019/3/22 22:01
@File       : 7-reverse.py
@Author     : ZZShi
@Difficulty ：简单
@Question   : 整数反转
@Describe   : 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
import doctest


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        >>> Solution().reverse(123)
        321
        >>> Solution().reverse(-123)
        -321
        >>> Solution().reverse(120)
        21
        >>> Solution().reverse(-1200)
        -21
        """
        f = lambda n: int(str(n)[::-1])
        rst = f(x) if x >= 0 else -f(-x)
        return rst if -2**31 <= rst <= 2**31 - 1 else 0


if __name__ == '__main__':
    doctest.testmod()
