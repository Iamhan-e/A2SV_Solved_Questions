t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    odd_pos = any(int(s[i]) % 2 == 1 for i in range(0, n, 2))
    even_pos = any(int(s[i]) % 2 == 0 for i in range(1, n, 2))
    
    if n % 2 == 1:  
        if odd_pos:
            print(1)
        else:
            print(2)
    else:  
        if even_pos:
            print(2)
        else:
            print(1)