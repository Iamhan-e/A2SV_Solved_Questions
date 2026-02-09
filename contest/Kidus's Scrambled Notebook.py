import sys

input= sys.stdin.readline
t= int(input())

for _ in range(t):
    s= input().strip()
    
    found= False
    for i in range(len(s)):
        a= s[:i+1]
        b= s[i+1:]

        
        if b != '':
            if a[0] == '0' or b[0]== '0':
                continue
            elif int(b) > int(a):
                found= True
                print(a, b)
                break
    if not found:
        print(-1)