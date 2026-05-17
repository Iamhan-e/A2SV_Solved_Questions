from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        left= str(x)
        right= ''
        
        for i in range(len(left)-1, -1, -1):
            right+= left[i]

        if left== right:
            return True
        return False
    
sol = Solution()


result = sol.isPalindrome(121)
print(result)

print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))