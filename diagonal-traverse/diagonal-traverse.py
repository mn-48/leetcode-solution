class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        N, M = len(mat), len(mat[0])
        
        result, intermediate = [], []
        
        for d in range(M+N-1):
            intermediate.clear()
            r ,c = 0 if d<M else d-M+1, d if d<M else M-1
            
            while r<N and c>-1:
                intermediate.append(mat[r][c])
                r+=1
                c-=1
            if d%2==0:
                result.extend(intermediate[::-1])
                
            else:
                result.extend(intermediate)
                
                
        return result
        
# Time complexity O(M.N)
# Space complexity O(min(M.N))