class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        copy = [row[:] for row in board]

        for i in range(m):
            for j in range(n):
                live = 0
                for x, y in d:
                    r, c = i + x, j + y
                    if 0 <= r < m and 0 <= c < n and copy[r][c] == 1:
                        live += 1

                if copy[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 0
                elif copy[i][j] == 0 and live == 3:
                    board[i][j] = 1