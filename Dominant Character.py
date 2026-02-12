import sys
from collections import Counter

input= sys.stdin.readline

t= int(input())

for _ in range(t):
    l= int(input())
    strs= input()
    
    if "aa" in strs:
        print(2)
        
    elif "aba" in strs or "aca" in strs:
        print(3)
        
    elif "abca" in strs or "acba" in strs:
        print(4)
        

    elif "abcabca" in strs or "acbacba" in strs:
        print(7)
    
    else:   

        print (-1)