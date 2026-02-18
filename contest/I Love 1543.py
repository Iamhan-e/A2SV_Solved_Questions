import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    total = 0
    top, bottom, left, right = 0, n - 1, 0, m - 1

    while top < bottom and left < right:
        layer = []
        
        for j in range(left, right + 1):
            layer.append(grid[top][j])
        
        for i in range(top + 1, bottom):
            layer.append(grid[i][right])
        
        for j in range(right, left - 1, -1):
            layer.append(grid[bottom][j])
        
        for i in range(bottom - 1, top, -1):
            layer.append(grid[i][left])

        
        layer_str = ''.join(layer)
        layer_str += layer_str[:3]

    
        for i in range(len(layer_str) - 3):
            if layer_str[i:i+4] == "1543":
                total += 1

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    print(total)