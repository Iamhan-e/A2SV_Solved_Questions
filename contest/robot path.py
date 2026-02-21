import sys

input= sys.stdin.readline

n,k = map(int, input().split())

path= input().strip()
obstacle= False

i=0
next= 0
path_indx= []

for i in range(n):
    if path[i]== '.':
        path_indx.append(i)



for i in range(1, len(path_indx)):
    if path_indx[i] - path_indx[i-1] > k:
        obstacle= True

print("NO" if obstacle else "YES")
