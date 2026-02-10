from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        major= len(nums)//3
        cnt= Counter(nums)
        res= []

        for num, freq in cnt.items():
            if freq > major:
                res.append(num)
        return res