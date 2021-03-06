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
        re = ListNode(0)
        r = re
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            r.next = ListNode(0)
        return re.next


if __name__ == "__main__":
    doctest.testmod()
