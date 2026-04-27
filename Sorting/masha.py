
#https://codeforces.com/contest/1741/problem/D

import sys

input = sys.stdin.readline

def dfs(l, r, arr, impossible_flag):
    if impossible_flag[0] or r - l == 1:
        return 0
    
    mid = (l + r) // 2
    
    
    max_l = max(arr[l:mid])
    max_r = max(arr[mid:r])
    
    ops = 0
    
    
    if max_l > max_r:
        ops = 1
       
        for i in range(mid - l):
            arr[l + i], arr[mid + i] = arr[mid + i], arr[l + i]
      
        max_l, max_r = max_r, max_l
    
  
    if max_l > max_r:
        impossible_flag[0] = True
        return 0
    
    return dfs(l, mid, arr, impossible_flag) + dfs(mid, r, arr, impossible_flag) + ops

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    tree = list(map(int, input().split()))
    
   
    arr = tree[:]
    impossible_flag = [False]  
    
    total_ops = dfs(0, n, arr, impossible_flag)
    
   
    is_sorted = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break
    
    if impossible_flag[0] or not is_sorted:
        print(-1)
    else:
        print(total_ops)

