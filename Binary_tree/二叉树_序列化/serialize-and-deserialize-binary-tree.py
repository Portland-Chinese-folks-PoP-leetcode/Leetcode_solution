# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '#'
        return str(root.val)+','+str(self.serialize(root.left))+','+str(self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def traverse(data_list):

            root_val = data_list.pop(0)
            if root_val == '#':
                return None
            root = TreeNode(root_val)
            # 为什么 root的left和root的right看传入的参数可以一样？ 之前那做的题目，root.left后调用递归的参数和root.right后面调用递归所用的参数必定是不一样的，
            # 答：因为这里调用的参数很特别，data_list是把她当做栈来使用，每一次的pop都是把栈顶的元素给推出去了，所以当把root.left=traverse(data_list) 执行完了以后，
            # root.right=traverse(data_list)  只剩剩下的右子树一部分了
            root.left = traverse(data_list)
            root.right = traverse(data_list)
            return root

        data_List = data.split(',')
        return traverse(data_List)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
