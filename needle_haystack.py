import sys
from collections import Counter

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1
    out_lines = []
    
    for _ in range(t):
        s = data[index].strip()
        index += 1
        t_str = data[index].strip()
        index += 1
        
        s_count = Counter(s)
        t_count = Counter(t_str)
        possible = True
        for char in s_count:
            if s_count[char] > t_count.get(char, 0):
                out_lines.append("Impossible")
                possible = False
                break
                
        if not possible:
            continue
            
        n = len(s)
        suffix = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(26):
                suffix[i][j] = suffix[i + 1][j]
            char_index = ord(s[i]) - ord('a')
            suffix[i][char_index] += 1
            
        current_counts = [0] * 26
        for i in range(26):
            char = chr(ord('a') + i)
            current_counts[i] = t_count.get(char, 0)
            
        s_pos = 0
        res = []
        len_t = len(t_str)
        
        for _ in range(len_t):
            found = False
            for c_idx in range(26):
                if current_counts[c_idx] == 0:
                    continue
                new_s_pos = s_pos
                if s_pos < n and s[s_pos] == chr(ord('a') + c_idx):
                    new_s_pos += 1
                valid = True
                for d_idx in range(26):
                    required = suffix[new_s_pos][d_idx]
                    available = current_counts[d_idx]
                    if d_idx == c_idx:
                        available -= 1
                    if available < required:
                        valid = False
                        break
                if valid:
                    res.append(chr(ord('a') + c_idx))
                    current_counts[c_idx] -= 1
                    s_pos = new_s_pos
                    found = True
                    break
            if not found:
                out_lines.append("Impossible")
                break
        else:
            out_lines.append(''.join(res))
            
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
