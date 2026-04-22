class Solution:
    def decodeString(self, s: str) -> str:
         
        num_stack = []
        str_stack = []
        curr_str = ""
        curr_num = 0
        
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_str = ""
                curr_num = 0
            elif c == ']':
                curr_str = str_stack.pop() + curr_str * num_stack.pop()
            else:  
                curr_str += c
        
        return curr_str