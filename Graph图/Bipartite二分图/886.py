class Solution:
    def __init__(self):
        self.ok = True
        self.color = []
        self.visited = []

    def buildGraph(self, n: int, dislikes: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n+1)]
        for edge in dislikes:
            v, w = edge[1], edge[0]
            # 「无向图」相当于「双向图」
            # v -> w
            graph[v].append(w)
            # w -> v
            graph[w].append(v)
        return graph

    def traverse(self, graph: List[List[int]], v: int) -> None:
        if not self.ok:
            return
        self.visited[v] = True
        for w in graph[v]:
            if not self.visited[w]:
                self.color[w] = not self.color[v]
                self.traverse(graph, w)
            else:
                if self.color[w] == self.color[v]:
                    self.ok = False
                    return
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.color = [False] * (n+1)
        self.visited = [False] * (n+1)
        graph = self.buildGraph(n, dislikes)
        
        for v in range(1, n+1):
            if not self.visited[v]:
                self.traverse(graph, v)
        
        return self.ok
