class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = []

        def traverse(graph, s, path):
            path.append(s)
            print(path)
            if s == len(graph)-1:
                res.append(list(path))
            for node in graph[s]:
                traverse(graph, node, path)
            path.pop(-1)
        traverse(graph, 0, path)
        return res
# 这一题用的是邻接表
# https://leetcode.cn/problems/all-paths-from-source-to-target/submissions/
