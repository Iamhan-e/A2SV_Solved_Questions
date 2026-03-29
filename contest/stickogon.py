import sys
from collections import Counter

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):

    n= int(input().strip())
    sticks= list(map(int, input().split()))

    cnt = Counter(sticks)
    res=0
    for c in cnt.values():
        res+= c//3

    print(res)

    