class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt= defaultdict(int)
        lft_near, lft_far, res=0, 0, 0

        for r in range(len(nums)):
            cnt[nums[r]]+=1

            while len(cnt) > k:

                cnt[nums[lft_near]]-=1
                if cnt[nums[lft_near]] == 0:
                    cnt.pop(nums[lft_near])
                lft_near+=1
                lft_far= lft_near
            
            while cnt[nums[lft_near]] > 1:
                cnt[nums[lft_near]]-=1
                lft_near+=1

            if len(cnt)== k:
                res+= lft_near - lft_far +1

        return res