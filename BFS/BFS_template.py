def BFS(start, target):
    queue = []  # This is a queue
    visited = set()
    queue.append(start)
    visited.add(start)
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            current_node = queue.pop(0)
            if current_node == target:
                return
            for node in current_node.neighbours:
                if node in visited:
                    continue
                if node not in queue:
                    queue.append(node)
                    visited.add(node)


#### an example
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 1
        q = []
        q.append(root)

        while len(q) > 0:
            size = len(q)
            for i in range(size):
                current = q.pop(0)
                if current.left is None and current.right is None:
                    return depth
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            depth += 1
        return depth
