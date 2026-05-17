import sys

input= sys.stdin.readline

n, s= map(int, input().split())
arr= list(map(int, input().split()))

l=0
res=0
ans=0
for r in range(n):

    res+= arr[r]
    while res > s and l<= r:
        res-=arr[l]
        l+=1
    ans= max(ans, r-l+1)
print(ans)