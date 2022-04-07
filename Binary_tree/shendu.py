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

    def maxDepth_v2(self, root):
        if root is None:
            return 0
        left_max = self.maxDepth_v2(root.left)
        right_max = self.maxDepth_v2(root.right)
        return max(left_max, right_max)+1
