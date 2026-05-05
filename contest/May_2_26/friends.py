t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    p = list(map(int, input().split()))
    found = False
    for i in range(n):
        
        if p[p[i]-1] == i+1:
            found = True
            break
    if found:
        results.append("2")
    else:
        results.append("3")

for res in results:
    print(res)
