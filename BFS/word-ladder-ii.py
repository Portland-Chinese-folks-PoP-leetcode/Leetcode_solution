import string
from typing import List


class Solution:

    marked = {}

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordSet = set(wordList)
        visited = {i: False for i in wordSet}
        q = [beginWord]
        graph = []

        def isDifOne(a, b):
            count = 0
            for i in range(len(a)):
                if(a[i] != b[i]):
                    count += 1
            return count == 1

        def constructGraph(wordSet, queue):
            while len(q) > 0:
                size = len(q)
                level = []
                for i in range(size):
                    cur = queue.pop(0)
                    level.append(cur)
                    chars = list(cur)

                    for j in range(len(chars)):
                        ch = chars[j]
                        for c in string.ascii_letters:

                            if c == ch:
                                continue
                            chars[j] = c
                            cs = ''.join(map(str, chars))
                            if cs in wordSet and visited[cs] == False:
                                q.append(cs)
                                visited[cs] = True
                        chars[j] = ch
                graph.append(list(level))
            graph.pop(0)
        constructGraph(wordSet, q)
        res = []

        def backtrack(beginWord, endWord, path, level):
            if beginWord == endWord:
                res.append(list(path))
                return

            i = 0
            while level < len(graph) and i < len(graph[level]):
                s = graph[level][i]
                if isDifOne(s, path[-1]) is False:
                    i = i+1
                    continue
                path.append(s)
                backtrack(s, endWord, path, level+1)
                path.pop(-1)
                # level=level-1
                i = i+1

        path = [beginWord]
        backtrack(beginWord, endWord, path, 0)
        return res


testcase1 = ["hot", "dot", "dog", "lot", "log", "cog"]
testcase2 = ['a', 'b', 'c']
s = Solution()
s.findLadders("hit", "cog", testcase1)
