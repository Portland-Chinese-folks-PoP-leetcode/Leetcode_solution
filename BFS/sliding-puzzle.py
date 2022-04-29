# https: // leetcode-cn.com/problems/sliding-puzzle/submissions/
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(chars: List[str], i, j):
            temp = chars[i]
            chars[i] = chars[j]
            chars[j] = temp
            return ''.join(map(str, chars))
        neighbour = [[1, 3], [0, 4, 2], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        m, n = 2, 3
        sb = []
        for i in range(m):
            for j in range(n):
                sb.append(board[i][j])
        start = ''.join(map(str, sb))
        target = '123450'
        q = []
        visited = set()
        q.append(start)
        visited.add(start)
        step = 0
        while len(q) > 0:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur == target:
                    return step
                idx = cur.index('0')

                for adj in neighbour[idx]:

                    new_board = swap(list(cur), adj, idx)
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)

            step += 1
        return -1
