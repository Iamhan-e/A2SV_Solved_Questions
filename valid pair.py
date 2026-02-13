from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        
        cnt= Counter(s)
        

        for i in range(len(s)-1):
            first= s[i]
            second= s[i+1]

            if first != second:

                if str(cnt[first]) == first and str(cnt[second]) == second:
                    return first+second

        return ""
