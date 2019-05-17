# -*- coding: utf-8 -*-
"""
@Time       : 2019/3/13 19:05
@File       : 3-lengthOfLongestSubstring.py
@Author     : ZZShi
@Difficulty : middle
@Question   : 无重复字符的最长子串
@Describe   : 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
import doctest


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        >>> Solution().lengthOfLongestSubstring("abcabcbb")
        3
        >>> Solution().lengthOfLongestSubstring("bbbbb")
        1
        >>> Solution().lengthOfLongestSubstring("pwwkew")
        3
        >>> Solution().lengthOfLongestSubstring("")
        0
        >>> Solution().lengthOfLongestSubstring("a")
        1
        """
        left, right = 0, 1
        longest_sub_str = ''
        while right <= len(s):
            sub_str = s[left: right]
            if len(sub_str) == len(set(sub_str)):
                longest_sub_str = sub_str
                right += 1
            else:
                left += 1
                right += 1
        return len(longest_sub_str)

    def lengthOfLongestSubstring_v1(self, s):
        """
        使用动态规划
        :type s: str
        :rtype: int
        >>> Solution().lengthOfLongestSubstring_v1("abcabcbb")
        3
        >>> Solution().lengthOfLongestSubstring_v1("bbbbb")
        1
        >>> Solution().lengthOfLongestSubstring_v1("pwwkew")
        3
        >>> Solution().lengthOfLongestSubstring_v1("")
        0
        >>> Solution().lengthOfLongestSubstring_v1("a")
        1
        """
        longest_sub_s, this_sub_s = "", ""
        for ch in s:
            if ch in this_sub_s:
                index = this_sub_s.index(ch)
                this_sub_s = this_sub_s[index + 1:]
            this_sub_s += ch
            if len(this_sub_s) > len(longest_sub_s):
                longest_sub_s = this_sub_s
        return len(longest_sub_s)


if __name__ == "__main__":
    doctest.testmod()
