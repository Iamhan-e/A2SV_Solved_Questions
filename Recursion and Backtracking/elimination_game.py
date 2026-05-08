class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def helper(n, head, gap, ltr):

            if n== 1:
                return head

            if ltr or n%2 !=0:
                head+=gap

            return helper(n//2, head, gap*2, not ltr)

        return helper(n, 1, 1, True )
    

#https://leetcode.com/problems/elimination-game/