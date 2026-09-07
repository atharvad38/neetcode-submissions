class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]
        squares = [[] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                cur = board[r][c]
                square_index = (r // 3) * 3 + (c // 3)

                if cur in rows[r] or cur in cols[c] or cur in squares[square_index]:
                    return False

                rows[r].append(cur)
                cols[c].append(cur)
                squares[square_index].append(cur)

        return True