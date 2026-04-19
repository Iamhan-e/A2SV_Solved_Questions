class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l= max(weights)
        h= sum(weights)

        ans= h

        def canHold(cap):
            day= 1
            curr= cap

            for w in weights:
                if curr - w < 0:
                    day+=1
                    curr= cap 
                
                curr-= w
            return day <= days
        
        while l<= h:
            mid= l+ (h-l)//2

            if canHold(mid):
                ans= min(ans, mid)
                h= mid-1
            
            else:
                l= mid+1

        return ans
