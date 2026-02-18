import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    grid = [list(input().strip()) for _ in range(n)]

    total_cost = 0
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            
            vals = [
                int(grid[i][j]),
                int(grid[j][n - 1 - i]),
                int(grid[n - 1 - i][n - 1 - j]),
                int(grid[n - 1 - j][i])
            ]
            ones = sum(vals)
            total_cost += min(ones, 4 - ones)

    print(total_cost)