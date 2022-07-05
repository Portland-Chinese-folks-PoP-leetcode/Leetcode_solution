class Solution:
    res = 0

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        wordset = set(wordList)
        graph = {i: []for i in wordset}

        def construct(wordset):
            for i in wordset:
                for j in wordset:
                    if sum(1 for a, b in zip(i, j) if a != b) == 1 and i != j:
                        graph[i].append(j)
        construct(wordset)
        # print(graph)

        queue = []
        visited = {i: False for i in wordset}
        breadth = {}

        def bfs(visited, graph, node):
            visited[node] = True
            queue.append(node)
            while queue:
                # print(queue)
                cur = queue.pop(0)
                level = []
                for neighbour in graph[cur]:
                    if visited[neighbour] == False:
                        level.append(neighbour)
                        visited[neighbour] = True
                        queue.append(neighbour)
                breadth[cur] = level

        bfs(visited, graph, beginWord)
        # print(breadth)

        def backTrack(cur_node, track, visited):
            # if cur_node==endWord:
            #     print(res)
            #     res.append(list(track))
            #     return

            for node in breadth[cur_node]:
                if node == endWord:
                    track.append(node)
                    res.append(list(track))
                    return
                if visited[node] == False:
                    track.append(node)
                    visited[node] == True
                    backTrack(node, track, visited)
                    track.pop(-1)
                    visited[node] == False

        res = []
        visited = {i: False for i in wordset}
        track = [beginWord]
        backTrack(beginWord, track, visited)
        print(res)
