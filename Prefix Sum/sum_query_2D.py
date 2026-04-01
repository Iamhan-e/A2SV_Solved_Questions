class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if not matrix or not matrix[0]:
            self.prefix = []          
            return

        m, n = len(matrix), len(matrix[0])

        self.prefix = [[0] * n for _ in range(m)]
        for r in range(m):
            running = 0
            for c in range(n):
                running += matrix[r][c]
                self.prefix[r][c] = running
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.prefix:          
            return 0
        total = 0
        for r in range(row1, row2 + 1):
            row_sum = self.prefix[r][col2]
            if col1 > 0:
                row_sum -= self.prefix[r][col1 - 1]
            total += row_sum
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)