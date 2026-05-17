import sys

input= sys.stdin.readline

n, k= map(int, input().split())

a= list(map(int, input().split()))
b= list(map(int, input().split()))


jobs = [[] for _ in range(k + 1)]
for cost, job in zip(b, a):
    jobs[job].append(cost)
    
candidates = []
needed = 0


for j in range(1, k + 1):
    if not jobs[j]:
        
        needed += 1
    else:
    
        jobs[j].sort()
        
        candidates.extend(jobs[j][:-1])
        

candidates.sort()
print(sum(candidates[:needed]))