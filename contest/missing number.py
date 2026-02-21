import sys

input = sys.stdin.readline

n= int(input().strip())
levels= set(map(int, input().split()))



for i in range(1, n+1):
    if i not in levels:
        print(i)
        break

