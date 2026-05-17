
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
            if n%2==0:
                return n
            return n*2
    
sol = Solution()




print(sol.smallestEvenMultiple(5))
print(sol.smallestEvenMultiple(6))
