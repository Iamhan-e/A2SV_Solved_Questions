import sys
from collections import defaultdict

input= sys.stdin.readline

n, k= map(int, input().split())
nums= list(map(int, input().split()))
freq= defaultdict(int)

res=0
j=0
distinct=0
for i in range(n):
    freq[nums[i]]+=1
    if freq[nums[i]] == 1:
        distinct+=1

    while distinct > k:
        freq[nums[j]]-=1
        
        if freq[nums[j]] == 0:
            distinct-=1
        j+=1

    res+= (i-j+1)
print(res)