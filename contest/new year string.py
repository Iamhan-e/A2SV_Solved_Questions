import sys
input= sys.stdin.readline

t= int(input())



for _ in range(t):
    n= int(input())
    s= input().strip()
    cnt=0
    if '2026' in s or '2025' not in s:
        print(cnt)
    elif '2025' in s:
        print(cnt+1)
    else:
        print(cnt)
     
