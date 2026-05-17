class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n= len(mat)

        for _ in range(4):
            if mat== target:
                return True
        
            for r in range(n):
                for c in range(r+1, n):
                    mat[r][c], mat[c][r]= mat[c][r], mat[r][c]

            for r in range(n):
                for c in range(n//2):
                    mat[r][c], mat[r][n-c-1]= mat[r][n-c-1], mat[r][c]

        return False