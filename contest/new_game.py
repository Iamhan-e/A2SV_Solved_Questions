1import sys
from collections import Counter
input= sys.stdin.readline

t= int(input().strip())

for _ in range(t):
    n, k= map(int, input().split())
    cards= list(map(int, input().split()))

    cards.sort()
    freq= Counter(cards)

    unique= list(freq.keys())
    count= list(freq.values())

   
    start=0
    
    current_sum=0
    ans= 0

    for end in range(len(unique)):
        current_sum+= count[end]

        if end > start and unique[end] != unique[end-1]+1:
            start= end
            current_sum= count[end]

        while unique[end] - unique[start] > k-1:
            current_sum-= count[start]
            start+=1
           

        ans= max(ans, current_sum)
       

    print(ans)

        

    
            

    
        



