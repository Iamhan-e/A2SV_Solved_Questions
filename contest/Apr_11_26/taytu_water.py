import sys

input = sys.stdin.readline

t = int(input().strip())
answers = []

for _ in range(t):
    n, k = map(int, input().split())

    d = list(map(int, input().split()))   
    a = list(map(int, input().split()))  


    if sum(a) > k:                
        answers.append("-1")
        continue

    lo, hi = 1, max(d)            

    while lo < hi:
        mid = (lo + hi) // 2
        total = 0
        
        for di, ai in zip(d, a):
            trips = (di + mid - 1) // mid          
            total += trips * ai
            if total > k:         
                break

        if total <= k:             
            hi = mid
        else:                      
            lo = mid + 1

    answers.append(str(lo))

print("\n".join(answers))
