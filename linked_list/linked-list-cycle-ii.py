# https://leetcode.cn/problems/linked-list-cycle-ii/submissions/
# you
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        we need to find a start node in the linkedlist with a cycle in it 
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
