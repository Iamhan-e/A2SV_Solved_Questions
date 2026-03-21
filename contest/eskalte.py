import sys

input= sys.stdin.readline

n= int(input().strip())
ppl= list(map(int, input().split()))

rank=0
for i in range(n):
    
    if max(ppl) > 25:
        rank= max(ppl)- 25
        
print(rank) 

    



