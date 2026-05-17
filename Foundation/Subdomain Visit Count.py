from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        pairs= Counter()
        for d in cpdomains:
            parts= d.split()
            visited= int(parts[0])
            domain= parts[1]

            current= domain
            while current:
                pairs[current]+=visited
                d_indx= current.find('.')
                if d_indx == -1:
                    break
                current= current[d_indx+1:]
        
        result= []
        for dom, vis in pairs.items():
            result.append(f"{vis} {dom}")
        return result


            
