import sys

input = sys.stdin.readline

t = int(input().strip())
answers = []

for _ in range(t):
 
    n, m = map(int, input().split())

    s = input().strip()          
    w = input().strip()         

   
    target = 0
    for ch in w:
        target += ord(ch) - ord('a')          


    pref = [0] * (n + 1)
    for i, ch in enumerate(s, start=1):
        pref[i] = pref[i - 1] + (ord(ch) - ord('a'))

   
    ok = False
    for start in range(0, n - m + 1):
        cur = pref[start + m] - pref[start]  
        if cur == target:
            ok = True
            break

    answers.append("YES" if ok else "NO")

print("\n".join(answers))
