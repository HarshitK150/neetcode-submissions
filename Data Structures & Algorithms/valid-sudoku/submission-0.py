class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val == ".":
                    continue
                if val in seen:
                    return False
                else:
                    seen.add(val)

        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                else:
                    seen.add(val)

        def check3by3(r: int, c: int) -> bool:
            x, y = 0, 0
            seen = set()
            while x < 3 and y < 3:
                val = board[r+x][c+y]
                if val != ".":
                    if val in seen:
                        return False
                    else:
                        seen.add(val)

                if x == 2:
                    x = 0
                    y += 1
                else:
                    x += 1
            return True

        r, c = 0, 0
        while r <= 6 and c <= 6:
            if not check3by3(r, c):
                return False
            
            if r == 6:
                r = 0
                c += 3
            else:
                r += 3

        return True