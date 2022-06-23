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
