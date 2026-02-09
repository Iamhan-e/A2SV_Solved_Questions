import sys

def solve():
   
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        s = input_data[i]
        n = len(s)
        
        
        is_infinite = False
        for j in range(n - 1):
           
            can_move_right = (s[j] == '>' or s[j] == '*')
            can_move_left = (s[j+1] == '<' or s[j+1] == '*')
            
            if can_move_right and can_move_left:
                is_infinite = True
                break
        
        if is_infinite:
            results.append("-1")
            continue
            
        l_count = 0
        for char in s:
            if char == '<': l_count += 1
            else: break
            
        r_count = 0
        for char in reversed(s):
            if char == '>': r_count += 1
            else: break
            
        if '*' in s:
            results.append(str(max(l_count + 1, r_count + 1)))
        else:
            results.append(str(max(l_count, r_count)))
            
  
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()