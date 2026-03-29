import sys

from collections import Counter

input= sys.stdin.readline

n= int(input().strip())
food= input().strip()


mid=n//2




for i in range(1, n):
    my_food= Counter(food[:i])
    their_food= Counter(food[i:])

    if my_food['L'] != their_food['L'] and my_food['O'] != their_food['O']:
        print(i)
        break
   

else:
    print(-1)



