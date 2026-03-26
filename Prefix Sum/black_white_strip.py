import sys

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    s= input().strip()


    prefix= [0] * (n+1)
    minimum= float('inf')
    for i in range(n):
        prefix[i+1]= prefix[i] + (1 if s[i]== 'W' else 0)
    
    for i in range(n-k+1):
        white_window= prefix[k+i] - prefix[i]

        minimum= min(minimum, white_window)
    
    print(minimum)
 