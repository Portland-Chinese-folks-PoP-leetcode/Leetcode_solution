# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    https://leetcode.cn/problems/palindrome-linked-list/submissions/
    1.先通过 双指针技巧 中的快慢指针来找到链表的中点：
    2、如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步：
    3、从slow开始反转后面的链表，现在就可以开始比较回文串了：
    
 """


class Solution:
    def reverse(self, head):
        pre = None
        cur = head
        nxt = head
        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        if fast is not None:
            slow = slow.next
        left = head
        right = self.reverse(slow)
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
