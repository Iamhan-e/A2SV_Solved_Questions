import sys


input_data= sys.stdin.read().split()

if input_data:
    t= int(input_data[0])
    i=1

    for _ in range(t):
        l= int(input_data[i])
        strs= input_data[i+1]
        i+=2
        
        if "aa" in strs:
            print(2)
            
        elif "aba" in strs or "aca" in strs:
            print(3)
            
        elif "abca" in strs or "acba" in strs:
            print(4)
            

        elif "abbacca" in strs or "accabba" in strs:
            print(7)
        
        else:   

            print (-1)