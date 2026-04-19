import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    items = list(map(int, input().split()))

    items.sort(reverse=True)

    diffs = []
    for i in range(0, n - 1, 2):
        diffs.append(items[i] - items[i + 1])

    diffs.sort(reverse=True)

    remaining_k = k
    for i in range(len(diffs)):
        if remaining_k >= diffs[i]:
            remaining_k -= diffs[i]
            diffs[i] = 0
        else:
            diffs[i] -= remaining_k
            remaining_k = 0
            break

    result = sum(diffs)
    if n % 2 == 1:
        result += items[-1]

    print(max(0, result))