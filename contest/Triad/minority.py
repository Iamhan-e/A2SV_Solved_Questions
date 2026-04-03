import sys

input = sys.stdin.readline

t_str = input().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        s = input().strip()
        
      
        zeros = s.count('0')
        ones = s.count('1')
        
        if zeros != ones:
            
            print(min(zeros, ones))
        else:
            
            print(zeros - 1)