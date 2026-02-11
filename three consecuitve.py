from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        init= (num-3)//3
        cons= [init, init+1, init+2]
       
        if sum(cons)== num:
            return cons
        else:
            return []

print(Solution().sumOfThree(33))