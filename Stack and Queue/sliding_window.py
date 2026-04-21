from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_win = []
        
        window = deque() 
        
        for i in range(len(nums)):
           
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            
            window.append(i)
            
            
            if window[0] == i - k:
                window.popleft()
            
           
            if i >= k - 1:
                max_win.append(nums[window[0]])
                
        return max_win

print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))