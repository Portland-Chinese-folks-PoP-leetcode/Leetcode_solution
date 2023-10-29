from typing import List
from queue import Queue
class Solution:
    # 记录图是否符合二分图性质
    ok = True
    # 记录图中节点的颜色，False 和 True 代表两种不同颜色
    color = [] 
    # 记录图中节点是否被访问过
    visited = []

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.color = [False] * n
        self.visited = [False] * n

        def bfs(graph, start):
            # 引用闭包变量 ok
            q = Queue()
            q.put(start)
            self.visited[start] = True

            while not q.empty() and self.ok:
                v = q.get()
                for w in graph[v]:
                    if not self.visited[w]:
                        # 相邻节点 w 没有被访问过
                        # 那么应该给节点 w 涂上和节点 v 不同的颜色
                        self.color[w] = not self.color[v]
                        # 标记 w 节点，并放入队列
                        self.visited[w] = True
                        q.put(w)
                    else:
                        # 相邻节点 w 已经被访问过
                        # 根据 v 和 w 的颜色判断是否是二分图
                        if self.color[w] == self.color[v]:
                            # 若相同，则此图不是二分图
                            self.ok = False
                            return

        for v in range(n):
            if not self.visited[v]:
                bfs(graph, v)

        return self.ok
    