class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        MOD= 7+ 10 ** 9
        def power(x,n):
            
            if n == 0:
                return 1
            half= power(x, n//2)    
            if n % 2 == 0:
                
                return  half * half  %MOD
            
            return  x * half * half  %MOD
            
        return power(5, (n +1)//2)  * power(4 , n//2) % MOD

#https://leetcode.com/problems/count-good-numbers/description/