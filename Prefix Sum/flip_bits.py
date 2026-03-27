import sys

input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):

    n= int(input().strip())
    a= input().strip()
    b= input().strip()
    
    balance = [0] * n
    zero = 0
    one = 0

    for i in range(n):
        if a[i] == '0':
            zero += 1
        else:
            one += 1
        
        if zero == one:
            balance[i] = 1

    flip = False
    possible = True

    for i in range(n - 1, -1, -1):
        cur = a[i]

        if flip:
            cur = '1' if cur == '0' else '0'

        if cur == b[i]:
            continue

       
        if balance[i] == 0:
            possible = False
            break

        flip = not flip

    print("YES" if possible else "NO")

#https://codeforces.com/problemset/problem/1504/B