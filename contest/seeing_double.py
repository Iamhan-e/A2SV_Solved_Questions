import sys

input= sys.stdin.readline

t= int(input())

for _ in range(t):
   s= input().strip()
   n= len(s)
   
  
   new_s= s

   for i in range(n-1, -1, -1):
    new_s+= s[i]
   
   print(new_s)