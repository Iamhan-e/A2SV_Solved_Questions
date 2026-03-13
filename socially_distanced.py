import sys

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    n= int(input().strip())
    p= list(map(int, input().split()))

    res=[p[0]]
    for i in range(1, n-1):
        if (p[i] - p[i-1]) * (p[i+1]- p[i]) < 0:
            res.append(p[i])
    
    res.append(p[-1])
    print(len(res))
    print(*res)


            