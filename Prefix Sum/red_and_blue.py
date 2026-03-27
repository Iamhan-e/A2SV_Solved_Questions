#https://codeforces.com/contest/1469/problem/B

import sys

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    n= int(input().strip())
    red= list(map(int, input().split()))

    m= int(input().strip())
    blue= list(map(int, input().split()))

    current= 0
    max_r, max_b=0,0

    for r in red:
        current+=r
        max_r= max(max_r, current)
   
    current=0
    for b in blue:
        current+=b
        max_b= max(max_b, current)

    print(max_b+ max_r)


    
   