class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            board.append([board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i] , board[6][i], board[7][i], board[8][i]])

        for i in range(0, 3):
            board.append(board[i*3][0:3] + board[i*3+1][0:3] + board[i*3+2][0:3])
            board.append(board[i*3][3:6] + board[i*3+1][3:6] + board[i*3+2][3:6])
            board.append(board[i*3][6:9] + board[i*3+1][6:9] + board[i*3+2][6:9])
            
        for b in board:
            m = {}
            for v in b:
                if v == '.': 
                    continue
                if v in m:
                    return False
                m[v] = True
                
        return True