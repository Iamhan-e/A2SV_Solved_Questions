class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        
        stack = [0]  
        
        for ch in s:
            if ch == '(':
                stack.append(0)     
            else:  
                top = stack.pop()    
                if top == 0:        
                    score = 1
                else:                
                    score = 2 * top
                
                stack[-1] += score
        
        return stack[0]