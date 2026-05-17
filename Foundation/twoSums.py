class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res= []
        for i, val in enumerate(nums):
            num2= target- val 
            
            
            if num2 in nums:
                indx= nums.index(num2)
                if  i!= indx:
                    res.append(indx)
                    res.append(i)
                    return res

        

    
