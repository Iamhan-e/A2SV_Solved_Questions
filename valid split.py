class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority= 0
        cnt= 0

        for n in nums:
            if cnt== 0:
                cnt+=1
                majority= n
            elif n == majority:
                cnt+=1
            else:
                cnt-=1

        lft_cnt= 0
        rigt_cnt= nums.count(majority)

        for i in range(len(nums)):
            
            if nums[i] == majority:
                lft_cnt+=1
                rigt_cnt-=1
            
            lft_len= i+1
            rigt_len= len(nums)- i -1

            if 2 * lft_cnt > lft_len and 2* rigt_cnt > rigt_len:
                return i
        return -1