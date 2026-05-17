import sys

input= sys.stdin.readline

n_a, n_b= map(int, input().split())

a= list(map(int, input().split()))
b= list(map(int, input().split()))

cnt=0

pa=0
pb=0
ans=0
while pa < n_a and pb < n_b:

    if a[pa] < b[pb]:
      pa+=1

    elif a[pa] > b[pb]:
      pb+=1
    
    else:
        curr= a[pa]
        cntA=0
        cntB=0

        while pa < n_a and a[pa]== curr:
          cntA+=1
          pa+=1
        
        

        while pb < n_b and b[pb]== curr:
          cntB+=1
          pb+=1

        
        ans+= cntA * cntB

print(ans)
