import sys

input= sys.stdin.readline

n= int(input().strip())
nums= list(map(int, input().split()))
nums.sort()


j= n-1
total=0
for i in range(n//2):
    total+= (nums[i] + nums[j]) ** 2
    j-=1

print(total)