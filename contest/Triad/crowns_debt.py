import sys
import math
input= sys.stdin.readline

t= int(input().strip())

if t:
    for _ in range(t):
        debt, threshold = map(int, input().split())
        
        ratio = (debt + threshold - 1) // threshold   
        cnt = (ratio - 1).bit_length() 
        print(cnt)