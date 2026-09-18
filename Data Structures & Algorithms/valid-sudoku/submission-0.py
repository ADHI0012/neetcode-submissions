class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSquare(rowStart, rowEnd, colStart, colEnd):
            seen = set()
            for i in range(rowStart, rowEnd + 1):
                for j in range(colStart, colEnd + 1):
                    if board[i][j] != "." and board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True

        def checkRowAndColumn():
            for i in range(9):
                seenRow = set()
                seenCol = set()
                for j in range(9):
                    if board[i][j] != "." and board[i][j] in seenRow:
                        return False
                    if board[j][i] != "." and board[j][i] in seenCol:
                        return False
                    seenRow.add(board[i][j])
                    seenCol.add(board[j][i])
            return True
        
        if not checkRowAndColumn():
            return False
        
        if (checkSquare(0, 2, 0, 2) 
        and checkSquare(0, 2, 3, 5) and 
        checkSquare(0, 2, 6, 8) 
        and checkSquare(3, 5, 0, 2) and 
        checkSquare(3, 5, 3, 5) and 
        checkSquare(3, 5, 6, 8) and 
        checkSquare(6, 8, 0, 2) and
        checkSquare(6, 8, 3, 5) and
        checkSquare(6, 8, 6, 8)):
            return True
        
        return False
        
    