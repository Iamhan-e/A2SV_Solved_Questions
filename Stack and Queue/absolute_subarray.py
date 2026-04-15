from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deq= deque()
        min_deq= deque()

        lft= 0
        max_len= 0

        for right in range(len(nums)):
            curr= nums[right]
            
            while max_deq and nums[max_deq[-1]] < curr:
                max_deq.pop()
            max_deq.append(right)

            while min_deq and nums[min_deq[-1]] > curr:
                min_deq.pop()
            min_deq.append(right)

            while nums[max_deq[0]] - nums[min_deq[0]] > limit:

                if max_deq[0] == lft:
                    max_deq.popleft()
                
                if min_deq[0] == lft:
                    min_deq.popleft()
                lft+=1

            max_len= max(max_len, right - lft+1)
        
        return max_len

