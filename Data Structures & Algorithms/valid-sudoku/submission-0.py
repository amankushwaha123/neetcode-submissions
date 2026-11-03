class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row
        for row in range(9):
            seen=set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # for column
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[col][row] == '.':
                    continue
                if board[col][row] in seen:
                    return False
                seen.add(board[col][row])

        # for 3*3 box
        for sqre in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sqre//3)*3+i
                    col = (sqre%3)*3+j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col]) 
        return True
                

        
        
        