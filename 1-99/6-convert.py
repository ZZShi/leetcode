# -*- coding: utf-8 -*-
"""
@Time   : 2019/3/22 21:17
@File   : convert.py
@Author : ZZShi
@Difficulty：中等
@Question: Z字形变换
@Describe: 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
"""
import doctest


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        >>> Solution().convert('', 1)
        ''
        >>> Solution().convert('LEETCODEISHIRING', 3)
        'LCIRETOESIIGEDHN'
        >>> Solution().convert('LEETCODEISHIRING', 4)
        'LDREOEIIECIHNTSG'
        >>> Solution().convert('ABCDEF', 2)
        'ACEBDF'
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        lst = [[] for _ in range(numRows)]
        is_positive = True
        flag = 0
        for ch in s:
            lst[flag].append(ch)
            if is_positive:
                flag += 1
                if flag == numRows:
                    is_positive = False
                    flag -= 2
            else:
                flag -= 1
                if flag == 0:
                    is_positive = True
        return ''.join(map(lambda x: ''.join(x), lst))


if __name__ == '__main__':
    doctest.testmod()
