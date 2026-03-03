import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    cards = list(map(int, input().split()))

    cnt = 0
    s = 0
    start = 0
    
    for i in range(n):
        s += cards[i]
        if s > r:
            
            while start <= i and s > r:
                s -= cards[start]
                start += 1
        
        if l <= s <= r:
            cnt += 1
            s = 0
            start = i + 1
    
    print(cnt)