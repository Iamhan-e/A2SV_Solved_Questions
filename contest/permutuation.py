import sys

input= sys.stdin.readline

t= int(input())

for _ in range(t):
    m,s = map(int, input().split())
    b= list(map(int, input().split()))
    
    

    i=1
    total=0
    cnt = 0
    b_s= set(b)

    while total < s:
        if i not in b_s:
            b_s.add(i)
            total+=i
            
        i+=1
    
    set_range= set(range(1, max(b_s)+1))

    if total == s and  b_s == set_range:
        print("YES")
    else:
        print("NO")

    