import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    pos = list(input().strip())
    cnt = 0
    
    curr_x = x
    first_hit = -1
    
    for i in range(n):
        if pos[i] == 'L':
            curr_x -= 1
        else:
            curr_x += 1
        
        if curr_x == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    cnt = 1
    
    curr_x = 0
    cycle = -1
    
    for i in range(n):
        if pos[i] == 'L':
            curr_x -= 1
        else:
            curr_x += 1
        
        if curr_x == 0:
            cycle = i + 1
            break
    
    if cycle == -1:
        print(cnt)
    else:
        remaining = k - first_hit
        cnt += remaining // cycle
        print(cnt)