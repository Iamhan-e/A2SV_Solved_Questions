import sys
from collections import defaultdict

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    n, k= map(int, input().split())
    juice= [list(map(int,input().split())) for _ in range(k)]

    brand_cost= defaultdict(int)
   
    juice.sort()

    for b, c in juice:
        brand_cost [b]+=c
    tot=sorted(brand_cost.values(), reverse=True)

   
    print(sum(tot[:n]))
   
    
