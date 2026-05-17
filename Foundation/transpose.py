class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row= len(matrix)
        col= len(matrix[0])

        res= []
        for c in range(col):
            new_m= []
            for r in range(row):
                new_m.append(matrix[r][c])
            res.append(new_m)

        return res