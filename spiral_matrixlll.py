class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
       directions= [[0,1], [1,0], [0, -1], [-1,0]]

       res = []
       i=0
       step= 1

       while len(res)< rows* cols:

        for _ in range(2):
            dr, dc= directions[i]

            for _ in range(step):
                if 0<= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                
                rStart, cStart= rStart+ dr , cStart+dc
            i= (i+1)% 4
            
        step+=1

       return res

            
