import sys
import math

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    low = 1
    high = k + 2000000  # Safe upper bound
    while low < high:
        mid = (low + high) // 2
        sqrt_mid = math.isqrt(mid)
        if mid - sqrt_mid >= k:
            high = mid
        else:
            low = mid + 1
    print(low)
