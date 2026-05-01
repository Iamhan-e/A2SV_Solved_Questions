
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def adv(i, j):

            if i== j:
                return nums[i]

            take_left= nums[i] - adv(i+1, j)
            take_right= nums[j] - adv(i, j-1)

            return max(take_left, take_right)

        return adv(0, len(nums)-1) >=0

                
#https://leetcode.com/problems/predict-the-winner/description/