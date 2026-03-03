import sys

input= sys.stdin.readline

n= int(input().strip())
a= list(map(int, input().split()))
d=0

a.sort()
for size in a:
    if size >= d+1:
        d+=1
    
print(d)