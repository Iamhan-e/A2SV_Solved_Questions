class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack= []
        total= 0
        for i in range(len(s)):

            if s[i] == '(':
                stack.append(s[i])

            else:
                if stack and stack[-1] == '(' :
                    
                    stack.pop()
                    stack.append(1)
                else:
                    score= 0
                    while stack and isinstance(stack[-1], int):
                        score+= stack.pop()
                    stack.pop()
                    stack.append(2 * score)

                
        return sum(stack)