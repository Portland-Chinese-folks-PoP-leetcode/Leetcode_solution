class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []
        for i in range(n):
            board.append(['.'] * n)

        def isValid(row, col):
            # 检查列是否有皇后
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            # 检查右上方是否有皇后
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            # 检查左上方是否有皇后
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            return True

        def backtrack(row):
            # 超出左后一行
            if row == n:
                result.append([''.join(b) for b in board])
                print('broad is ', board)
                print('result is ', result)
                return

            for col in range(n):
                # 排除不合法选择
                if not isValid(row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 进入下一秒决策
                backtrack(row + 1)
                # 撤销选择
                board[row][col] = '.'

        backtrack(0)
        return result
