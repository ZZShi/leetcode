# -*- coding: utf-8 -*-
"""
@Time   : 2019/3/13 22:50
@File   : 5-longestPalindrome.py
@Author : ZZShi
@Difficulty：middle
@Question: 最长回文子串
@Describe: 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""
import doctest


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        >>> Solution().longestPalindrome("babad")
        'bab'
        >>> Solution().longestPalindrome("cbbd")
        'bb'
        """
        length = len(s)
        flag = 1
        while length:
            for i in range(flag):
                sub_s = s[i: length + i]
                if sub_s == sub_s[::-1]:    # 判断sub_s是否是回文
                    return sub_s
            length -= 1
            flag += 1
        return ""

    def longestPalindrome_v1(self, s):
        """
        :type s: str
        :rtype: str
        >>> Solution().longestPalindrome_v1("babad")
        'bab'
        >>> Solution().longestPalindrome_v1("cbbd")
        'bb'
        """
        length = len(s)
        for i in range(length):
            for j in range(i):
                sub_s = s[j: length - i + j]
                if sub_s == sub_s[::-1]:
                    return sub_s
        return ''


if __name__ == "__main__":
    doctest.testmod()
