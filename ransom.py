class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        cnt= Counter(magazine)

        for r in ransomNote:
            if r not in magazine:
                return False
            
            if r in magazine:
                
                if cnt[r] ==0:
                    return False
                cnt[r]-=1
        return True

