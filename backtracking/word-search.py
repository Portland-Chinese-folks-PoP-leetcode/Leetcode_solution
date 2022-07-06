from typing import List


class Solution:
    res = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(i, j, start):
            if board[i][j] != word[start]:
                return False
            if start == len(word)-1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in direction:
                newi, newj = i+di, j+dj
                if 0 <= newi < n and 0 <= newj < m and (newi, newj) not in visited:
                    if backtrack(newi, newj, start+1):
                        result = True
                        break
            visited.remove((i, j))
            return result
        visited = set()
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
        return False


# class Solution:  # 我的思路 通过50个用例
#     res = False

#     def exist(self, board: List[List[str]], word: str) -> bool:
#         n = len(board)
#         m = len(board[0])
#         track = []

#         def backtrack(i, j, track, start, visited):
#             print(track)
#             if i >= n or j >= m or i < 0 or j < 0 or visited[i][j] == True:
#                 return
#             if len(track) == len(word):
#                 if ''.join(map(str, track)) == word:
#                     print(''.join(map(str, track)))
#                     self.res = True
#                     print("True")
#                     return
#             if board[i][j] != word[start]:
#                 return

#             visited[i][j] = True
#             track.append(board[i][j])
#             backtrack(i-1, j, track, start+1, visited)
#             backtrack(i+1, j, track, start+1, visited)
#             backtrack(i, j-1, track, start+1, visited)
#             backtrack(i, j+1, track, start+1, visited)
#             track.pop(-1)
#             visited[i][j] == False
#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] == word[0]:
#                     track = []
#                     visited = [[False for i in range(m)] for i in range(n)]
#                     backtrack(i, j, track, 0, visited)
#         print(self.res)
#         return self.res


s = Solution()
board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCB"
board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word2 = "ABCCED"
b3 = [['a']]
w3 = "a"
s.exist(b3, w3)
