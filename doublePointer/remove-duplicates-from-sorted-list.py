# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
这里可能有读者会问，链表中那些重复的元素并没有被删掉，就让这些节点在链表上挂着，合适吗？

这就要探讨不同语言的特性了，像 Java/Python 这类带有垃圾回收的语言，
可以帮我们自动找到并回收这些「悬空」的链表节点的内存，而像 C++ 这类语言没有自动垃圾回收的机制，
确实需要我们编写代码时手动释放掉这些节点的内存。
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        fast = head
        slow = head
        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next  # 我写的代码只少了这一步
            fast = fast.next
        slow.next = None
        return head

