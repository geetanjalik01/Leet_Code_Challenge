class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                num = int(val)
                box = (r // 3) * 3 + (c // 3)

                if rows[r][num] or cols[c][num] or boxes[box][num]:
                    return False

                rows[r][num] = True
                cols[c][num] = True
                boxes[box][num] = True

        return True
    