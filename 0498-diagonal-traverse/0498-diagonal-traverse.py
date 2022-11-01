class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # check for empty matrix
        if not matrix or not matrix[0]:
            return []
        
        # N=Row, M = Column
        N, M = len(matrix), len(matrix[0])
        
        row, column = 0, 0
        
        result = []
        
        direction = 1  # Goto up
        while row<N and column <M:
            result.append(matrix[row][column])
            
            # dirention 1 hole uporer dike uthbe ba column value barbe
            new_row = row + (-1 if direction==1 else 1) 
            new_column = column + (1 if direction==1 else -1)
            
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                if direction:
                    row += (column==M-1)
                    column += (column<M-1)
                else:
                    column += (row==N-1)
                    row += (row<N-1)
                
                direction = 1 - direction
            else:
                row = new_row
                column = new_column
            
        return result