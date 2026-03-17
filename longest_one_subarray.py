class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)-1

        l=0
        r=0
        res=0
        z_cnt=0

        for r in range(len(nums)):
            if nums[r] == 0:
                z_cnt+=1
            

            while z_cnt > 1:
                if nums[l]== 0:
                    z_cnt-=1

                l+=1

            res= max(res, r-l+1)
            
        return res-1


