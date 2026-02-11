class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuf_map= {}
        shuf_str= ''
        s_list= list(s)

        for strs, i in zip(s_list, indices):
            shuf_map[i]= strs
        
        for i in range(len(indices)):

            shuf_str+= shuf_map[i]
            
        return shuf_str