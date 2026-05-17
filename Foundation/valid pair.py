from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        
        cnt= Counter(s)

        for i in range(len(s)-1):
            if s[i] != s[i+1] and str(cnt[s[i]]) == s[i] and str(cnt[s[i+1]]) == s[i+1]:
                return s[i]+s[i+1]

        return ""
