class Solution:
    def __init__(self):
        # 记录图是否符合二分图性质
        self.ok = True
        # 记录图中节点的颜色，False和True代表两种不同颜色
        self.color = []
        # 记录图中节点是否被访问过
        self.visited = []

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.color = [False] * n
        self.visited = [False] * n
        # 因为图不一定是联通的，可能存在多个子图
        # 所以要把每个节点都作为起点进行一次遍历
        # 如果发现任何一个子图不是二分图，整幅图都不算二分图
        for v in range(n):
            if not self.visited[v]:
                self.traverse(graph, v)
                if not self.ok:
                    break
        return self.ok

    def traverse(self, graph: List[List[int]], v: int) -> None:
        # 如果已经确定不是二分图了，就不用浪费时间再递归遍历了
        if not self.ok:
            return
        self.visited[v] = True
        for w in graph[v]:
            if not self.visited[w]:
                # 相邻节点 w 没有被访问过
                # 那么应该给节点 w 涂上和节点 v 不同的颜色
                self.color[w] = not self.color[v]
                # 继续遍历 w
                self.traverse(graph, w)
            else:
                # 相邻节点 w 已经被访问过
                # 根据 v 和 w 的颜色判断是否是二分图
                if self.color[w] == self.color[v]:
                    # 若相同，则此图不是二分图
                    self.ok = False
                    return