import sys

input = sys.stdin.readline

n, k = map(int, input().split())
strs = input().strip()

s_strs = ''.join(sorted(strs))

mass_map = {}
for s in s_strs:
    mass_map[s] = ord(s) - 96


last_selected = None
res = 0
selected_count = 0

for ch in s_strs:
    if selected_count == k:
        break
    
    if last_selected is None or (mass_map[ch] - mass_map[last_selected] >= 2):
        res += mass_map[ch]
        last_selected = ch
        selected_count += 1

if selected_count < k:
    print(-1)
else:
    print(res)
