import sys

input= sys.stdin.readline

n, m= map(int, input().split())
saving= []
total_size= 0

for _ in range(n):
    a, b= map(int, input().split())
    saving.append(a- b)
    total_size+= a

cnt= 0
if total_size <= m:
    print(0)
    sys.exit()
   

saving.sort(reverse=True)

for s in saving:
    total_size-=s
    cnt+=1

    if total_size <= m:
        print(cnt)
        sys.exit()
        
print(-1)
        
    

