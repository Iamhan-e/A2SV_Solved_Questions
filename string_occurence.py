class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        i,j = 0,0

        while i+j < n:
            if haystack[i+j]== needle[j]:
                j+=1
                if j==m:
                    return i

            else:
                i+=1
                j=0
        return -1

