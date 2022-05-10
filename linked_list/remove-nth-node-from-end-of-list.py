#https://leetcode.cn/problems/remove-nth-node-from-end-of-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def findFromEnd(head, k):
            p1 = head
            for i in range(k):
                p1 = p1.next
            p2 = head
            while p1 is not None:
                p1 = p1.next
                p2 = p2.next
            return p2
        dummy = ListNode(-1)
        dummy.next = head
        x = findFromEnd(dummy, n+1)
        x.next = x.next.next
        return dummy.next

# 这题就是利用了 一个小套路 返回 倒数第n个数字 the nth last node 
