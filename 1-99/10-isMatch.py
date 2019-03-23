# -*- coding: utf-8 -*-
"""
@Time   : 2019/3/22 22:51
@File   : 10-isMatch.py
@Author : ZZShi
@Difficulty：困难
@Question: 正则表达式匹配
@Describe: 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
"""
import re
import doctest


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        >>> Solution().isMatch('aa', 'a')
        False
        >>> Solution().isMatch('aa', 'a*')
        True
        >>> Solution().isMatch('ab', '.*')
        True
        >>> Solution().isMatch('aab', 'c*a*b')
        True
        >>> Solution().isMatch('mississippi', 'mis*is*p*.')
        False
        """
        pass


if __name__ == '__main__':
    doctest.testmod()
