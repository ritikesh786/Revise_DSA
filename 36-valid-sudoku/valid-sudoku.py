class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for item in board:
            clean_list = [v for v in item if v != '.']
            if len(set(clean_list)) == len(clean_list):
                continue
            else:
                return False
        
        
        for i in range(len(board)):
            j = 0
            col_list = []  
            while j < len(board):
                if board[j][i] != '.':
                    
                    col_list.append(board[j][i])
                j +=1
            # print(col_list)
            if len(set(col_list)) == len(col_list):
                continue
            else:
                return False
        for r_b in range(3):
            for c_b in range(3):
                mat_list = []
                for r in range(3):
                    for c in range(3):
                        
                        row = r_b * 3 + r
                        col = c_b * 3 + c

                        if board[row][col] != '.':
                            mat_list.append(board[row][col])
                if len(set(mat_list)) == len(mat_list):
                    continue
                else:
                    return False

                        # print(board[row][col])
                    
        return  True