import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
   
    strs = input().strip()          
    price = int(input().strip())    

    
    cnt = [0] * 26                   
    total = 0
    for ch in strs:
        val = ord(ch) - 96            
        cnt[val - 1] += 1
        total += val

  
    if total <= price:
        print(strs)
        continue

    need = total - price

   
    del_cnt = [0] * 26

    for i in range(25, -1, -1):           
        if need <= 0:
            break
        cost = i + 1                      
        
        must_take = (need + cost - 1) // cost
        take = min(cnt[i], must_take)    
        del_cnt[i] = take
        need -= take * cost                

   
    ans = []
    
    for ch in strs:
        idx = ord(ch) - 97                 
        if del_cnt[idx] > 0:               
            del_cnt[idx] -= 1
        else:
            ans.append(ch)

    print(''.join(ans))
