import sys


input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):

    num= input().strip()
    pi= "3141592653589793238462643383279"
    314159265358979323846264338327
    cnt= 0
    for i in range(min(len(pi), len(num))):
        
        if num[i] == pi[i]:
            cnt+=1
        else:
            break

    print(cnt)
    