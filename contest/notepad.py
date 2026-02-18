import sys

input= sys.stdin.readline

t= int(input())

for _ in range(t):
    n= int(input())
    s= input().strip()

    is_copy= False
    sets= set()

    for i in range(1, n-1):
        pair= s[i:i+2]

        if pair in sets:
            is_copy= True
            break
        
        sets.add(s[i-1:i+1])
    if not is_copy:
        print("NO")
    else:
        print("YES")