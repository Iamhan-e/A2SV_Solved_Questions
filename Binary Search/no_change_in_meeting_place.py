import sys

input= sys.stdin.readline

n= int(input().strip())

dis= list(map(int, input().split()))
speed= list(map(int, input().split()))

lo=0
hi= 1e9

def canMeet(t):
    lft_max= float('-inf')
    right_min= float('inf')

    for s, v in zip(dis, speed):
        lb= s - v*t
        ub= s + v* t

        lft_max= max(lb, lft_max)
        right_min= min(ub, right_min)
        
    return lft_max <= right_min

for _ in range(60):
    mid= (hi + lo)/2

    if canMeet(mid):
        hi= mid 
    else:
        lo= mid

print(f"{hi:.12f}")


#https://codeforces.com/problemset/problem/780/B