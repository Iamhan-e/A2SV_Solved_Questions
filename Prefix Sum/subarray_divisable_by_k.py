class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
       
        total=0
        res=0
        table = defaultdict(int)
        table[0]=1

        for n in nums:
            total+=n
            r= total % k

            res += table[r]
            table[r]+=1

        return res
