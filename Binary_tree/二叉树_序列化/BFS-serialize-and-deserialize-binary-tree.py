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
        print(root)
        if root == None:
            return ''
        q = [root]
        string = ''
        while len(q) > 0:
            current = q.pop(0)

            if current is not None:
                string = string+str(current.val)+','
            else:
                string = string+str(current)+','
            if current == None:
                continue
            # print(string)

            q.append(current.left)
            q.append(current.right)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return []
        data_list = data.split(',')
        data_list.pop(-1)
        root = TreeNode(int(data_list[0]))
        q = [root]
        i = 0
        while len(q) > 0:
            parent = q.pop(0)
            
            # 开始build cur 的左右子树
            i = i+1
            left = data_list[i]
            if left != 'None':
                parent.left = TreeNode(int(left))
                q.append(parent.left)
            else:
                parent.left = None
            i = i+1
            right = data_list[i]
            if right != 'None':
                parent.right = TreeNode(int(right))
                q.append(parent.right)
            else:
                parent.right = None
        return root
