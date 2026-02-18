import sys


input = sys.stdin.readline
line = input().strip()

if line:
    t = int(line)
    for _ in range(t):
        n = int(input().strip())
        
        a = 0
        b = 0
       
        i=1
        
        while n>0:
            
            give_card= min(i, n)
            if i%4== 0 or i%4== 1:
                a+=give_card
            else:
                b+=give_card
            i+=1

            n-=give_card
            
        print(f"{a} {b}")