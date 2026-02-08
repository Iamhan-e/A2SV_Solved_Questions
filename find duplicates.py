
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res= set()
        ans=[]

        for num in nums:
            if num in res:
                ans.append(num)
            else:
                res.add(num)
        return ans