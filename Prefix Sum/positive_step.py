class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=[0] * (len(nums)+1)

        for i in range(len(nums)):
            prefix[i+1]+= nums[i] + prefix[i]

        min_val= min(prefix)

        return max(1, 1-min_val)