from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s= Counter(s)
        cnt_t= Counter(t)

        step=0

        for char in cnt_s:
            if cnt_s[char] > cnt_t[char]:
                step+= (cnt_s[char] - cnt_t[char])
                
          
        return step

print(Solution().minSteps(s = "leetcode", t = "practice"))