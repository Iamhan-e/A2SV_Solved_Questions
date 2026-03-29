import sys

input = sys.stdin.readline

n = int(input().strip())
weight = list(map(int, input().split()))

total = sum(weight)
ans = float('inf')

def dfs(i, current_sum):
    global ans
    if i == n:
        other_sum = total - current_sum
        ans = min(ans, abs(current_sum - other_sum))
        return
    
   
    dfs(i + 1, current_sum + weight[i])
   
    dfs(i + 1, current_sum)

dfs(0, 0)
print(ans)
