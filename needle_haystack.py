import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    t_str = input().strip()

    cs = [0]*26
    ct = [0]*26

    for c in s:
        cs[ord(c)-97] += 1
    for c in t_str:
        ct[ord(c)-97] += 1

    possible = True
    for i in range(26):
        if cs[i] > ct[i]:
            possible = False
            break

    if not possible:
        print("Impossible")
        continue

    rem = [ct[i] - cs[i] for i in range(26)]
    first = ord(s[0]) - 97

    
    a = []
    for i in range(first):
        a.append(chr(i+97)*rem[i])
    a.append(s)
    for i in range(first,26):
        a.append(chr(i+97)*rem[i])
    cand1 = "".join(a)

    
    b = []
    for i in range(first+1):
        b.append(chr(i+97)*rem[i])
    b.append(s)
    for i in range(first+1,26):
        b.append(chr(i+97)*rem[i])
    cand2 = "".join(b)

    print(min(cand1, cand2))