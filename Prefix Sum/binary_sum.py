
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum= 0
        pre_freq= {0:1}
        cnt=0

        for n in nums:
            prefix_sum+= n

            if prefix_sum - goal in pre_freq:
                cnt+= pre_freq[prefix_sum - goal]
            
            pre_freq[prefix_sum]= pre_freq.get(prefix_sum, 0)+ 1
        return cnt
    
print(Solution().numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))