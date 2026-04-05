import sys

input= sys.stdin.readline

t= int(input())

for _ in range(t):
    n= int(input().strip())
    books= list(map(int, input().split()))

    ans=0
    for i in range(n-1):
        total= books[i] + books[-1]

        if total > ans:
            ans= total
    print(ans)