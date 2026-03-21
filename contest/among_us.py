import sys

input= sys.stdin.readline

a, b= map(int, input().split())

res=[b]

while a < b:
    
    if b % 2 ==0:
        b/=2

    elif b % 10 == 1:
        b//= 10
    else:
        break
    res.insert(0, int(b))

if res[0] == a:
    print("YES")
    print(len(res))
    print(*res)

else:
    print("NO")