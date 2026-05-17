from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        cnt= Counter(s)
        freq_str= ""
        for char, freq in cnt.most_common():
            freq_str+= (char * freq)
        
        return freq_str
        
        