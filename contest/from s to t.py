import sys
from collections import Counter

input = sys.stdin.readline

line = input().strip()
if line:
    q = int(line)
    
    for _ in range(q):
        
        s = input().strip()
        t = input().strip()
        p = input().strip()

        
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        
        
        if i != len(s):
            print("NO")
            continue

        
        counts_s = Counter(s)
        counts_t = Counter(t)
        counts_p = Counter(p)
        
       
        possible = True
        for char in counts_s:
            if counts_s[char] > counts_t[char]:
                possible = False
                break
        
        if not possible:
            print("NO")
            continue

        
        needed = counts_t - counts_s
        
        
        if not (needed - counts_p):
            print("YES")
        else:
            print("NO")