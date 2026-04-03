import sys

def solve():
    # Efficiently reading input for competitive programming
    input = sys.stdin.read().split()
    if not input:
        return
    
    # Example logic: Using a hash map to track occurrences
    n = int(input[0])
    elements = input[1:]
    counts = {}
    
    for x in elements:
        counts[x] = counts.get(x, 0) + 1
        # Insert specific logic for the "He Won" condition here
        
if __name__ == "__main__":
    solve()