class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt=0
        rows= len(grid)
        cols= len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    cnt+=1

        return cnt