class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        count = Counter(changed)
        ans = []
        
        for num in changed:
            if count[num]==0:
                continue
            
            ans.append(num)
            count[num]-=1

            twice= num*2
            if count[twice]== 0:
                return []
            
            count[twice]-=1

        return ans