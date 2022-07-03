# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        track = [root.val]

        def backtrack(root):
            if root.left is None and root.right is None:
                res.append(list(track))
            if root.left:
                track.append(root.left.val)
                backtrack(root.left)
                track.pop(-1)
            if root.right:
                track.append(root.right.val)
                backtrack(root.right)
                track.pop(-1)
        backtrack(root)
        answer = []
        for path in res:
            string = '->'.join(map(str, path))
            answer.append(string)
        return answer
