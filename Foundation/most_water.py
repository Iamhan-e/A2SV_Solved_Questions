class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l= 0
        r= len(height)-1
        max_val= 0

        while l < r:
            x= min(height[l], height[r]) * (r-l)
            max_val= max(max_val, x)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_val
