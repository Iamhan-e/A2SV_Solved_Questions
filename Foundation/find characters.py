class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map= {}
        total=0
        for char in chars:
            char_map[char]= char_map.get(char, 0)+1
        
        for word in words:
            available= char_map.copy()
            can_form= True
            for c in word:
                if c not in available or available[c]==0:
                    can_form= False
                    break
                available[c]-=1
            if can_form:
                total+=len(word)
        return total
        
        return total