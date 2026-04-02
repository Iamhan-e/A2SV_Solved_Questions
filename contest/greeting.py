import sys
from collections import defaultdict

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):

    n= int(input().strip())
    pos= list(map(int, input().split()) for _ in range(n))

    arr= []
    meet= 0
    cnt= defaultdict(int) 
    for start, end in pos:
        
        arr.extend(s for s in range(start, end))
    #print(arr)
    for num in arr:
        cnt[num]+=1
    print(cnt)
    for c in cnt.values():
        if c > 1:
            meet+=1
    
    #print(meet)
