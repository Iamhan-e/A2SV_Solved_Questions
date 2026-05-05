import math
t= int(input().strip())

for _ in range(t):

    n, m, k= map(int, input().split())
    a_win= False
    even_freq= math.ceil(n/m)
    if m== 1 :
        print("NO")
        

    elif even_freq + k >= n:
        print("NO")
    else:
        print("YES")