from collections import defaultdict
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        sum = 0
        indices = defaultdict(list) 

        for j in range(len(nums)):
            relevant = indices[nums[j]]

            
            for i in relevant:
                if not (i * j) % k:
                    sum += 1

            indices[nums[j]].append(j)

        return sum

print(Solution().countPairs(nums = [3,1,2,2,2,1,3], k = 2))
        


        