from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        dup_map= defaultdict(list)
        
        for d in paths:
            parts= d.split()
            directory= parts[0]

            for i in parts[1:]:
                indx= i.index('(')
                filename= i[:indx] 
                content= i[indx+1: -1]

                full_path= directory + '/' + filename
                dup_map[content].append(full_path)
        
        result= []
        for l in dup_map.values():
            if len(l)>= 2:
                result.append(l)
        return result
