class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        srt_nums= sorted(nums)
        res= {}

        for i in range(len(srt_nums)):
            if srt_nums[i] not in res:
                res[srt_nums[i]]= i
        
        ans= []

        for num in nums:
            ans.append(res[num])

        return ans

            