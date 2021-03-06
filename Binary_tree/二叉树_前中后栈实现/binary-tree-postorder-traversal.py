from collections import deque


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        while root != None or len(stack) > 0:
            while root is not None:
                res.append(root.val)
                stack.append(root)
                root = root.right
            cur = stack.pop()
            root = cur.left
        res.reverse()
        return res
