import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    res = set() 

    i=0

    while i < len(s):
        j=i

        while j < len(s) and s[i]== s[j]:
            j+=1

        length= j- i

        if length % 2 != 0:
            res.add(s[i])
        i=j
    print("".join(sorted(list(res))))
