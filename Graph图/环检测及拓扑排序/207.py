from typing import List
class Solution1:
    hasCycle = False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        onPath = []
        visited = []
        
        def buildGraph(numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
            # 图中共有 numCourses 个节点
            graph = [[] for _ in range(numCourses)]
            for edge in prerequisites:
                from_, to_ = edge[1], edge[0]
                # 添加一条从 from 指向 to 的有向边
                # 边的方向是「被依赖」关系，即修完课程 from 才能修课程 to
                graph[from_].append(to_)
            return graph

        def traverse(graph: List[list], s: int) -> None:
            if onPath[s]:
                # 发现环！！！
                self.hasCycle = True
            if visited[s] or self.hasCycle:
                return
            # 将节点 s 标记为已遍历
            visited[s] = True
            # 开始遍历节点 s
            onPath[s] = True
            for t in graph[s]:
                traverse(graph, t)
            # 节点 s 遍历完成
            onPath[s] = False
        graph = buildGraph(numCourses, prerequisites)
        visited = [False] * numCourses
        onPath = [False] * numCourses
        for i in range(numCourses):
            traverse(graph, i)
        return not self.hasCycle
    


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            """
            0: Not visited
            1: Visited and safe (no cycle found starting from this node)
            -1: Being visited (currently in recursion stack)
            
            """
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True