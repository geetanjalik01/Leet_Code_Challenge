class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        old = [row[:] for row in board]

        for i in range(m):
            for j in range(n):
                live = 0

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if (x == i and y == j):
                            continue

                        if 0 <= x < m and 0 <= y < n:
                            live += old[x][y]

                
                if old[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1