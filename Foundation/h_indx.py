class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        cit= citations
        cit.sort()
        
        for i in range(len(cit)):
            num_len= len(cit)- i
            if cit[i] >= num_len:
                return num_len

        return 0
            