class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
           
        pre_sum= {0:1}
        curr_sum= 0
        cnt=0

        for n in nums:
            curr_sum+=n

            if curr_sum - k in pre_sum:
                cnt+= pre_sum[curr_sum - k]

            pre_sum[curr_sum]= pre_sum.get(curr_sum, 0)+ 1

        return cnt

    

    
        
        

            