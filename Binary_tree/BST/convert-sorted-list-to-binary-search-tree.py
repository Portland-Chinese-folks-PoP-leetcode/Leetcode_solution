# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """解法一 快慢指针
    """

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build(head, end):
            if head == end:
                return None
            slow, fast = head, head
            while fast is not end and fast.next is not end:
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)

            root.left = build(head, slow)
            root.right = build(slow.next, end)
            return root
        return build(head, None)
