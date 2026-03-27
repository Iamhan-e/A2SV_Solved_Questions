import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())

cnt = [0] * (200002)


for _ in range(n):
    l, r = map(int, input().split())
    cnt[l] += 1
    cnt[r + 1] -= 1

for i in range(1, 200001):
    cnt[i] += cnt[i - 1]


good = [0] * (200002)
for i in range(1, 200001):
    if cnt[i] >= k:
        good[i] = 1


pref = [0] * (200002)
for i in range(1, 200001):
    pref[i] = pref[i - 1] + good[i]


for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a - 1])


#https://codeforces.com/contest/816/problem/B