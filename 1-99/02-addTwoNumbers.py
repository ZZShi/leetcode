# -*- coding: utf-8 -*-
"""
@Time       : 2019/3/13 18:47
@File       : 2-addTwoNumbers.py
@Author     : ZZShi
@Difficulty : middle
@Question   ：两数相加
@Describe   : 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
        如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
        您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
import doctest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    doctest.testmod()
