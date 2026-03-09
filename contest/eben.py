import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())         
    s = input().strip()              

    
    odd_pos = []
    for i, ch in enumerate(s):
        if (ord(ch) - ord('0')) % 2 == 1:  
            odd_pos.append(i)
            if len(odd_pos) == 2:          
                break

    if len(odd_pos) < 2:       
        print(-1)
    else:
        i, j = odd_pos[0], odd_pos[1]
        print(s[i] + s[j])
