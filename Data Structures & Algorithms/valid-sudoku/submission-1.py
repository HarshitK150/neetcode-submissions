from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[int]]) -> bool:
        rows = defaultdict(set)       # row(int) -> seen_values(set)
        cols = defaultdict(set)       # col(int) -> seen_values(set)
        subBoxes = defaultdict(set)   # box_coordinates(tuple(x, y)) -> seen_values(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                
                if val == ".":
                    continue

                if (val in rows[r] or 
                    val in cols[c] or 
                    val in subBoxes[(r // 3, c // 3)]):

                    return False

                rows[r].add(val)
                cols[c].add(val)
                subBoxes[(r // 3, c // 3)].add(val)

        return True