import sys
input = sys.stdin.readline

answers = []

n, B = map(int, input().split())   
a = list(map(int, input().split()))   

even = odd = 0
cut_costs = []                   

for i in range(n - 1):            
    if a[i] % 2 == 0:
        even += 1
    else:
        odd += 1

    if even == odd:               
        cut_costs.append(abs(a[i] - a[i + 1]))


cut_costs.sort()
spent = 0
taken = 0
for c in cut_costs:
    if spent + c > B:
        break
    spent += c
    taken += 1

answers.append(str(taken))

print('\n'.join(answers))
