import sys

input= sys.stdin.readline
t= int(input().strip())

for _ in range(t):
    word= input().strip()
    n= len(word) // 2

    exist= False

    for i in range(1, n):
        if word[i] != word[i-1]:
            exist= True
            break
    
    print("YES") if exist else print("NO")
