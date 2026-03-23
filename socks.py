import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))
    
    # Count frequencies of left and right socks
    left_count = [0] * (n + 1)  # 1-indexed for colors
    right_count = [0] * (n + 1)
    
    # First l socks are left, next r socks are right
    for i in range(n):
        if i < l:
            left_count[socks[i]] += 1
        else:
            right_count[socks[i]] += 1
    
    # Remove already matching pairs (no cost)
    for color in range(1, n + 1):
        matches = min(left_count[color], right_count[color])
        left_count[color] -= matches
        right_count[color] -= matches
        l -= matches
        r -= matches
    
    # Ensure left side has more or equal socks
    if l < r:
        left_count, right_count = right_count, left_count
        l, r = r, l
    
    # Now l >= r
    cost = 0
    
    # Smart conversions: move duplicate socks from left to right
    for color in range(1, n + 1):
        extra = l - r  # how many more left socks we have
        if extra <= 0:
            break
            
        duplicate_pairs = left_count[color] // 2
        socks_to_move = min(duplicate_pairs * 2, extra)
        
        cost += socks_to_move // 2  # each pair moved costs 1
        l -= socks_to_move
    
    # Final operations
    cost += (l - r) // 2  # balance remaining difference
    cost += (l + r) // 2  # recolor remaining socks
    
    print(cost)
