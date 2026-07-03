class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkBoxes(board,r_start,c_start):
            b_set = set()
            for i in range(r_start,r_start+3):
                for j in range(c_start,c_start+3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in b_set:
                        return False
                    b_set.add(board[i][j])
            return True



        
        row = len(board)
        col = len(board[0])
        
        for i in range(row):
            r_set = set()
            for j in range(col):
                if board[i][j] == '.':
                    continue
                if board[i][j] in r_set:
                    return False
                r_set.add(board[i][j])
        
        for j in range(col):
            c_set = set()
            for i in range(row):
                if board[i][j] == '.':
                    continue
                if board[i][j] in c_set:
                    return False
                c_set.add(board[i][j])

            
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not checkBoxes(board,i,j):
                    return False
        
        return True


            
