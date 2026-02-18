class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set= set(nums)
        max_len= 0

        for n in num_set:
            if n-1 not in num_set:
                l= 1

                while l+n in num_set:
                    l+=1
                
                max_len= max(l, max_len)

        return max_len