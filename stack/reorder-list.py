# https://leetcode.cn/problems/reorder-list/
# labuladong的解法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stk = []
        p = head
        while p != None:
            stk.append(p)
            p = p.next
        p = head
        while p is not None:
            lastNode = stk.pop(-1)
            next = p.next
            if lastNode == next or lastNode.next == next:
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next
            p = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        node_stack = []
        while p is not None:

            node_stack.append(p)
            p = p.next
        dummy = ListNode(-1)
        p2 = dummy
        while len(node_stack) > 0:
            if len(node_stack) is not 0:
                p2.next = ListNode(node_stack.pop(0).val)
                p2 = p2.next
            if len(node_stack) is not 0:
                p2.next = ListNode(node_stack.pop(-1).val)
                p2 = p2.next
        dummy = dummy.next
        while head is not None:
            head.val = dummy.val
            head = head.next
            dummy = dummy.next
