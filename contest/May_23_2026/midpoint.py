

t = int(input().strip())
for _ in range(t):
    a, x, y = map(int, input().split())
    
    if (a < x and a < y) or (a > x and a > y):
        print("YES")
    else:
        print("NO")