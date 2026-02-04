class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        buffer = ""
        in_block = False
        
        for line in source:
            i = 0
        
            if not in_block:
                buffer = ""
                
            while i < len(line):
                char = line[i]
            
                nxt = line[i + 1] if i + 1 < len(line) else None
                
                if not in_block:
                    if char == '/' and nxt == '*':
                        in_block = True
                        i += 1 
                    elif char == '/' and nxt == '/':
                        break
                    else:
                        buffer += char
                else:
                    
                    if char == '*' and nxt == '/':
                        in_block = False
                        i += 1 
                
                i += 1
            
            
            if not in_block and buffer:
                res.append(buffer)
                
        return res