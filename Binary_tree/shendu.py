class Solution(object):

    def traverse(self, root):

        if root == None:
            res = max(self.res, self.depth)
            return 0
        depth += 1
        self.traverse(root.left)
        self.traverse(root.right)
        depth -= 1

    def maxDepth(self, root):
        global depth
        depth = 0
        global res
        res = 0
        self.traverse(root)
        return self.res
