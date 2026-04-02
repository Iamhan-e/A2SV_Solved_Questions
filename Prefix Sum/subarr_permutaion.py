class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        diff= [0] * (len(nums)+1)
        

        for i, j in requests:
            diff[i]+=1
            diff[j+1]-=1

        freq= [0] * len(nums)
        freq[0]= diff[0]
        for i in range(1, len(freq)):
            freq[i]= freq[i-1] + diff[i]

        freq.sort()
        nums.sort()
        total=0
        for n, f in zip(nums, freq):

            total+= (n*f)

        return total % (10**9 + 7)