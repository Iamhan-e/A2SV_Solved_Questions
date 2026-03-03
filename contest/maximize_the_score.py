import sys

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    n= int(input().strip())
    x_y= list(map(int, input().split()))

    x_y.sort()
    score= 0

    for i in range(1, n*2, 2):
        score+= min(x_y[i], x_y[i-1])

    print(score)