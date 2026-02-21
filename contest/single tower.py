import sys

input= sys.stdin.readline

n= int(input().strip())
towers= []
all_blocks= []
s=0

for _ in range(n):

    tow= list(map(int, input().split()))
    tower= tow[1:]
    sort_tower= sorted(tower)

    towers.append(tower)
    all_blocks.extend(tower)

sort_blocks= sorted(all_blocks)

rank= {val: i for i, val in enumerate(sort_blocks)}

s=0
for t in towers:

    for i in range(len(t)-1):

        if rank[t[i+1]] != rank[t[i]] +1:
            s+=1

c= n+s-1

print(s, c)