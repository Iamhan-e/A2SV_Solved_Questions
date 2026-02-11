from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res= []
        top_k= Counter(nums).most_common(k)
        for num, freq in top_k:
            res.append(num)
        return res