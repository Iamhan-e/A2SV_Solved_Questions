class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq= defaultdict(int)
        max_cnt=0
        res=0
        i=0
        
        for j in range(len(s)):
            
            freq[s[j]]+=1
            max_cnt= max(max_cnt, freq[s[j]])

            while (j-i+1) - max_cnt >k :
                
                freq[s[i]]-=1
                i+=1
            res= max(res, j-i+1)
            
        return res