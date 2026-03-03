import sys

input= sys.stdin.readline

n, k= map(int, input().split())
a= list(map(int, input().split()))

instruments= []

for i in range(n):
    instruments.append((a[i], i+1))

instruments.sort()

cnt= 0
res= []

for num, indx in instruments:
    if k >= num:
        k-= num
        cnt+=1
        res.append(indx)
    else:
        break


print(cnt)
print(*res)
