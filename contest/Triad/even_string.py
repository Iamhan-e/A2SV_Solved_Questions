import sys

input = sys.stdin.readline

t_str = input().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        s = input().strip()
        n = len(s)
        
        seen = set()
        pairs_found = 0
        
        for char in s:
            if char in seen:
                pairs_found += 1
                seen.clear()
            else:
                seen.add(char)
        
        print(n - 2 * pairs_found)