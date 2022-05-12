# https://leetcode.cn/problems/palindrome-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        global left
        left = head

        def traverse(right):
            global left
            if right == None:
                return True
            res = traverse(right.next)
            res = res and (left.val == right.val)
            left = left.next
            return res
        return traverse(head)
