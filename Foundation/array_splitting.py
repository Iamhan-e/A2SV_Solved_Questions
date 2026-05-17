import sys
input= sys.stdin.readline

n, k = map(int, input().split())
arr= list(map(int, input().split()))

diff= []
for i in range(1, n):
    
    diff.append(arr[i]- arr[i-1])

diff.sort(reverse=True)

s=0

for i in range(k-1):
    s+= diff[i]

max_span= arr[-1] - arr[0]
min_span= max_span - s

print(min_span)