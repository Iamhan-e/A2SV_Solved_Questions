import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())        
    s = input().strip()              

    
    answer = None                    

    for first_len in range(1, n):     
        segs = [s[:first_len]]       
        prev = segs[0]
        pos  = first_len
        ok   = True

        
        while pos < n:
            cur = ''
            found = False
            for end in range(pos, n):
                cur += s[end]                    
                
                if len(cur) > len(prev) or (len(cur) == len(prev) and cur > prev):
                    segs.append(cur)
                    prev = cur
                    pos = end + 1
                    found = True
                    break
            if not found:            
                ok = False
                break

        if ok and len(segs) >= 2:       
            answer = segs
            break

    
    if answer is None:
        print("NO")
    else:
        print("YES")
        print(len(answer))
        print(" ".join(answer))
