class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        boxes = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if row not in rows:
                    rows[row] = set()
                if val != "." and val in rows[row]:
                    return False
                rows[row].add(val)

                if col not in cols:
                    cols[col] = set()
                if val != "." and val in cols[col]:
                    return False
                cols[col].add(val)

                key = (row // 3, col // 3)

                if key not in boxes:
                    boxes[key] = set()

                if val != "." and val in boxes[key]:
                    return False
                boxes[key].add(val)
        return True
        
        
        
        
        

            
