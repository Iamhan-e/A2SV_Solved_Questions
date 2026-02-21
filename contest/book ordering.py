import sys

input = sys.stdin.readline

n = int(input())

possible = True
current_max = float('inf')

for _ in range(n):
    w, h = map(int, input().split())
    
    hi = max(w, h)
    lo = min(w, h)
    
    if hi <= current_max:
        current_max = hi
    elif lo <= current_max:
        current_max = lo
    else:
        possible = False
        break

print("YES" if possible else "NO")