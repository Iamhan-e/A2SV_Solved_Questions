import sys

input_data= sys.stdin.read().split()

indx= input_data.index('1')

row= (indx // 5) +1
col= (indx % 5)+1

moves= abs(row-3) + abs(col-3)

print(moves)
