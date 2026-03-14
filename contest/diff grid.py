import sys

input = sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    rows, cols = map(int, input().split())
    
    
    grid= []
    for _ in range(rows):
        grid.extend(input().split())
    
    
    total = rows * cols
    
    
    if total == 1:
        print("-1")
        continue
        
    
    shifted = grid[1:] + [grid[0]]
    
    
    for i in range(0, total, cols):
        
        row_to_print = shifted[i : i + cols]
        print(*(row_to_print))