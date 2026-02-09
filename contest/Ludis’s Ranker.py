import sys

input= sys.stdin.readline

n= int(input())

a= list(map(int, input().split()))
sort_a= sorted(set(a), reverse=True)
greater= {}

rank=1
for num in sort_a:
    greater[num]= rank
    rank+= a.count(num)

print(*(greater[num] for num in a))