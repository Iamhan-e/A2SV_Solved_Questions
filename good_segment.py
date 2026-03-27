import sys
from collections import defaultdict

input= sys.stdin.readline

n, k= map(int, input().split())
a= list(map(int, input().split()))

l=0
best_l, best_r= 0,0
cnt= defaultdict(int)

for r in range(n):

    cnt[a[r]]+=1

    while len(cnt) > k:
        cnt[a[l]] -=1
        if cnt[a[l]]== 0:
            del cnt[a[l]]
        l+=1

    if r-l > best_r - best_l:
        best_r= r
        best_l= l

print(best_l+1, best_r+1)


#https://codeforces.com/problemset/problem/616/D