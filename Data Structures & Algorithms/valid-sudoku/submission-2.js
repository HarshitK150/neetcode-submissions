class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const rows = new Map();
        const cols = new Map();
        const boxes = new Map();

        for (let i = 0; i < board.length; i++) {
            rows.set(i, new Set());
            cols.set(i, new Set());
            boxes.set(i, new Set());
        }

        for (let r = 0; r < board.length; r++) {
            for (let c = 0; c < board[0].length; c++) {
                const val = board[r][c];
                if (val === ".") {
                    continue;
                }

                if (rows.get(r).has(val) || 
                    cols.get(c).has(val) || 
                    boxes.get(
                        Math.floor(r/3) * 3 + Math.floor(c/3)
                        ).has(val)) {
                        
                        return false;
                }

                rows.get(r).add(val);
                cols.get(c).add(val);
                boxes.get(Math.floor(r/3) * 3 + Math.floor(c/3)).add(val);
            }
        }
        return true;
    }
}
