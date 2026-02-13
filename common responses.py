from typing import List
from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        res= []
        for r in responses:
            x= set(r)
            for i in x:
                res.append(i)
        

        res.sort()
        cnt= Counter(res)

        return cnt.most_common(1)[0][0]
        

print(Solution().findCommonResponse([["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]))