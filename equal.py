class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
            
        counts = {}
        for num in a:
            counts[num] = counts.get(num, 0) + 1
            
        
        for num in b:
            if num not in counts or counts[num] == 0:
                
                return False
            counts[num] -= 1
            
        return True