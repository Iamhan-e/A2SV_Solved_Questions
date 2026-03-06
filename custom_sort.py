class Solution:
    def customSortString(self, order: str, s: str) -> str:
       
        custom = {ch: i for i, ch in enumerate(order)}
    
        buckets = [[] for _ in range(len(order))]
        leftover = []
        
        for char in s:
            if char in custom: 
                buckets[custom[char]].append(char)
            else:  
                leftover.append(char)
        
       
        result = []
        for bucket in buckets:
            result.extend(bucket)
        result.extend(leftover)
        return ''.join(result)
