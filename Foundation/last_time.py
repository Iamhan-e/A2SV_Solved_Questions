import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
   
    casinos.sort()
    
    cur = k
    for l, r, real in casinos:
        if l > cur:
            break
        cur = max(cur, real)
    
    print(cur)