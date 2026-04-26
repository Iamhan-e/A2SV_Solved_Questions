
t = int(input())
for _ in range(t):
    n = int(input())
    enemy = input().strip()
    our = input().strip()
    
    taken = [False] * n  # taken[col] = is row-1 column 'col' occupied?
    count = 0
    
    for col in range(n):
        if our[col] == '1':  # Pawn at column 'col' in bottom row
            
            # Priority 1: Go straight up to same column
            if enemy[col] == '0' and not taken[col]:
                count += 1
                taken[col] = True
            
            # Priority 2: Capture enemy to the left
            elif col > 0 and enemy[col - 1] == '1' and not taken[col - 1]:
                count += 1
                taken[col - 1] = True
            
            # Priority 3: Capture enemy to the right
            elif col < n - 1 and enemy[col + 1] == '1' and not taken[col + 1]:
                count += 1
                taken[col + 1] = True
    
    print(count)

