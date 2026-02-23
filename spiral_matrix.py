class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral= []
        m= len(matrix)
        n= len(matrix[0])

        right, left= n-1, 0
        top, bottom= 0, m-1
        
        

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                spiral.append(matrix[top][i])
            top+=1

            for i in range(top, bottom+1):
                spiral.append(matrix[i][right])
            right-=1

            if not (left <= right and top <= bottom):
                break
            
            for i in range(right, left-1, -1):
                spiral.append(matrix[bottom][i])
            bottom-=1

            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left+=1

        return spiral
