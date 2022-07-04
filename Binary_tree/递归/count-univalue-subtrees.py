class Solution:
    res = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def traverse(root):  # 定义 返回root和他的所有子节点是相同则返回他们的值
            if root == None:
                return True
            cur_status = False
            left = traverse(root.left)
            right = traverse(root.right)
            if left and right:
                statusL = root.left == None or (
                    root.left != None and root.left.val == root.val)  # 记录root.val 是否和root.right 相等
                statusR = root.right == None or (
                    root.right != None and root.right.val == root.val)
                cur_status = statusL and statusR
                if cur_status:
                    self.res += 1
            return cur_status and statusL and statusR
        traverse(root)
        return self.res
# https://leetcode.cn/problems/count-univalue-subtrees/submissions/
# 找个题目很有必要去多看一遍
