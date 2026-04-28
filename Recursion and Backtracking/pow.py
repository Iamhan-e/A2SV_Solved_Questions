#https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        def pow(x, n):
            
            if n== 0:
                return 1
            if n < 0:
                return 1 / pow(x, -n)
            else:
                half= pow(x, n//2)
                if n%2 !=0: 
                    
                    return x * half * half
                else:
                    return half * half
          

          
                

        return pow(x,n)

print(Solution().myPow(2, 10))

