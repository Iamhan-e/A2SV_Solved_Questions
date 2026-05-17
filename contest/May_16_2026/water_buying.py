import sys

input= sys.stdin.readline

q= int(input())
res= []
for _ in range(q):
    n, a, b = map(int, input().split())

    cost_per_2L = min(2 * a, b)
    pairs = n // 2
    
    remainder = n % 2
    
    total_cost = pairs * cost_per_2L + remainder * a
    res.append(str(total_cost))
        
print('\n'.join(res))