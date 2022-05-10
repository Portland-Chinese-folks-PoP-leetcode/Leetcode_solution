# https: // leetcode.cn/problems/middle-of-the-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
