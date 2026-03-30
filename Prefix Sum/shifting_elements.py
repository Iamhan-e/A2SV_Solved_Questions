class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n= len(s)
        diff= [0] * (n+1)

        for start, end, direction in shifts:

            if direction == 0:
                diff[start] -=1
                diff[end+1]+=1
            
            else:
                diff[start] +=1
                diff[end+1]-=1
        
        curr= 0
        shift_str= ''
        for i in range(n):
            curr+= diff[i]

            shift_str+= chr(((ord(s[i]) - ord('a')+ curr) % 26) + ord('a'))
        return shift_str